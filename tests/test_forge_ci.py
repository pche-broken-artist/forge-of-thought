"""
forge-ci: how what GitHub ran on the head of the origin ended, and the
waiting for it (POS.2070). The reading itself, forge_repos.github_ci,
is tested with the module; here it is replaced by a function of the
test, and the clock and the pause by the test's own, so that no test
touches the network or waits. The script is also run as the forge runs
it, on the fixture's throwaway repository, whose origin no gh can
read.
"""
import pytest

from conftest import git


@pytest.fixture
def script(load_script, monkeypatch, git_env):
    """The script as a module; `script.answers(...)` makes
    forge_repos.github_ci give those answers one per reading, the last
    one from then on, and `script.slept` holds every pause the script
    took, the clock moving by each."""
    module = load_script("forge-ci")
    for key, value in git_env.items():
        monkeypatch.setenv(key, value)
    now = [0.0]
    module.slept = []
    monkeypatch.setattr(module, "clock", lambda: now[0])
    monkeypatch.setattr(module, "sleep", lambda s: (module.slept.append(s), now.__setitem__(0, now[0] + s)))

    def answers(*given):
        left = list(given)
        monkeypatch.setattr(module.fr, "github_ci",
                            lambda path, sha: left.pop(0) if len(left) > 1 else left[0])

    module.answers = answers
    return module


def test_without_wait_the_jobs_are_read_once_as_they_stand(script, repo):
    script.answers(("running", ["running at 1234567, 1 of 4 job(s) ended"]))
    assert script.read(repo, "1234567890", False, 600) == ("running", ["running at 1234567, 1 of 4 job(s) ended"])
    assert script.slept == []


def test_wait_reads_again_until_no_job_runs(script, repo):
    script.answers(("running", ["running at 1234567, 0 of 4 job(s) ended"]),
                   ("running", ["running at 1234567, 3 of 4 job(s) ended"]),
                   ("failing", ["failing at 1234567, 1 of 4 job(s)", "tests / linux: failed"]))
    assert script.read(repo, "1234567890", True, 600) == (
        "failing", ["failing at 1234567, 1 of 4 job(s)", "tests / linux: failed"])
    assert script.slept == [script.PAUSE, script.PAUSE]


def test_a_repository_with_workflows_is_waited_for_until_its_first_job_shows(script, repo):
    (repo / ".github" / "workflows").mkdir(parents=True)
    (repo / ".github" / "workflows" / "tests.yml").write_text("name: tests\n", encoding="utf-8")
    script.answers(("none", []), ("none", []), ("passing", ["passing at 1234567, 4 job(s)"]))
    assert script.read(repo, "1234567890", True, 600) == ("passing", ["passing at 1234567, 4 job(s)"])
    assert len(script.slept) == 2


def test_nothing_is_waited_for_where_there_is_no_workflow_or_none_started(script, repo):
    script.answers(("none", []))
    assert script.read(repo, "1234567890", True, 600) == ("none", [])
    assert script.slept == []
    # With a workflow, GitHub is given its time to start one, and no longer.
    (repo / ".github" / "workflows").mkdir(parents=True)
    (repo / ".github" / "workflows" / "tests.yaml").write_text("name: tests\n", encoding="utf-8")
    assert script.read(repo, "1234567890", True, 600) == ("none", [])
    assert sum(script.slept) == script.STARTING


def test_after_the_limit_it_says_that_jobs_still_run(script, repo):
    script.answers(("running", ["running at 1234567, 1 of 4 job(s) ended"]))
    word, lines = script.read(repo, "1234567890", True, 60)
    assert word == "running"
    assert lines == ["running at 1234567, 1 of 4 job(s) ended",
                     "jobs still run after the limit; the map says the rest (forge-status --remote)"]
    assert sum(script.slept) == 60


def test_the_report_names_the_repository_and_ends_green_on_a_red_run(script, repo, capsys, git_env):
    sha = git(["rev-parse", "HEAD"], repo, git_env)
    script.answers(("failing", [f"failing at {sha[:7]}, 1 of 4 job(s)",
                                'tests / linux: failed at "Run python -m pytest"',
                                "  FAILED tests/test_x.py::test_y - AssertionError"]))
    assert script.main([str(repo)]) == 0
    out = capsys.readouterr().out.splitlines()
    assert out[0].split() == ["fixture", "ci", "failing", "at", f"{sha[:7]},", "1", "of", "4", "job(s)"]
    assert out[1].strip() == 'tests / linux: failed at "Run python -m pytest"'
    assert out[2].strip() == "FAILED tests/test_x.py::test_y - AssertionError"


def test_a_repository_with_nothing_run_or_without_an_upstream_is_said_and_passed(script, repo, capsys, git_env):
    script.answers(("none", []))
    assert script.main([str(repo)]) == 0
    assert "nothing ran on" in capsys.readouterr().out
    git(["checkout", "-q", "-b", "never-pushed"], repo, git_env)
    assert script.main([str(repo)]) == 0
    assert "no upstream" in capsys.readouterr().out


def test_on_the_fixture_whose_origin_no_gh_reads_it_says_so_and_ends_green(repo, git_env, run_script):
    r = run_script("forge-ci", repo, "--wait", env=git_env)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "ci could not read: " in r.stdout
