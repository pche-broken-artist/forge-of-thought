"""
forge-check light on the fixture: the mechanical clauses of the light
check as a program (THR.0530; projects/forge/00-brief-tests.md). The
fixture conforms, so the check on it finds nothing; a defect planted
in a copy is found and named. The check is run as the forge runs it,
by the path of the copy; the fixture conforming is also what keeps it
honest against the templates as they stand.
"""


def test_the_fixture_conforms(project, run_script):
    r = run_script("forge-check", "light", project)
    assert r.returncode == 0, r.stderr
    lines = r.stdout.splitlines()
    assert lines[0].startswith("# Check (light) — ") and str(project) in lines[0]
    assert lines[2] == "conforms"


def test_an_integer_version_with_status_draft_is_found_twice_over(project, run_script):
    intent = project / "10-intent.md"
    intent.write_text(intent.read_text(encoding="utf-8").replace("version: 0.2", "version: 1.0", 1), encoding="utf-8")
    r = run_script("forge-check", "light", project)
    assert r.returncode == 0, r.stderr
    assert "conforms" not in r.stdout.splitlines()[2]
    assert "integer version 1.0 with status `draft`" in r.stdout        # status disagrees with the number
    assert "stands at 1.0 while the newest record of its history is at 0.2" in r.stdout   # no record of the version


def test_a_record_out_of_shape_is_found_at_its_line(project, run_script):
    hist = project / "10-intent.history.md"
    with open(hist, "a", encoding="utf-8") as f:
        f.write("- 2026-03-06 | tester | POS.0010 | changed\n")   # the version left out
    r = run_script("forge-check", "light", project)
    assert r.returncode == 0, r.stderr
    assert "conforms" not in r.stdout.splitlines()[2]
    last = len(hist.read_text(encoding="utf-8").splitlines())
    assert f"10-intent.history.md:{last}" in r.stdout


def test_the_report_is_written_where_out_says(project, tmp_path, run_script):
    out = tmp_path / "reports" / "check.md"
    r = run_script("forge-check", "light", project, "--out", out)
    assert r.returncode == 0, r.stderr
    assert out.exists() and "conforms" in out.read_text(encoding="utf-8")
    assert "0 findings" in r.stdout


def test_a_priority_outside_the_three_words_is_found(project, run_script):
    thread = project / "threads" / "THR.0010.md"
    thread.write_text(thread.read_text(encoding="utf-8").replace("priority: high", "priority: urgent", 1), encoding="utf-8")
    r = run_script("forge-check", "light", project)
    assert r.returncode == 0, r.stderr
    assert "conforms" not in r.stdout.splitlines()[2]
    assert "carries priority `urgent`" in r.stdout
