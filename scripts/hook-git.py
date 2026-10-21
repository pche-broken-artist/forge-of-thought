#!/usr/bin/env python3
"""
hook-git.py - PreToolUse hook of the engine on the Bash tool: the wall
between reading git and writing it (POS.0550, POS.1200, SOL.0520).

WHAT IT DOES
    Claude Code runs this script before every Bash command Claude
    sends (configured in .claude/settings.json; the PowerShell tool
    stays closed to git whole by a deny rule, so that there is one
    parser and one door). The script reads the command from the
    hook's JSON on stdin, splits it at the shell's separators, and
    judges every part that calls git:
      - a reading verb (status, log, diff, show, fetch, ...) with
        reading flags: allow;
      - everything else: deny, with the script of the forge to use
        instead where one exists. Denied are the writing verbs, a
        verb the script does not know (an alias among them), a
        reading verb with a writing flag (branch -d, tag v1, config
        with a value, log --output, fetch --prune), a global option
        that changes how git runs (-c, --git-dir, --work-tree,
        --exec-path), git inside another command (xargs, sh -c, a
        substitution) and a part the script cannot read. It never
        answers ask: an ask is not known to hold in an automatic
        permission mode, a deny holds in every mode.
    A part that is not git is left to the harness: the hook answers
    allow only where every part of the command is a reading git,
    deny where any part is a git it refuses, and nothing otherwise.
    The reason of a deny names the rule and the door: the scripts in
    scripts/ are the only door to a write of git.

    It reads no file and writes nothing. The hook is for Claude's
    tools alone; the principal's own git from the shell is his.

WHAT IT NEEDS
    Python 3.8 or newer on PATH as `python`. Nothing else.

USAGE
    python scripts/hook-git.py            # as a hook: JSON on stdin
    python scripts/hook-git.py --test     # the built-in cases, exit 1 on a failure
    echo 'git status' | python scripts/hook-git.py --judge   # one command, the verdict printed
"""
import json
import re
import shlex
import sys

DOOR = "the scripts in scripts/ are the only door to a write of git (CLAUDE.md, Persistence; POS.1200)"

# the script of the forge that does what the denied verb would do
INSTEAD = {
    "commit": "python scripts/forge-save.py <slug> -m \"<message>\" (/save)",
    "push": "python scripts/forge-save.py <slug> (/save)",
    "add": "python scripts/forge-save.py <slug> (/save stages everything it commits)",
    "rm": "remove the file and let /save commit it",
    "mv": "rename the file and let /save commit it",
    "pull": "python scripts/forge-pull.py [slug] (/pull)",
    "checkout": "python scripts/forge-branch.py <slug> <branch> (a branch) or the principal's own hand (a file)",
    "switch": "python scripts/forge-branch.py <slug> <branch>",
    "branch": "python scripts/forge-branch.py <slug> <branch>",
    "clone": "python scripts/forge-clone.py <git-url> (/import-project)",
    "config": "python scripts/forge-config.py (/setup) for the global file; a repository's configuration is the principal's",
    "merge": "a merge is git's, by the principal's hand or by a merge request (CLAUDE.md, Persistence)",
    "rebase": "the one rebase of the forge is /save's (python scripts/forge-save.py)",
    "tag": "python scripts/forge-save.py <slug> --tag <name>, or /release",
    "fetch": "python scripts/forge-status.py --remote (fetches without pruning)",
    "init": "the principal's one-off act: git -C projects/<slug> init -b main (CLAUDE.md, Persistence)",
    "remote": "the principal's one-off act at creation (CLAUDE.md, Persistence)",
    "stash": "no script: ask the principal",
    "reset": "no script: ask the principal",
    "restore": "no script: ask the principal",
    "clean": "git clean is forbidden (POS.1740): ask the principal",
}

# verbs that only read, whatever their flags, bar the output flags below
READ = {
    "status", "log", "diff", "show", "ls-files", "ls-tree", "ls-remote", "blame",
    "annotate", "rev-parse", "rev-list", "describe", "cat-file", "merge-base",
    "for-each-ref", "name-rev", "shortlog", "check-ignore", "check-attr",
    "check-ref-format", "count-objects", "show-ref", "grep", "diff-tree",
    "diff-index", "diff-files", "var", "version", "help", "whatchanged",
    "range-diff", "cherry", "show-branch", "verify-commit", "verify-tag",
    "fsck", "merge-tree", "get-tar-commit-id", "rev-list",
}
# flags that make a reading verb write a file or run a program
READ_BAD = ("--output", "-o", "-O", "--open-files-in-pager", "--ext-diff", "--textconv")

