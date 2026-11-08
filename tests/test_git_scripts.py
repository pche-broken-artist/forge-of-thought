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


def test_status_with_remote_says_when_github_cannot_be_read(repo, git_env, run_script):
    # The fixture's origin is a local bare repository, which no gh can
    # read, on a machine with gh or without one: the github: line says
    # it could not read and why, and the script ends green (POS.1970,
    # SOL.0910).
    r = run_script("forge-status", repo, "--remote", env=git_env)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "github:      could not read: " in r.stdout


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


def merges_kept(path, env):
    """The merge commits reachable from HEAD, as their subjects."""
    return git(["log", "--merges", "--format=%s"], path, env).splitlines()


def test_save_after_a_merge_by_hand_pushes_the_merge_as_it_stands(repo, other_clone, git_env, run_script):
    # The integrator: another person's branch merged into main by git
    # itself, the origin's main unchanged; the save pushes the merge
    # commit as it stands, no rebase flattening it into the branch's
    # commits replayed one by one (CLAUDE.md, Persistence; POS.1710).
    git(["checkout", "-q", "-b", "feature"], other_clone, git_env)
    change(other_clone, "00-brief.md", "\nThe gate is on the north side.\n")
    git(["commit", "-q", "-am", "other: the gate"], other_clone, git_env)
    change(other_clone, "00-brief.md", "\nThe gate is painted green.\n")
    git(["commit", "-q", "-am", "other: the paint"], other_clone, git_env)
    git(["push", "-q", "-u", "origin", "feature"], other_clone, git_env)
    git(["fetch", "-q", "origin"], repo, git_env)
    git(["merge", "-q", "--no-ff", "-m", "fixture: feature merged", "origin/feature"], repo, git_env)
    r = run_script("forge-save", repo, env=git_env)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "saved and pushed" in r.stdout
    assert origin_main(repo, git_env) == head(repo, git_env)
    assert merges_kept(repo, git_env) == ["fixture: feature merged"]


def test_save_after_a_merge_of_the_main_into_a_branch_keeps_the_merge(repo, other_clone, git_env, run_script):
    # The contributor: a branch saved to the origin, the origin's main
    # moved on by another person, that main merged into the branch by
    # git itself and one more change saved; the save pushes the merge
    # as it stands and replays nothing of the other person's commits.
    assert run_script("forge-branch", repo, "trial", env=git_env).returncode == 0
    change(repo, "00-brief.md", "\nA bench by the gate.\n")
    assert run_script("forge-save", repo, "-m", "fixture: a bench", env=git_env).returncode == 0
    for line, msg in (("\n- **POS.0030** A light in the shed.\n", "other: a light"),
                      ("\n- **POS.0040** A roof on the shed.\n", "other: a roof")):
        change(other_clone, "10-intent.md", line)
        git(["commit", "-q", "-am", msg], other_clone, git_env)
    git(["push", "-q"], other_clone, git_env)
    git(["fetch", "-q", "origin"], repo, git_env)
    git(["merge", "-q", "--no-ff", "-m", "fixture: main merged into trial", "origin/main"], repo, git_env)
    change(repo, "00-brief.md", "\nThe bench is oak.\n")
    r = run_script("forge-save", repo, "-m", "fixture: oak", env=git_env)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "saved and pushed" in r.stdout
    assert merges_kept(repo, git_env) == ["fixture: main merged into trial"]
    origin_trial = git(["rev-parse", "trial"], repo.parent / "origin.git", git_env)
    assert origin_trial == head(repo, git_env)


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


# ---- the step of a conflict (POS.1710) and the ways of merging (SOL.0730, SOL.0740)

def conflicting_change(repo, other_clone, env):
    """Both sides append a different line at the end of the same file,
    the other's pushed, the local one not yet saved."""
    change(other_clone, "10-intent.md", "\n- **POS.0030** A light in the shed.\n")
    git(["commit", "-q", "-am", "other: a light"], other_clone, env)
    git(["push", "-q"], other_clone, env)
    change(repo, "10-intent.md", "\n- **POS.0030** A bench by the shed.\n")


