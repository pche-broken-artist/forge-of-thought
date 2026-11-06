"""
The judgement of scripts/hook-git.py over a command: every case is one
command and the verdict expected of it, allow, ask, deny or None
(a command that is not git, left to the harness). The cases were the
hook's own `--test` until 2026-11-06 and moved here as the first test
of the suite (projects/forge/00-brief-tests.md). A case that fails
names the command and both verdicts.
"""
import pytest

CASES = [
    # reading
    ("git status", "allow"), ("git status --short", "allow"), ("git log --oneline -5", "allow"),
    ("git -C projects/flow-ba status", "allow"), ("git --no-pager log -3", "allow"),
    ("git diff HEAD~1 -- CLAUDE.md", "allow"), ("git show HEAD:README.md", "allow"),
    ("git ls-files projects/forge", "allow"), ("git blame -L 1,5 CLAUDE.md", "allow"),
    ("git fetch origin", "allow"), ("git fetch --all", "allow"), ("git ls-remote origin", "allow"),
    ("git branch", "allow"), ("git branch -a", "allow"), ("git branch --show-current", "allow"),
    ("git branch --list 'r*'", "allow"), ("git branch --contains abc123", "allow"),
    ("git tag", "allow"), ("git tag -l 'v*'", "allow"), ("git tag -n", "allow"),
    ("git remote -v", "allow"), ("git remote show origin", "allow"), ("git remote get-url origin", "allow"),
    ("git config --get user.name", "allow"), ("git config -l", "allow"), ("git config --global --list", "allow"),
    ("git config user.name", "allow"), ("git config --get-regexp 'includeIf.*'", "allow"),
    ("git stash list", "allow"), ("git worktree list", "allow"), ("git reflog", "allow"),
    ("git rev-parse --abbrev-ref HEAD", "allow"), ("git symbolic-ref --short HEAD", "allow"),
    ("git log --oneline | head -5", None), ("cd projects/flow-ba && git status", None),
    ("git status && git log -1", "allow"), ("git --version", "allow"), ("git", "allow"),
    ("git describe --tags", "allow"), ("git merge-base main origin/main", "allow"),
    ("git log --format=%H -1", "allow"), ("git diff --stat", "allow"),
    ("git check-ignore -v projects/forge/ledger.md", "allow"),
    ("git cat-file -p HEAD", "allow"), ("git for-each-ref refs/heads", "allow"),
    ("git grep -n 'POS.1200' -- projects/forge", "allow"),
    # writing
    ("git commit -m 'x'", "deny"), ("git push", "deny"), ("git push origin main", "deny"),
    ("git -C . push origin main", "deny"), ("git -c push.default=current push", "deny"),
    ("git 'push' origin main", "deny"), ("git pull", "deny"),
    ("git checkout main", "deny"), ("git checkout -- CLAUDE.md", "deny"), ("git switch -c x", "deny"),
    ("git restore CLAUDE.md", "deny"), ("git reset --hard", "deny"), ("git clean -fd", "deny"),
    ("git rebase main", "deny"), ("git cherry-pick abc", "deny"),
    # the step of a conflict: ask (R6.01)
    ("git add CLAUDE.md", "ask"), ("git add .", "ask"), ("git add -A", "ask"), ("git add -u -- projects/forge", "ask"),
    ("git -C projects/fixture add README.md", "ask"),
    ("git add -f x", "deny"), ("git add --force x", "deny"), ("git add -p", "deny"), ("git add -i", "deny"),
    ("git rebase --continue", "ask"), ("git rebase --abort", "ask"), ("git rebase --skip", "deny"),
    ("git rebase --continue --no-verify", "deny"), ("git rebase -i HEAD~3", "deny"),
    ("git merge --continue", "ask"), ("git merge --abort", "ask"), ("git merge x", "ask"),
    ("git merge origin/main", "ask"), ("git -C projects/fixture merge r1", "ask"),
    ("git merge --squash x", "deny"), ("git merge --no-commit x", "deny"), ("git merge -X ours x", "deny"),
    ("git merge x y", "deny"), ("git merge", "deny"),
    ("git checkout --ours CLAUDE.md", "ask"), ("git checkout --theirs -- a.md b.md", "ask"),
    ("git checkout --ours", "deny"), ("git checkout --ours -b x", "deny"),
    ("git status && git add CLAUDE.md", "ask"), ("git add x && git push", "deny"),
    ("git rebase --continue 2>&1 | tail -3", "ask"), ("GIT_EDITOR=true git -C projects/x rebase --continue 2>&1", "ask"),
    ("git merge --abort > /dev/null 2>&1", "ask"), ("git status 2>/dev/null", "allow"), ("git log -1 > out.txt", "allow"),
    ("git rebase --continue --skip 2>&1", "deny"),
    ("git add x; git commit -m y", "deny"), ("sh -c 'git add x'", "deny"), ("echo $(git add x)", "deny"),
    ("git branch -d x", "deny"), ("git branch -D x", "deny"), ("git branch x", "deny"),
    ("git branch -m x y", "deny"), ("git branch --set-upstream-to=origin/main", "deny"),
    ("git tag v6", "deny"), ("git tag -d v6", "deny"), ("git tag -a v6 -m x", "deny"),
    ("git remote add origin x", "deny"), ("git remote set-url origin x", "deny"), ("git remote remove origin", "deny"),
    ("git config user.name X", "deny"), ("git config --global user.name X", "deny"),
    ("git config --unset user.name", "deny"), ("git config --add x y", "deny"), ("git config -e", "deny"),
    ("git stash", "deny"), ("git stash pop", "deny"), ("git stash drop", "deny"),
    ("git worktree add ../x", "deny"), ("git worktree remove x", "deny"),
    ("git reflog expire --all", "deny"), ("git symbolic-ref HEAD refs/heads/x", "deny"),
    ("git fetch --prune", "deny"), ("git fetch -p origin", "deny"), ("git fetch origin main:main", "deny"),
    ("git log --output=x.txt", "deny"), ("git diff --output x", "deny"), ("git grep -O x", "deny"),
    ("git init", "deny"), ("git clone x", "deny"), ("git gc --prune=now", "deny"), ("git filter-branch", "deny"),
    ("git update-ref -d refs/heads/x", "deny"), ("git format-patch -1", "deny"), ("git archive HEAD", "deny"),
    ("git st", "deny"), ("git lg", "deny"), ("git --git-dir=.git status", "deny"), ("git --work-tree=x status", "deny"),
    ("git --exec-path=/tmp status", "deny"), ("git -c alias.s='!rm' s", "deny"),
    ("git status; git push", "deny"), ("git status && git commit -m x", "deny"),
    ("echo $(git push)", "deny"), ("echo `git push`", "deny"), ("xargs git push", "deny"),
    ("sh -c 'git push'", "deny"), ("bash -c \"git push origin main\"", "deny"), ("eval git push", "deny"),
    ("FOO=1 git push", "deny"), ("timeout 5 git push", "deny"), ("/usr/bin/git push", "deny"),
    ("git.exe push", "deny"), ("GIT_DIR=x git status", "allow"),
    # text that only mentions git
    ("echo 'git push is denied'", None), ("grep -rn 'git push' docs/", None), ("python scripts/forge-save.py forge -m 'the door to git'", None),
    ("python scripts/forge-save.py forge -m \"never git push by hand\"", None),
    ("cat <<'EOF'\ngit push origin main\nEOF", None),
    ("python - <<'EOF'\nprint('git commit')\nEOF", None),
    ("ls", None), ("cat CLAUDE.md | grep git", None), ("python scripts/forge-ledger.py forge", None),
    ("find . -name x -exec git push \\;", "deny"), ("env git push", "deny"), ("nohup git push &", "deny"),
    ("grep -rn git scripts/", None), ("echo git", None),
    ("python -c \"import os; os.system('git push')\"", "deny"), ("python scripts/x.py git", None),
]


def _id(case):
    return case[0].replace("\n", "\\n")


@pytest.mark.parametrize("command,expected", CASES, ids=[_id(c) for c in CASES])
def test_judge(load_script, command, expected):
    hook = load_script("hook-git")
    verdict, reason = hook.judge(command)
    assert verdict == expected, reason
