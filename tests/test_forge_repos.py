"""
forge_repos: how a project is named and found (projects/forge/00-brief-tests.md).
A bare word is a slug, `projects/<slug>`; a path with a separator or an
absolute one is the project's directory itself; the name of a project
is the `project` field of its project file, the directory's name
without one. No git is run here.
"""
from pathlib import Path

import forge_repos as fr


def test_a_bare_word_is_a_slug_under_projects():
    assert fr.project_path("flow-ba") == fr.ENGINE_ROOT / "projects" / "flow-ba"
    assert fr.project_label("flow-ba") == "projects/flow-ba"


def test_a_relative_path_is_the_directory_itself(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "fixture-copy").mkdir()
    assert fr.project_path("./fixture-copy") == (tmp_path / "fixture-copy").resolve()
    assert fr.project_path("tests/fixture") == (tmp_path / "tests" / "fixture").resolve()
    assert fr.project_label("tests/fixture") == "tests/fixture"


def test_an_absolute_path_is_taken_as_given(tmp_path):
    assert fr.project_path(str(tmp_path)) == tmp_path.resolve()
    assert fr.project_label(str(tmp_path)) == str(tmp_path)


def test_the_name_is_the_project_field_of_the_project_file(tmp_path):
    proj = tmp_path / "copy-of-something"
    proj.mkdir()
    (proj / "project.md").write_text("---\nproject: fixture\nkind: thought\nlanguage: en\nfixture: true\n---\n", encoding="utf-8")
    info = fr.project_file(proj)
    assert info["project"] == "fixture"
    assert info["fixture"] is True
    assert info["shape"] == "current"


def test_without_a_project_file_the_directory_names_the_project(tmp_path):
    proj = tmp_path / "bare"
    proj.mkdir()
    info = fr.project_file(proj)
    assert info["project"] == "bare"
    assert info["shape"] == "none"
    assert (info["kind"], info["language"], info["fixture"]) == ("thought", "en", False)
