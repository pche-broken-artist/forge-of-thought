"""
forge-record on a copy of the fixture: a record or a decision appended
at the end of its file and nothing else changed (THR.0880). The script
is run as the forge runs it, by the path of the copy, with an instance
file of the test's own named by --instance, never the machine's.
"""
import datetime

import forge_docs as fd

TODAY = datetime.date.today().isoformat()


def instance(tmp_path, author="tester"):
    path = tmp_path / "CLAUDE.local.md"
    line = f"- **Author:** {author}\n" if author else "- **Principal:** someone\n"
    path.write_text("# CLAUDE.local.md\n\n" + line, encoding="utf-8")
    return path


def record(run_script, project, inst, *args):
    return run_script("forge-record", "history", project, "10-intent.md", "--instance", inst, *args)


def test_a_record_lands_last_and_nothing_else_changes(project, tmp_path, run_script):
    history = project / "10-intent.history.md"
    before = history.read_bytes()
    r = record(run_script, project, instance(tmp_path),
               "--subject", "POS.0020", "--kind", "changed", "--reason", "the width moved",
               "--was", "a | b, Action: and Was: kept in Was")
    assert r.returncode == 0, r.stdout + r.stderr
    after = history.read_bytes()
    assert after.startswith(before)
    added = after[len(before):].decode("utf-8")
    assert added == (f"- {TODAY} | 0.2 | tester | POS.0020 | changed | the width moved"
                     " | Was: a | b, Action: and Was: kept in Was\n")
    last = fd.records(history)[-1]
    assert (last["subject"], last["kind"], last["version"], last["author"]) == ("POS.0020", "changed", "0.2", "tester")


def test_crlf_is_kept_and_a_missing_last_break_is_added(project, tmp_path, run_script):
    history = project / "10-intent.history.md"
    text = history.read_text(encoding="utf-8").rstrip("\n")
    history.write_bytes(text.replace("\n", "\r\n").encode("utf-8"))  # CRLF, no final break
    before = history.read_bytes()
    r = record(run_script, project, instance(tmp_path), "--subject", "THR.0030", "--kind", "created")
    assert r.returncode == 0, r.stdout + r.stderr
    after = history.read_bytes()
    assert after.startswith(before)
    assert after[len(before):] == f"\r\n- {TODAY} | 0.2 | tester | THR.0030 | created\r\n".encode("utf-8")
    assert b"\n" not in after.replace(b"\r\n", b"")


def test_action_comes_before_was(project, tmp_path, run_script):
    r = record(run_script, project, instance(tmp_path), "--subject", "POS.0020", "--kind", "changed",
               "--reason", "r", "--action", "run /migrate", "--was", "old")
    assert r.returncode == 0, r.stdout
    last = fd.records(project / "10-intent.history.md")[-1]
    assert (last["reason"], last["action"], last["was"]) == ("r", "run /migrate", "old")


def test_refusals_leave_the_file_untouched(project, tmp_path, run_script):
    history = project / "10-intent.history.md"
    before = history.read_bytes()
    inst = instance(tmp_path)
    cases = [
        ("--subject", "POS.0020", "--kind", "edited", "--reason", "x"),           # no such kind
        ("--subject", "POS.0020", "--kind", "changed"),                           # changed without a reason
        ("--subject", "POS.0020", "--kind", "changed", "--reason", "a | b"),      # breaks the fields
        ("--subject", "POS.0020", "--kind", "changed", "--reason", "Was: x"),     # a field marker in the reason
        ("--subject", "POS.0020", "--kind", "changed", "--reason", "two\nlines"),  # a line break
        ("--subject", "POS.0020", "--kind", "changed", "--reason", "r", "--was", "two\nparas"),
    ]
    for args in cases:
        r = record(run_script, project, inst, *args)
        assert r.returncode == 1, args
        assert r.stdout.startswith("forge-record:"), args
    assert history.read_bytes() == before


def test_no_author_no_record(project, tmp_path, run_script):
    history = project / "10-intent.history.md"
    before = history.read_bytes()
    r = record(run_script, project, instance(tmp_path, author=None), "--subject", "THR.0030", "--kind", "created")
    assert r.returncode == 1 and "/setup" in r.stdout
    assert history.read_bytes() == before


def test_a_document_without_companion_is_refused(project, tmp_path, run_script):
    r = run_script("forge-record", "history", project, "README.md", "--instance", instance(tmp_path),
                   "--subject", "README.md", "--kind", "created")
    assert r.returncode == 1 and "companion" in r.stdout


def test_dry_run_writes_nothing(project, tmp_path, run_script):
    history = project / "10-intent.history.md"
    before = history.read_bytes()
    r = record(run_script, project, instance(tmp_path), "--subject", "THR.0030", "--kind", "created", "--dry-run")
    assert r.returncode == 0
    assert f"- {TODAY} | 0.2 | tester | THR.0030 | created" in r.stdout
    assert history.read_bytes() == before


def test_a_decision_takes_the_next_number_and_lands_last(project, tmp_path, run_script):
    decisions = project / "decisions.md"
    before = decisions.read_bytes()
    reason = "A reason long enough to be wrapped at seventy-two columns, " * 3
    r = run_script("forge-record", "decision", project, "--instance", instance(tmp_path),
                   "--title", "The roof is green", "--decision", "The roof is painted green.",
                   "--reason", reason, "--verdict", "FND.0010 rejected")
    assert r.returncode == 0, r.stdout + r.stderr
    after = decisions.read_bytes()
    assert after.startswith(before)
    added = after[len(before):].decode("utf-8")
    assert added.startswith("\n## DEC.0020 — The roof is green\n- **Decision:** The roof is painted green.\n")
    assert all(len(line) <= 72 for line in added.split("\n") if not line.startswith("## "))
    assert "\n  " in added  # the reason wrapped, its lines indented
    assert added.endswith(f"- **Verdict:** FND.0010 rejected\n- **Date:** {TODAY}\n")
