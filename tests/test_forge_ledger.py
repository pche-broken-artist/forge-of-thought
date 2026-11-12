"""
forge-ledger on the fixture: the ledger made at read time from the
documents (projects/forge/00-brief-tests.md). The script is run as the
forge runs it, by the path of a copy of tests/fixture; the tables of
templates/ledger.md are read back and checked for the kind of content
each is to carry, not for its wording.
"""
import forge_docs as fd


def rows(text, table):
    """The rows of one table of a ledger, as dicts by column."""
    return fd.tables(text).get(table, [])


def test_the_ledger_reads_every_kind_of_document(project, run_script):
    out = project.parent / "ledger-out.md"
    r = run_script("forge-ledger", project, "--out", out)
    assert r.returncode == 0, r.stderr
    assert not (project / "ledger.md").exists()  # --out: the project untouched
    text = out.read_text(encoding="utf-8")
    assert "project: fixture" in text and "unparsed" not in text

    briefs = rows(text, "Briefs")
    assert [(b["File"], b["Version"], b["Status"], b["Mined"]) for b in briefs] == [("00-brief.md", "0.1", "draft", "mined")]

    docs = rows(text, "Documents")
    assert [(d["File"], d["Version"], d["Date"]) for d in docs] == [("10-intent.md", "0.2", "2026-03-05")]

    renders = rows(text, "Renders")
    assert len(renders) == 1 and renders[0]["Render"] == "README.md"
    assert renders[0]["Recipe"] == "recipes/readme.md v0.1" and renders[0]["Generated"] == "2026-03-06"
    assert renders[0]["Audience"] == "humans arriving at the project's repository"  # read from the recipe

    sources = rows(text, "Sources")
    assert [(s["File"], s["Date"], s["Date origin"], s["Form"]) for s in sources] == [("shed-minutes.md", "2026-02-28", "content", "text")]
    assert rows(text, "Research") == [] and rows(text, "Dependencies") == []
    assert rows(text, "Published") == [] and rows(text, "Work") == []


def test_findings_and_challenges_take_their_state_from_records_and_verdicts(project, run_script):
    out = project.parent / "ledger-out.md"
    assert run_script("forge-ledger", project, "--out", out).returncode == 0
    text = out.read_text(encoding="utf-8")

    fnd = {f["ID"]: f for f in rows(text, "Findings")}
    assert fnd["FND.0010"]["State"] == "resolved"                 # a `closed` record of the intent's history
    assert fnd["FND.0010"]["Resolution"] == "POS.0020 names the width"
    assert fnd["FND.0020"]["State"] == "rejected"                 # a decision's Verdict
    assert fnd["FND.0020"]["Resolution"] == "DEC.0010"
    assert fnd["FND.0010"]["Source review"] == "2026-03-02-critique-clarity-1000-ab12.md"
    assert (fnd["FND.0010"]["Severity"], fnd["FND.0010"]["Category"]) == ("minor", "ambiguity")

    chl = {c["ID"]: c for c in rows(text, "Challenges")}
    assert chl["CHL.0010"]["State"] == "open" and chl["CHL.0010"]["Resolution"] == "—"
    assert chl["CHL.0010"]["Headline"].endswith("(minor)")


def test_waiting_on_principal_cites_the_open_thread_and_the_open_challenge(project, run_script):
    out = project.parent / "ledger-out.md"
    assert run_script("forge-ledger", project, "--out", out).returncode == 0
    text = out.read_text(encoding="utf-8")
    waiting = text.split("## Waiting on principal", 1)[1]
    lines = [l for l in waiting.splitlines() if l.startswith("- ")]
    assert [l.split(" — ")[0] for l in lines] == ["- THR.0010", "- CHL.0010"]
    assert "THR.0020" not in waiting                              # closed: not waiting
    assert "the question goes to the next house meeting" in lines[0]  # the thread's last dated paragraph


def test_the_open_threads_stand_by_what_waits_and_by_priority(project, run_script):
    def thread(n, head, matter):
        (project / "threads" / f"THR.{n}.md").write_text(
            f"---\nid: THR.{n}\nconcerns: intent\norigin: the principal\n{head}status: open\n---\n\n{matter} Opened 2026-03-06.\n",
            encoding="utf-8")
    thread("0030", "priority: low\n", "The colour of the door.")
    thread("0040", "", "Who keeps the key.")                          # no priority: read as medium
    thread("0050", "priority: low\nblocks: the roof\n", "Which timber is ordered.")
    out = project.parent / "ledger-out.md"
    assert run_script("forge-ledger", project, "--out", out).returncode == 0
    waiting = out.read_text(encoding="utf-8").split("## Waiting on principal", 1)[1]
    lines = [l for l in waiting.splitlines() if l.startswith("- THR.")]
    # what something waits on first, then high, medium, low
    assert [l.split(" — ")[0] for l in lines] == ["- THR.0050", "- THR.0010", "- THR.0040", "- THR.0030"]
    assert lines[0].split(" — ")[1].startswith("[low; blocks: the roof] Which timber")
    assert lines[1].split(" — ")[1].startswith("[high] ")
    assert lines[2].split(" — ")[1].startswith("[medium] Who keeps the key.")


def test_without_out_the_ledger_is_written_into_the_project(project, run_script):
    r = run_script("forge-ledger", project)
    assert r.returncode == 0, r.stderr
    assert (project / "ledger.md").exists()
    assert "ledger.md made" in r.stdout


def test_a_missing_project_fails_aloud(tmp_path, run_script):
    r = run_script("forge-ledger", tmp_path / "nowhere")
    assert r.returncode != 0
    assert "not found" in r.stderr + r.stdout
