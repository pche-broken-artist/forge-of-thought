"""
forge_repos: how a project is named and found (projects/forge/00-brief-tests.md).
A bare word is a slug, `projects/<slug>`; a path with a separator or an
absolute one is the project's directory itself; the name of a project
is the `project` field of its project file, the directory's name
without one. No git is run here. What waits on GitHub
(`github_waiting`, POS.1970) is read with gh stood in for by a
function of the test: the lines of the three kinds, the issues beyond
the listed ones counted and said, gh's own words relayed. So is how
what GitHub ran on a commit ended (`github_ci`, POS.2070): passing,
failing with the job, its step and what says why, running, none.
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


def test_a_pull_request_is_listed_with_the_state_of_its_checks(monkeypatch):
    def pr(number, state):
        rollup = {"statusCheckRollup": {"state": state} if state else None}
        return {"number": number, "title": "A change", "createdAt": "2026-11-27T08:00:00Z", "changedFiles": 1,
                "author": by("visitor"), "commits": {"nodes": [{"commit": rollup}]}}
    lines = waiting(monkeypatch, repository(prs=[pr(21, "FAILURE"), pr(22, "SUCCESS"), pr(23, "PENDING"),
                                                 pr(24, None)]))
    assert lines[1:] == [
        '#21 pull request "A change" by visitor, 2026-11-27, 1 file(s), ci failing',
        '#22 pull request "A change" by visitor, 2026-11-27, 1 file(s), ci passing',
        '#23 pull request "A change" by visitor, 2026-11-27, 1 file(s), ci running',
        '#24 pull request "A change" by visitor, 2026-11-27, 1 file(s)',
    ]


# ---- how what GitHub ran on a commit ended (POS.2070)

SHA = "abcdef0123456789abcdef0123456789abcdef01"


def job(name, conclusion="SUCCESS", status="COMPLETED", steps=(), notes=(), number=None, workflow="tests"):
    """A job of a workflow as GitHub gives it among the checks of a
    commit; `steps` are (name, conclusion) pairs, `notes` the messages
    GitHub noted at the job as failures."""
    return {"__typename": "CheckRun", "name": name, "status": status, "conclusion": conclusion,
            "databaseId": number, "checkSuite": {"workflowRun": {"workflow": {"name": workflow}}},
            "steps": {"nodes": [{"name": s, "conclusion": c} for s, c in steps]},
            "annotations": {"nodes": [{"annotationLevel": "FAILURE", "message": m} for m in notes]}}


def checks(monkeypatch, nodes, said=None, log=None):
    """`github_ci` of acme/widgets at SHA with gh stood in for: the
    commit carries the checks `nodes` (None: GitHub ran none), or the
    request fails with `said`; a job's log is `log`. Returns what the
    function returned and the paths whose logs were asked for."""
    asked = []
    rollup = None if nodes is None else {"contexts": {"nodes": list(nodes)}}
    monkeypatch.setattr(fr.shutil, "which", lambda name: name)
    monkeypatch.setattr(fr, "github_origin",
                        lambda path: ("acme", "widgets", "https://github.com/acme/widgets.git"))
    monkeypatch.setattr(fr, "gh_graphql", lambda query, variables, cwd: (
        {"data": {"repository": {"object": {"statusCheckRollup": rollup}}}}, said))
    monkeypatch.setattr(fr, "gh_rest", lambda path, cwd: (asked.append(path), (log, None))[1])
    return fr.github_ci(Path("."), SHA), asked


def test_checks_that_all_ended_well_are_passing(monkeypatch):
    got, asked = checks(monkeypatch, [job("ubuntu-latest / python 3.x"), job("build", workflow="pages"),
                                      job("a skipped one", conclusion="SKIPPED")])
    assert got == ("passing", ["passing at abcdef0, 3 job(s)"])
    assert asked == []


def test_a_failed_job_is_named_with_its_step_and_what_github_noted(monkeypatch):
    # What GitHub noted says why: the log is not asked for.
    got, asked = checks(monkeypatch, [
        job("windows-latest / python 3.8"),
        job("ubuntu-latest / python 3.8", conclusion="FAILURE", number=77,
            steps=[("Set up job", "SUCCESS"), ("Run actions/setup-python@v5", "FAILURE"), ("Run pytest", "SKIPPED")],
            notes=["The version '3.8' with architecture 'x64' was not found for Ubuntu 26.04.\n"
                   "The list of all available versions can be found here: https://example.invalid/manifest"])])
    assert got == ("failing", [
        "failing at abcdef0, 1 of 2 job(s)",
        'tests / ubuntu-latest / python 3.8: failed at "Run actions/setup-python@v5"',
        "  The version '3.8' with architecture 'x64' was not found for Ubuntu 26.04.",
        "  The list of all available versions can be found here: https://example.invalid/manifest",
    ])
    assert asked == []


LOG = ("﻿2026-11-26T20:19:00.0000000Z ##[group]Run python -m pytest\n"
       "2026-11-26T20:19:01.0000000Z ....F....\n"
       "2026-11-26T20:20:30.0000000Z =========================== short test summary info ============================\n"
       "2026-11-26T20:20:30.0000000Z FAILED tests/test_forge_repos.py::test_a_bare_word - AssertionError: assert 1 == 2\n"
       "2026-11-26T20:20:30.0000000Z \n"
       "2026-11-26T20:20:30.0000000Z ======================== 1 failed, 293 passed in 90.00s ========================\n"
       "2026-11-26T20:20:31.0000000Z ##[error]Process completed with exit code 1.\n"
       "2026-11-26T20:20:32.0000000Z Post job cleanup.\n")


def test_a_failed_test_is_said_from_the_summary_of_pytest_in_the_log(monkeypatch):
    # GitHub notes the exit code alone, which says nothing: the log of the job is read.
    got, asked = checks(monkeypatch, [
        job("ubuntu-latest / python 3.x", conclusion="FAILURE", number=77,
            steps=[("Run python -m pytest", "FAILURE")], notes=["Process completed with exit code 1."])], log=LOG)
    assert got == ("failing", [
        "failing at abcdef0, 1 of 1 job(s)",
        'tests / ubuntu-latest / python 3.x: failed at "Run python -m pytest"',
        "  FAILED tests/test_forge_repos.py::test_a_bare_word - AssertionError: assert 1 == 2",
        "  ======================== 1 failed, 293 passed in 90.00s ========================",
    ])
    assert asked == ["repos/acme/widgets/actions/jobs/77/logs"]


def test_a_log_without_a_summary_gives_the_lines_github_marks_as_errors_or_the_note(monkeypatch):
    assert fr.log_failure("2026-11-26T20:19:00.0000000Z building\n"
                          "2026-11-26T20:19:01.0000000Z ##[error]No space left on device\n") == ["No space left on device"]
    # The log could not be read: the note of the exit code is what is left.
    got, _ = checks(monkeypatch, [job("build", conclusion="TIMED_OUT", number=77,
                                      notes=["Process completed with exit code 1."])], log=None)
    assert got[1][1:] == ["tests / build: failed", "  Process completed with exit code 1."]


def test_checks_still_running_say_how_many_ended_and_what_failed_so_far(monkeypatch):
    got, _ = checks(monkeypatch, [
        job("ubuntu-latest / python 3.x", status="IN_PROGRESS", conclusion=None),
        job("windows-latest / python 3.x"),
        {"__typename": "StatusContext", "context": "deploy/preview", "state": "FAILURE",
         "description": "The deployment failed"}])
    assert got == ("running", [
        "running at abcdef0, 2 of 3 job(s) ended, 1 failed",
        "deploy/preview: failed",
        "  The deployment failed",
    ])


def test_a_commit_without_checks_has_none_and_what_keeps_from_reading_is_said(monkeypatch):
    assert checks(monkeypatch, None)[0] == ("none", [])
    assert checks(monkeypatch, [], said="gh: HTTP 502")[0] == ("unread", ["could not read: gh: HTTP 502"])
