---
generated: 2026-10-09
made: mirrored
inputs-hash: 19bf7e4afea23c04
inputs:
  - .claude/settings.json
  - .gitignore
  - templates/CLAUDE.local.md
  - .claude/skills/setup/SKILL.md
  - CLAUDE.md
  - projects/forge/40-solution-design.md
---

# Configuration

This page lists the files that configure an instance of the forge and says what each holds. It is for the person who sets up an instance and for the one who extends the engine.

## The files

| File | Shared | What it holds |
|---|---|---|
| `.claude/settings.json` | yes | The settings every instance shares, below. |
| `.claude/settings.local.json` | no, gitignored | The session model; created by `/setup`. |
| `CLAUDE.local.md` | no, gitignored | The principal, by role, and the conversation language; made from `templates/CLAUDE.local.md`. |
| `.gitignore` | yes | What the engine repository leaves out, below. |
| Git identity | outside the engine | Name and e-mail per git host, in the user's own git configuration, with a guard. |

## `.claude/settings.json`

- `attribution`: the commit attribution is empty and `sessionUrl` is false, so nothing is appended to a commit.
- `permissions.deny`: reading `~/.ssh/**` and `~/.aws/**` is denied, and so is raw `git` in both shells (`Bash(git *)` and `PowerShell(git *)`), because the scripts in `scripts/` are the only door to git.
- `hooks.UserPromptSubmit`: runs `python` on `${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.py` at every prompt, so the walkthrough rules hold in a long conversation.

## `.claude/settings.local.json`

Gitignored and per machine. `/setup` creates it with the session model and leaves an existing file untouched. The model can be changed later with `/model` or by editing the file.

## `CLAUDE.local.md`

Gitignored, at the engine root. It carries two entries: the principal (the role whose thinking is being forged) and the conversation language. `/setup` copies the template and fills it by interview, and leaves an existing file untouched.

## `.gitignore`

| Entry | Effect |
|---|---|
| `.claude/settings.local.json` | the local settings stay on the machine |
| `/CLAUDE.local.md` | the instance facts stay on the machine |
| `projects/*` with `!projects/forge` | every project is a repository of its own, and only the forge's own project is tracked; the pattern is `projects/*`, never `projects/`, so the re-include works |
| `/tmp/` | the principal's private scratch at the engine root |
| `__pycache__/` | Python byte-code caches |
| `Thumbs.db`, `desktop.ini`, `~$*` | Windows and office noise: folder metadata and lock files of open documents |

## Git identity

The engine keeps no roster of identities. Git resolves the commit identity per host from the user's own global git configuration: one `includeIf` stanza for the `https` form and one for the `ssh` form of each host, each pointing to a file beside the global one that holds `user.name` and `user.email`. The recommended guard is `user.useConfigOnly = true` with no global name or e-mail, so a repository on a host with no stanza fails aloud instead of taking a default; a global identity defeats the guard. `/setup` offers to write all of this on the user's word and prints it for hand application when declined. These are the only edits it makes outside the engine.

## See also

- [Set up the forge](../start/setup.md): the command that fills the instance files.
- [About how the rules are held](../about/how-the-rules-are-held.md): why the deny rules and the hook exist.
