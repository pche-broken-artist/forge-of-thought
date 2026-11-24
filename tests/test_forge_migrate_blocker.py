"""
The mark of blocking (POS.2040, SOL.0980): a TBC says whether it blocks
by one mark in its brackets, `blocker: yes | no`, the same in every
layer that has one; a document written before carries the wording of
its layer, and `forge-migrate --blocker` brings it to the mark on the
owner's word, in every file that is not immutable. Run on a copy of the
fixture outside git, by its path.
"""

HEAD = "---\nversion: 0.1\nstatus: draft\nproject: fixture\n---\n\n"
BRD = (HEAD + "# Fixture — BRD\n\n## Open questions\n"
       "- **TBC.0010** (owner: the joiner; blocks estimation: no) Which hinge the door takes.\n"
       "- **TBC.0020** (owner: principal) Whether the shed is painted.\n"
       "- **TBC.0030** (owner: the joiner; blocks estimation:\n  yes) How wide the door is. It waits for the\n  measurement.\n"
       "- **TBC.0040** (owner: unassigned; blocker: yes) What the roof may weigh.\n")
DESIGN = (HEAD + "# Fixture — Solution design\n\n## Open\n"
          "- **TBC.0060** (owner: JDo) Which screws hold the frame. Closed by: a trial. Blocks\n  realisation: yes.\n"
          "- **TBC.0070** (owner: JDo) Which colour the screws are. Closed by: a word. Blocks\n"
          "  realisation: no; the paint covers them.\n")
LEFT = "40-solution-design.md: TBC.0070 has text after the old mark - left as it is, for the principal"


def plant(project):
    (project / "30-brd.md").write_text(BRD, encoding="utf-8")
    (project / "40-solution-design.md").write_text(DESIGN, encoding="utf-8")


def flat(path):
    """The text with every run of white space as one space: what an item
    says, whatever its line breaks."""
    return " ".join(path.read_text(encoding="utf-8").split())


def test_the_dry_run_names_the_items_and_changes_nothing(project, run_script):
    plant(project)
    r = run_script("forge-migrate", project, "--blocker")
    assert r.returncode == 0, r.stderr
    assert "30-brd.md: 2 item(s) brought to the mark" in r.stdout
    assert "40-solution-design.md: 1 item(s) brought to the mark" in r.stdout
    assert LEFT in r.stdout
    assert "dry run: 2 file(s) would change" in r.stdout
    assert (project / "30-brd.md").read_text(encoding="utf-8") == BRD
    assert (project / "40-solution-design.md").read_text(encoding="utf-8") == DESIGN


def test_apply_brings_the_wording_of_a_brd_to_the_mark(project, run_script):
    plant(project)
    r = run_script("forge-migrate", project, "--blocker", "--apply")
    assert r.returncode == 0, r.stderr
    brd = project / "30-brd.md"
    lines = brd.read_text(encoding="utf-8").splitlines()
    # an item of one line stays one line
    assert "- **TBC.0010** (owner: the joiner; blocker: no) Which hinge the door takes." in lines
    # a longer one is wrapped again, its continuation indented
    assert "- **TBC.0030** (owner: the joiner; blocker: yes) How wide the door is. It waits for the measurement." in flat(brd)
    i = next(n for n, l in enumerate(lines) if l.startswith("- **TBC.0030**"))
    item = [lines[i]] + [l for l in lines[i + 1:i + 3] if l.startswith("  ")]
    assert len(item) > 1 and all(len(l) <= 72 for l in item)
    # an item without a mark and one that has it already are left as they are
    assert "- **TBC.0020** (owner: principal) Whether the shed is painted." in lines
    assert "- **TBC.0040** (owner: unassigned; blocker: yes) What the roof may weigh." in lines
    assert "blocks estimation" not in flat(brd)


def test_apply_moves_the_mark_of_a_solution_design_into_the_brackets(project, run_script):
    plant(project)
    r = run_script("forge-migrate", project, "--blocker", "--apply")
    assert r.returncode == 0, r.stderr
    design = project / "40-solution-design.md"
    assert "- **TBC.0060** (owner: JDo; blocker: yes) Which screws hold the frame. Closed by: a trial. - **TBC.0070**" in flat(design)
    # an item where text follows the old mark is printed and left for the hand
    assert LEFT in r.stdout
    assert "Blocks\n  realisation: no; the paint covers them." in design.read_text(encoding="utf-8")
    again = run_script("forge-migrate", project, "--blocker")
    assert LEFT in again.stdout and "dry run: 0 file(s) would change" in again.stdout


def test_the_ledger_reads_the_mark_the_step_wrote(project, run_script):
    plant(project)
    assert run_script("forge-migrate", project, "--blocker", "--apply").returncode == 0
    out = project.parent / "ledger-out.md"
    assert run_script("forge-ledger", project, "--out", out).returncode == 0
    waiting = out.read_text(encoding="utf-8").split("## Waiting on principal", 1)[1]
    assert [l for l in waiting.splitlines() if l.startswith("- TBC.")] == [
        "- TBC.0030 of 30-brd.md — [blocks] How wide the door is.",
        "- TBC.0040 of 30-brd.md — [no owner; blocks] What the roof may weigh.",
        "- TBC.0060 of 40-solution-design.md — [blocks] Which screws hold the frame.",
        "- TBC.0020 of 30-brd.md — Whether the shed is painted.",
    ]


def test_a_work_file_is_read_and_what_is_immutable_is_not(project, run_script):
    old = "- **TBC.0010** (owner: the joiner; blocks estimation: yes) Which hinge the door takes.\n"
    work = project / "work"
    work.mkdir()
    (work / "brd-from-notes.md").write_text("# A BRD made from a source\n\n## Open questions\n" + old, encoding="utf-8")
    source, history = project / "sources" / "shed-minutes.md", project / "10-intent.history.md"
    kept = {}
    for p in (source, history):
        p.write_text(p.read_text(encoding="utf-8") + "\n" + old, encoding="utf-8")
        kept[p] = p.read_text(encoding="utf-8")
    r = run_script("forge-migrate", project, "--blocker", "--apply")
    assert r.returncode == 0, r.stderr
    assert "work/brd-from-notes.md: 1 item(s) brought to the mark" in r.stdout
    assert "(owner: the joiner; blocker: yes) Which hinge" in (work / "brd-from-notes.md").read_text(encoding="utf-8")
    for p, text in kept.items():
        assert p.read_text(encoding="utf-8") == text, p


def test_a_project_without_an_old_wording_has_nothing_to_change(project, run_script):
    r = run_script("forge-migrate", project, "--blocker")
    assert r.returncode == 0, r.stderr
    assert "nothing to change" in r.stdout and "dry run: 0 file(s) would change" in r.stdout