GLOBAL_OK = {"--no-pager", "-P", "--paginate", "-p", "--no-optional-locks",
             "--literal-pathspecs", "--glob-pathspecs", "--noglob-pathspecs",
             "--icase-pathspecs", "--no-replace-objects", "--bare",
             "--version", "--help", "--html-path", "--man-path", "--info-path",
             "--exec-path"}  # bare --exec-path prints; with a value it changes (handled below)
GLOBAL_VALUE_OK = {"-C"}
GLOBAL_VALUE_BAD = {"-c", "--config-env", "--git-dir", "--work-tree", "--namespace",
                    "--super-prefix", "--list-cmds", "--attr-source"}

SEPARATORS = {";", "&&", "||", "|", "|&", "&", "(", ")", "\n"}


def split_parts(command):
    """The command as a list of token lists, one per simple command;
    None where the command cannot be read."""
    # heredoc bodies are text, not commands: cut them out first
    lines = command.split("\n")
    kept, i = [], 0
    while i < len(lines):
        line = lines[i]
        m = re.search(r"<<-?\s*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1", line)
        kept.append(line)
        i += 1
        if m:
            delim = m.group(2)
            while i < len(lines) and lines[i].strip() != delim:
                i += 1
            i += 1  # the delimiter line
    text = "\n".join(kept)
    try:
        lex = shlex.shlex(text, posix=True, punctuation_chars=";|&()")
        lex.whitespace_split = True
        lex.commenters = ""
        tokens = list(lex)
    except ValueError:
        return None
    parts, cur = [], []
    for t in tokens:
        if t in SEPARATORS or (set(t) <= set(";|&()") and t):
            if cur:
                parts.append(cur)
            cur = []
        elif "\n" in t:
            for piece in t.split("\n"):
                pass
            cur.append(t)
        else:
            cur.append(t)
    if cur:
        parts.append(cur)
    # a newline inside a token is a separator shlex did not see
    out = []
    for p in parts:
        chunk = []
        for t in p:
            if t == "\n":
                if chunk:
                    out.append(chunk)
                chunk = []
            else:
                chunk.append(t)
        if chunk:
            out.append(chunk)
    return out


def is_git(token):
    t = token.replace("\\", "/").lower()
    return t == "git" or t == "git.exe" or t.endswith("/git") or t.endswith("/git.exe")


def mentions_git_inside(token):
    """git inside a command substitution: not readable."""
    return bool(re.search(r"(\$\(|`).*\bgit\b", token))


# programs that run what they are given: git behind them is a command, not text
WRAPPERS = {"sh", "bash", "zsh", "dash", "ksh", "fish", "eval", "exec", "xargs", "env", "nohup",
            "timeout", "command", "builtin", "nice", "ionice", "time", "sudo", "doas", "watch",
            "setsid", "flock", "stdbuf", "noglob", "busybox", "find", "pwsh", "powershell",
            "cmd", "script"}
# interpreters run what they are given only with inline code; a script of the forge
# given a message that names git is text (THR.0400, the refusal of 2026-09-26)
INTERPRETERS = {"python", "python3", "perl", "ruby", "node"}


def git_behind(head, rest):
    """git run by a wrapper: as a bare token, or inside the script a shell is given."""
    name = head.replace("\\", "/").rsplit("/", 1)[-1].lower().replace(".exe", "")
    inline = name in INTERPRETERS and any(t in ("-c", "-e", "-E") for t in rest)
    if name not in WRAPPERS and not inline:
        return False
    return any(is_git(t) or re.search(r"\bgit\b", t) for t in rest)


def judge_git(tokens):
    """(verdict, reason) for one git invocation; verdict 'allow' | 'deny'."""
    i = 1
    # global options
    while i < len(tokens) and tokens[i].startswith("-"):
        t = tokens[i]
        if t in GLOBAL_VALUE_OK:
            i += 2
            continue
        if t.startswith("-C") and len(t) > 2 and not t.startswith("--"):
            i += 1
            continue
        if t in GLOBAL_OK:
            i += 1
            continue
        key = t.split("=", 1)[0]
        if key in GLOBAL_VALUE_BAD or t.startswith("-c") or key == "--exec-path":
            return "deny", f"global option {key} changes how git runs; {DOOR}"
        return "deny", f"global option {t} not known as reading; {DOOR}"
    if i >= len(tokens):
        return "allow", "git alone prints its usage"
    verb, args = tokens[i], tokens[i + 1:]
    return judge_verb(verb, args)


