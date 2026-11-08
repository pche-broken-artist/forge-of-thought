"""
The word `forge` in the commands of git names the whole: the engine,
and the forge's own project beside it where it is a repository of its
own (POS.1980; projects/forge/00-brief-tests.md). Before the cut the
project lies inside the engine's repository and the engine alone is
named; the tests run both states on a throwaway engine
(conftest.engine_repo, conftest.cut), the scripts pointed at it
through forge_repos.ENGINE_ROOT and run in-process, never on the live
engine (DEC.0240).
"""
import pytest

import forge_repos as fr
from conftest import cut, git


@pytest.fixture
def engine(engine_repo, git_env, monkeypatch):
    """The throwaway engine as the scripts' engine root, git reading
    the test's configuration alone."""
    monkeypatch.setattr(fr, "ENGINE_ROOT", engine_repo)
    for k, v in git_env.items():
        monkeypatch.setenv(k, v)
    return engine_repo


def change(path, name="10-intent.md", line="\n- **POS.0030** A light in the shed.\n"):
    with open(path / name, "a", encoding="utf-8") as f:
        f.write(line)


# ---- forge_repos

def test_before_the_cut_the_project_is_the_engines_and_forge_names_the_engine_alone(engine):
    proj = engine / "projects" / "forge"
    assert fr.inside_engine(proj) and not fr.own_repo(proj)
    assert not fr.inside_engine(engine)                       # the root is not inside itself
    assert fr.forge_repos() == [("forge (engine)", engine)]
    assert fr.repos_to_visit("forge") == [("forge (engine)", engine)]
    assert fr.repos_to_visit(None) == [("forge (engine)", engine)]   # passed over in silence


def test_after_the_cut_forge_names_the_engine_and_the_project_beside_it(engine, git_env):
    proj = cut(engine, git_env)
    assert fr.own_repo(proj) and not fr.inside_engine(proj)
    assert fr.forge_repos() == [("forge (engine)", engine), ("forge (project)", proj)]
    assert fr.repos_to_visit("forge") == fr.forge_repos()
    assert fr.repos_to_visit(None) == fr.forge_repos()        # the sweep names it once, as the project


def test_a_project_outside_git_is_still_reported_in_the_sweep(engine, git_env, capsys):
    (engine / "projects" / "other").mkdir()
    (engine / "projects" / "other" / "project.md").write_text("---\nproject: other\n---\n", encoding="utf-8")
    assert fr.repos_to_visit(None) == [("forge (engine)", engine)]
    out = capsys.readouterr().out
    assert "other" in out and "not under git" in out


# ---- forge-save

def test_save_of_forge_commits_the_engine_and_the_project_each_its_own(engine, git_env, load_script):
    proj = cut(engine, git_env)
    save = load_script("forge-save")
    change(engine, "CLAUDE.md", "\nmore of the core\n")
    change(proj)
    assert save.main(["forge", "-m", "forge: both sides"]) == 0
    for repo, origin in ((engine, "engine-origin.git"), (proj, "forge-origin.git")):
        assert git(["log", "-1", "--format=%s"], repo, git_env) == "forge: both sides"
        assert git(["rev-parse", "HEAD"], repo, git_env) == git(["rev-parse", "main"], engine.parent / origin, git_env)
    assert "projects/forge" not in git(["ls-files"], engine, git_env)   # the engine tracks no project


def test_the_tag_of_forge_goes_on_the_engine_alone(engine, git_env, load_script):
    proj = cut(engine, git_env)
    save = load_script("forge-save")
    change(engine, "CLAUDE.md", "\nreleased\n")
    change(proj)
    assert save.main(["forge", "-m", "release 7.0: the cut", "--tag", "v7"]) == 0
    assert git(["tag"], engine, git_env) == "v7"
    assert git(["tag"], proj, git_env) == ""
    assert git(["tag"], engine.parent / "engine-origin.git", git_env) == "v7"


def test_before_the_cut_a_save_of_forge_is_the_engines_commit(engine, git_env, load_script):
    save = load_script("forge-save")
    change(engine / "projects" / "forge")
    assert save.main(["forge", "-m", "forge: a light"]) == 0
    assert git(["log", "-1", "--format=%s"], engine, git_env) == "forge: a light"


# ---- forge-status

def test_status_of_forge_shows_both_after_the_cut_and_the_engine_alone_before(engine, git_env, load_script, capsys):
    status = load_script("forge-status")
    assert status.main([]) == 0
    out = capsys.readouterr().out
    assert "== forge (engine)" in out and "== forge (project)" not in out and "not under git" not in out
    cut(engine, git_env)
    assert status.main(["forge"]) == 0
    out = capsys.readouterr().out
    assert "== forge (engine)" in out and "== forge (project)" in out
    assert status.main([]) == 0
    assert out.count("== forge") == 2


def test_status_of_a_directory_the_engine_tracks_says_so(engine, load_script, capsys):
    status = load_script("forge-status")
    assert status.main([str(engine / "projects" / "forge")]) == 0
    assert "inside the engine's repository" in capsys.readouterr().out


# ---- forge-branch

def test_branch_of_forge_switches_both_together(engine, git_env, load_script):
    proj = cut(engine, git_env)
    branch = load_script("forge-branch")
    assert branch.main(["forge", "cut-trial"]) == 0
    for repo in (engine, proj):
        assert git(["rev-parse", "--abbrev-ref", "HEAD"], repo, git_env) == "cut-trial"
    assert branch.main(["forge", "main"]) == 0
    for repo in (engine, proj):
        assert git(["rev-parse", "--abbrev-ref", "HEAD"], repo, git_env) == "main"


def test_unsaved_changes_in_one_stop_the_switch_of_both(engine, git_env, load_script):
    proj = cut(engine, git_env)
    branch = load_script("forge-branch")
    change(proj)
    with pytest.raises(SystemExit):
        branch.main(["forge", "cut-trial"])
    for repo in (engine, proj):
        assert git(["rev-parse", "--abbrev-ref", "HEAD"], repo, git_env) == "main"


# ---- forge-ledger

def test_the_ledger_finds_a_root_render_through_the_recipes_output(engine, git_env, load_script):
    proj = engine / "projects" / "forge"
    recipe = proj / "recipes" / "readme.md"
    recipe.write_text(recipe.read_text(encoding="utf-8").replace("output: README.md", "output: /README.md"), encoding="utf-8")
    (proj / "README.md").rename(engine / "README.md")
    ledger = load_script("forge-ledger")
    out = engine.parent / "ledger-out.md"
    assert ledger.main([str(proj), "--out", str(out)]) == 0
    text = out.read_text(encoding="utf-8")
    assert "| README.md (engine root) |" in text
    assert "| README.md |" not in text
    cut(engine, git_env)   # the same after the cut: the root render lies in the engine
    assert ledger.main([str(proj), "--out", str(out)]) == 0
    assert "| README.md (engine root) |" in out.read_text(encoding="utf-8")
