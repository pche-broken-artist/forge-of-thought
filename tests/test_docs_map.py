"""
The reading core of scripts/docs_map.py: the map's front-matter and
entries, the reader paths, the inputs with their parts and the text
of a part. Text in, values out; no git, no page made.
"""
import docs_map as dm

MAP = """---
target: engine
owner: projects/forge
---

# Documentation map - the engine

## Paths
- user: docs/start/what-it-is.md, `docs/use/forge-the-intent.md`
- extender: docs/extend/what-it-is-made-of.md

## start

### docs/start/what-it-is.md
- title: What the forge is
- inputs:
  CLAUDE.md#What this workspace is
  projects/forge/10-intent.md#POS.0780
  scripts/forge_repos.py
- links:
  `docs/use/forge-the-intent.md`: the first round.
  `docs/start/what-it-is.md`: itself, left out.
- state: regenerate

## use

### docs/use/forge-the-intent.md
- title: The first round
- inputs: CLAUDE.md
"""


def test_parse_reads_front_entries_and_continued_fields():
    front, entries = dm.parse(MAP)
    assert front == {"target": "engine", "owner": "projects/forge"}
    assert [(e["path"], e["section"], e["name"]) for e in entries] == [
        ("docs/start/what-it-is.md", "start", "what-it-is"),
        ("docs/use/forge-the-intent.md", "use", "forge-the-intent")]
    first = entries[0]
    assert first["fields"]["title"] == "What the forge is"
    assert first["fields"]["inputs"] == "CLAUDE.md#What this workspace is projects/forge/10-intent.md#POS.0780 scripts/forge_repos.py"
    assert first["lines"][0] == "### docs/start/what-it-is.md" and first["lines"][-1] == "- state: regenerate"


def test_reader_paths_in_order_without_backticks():
    assert dm.reader_paths(MAP) == [
        ("user", ["docs/start/what-it-is.md", "docs/use/forge-the-intent.md"]),
        ("extender", ["docs/extend/what-it-is-made-of.md"])]


def test_input_parts_join_a_heading_with_spaces_and_keep_an_id():
    _, entries = dm.parse(MAP)
    assert dm.input_parts(entries[0]) == [
        ("CLAUDE.md", "What this workspace is"),
        ("projects/forge/10-intent.md", "POS.0780"),
        ("scripts/forge_repos.py", None)]
    assert dm.input_paths(entries[0]) == ["CLAUDE.md", "projects/forge/10-intent.md", "scripts/forge_repos.py"]
    assert dm.linked_paths(entries[0]) == ["docs/use/forge-the-intent.md"]


def test_target_root_is_the_engine_for_the_engine_and_the_project_otherwise(tmp_path):
    engine_map = tmp_path / "projects" / "forge" / "docs-map.md"
    assert dm.target_root(engine_map, {"target": "engine"}) == tmp_path.resolve()
    assert dm.target_root(engine_map, {"target": "project"}) == engine_map.parent.resolve()


DOC = """# Top

## Roles
- **POS.0010** The first.
  Its second line.
- **POS.0020** The second.

### Inside roles
Still inside the section Roles.

## Next
**Inputs.** A block by its label.
Its second line.
**Outputs.** Another block.
"""


def test_part_text_cuts_a_section_an_item_and_a_block(tmp_path):
    (tmp_path / "doc.md").write_text(DOC, encoding="utf-8")
    assert dm.part_text(tmp_path, "doc.md", "Roles") == "## Roles\n- **POS.0010** The first.\n  Its second line.\n- **POS.0020** The second.\n\n### Inside roles\nStill inside the section Roles.\n"
    assert dm.part_text(tmp_path, "doc.md", "POS.0010") == "- **POS.0010** The first.\n  Its second line.\n"
    assert dm.part_text(tmp_path, "doc.md", "Inputs") == "**Inputs.** A block by its label.\nIts second line.\n"
    assert dm.part_text(tmp_path, "doc.md", None) == DOC
    assert dm.part_text(tmp_path, "doc.md", "POS.0030") is None
    assert dm.part_text(tmp_path, "doc.md", "Absent") is None
    assert dm.part_text(tmp_path, "absent.md", "Roles") is None