def flags_and_positionals(args, value_flags=()):
    flags, pos, skip = [], [], False
    for j, a in enumerate(args):
        if skip:
            skip = False
            continue
        if a == "--":
            pos.extend(args[j + 1:])
            break
        if a.startswith("-"):
            flags.append(a)
            if a in value_flags:
                skip = True
        else:
            pos.append(a)
    return flags, pos


def judge_verb(verb, args):
    deny = lambda why: ("deny", f"git {verb}: {why}; {DOOR}" + (f"; instead: {INSTEAD[verb]}" if verb in INSTEAD else ""))
    if verb in READ:
        for a in args:
            key = a.split("=", 1)[0]
            if key in READ_BAD:
                return deny(f"{key} writes a file or runs a program")
        return "allow", f"git {verb} reads"
    if verb == "fetch":
        for a in args:
            key = a.split("=", 1)[0]
            if key in ("--prune", "-p", "--prune-tags", "-P", "--force", "-f", "--update-head-ok", "-u", "--refmap", "--unshallow", "--negotiate-only"):
                return deny(f"{key} changes refs")
            if not a.startswith("-") and ":" in a and "://" not in a:
                return deny("a refspec writes a local ref")
        return "allow", "git fetch reads the remote"
    if verb == "branch":
        value = {"--contains", "--no-contains", "--merged", "--no-merged", "--points-at", "--sort", "--format", "--color", "--column", "--abbrev"}
        ok = {"-a", "--all", "-r", "--remotes", "-v", "-vv", "--verbose", "-l", "--list", "--show-current", "--no-color", "--no-column", "-i", "--ignore-case"}
        flags, pos = flags_and_positionals(args, value)
        listing = any(f in ("-l", "--list") for f in flags)
        for f in flags:
            key = f.split("=", 1)[0]
            if key not in ok and key not in value:
                return deny(f"{key} is not a listing flag")
        if pos and not listing:
            return deny("a name without --list creates or changes a branch")
        return "allow", "git branch lists"
    if verb == "tag":
        value = {"--contains", "--no-contains", "--merged", "--no-merged", "--points-at", "--sort", "--format", "--color", "--column"}
        ok = {"-l", "--list", "-n", "-v", "--verify", "-i", "--ignore-case", "--no-color", "--no-column"}
        flags, pos = flags_and_positionals(args, value)
        listing = any(f.split("=", 1)[0] in ("-l", "--list", "-v", "--verify") or f.startswith("-n") for f in flags)
        for f in flags:
            key = f.split("=", 1)[0]
            if key not in ok and key not in value and not key.startswith("-n"):
                return deny(f"{key} is not a listing flag")
        if pos and not listing:
            return deny("a name without --list creates a tag")
        return "allow", "git tag lists"
    if verb == "remote":
        flags, pos = flags_and_positionals(args)
        sub = pos[0] if pos else None
        if sub is None or sub in ("show", "get-url"):
            for f in flags:
                if f not in ("-v", "--verbose", "-n", "--push", "--all"):
                    return deny(f"{f} is not a reading flag")
            return "allow", "git remote lists"
        return deny(f"{sub} changes the remotes")
    if verb == "config":
        get = {"--get", "--get-all", "--get-regexp", "--get-urlmatch", "--list", "-l", "--get-color", "--get-colorbool"}
        scope = {"--global", "--local", "--system", "--worktree", "--show-origin", "--show-scope", "--name-only", "--null", "-z", "--includes", "--no-includes", "--bool", "--int", "--bool-or-int", "--path", "--expiry-date"}
        value = {"--type", "--default", "--file", "-f", "--blob"}
        flags, pos = flags_and_positionals(args, value)
        if pos and pos[0] in ("get", "list"):  # the subcommand form of git 2.46+
            return "allow", "git config reads"
        reading = any(f.split("=", 1)[0] in get for f in flags)
        for f in flags:
            key = f.split("=", 1)[0]
            if key not in get and key not in scope and key not in value:
                return deny(f"{key} writes the configuration")
        if reading and len(pos) <= 2 and not (len(pos) == 2 and not any(f.split("=", 1)[0] in ("--get-regexp", "--get-urlmatch", "--get-all", "--get") for f in flags)):
            return "allow", "git config reads"
        if not reading and len(pos) == 1:
            return "allow", "git config reads one key"
        return deny("a key with a value writes the configuration")
    if verb == "stash":
        if args and args[0] in ("list", "show"):
            return "allow", "git stash lists"
        return deny("stashes, applies or drops")
    if verb == "worktree":
        if args and args[0] == "list":
            return "allow", "git worktree lists"
        return deny("adds, moves or removes a working tree")
    if verb == "reflog":
        if not args or args[0] in ("show", "exists") or args[0].startswith("-"):
            return "allow", "git reflog shows"
        return deny("expires or deletes")
    if verb == "symbolic-ref":
        flags, pos = flags_and_positionals(args)
        if len(pos) == 1 and not any(f in ("-d", "--delete") for f in flags):
            return "allow", "git symbolic-ref reads"
        return deny("sets or deletes a symbolic ref")
    if verb == "notes" and args and args[0] in ("list", "show"):
        return "allow", "git notes lists"
    if verb == "submodule" and args and args[0] in ("status", "summary"):
        return "allow", "git submodule reads"
    if verb == "bundle" and args and args[0] in ("verify", "list-heads"):
        return "allow", "git bundle reads"
    if verb in INSTEAD:
        return deny("writes")
    return deny("not known as a reading verb (an alias is not read)")