def test_a_conflict_at_save_stands_and_the_step_of_a_conflict_finishes_it(repo, other_clone, git_env, run_script):
    conflicting_change(repo, other_clone, git_env)
    r = run_script("forge-save", repo, "-m", "fixture: a bench", env=git_env)
    assert r.returncode != 0
    said = r.stdout + r.stderr
    assert "conflict" in said and "10-intent.md" in said and "rebase --continue" in said
    assert "nothing was lost" in said
    # the commit is made and the rebase stands
    assert git(["log", "-1", "--format=%s", "main"], repo, git_env) == "fixture: a bench"
    assert "rebase in progress" in run_script("forge-status", repo, env=git_env).stdout
    # the step of a conflict, as the message says: settle, add, continue, save again
    text = (repo / "10-intent.md").read_text(encoding="utf-8")
    assert "<<<<<<<" in text
    settled = text.split("<<<<<<<")[0] + "- **POS.0030** A light in the shed.\n- **POS.0040** A bench by the shed.\n"
    (repo / "10-intent.md").write_text(settled, encoding="utf-8")
    git(["add", "10-intent.md"], repo, git_env)
    git(["rebase", "--continue"], repo, {**git_env, "GIT_EDITOR": "true"})
    r = run_script("forge-save", repo, env=git_env)
    assert r.returncode == 0, r.stderr
    assert "ahead of origin, pushing" in r.stdout
    assert git(["log", "--format=%s"], repo.parent / "origin.git", git_env).splitlines()[:2] == ["fixture: a bench", "other: a light"]
    assert "<<<<<<<" not in git(["show", "main:10-intent.md"], repo.parent / "origin.git", git_env)


def test_a_standing_rebase_is_refused_before_anything_is_staged(repo, other_clone, git_env, run_script):
    conflicting_change(repo, other_clone, git_env)
    assert run_script("forge-save", repo, "-m", "fixture: a bench", env=git_env).returncode != 0
    change(repo, "00-brief.md", "\nThe gate is on the north side.\n")
    r = run_script("forge-save", repo, "-m", "fixture: the gate", env=git_env)
    assert r.returncode != 0
    assert "in progress" in r.stdout + r.stderr and "nothing was staged" in r.stdout + r.stderr
    assert "00-brief.md" not in git(["diff", "--cached", "--name-only"], repo, git_env).splitlines()
    assert "rebase in progress" in run_script("forge-status", repo, env=git_env).stdout


def both_change_the_readme(repo, other_clone, env):
    change(other_clone, "README.md", "\nMade again on the other side.\n")
    git(["commit", "-q", "-am", "other: readme"], other_clone, env)
    git(["push", "-q"], other_clone, env)
    change(repo, "README.md", "\nMade again here.\n")


def test_a_derived_file_is_taken_as_ours_where_the_driver_is_registered(repo, other_clone, git_env, run_script):
    import forge_repos as fr
    for key, value in fr.REGISTRATION:                     # what /setup registers, in the test's global file
        git(["config", "--global", key, value], repo, git_env)
    both_change_the_readme(repo, other_clone, git_env)
    r = run_script("forge-save", repo, "-m", "fixture: readme", env=git_env)
    assert r.returncode == 0, r.stderr + r.stdout
    assert "saved and pushed" in r.stdout
    text = (repo / "README.md").read_text(encoding="utf-8")
    assert "<<<<<<<" not in text
    # one whole side, never a merge: at a rebase, "ours" is the side rebased onto (git's own meaning)
    assert ("Made again here." in text) != ("Made again on the other side." in text)


def test_without_the_registration_the_same_derived_file_conflicts(repo, other_clone, git_env, run_script):
    both_change_the_readme(repo, other_clone, git_env)
    r = run_script("forge-save", repo, "-m", "fixture: readme", env=git_env)
    assert r.returncode != 0
    assert "README.md" in r.stdout + r.stderr and "conflict" in r.stdout + r.stderr


def test_the_root_derived_files_are_ours_and_a_recipe_of_the_same_name_is_not(repo, git_env):
    # The three root patterns are anchored with a slash: a bare name
    # matches at every depth and, with core.ignorecase (the default on
    # Windows and macOS), in every case, so recipes/readme.md was taken
    # as ours at a merge (SOL.0730, 2026-11-08). The repository is set
    # case-insensitive so that the test says the same on every machine.
    git(["config", "core.ignorecase", "true"], repo, git_env)
    assert git(["check-attr", "merge", "README.md"], repo, git_env).endswith("merge: ours")
    assert git(["check-attr", "merge", "recipes/readme.md"], repo, git_env).endswith("merge: unspecified")
    assert git(["check-attr", "merge", "recipes/readme.history.md"], repo, git_env).endswith("merge: unspecified")
