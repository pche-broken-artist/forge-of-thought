"""
The comments of the skeletons (POS.2030, SOL.0970): a file made from a
template names it in one line and carries none of the template's
comments; a file made before may keep the comment it was born with,
which no check reports; `forge-migrate --comments` replaces it by the
line on the owner's word, in every file that is not immutable. Run on
a copy of the fixture outside git, by its path.
"""
import re

OLD = "<!-- The history of a versioned document, in a wording\nthe skeleton had long ago. -->"
LINE = "<!-- Shape: templates/history.md -->"


def plant(path, old, new):
    text = path.read_text(encoding="utf-8")
    assert old in text
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def test_every_file_of_the_fixture_names_its_template(project):
    made = [p for p in project.rglob("*.md")
            if p.parts[-2] not in ("reviews", "challenges") and p.name not in ("README.md", "shed-minutes.md")]
    assert made
    for p in made:
        assert re.search(r"^<!-- Shape: templates/[\w.-]+ -->$", p.read_text(encoding="utf-8"), re.M), p


def test_the_named_templates_exist_and_carry_the_same_line(project, engine_root):
    for p in project.rglob("*.md"):
        m = re.search(r"^<!-- Shape: (templates/[\w.-]+) -->$", p.read_text(encoding="utf-8"), re.M)
        if m:
            template = engine_root / m.group(1)
            assert template.exists(), (p, m.group(1))
            assert m.group(0) in template.read_text(encoding="utf-8"), template


def test_a_comment_a_file_was_born_with_is_no_finding(project, run_script):
    plant(project / "10-intent.history.md", LINE, OLD)
    plant(project / "sources" / "00-INDEX.md", "<!-- Shape: templates/index.md -->", "<!-- An index, in older words. -->")
    r = run_script("forge-check", "light", project)
    assert r.returncode == 0, r.stderr
    assert r.stdout.splitlines()[2] == "conforms"


def test_the_dry_run_names_the_file_and_changes_nothing(project, run_script):
    hist = project / "10-intent.history.md"
    plant(hist, LINE, OLD)
    before = hist.read_text(encoding="utf-8")
    r = run_script("forge-migrate", project, "--comments")
    assert r.returncode == 0, r.stderr
    assert "10-intent.history.md: the comment replaced by the line (history)" in r.stdout
    assert "dry run: 1 file(s) would change" in r.stdout
    assert hist.read_text(encoding="utf-8") == before


def test_apply_replaces_the_comment_by_the_line_and_keeps_the_records(project, run_script):
    hist = project / "10-intent.history.md"
    records = [l for l in hist.read_text(encoding="utf-8").splitlines() if l.startswith("- ")]
    plant(hist, LINE, OLD)
    r = run_script("forge-migrate", project, "--comments", "--apply")
    assert r.returncode == 0, r.stderr
    text = hist.read_text(encoding="utf-8")
    assert LINE in text and "long ago" not in text
    assert [l for l in text.splitlines() if l.startswith("- ")] == records
    again = run_script("forge-migrate", project, "--comments")
    assert "nothing to change" in again.stdout


def test_a_closed_thread_keeps_its_comment_and_an_open_one_gets_the_line(project, run_script):
    line = "<!-- Shape: templates/thread.md -->"
    old = "<!-- A thread, in older words. -->"
    closed, opened = project / "threads" / "THR.0020.md", project / "threads" / "THR.0010.md"
    plant(closed, line, old)
    plant(opened, line, old)
    r = run_script("forge-migrate", project, "--comments", "--apply")
    assert r.returncode == 0, r.stderr
    assert old in closed.read_text(encoding="utf-8") and line not in closed.read_text(encoding="utf-8")
    assert line in opened.read_text(encoding="utf-8") and old not in opened.read_text(encoding="utf-8")
    assert opened.read_text(encoding="utf-8").rstrip("\n").endswith(line)


def test_a_comment_of_an_artefacts_own_is_left_and_the_line_added(project, run_script):
    intent = project / "10-intent.md"
    plant(intent, "<!-- Shape: templates/intent.md -->", "<!-- a note of the author's own -->")
    r = run_script("forge-migrate", project, "--comments", "--apply")
    assert r.returncode == 0, r.stderr
    text = intent.read_text(encoding="utf-8")
    assert "<!-- a note of the author's own -->" in text
    assert "<!-- Shape: templates/intent.md -->" in text
    assert "the line added (intent); 1 comment(s) of its own left" in r.stdout


def test_a_file_without_any_comment_gets_the_line_under_its_heading(project, run_script):
    dec = project / "decisions.md"
    plant(dec, "<!-- Shape: templates/decisions.md -->\n\n", "")
    r = run_script("forge-migrate", project, "--comments", "--apply")
    assert r.returncode == 0, r.stderr
    lines = dec.read_text(encoding="utf-8").splitlines()
    i = lines.index("# Decisions")
    assert lines[i + 1] == "" and lines[i + 2] == "<!-- Shape: templates/decisions.md -->"
    assert "## DEC.0010 — The shed is built, not bought" in lines