def judge(command):
    """(verdict, reason) for a whole command; verdict 'allow' | 'deny' | None."""
    parts = split_parts(command)
    if parts is None:
        if re.search(r"\bgit\b", command):
            return "deny", f"the command cannot be read and names git; {DOOR}"
        return None, ""
    verdicts, reasons = [], []
    for part in parts:
        if not part:
            continue
        # leading environment assignments
        k = 0
        while k < len(part) and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", part[k]):
            k += 1
        if k >= len(part):
            verdicts.append("other")
            continue
        head, rest = part[k], part[k + 1:]
        if is_git(head):
            v, why = judge_git(part[k:])
            verdicts.append(v)
            reasons.append(why)
            continue
        if git_behind(head, rest):
            verdicts.append("deny")
            reasons.append(f"git behind `{head}` cannot be read; {DOOR}")
            continue
        if any(mentions_git_inside(t) for t in part):
            verdicts.append("deny")
            reasons.append(f"git inside a substitution or a script cannot be read; {DOOR}")
            continue
        verdicts.append("other")
    judged = [v for v in verdicts if v != "other"]
    if "deny" in verdicts:
        return "deny", "; ".join(r for v, r in zip(judged, reasons) if v == "deny")
    if "ask" in verdicts:
        return "ask", "; ".join(r for v, r in zip(judged, reasons) if v == "ask")
    if verdicts and all(v == "allow" for v in verdicts):
        return "allow", "; ".join(reasons)
    return None, ""


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
    ("git 'push' origin main", "deny"), ("git add .", "deny"), ("git pull", "deny"),
    ("git checkout main", "deny"), ("git checkout -- CLAUDE.md", "deny"), ("git switch -c x", "deny"),
    ("git restore CLAUDE.md", "deny"), ("git reset --hard", "deny"), ("git clean -fd", "deny"),
    ("git merge x", "deny"), ("git rebase main", "deny"), ("git cherry-pick abc", "deny"),
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


def run_tests():
    failed = 0
    for command, expected in CASES:
        verdict, reason = judge(command)
        ok = verdict == expected
        failed += not ok
        mark = "ok  " if ok else "FAIL"
        shown = command.replace("\n", "\\n")
        print(f"{mark} {str(expected):5} {str(verdict):5}  {shown}" + ("" if ok else f"\n        {reason}"))
    print(f"{len(CASES) - failed} of {len(CASES)} cases pass")
    return 1 if failed else 0


def main(argv):
    if "--test" in argv:
        return run_tests()
    data = sys.stdin.read()
    if "--judge" in argv:
        verdict, reason = judge(data.strip())
        print(verdict, reason)
        return 0
    try:
        hook = json.loads(data) if data.strip() else {}
    except json.JSONDecodeError:
        return 0
    if hook.get("tool_name") != "Bash":
        return 0
    command = (hook.get("tool_input") or {}).get("command") or ""
    verdict, reason = judge(command)
    if verdict is None:
        return 0
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": verdict,
        "permissionDecisionReason": reason}}))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
