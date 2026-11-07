"""
The git scripts on the fixture as a throwaway repository with a bare
origin beside it (projects/forge/00-brief-tests.md; DEC.0240: never a
live repository). Every script is run as the forge runs it, by the
path of the copy; git reads no configuration of the machine
(conftest, git_env). What is tested is the kind of behaviour each
script promises in its header, not its wording.
"""
from conftest import git


def head(path, env):
    return git(["rev-parse", "HEAD"], path, env)


def origin_main(repo, env):
    return git(["rev-parse", "main"], repo.parent / "origin.git", env)


def change(path, name="10-intent.md", line="\n- **POS.0030** A light in the shed.\n"):
    with open(path / name, "a", encoding="utf-8") as f:
        f.write(line)


# ---- status

def test_status_reports_one_repository_by_its_path(repo, git_env, run_script):
    r = run_script("forge-status", repo, env=git_env)
    assert r.returncode == 0, r.stderr
    assert "== fixture" in r.stdout and "clean - nothing to save" in r.stdout
    assert "branch:      main" in r.stdout
    assert "origin.git" in r.stdout
    assert "identity:    tester" in r.stdout      # set in the repository: said aloud
    assert "== forge (engine)" not in r.stdout    # one repository, not the sweep


def test_status_says_not_under_git(project, git_env, run_script):
    r = run_script("forge-status", project, env=git_env)
    assert r.returncode == 0, r.stderr
    assert "not under git" in r.stdout


def test_status_with_remote_reports_the_branch_against_its_origin(repo, other_clone, git_env, run_script):
    change(other_clone)
    git(["commit", "-q", "-am", "other: a light"], other_clone, git_env)
    git(["push", "-q"], other_clone, git_env)
    r = run_script("forge-status", repo, "--remote", env=git_env)
    assert "remote:      behind 1" in r.stdout


# ---- save

def test_save_commits_with_the_message_and_pushes_the_ledger_left_out(repo, git_env, run_script):
    change(repo)
    assert run_script("forge-ledger", repo, env=git_env).returncode == 0  # ledger.md made in the copy
    assert (repo / "ledger.md").exists()
    r = run_script("forge-save", repo, "-m", "fixture: a light in the shed", env=git_env)
    assert r.returncode == 0, r.stderr
    assert "saved and pushed" in r.stdout
    assert git(["log", "-1", "--format=%s"], repo, git_env) == "fixture: a light in the shed"
    assert "ledger.md" not in git(["ls-files"], repo, git_env).splitlines()
    assert origin_main(repo, git_env) == head(repo, git_env)


def test_save_with_nothing_to_save_says_so(repo, git_env, run_script):
    r = run_script("forge-save", repo, env=git_env)
    assert r.returncode == 0, r.stderr
    assert "nothing to save" in r.stdout
    assert git(["log", "--oneline"], repo, git_env).count("\n") == 0  # the one commit


def test_save_without_a_message_generates_one_from_the_files(repo, git_env, run_script):
    change(repo)
    r = run_script("forge-save", repo, env=git_env)
    assert r.returncode == 0, r.stderr
    assert git(["log", "-1", "--format=%s"], repo, git_env) == "fixture: 1 file(s) - 10-intent.md"


def test_save_without_an_identity_commits_nothing_and_says_what_to_do(repo, git_env, run_script):
    git(["config", "--unset", "user.email"], repo, git_env)
    git(["config", "--unset", "user.name"], repo, git_env)
    change(repo)
    r = run_script("forge-save", repo, env=git_env)
    assert r.returncode == 0
    assert "no commit identity" in r.stdout
    assert git(["status", "--porcelain"], repo, git_env)  # the change still unsaved


def test_save_pushes_a_clean_repository_that_is_ahead(repo, git_env, run_script):
    change(repo)
    git(["commit", "-q", "-am", "fixture: by hand, not pushed"], repo, git_env)
    r = run_script("forge-save", repo, env=git_env)
    assert r.returncode == 0, r.stderr
    assert "ahead of origin, pushing" in r.stdout
    assert origin_main(repo, git_env) == head(repo, git_env)


