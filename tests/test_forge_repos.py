"""
forge_repos: how a project is named and found (projects/forge/00-brief-tests.md).
A bare word is a slug, `projects/<slug>`; a path with a separator or an
absolute one is the project's directory itself; the name of a project
is the `project` field of its project file, the directory's name
without one. No git is run here. What waits on GitHub
(`github_waiting`, POS.1970) is read with gh stood in for by a
function of the test: the lines of the three kinds, the issues beyond
the listed ones counted and said, gh's own words relayed.
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


# ---- what waits on GitHub

def by(login):
    return {"login": login}


def repository(prs=(), issues=(), total=None, discussions=()):
    """The repository as gh answers with it, its owner `owner`; `total`
    is the count of the open issues where it is more than the listed."""
    return {"owner": by("owner"),
            "pullRequests": {"nodes": list(prs)},
            "issues": {"totalCount": len(issues) if total is None else total, "nodes": list(issues)},
            "discussions": {"nodes": list(discussions)}}


def waiting(monkeypatch, answer=None, said=None):
    """`github_waiting` of acme/widgets with gh stood in for: the one
    request answers with the repository `answer`, or fails with `said`."""
    monkeypatch.setattr(fr.shutil, "which", lambda name: name)
    monkeypatch.setattr(fr, "github_origin",
                        lambda path: ("acme", "widgets", "https://github.com/acme/widgets.git"))
    monkeypatch.setattr(fr, "gh_graphql",
                        lambda query, variables, cwd: ({"data": {"repository": answer}}, said))
    return fr.github_waiting(Path("."))


def test_what_waits_is_the_pull_requests_the_issues_and_the_unanswered_discussions(monkeypatch):
    lines = waiting(monkeypatch, repository(
        prs=[{"number": 21, "title": "A light in the shed", "createdAt": "2026-11-27T08:00:00Z",
              "changedFiles": 3, "author": by("visitor")}],
        issues=[{"number": 22, "title": "The door sticks", "createdAt": "2026-11-27T09:00:00Z",
                 "author": by("visitor")},
                {"number": 20, "title": "A note of the owner's", "createdAt": "2026-11-26T09:00:00Z",
                 "author": by("owner")}],
        discussions=[
            {"number": 18, "title": "Nobody of the repository answered", "createdAt": "2026-11-25T09:00:00Z",
             "author": by("visitor"),
             "comments": {"nodes": [{"author": by("other"), "replies": {"nodes": []}}]}},
            {"number": 17, "title": "Answered in a reply", "createdAt": "2026-11-24T09:00:00Z",
             "author": by("visitor"),
             "comments": {"nodes": [{"author": by("other"), "replies": {"nodes": [{"author": by("owner")}]}}]}},
            {"number": 16, "title": "The owner's own", "createdAt": "2026-11-23T09:00:00Z",
             "author": by("owner"), "comments": {"nodes": []}}]))
    assert lines == [
        "1 pull request(s) open, 2 issue(s) open, 1 discussion(s) unanswered",
        '#21 pull request "A light in the shed" by visitor, 2026-11-27, 3 file(s)',
        '#22 issue "The door sticks" by visitor, 2026-11-27',
        '#20 issue "A note of the owner\'s" by owner, 2026-11-26',
        '#18 discussion "Nobody of the repository answered" by visitor, 2026-11-25',
    ]


def test_issues_beyond_the_listed_ones_are_counted_and_said(monkeypatch):
    # An author GitHub no longer knows is a question mark, as on every line.
    lines = waiting(monkeypatch, repository(
        issues=[{"number": 40, "title": "The newest", "createdAt": "2026-11-27T09:00:00Z", "author": None}],
        total=23))
    assert lines == [
        "0 pull request(s) open, 23 issue(s) open, 0 discussion(s) unanswered",
        '#40 issue "The newest" by ?, 2026-11-27',
        "and 22 older issue(s), not listed",
    ]


def test_what_keeps_it_from_reading_is_said_in_the_words_of_gh(monkeypatch):
    assert waiting(monkeypatch, said="gh: To get started with GitHub CLI, please run:  gh auth login") == [
        "could not read: gh: To get started with GitHub CLI, please run:  gh auth login"]