def test_save_rebases_remote_changes_that_do_not_conflict(repo, other_clone, git_env, run_script):
    change(other_clone, "00-brief.md", "\nThe gate is on the north side.\n")
    git(["commit", "-q", "-am", "other: the gate"], other_clone, git_env)
    git(["push", "-q"], other_clone, git_env)
    change(repo)
    r = run_script("forge-save", repo, "-m", "fixture: a light", env=git_env)
    assert r.returncode == 0, r.stderr
    assert "saved and pushed" in r.stdout
    subjects = git(["log", "--format=%s"], repo, git_env).splitlines()
    assert subjects[:2] == ["fixture: a light", "other: the gate"]   # rebased on top, both kept
    assert origin_main(repo, git_env) == head(repo, git_env)


def test_save_with_a_tag_tags_and_pushes_the_tag_and_refuses_an_existing_one(repo, git_env, run_script):
    r = run_script("forge-save", repo, "--tag", "v1", env=git_env)
    assert r.returncode == 0, r.stderr
    assert "tagging the current state" in r.stdout and "tagged: v1" in r.stdout
    assert "v1" in git(["tag"], repo.parent / "origin.git", git_env).splitlines()
    r = run_script("forge-save", repo, "--tag", "v1", env=git_env)
    assert r.returncode != 0 and "already exists" in r.stdout + r.stderr


# ---- branch

def test_branch_reports_creates_switches_and_refuses_unsaved_changes(repo, git_env, run_script):
    r = run_script("forge-branch", repo, env=git_env)
    assert r.returncode == 0 and "on branch main" in r.stdout
    r = run_script("forge-branch", repo, "trial", env=git_env)
    assert r.returncode == 0, r.stderr
    assert "created trial from main" in r.stdout
    assert git(["rev-parse", "--abbrev-ref", "HEAD"], repo, git_env) == "trial"
    r = run_script("forge-branch", repo, "main", env=git_env)
    assert "switched to main" in r.stdout
    change(repo)
    r = run_script("forge-branch", repo, "trial", env=git_env)
    assert r.returncode != 0 and "unsaved changes" in r.stdout + r.stderr
    assert git(["rev-parse", "--abbrev-ref", "HEAD"], repo, git_env) == "main"


def test_a_new_branch_reaches_the_origin_with_its_first_save(repo, git_env, run_script):
    assert run_script("forge-branch", repo, "trial", env=git_env).returncode == 0
    change(repo)
    r = run_script("forge-save", repo, "-m", "fixture: on trial", env=git_env)
    assert r.returncode == 0, r.stderr
    assert "trial" in git(["branch", "--format=%(refname:short)"], repo.parent / "origin.git", git_env).splitlines()


# ---- pull

def test_pull_fast_forwards_a_clean_repository_that_is_behind(repo, other_clone, git_env, run_script):
    change(other_clone)
    git(["commit", "-q", "-am", "other: a light"], other_clone, git_env)
    git(["push", "-q"], other_clone, git_env)
    r = run_script("forge-pull", repo, env=git_env)
    assert r.returncode == 0, r.stderr
    assert "pulled" in r.stdout and "other: a light" in r.stdout
    assert head(repo, git_env) == head(other_clone, git_env)
    r = run_script("forge-pull", repo, env=git_env)
    assert "up to date" in r.stdout


def test_pull_refuses_unsaved_changes_and_a_diverged_history(repo, other_clone, git_env, run_script):
    change(repo)
    r = run_script("forge-pull", repo, env=git_env)
    assert r.returncode != 0 and "unsaved changes" in r.stdout + r.stderr
    git(["commit", "-q", "-am", "fixture: local"], repo, git_env)
    change(other_clone, "00-brief.md", "\nThe gate is on the north side.\n")
    git(["commit", "-q", "-am", "other: the gate"], other_clone, git_env)
    git(["push", "-q"], other_clone, git_env)
    before = head(repo, git_env)
    r = run_script("forge-pull", repo, env=git_env)
    assert r.returncode != 0 and "diverged" in r.stdout + r.stderr
    assert head(repo, git_env) == before                       # nothing pulled, nothing merged
