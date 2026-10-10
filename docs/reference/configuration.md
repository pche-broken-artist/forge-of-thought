---
generated: 2026-10-10
made: mirrored
inputs-hash: 8da0907a6edcc498
inputs:
  - .claude/settings.json
  - .gitignore
  - templates/CLAUDE.local.md
  - .claude/skills/setup/SKILL.md
  - CLAUDE.md
  - projects/forge/40-solution-design.md
---

# Configuration

This page lists the files that configure an instance of the forge and
what each one holds. It is for the person who sets up an instance and
for the one who extends the engine and needs to know where a setting
lives.

## Files in the engine

| File | Shared | What it holds |
|---|---|---|
| `.claude/settings.json` | yes | The shared settings of Claude Code, in the four items below. |
| `.claude/settings.local.json` | no, gitignored | The session model; `/setup` creates it. |
| `CLAUDE.local.md` | no, gitignored | The principal, named by role, and the conversation language; made from `templates/CLAUDE.local.md`. |
| `.gitignore` | yes | What git leaves out of the engine, listed below. |

### `.claude/settings.json`

- **Attribution:** `attribution.commit` is empty and
  `attribution.sessionUrl` is false, so no co-author or session
  trailer is added to a commit.
- **Deny rules for sensitive paths:** `Read(~/.ssh/**)` and
  `Read(~/.aws/**)` keep credentials out of reach.
- **Deny rules for raw git:** `Bash(git *)` and `PowerShell(git *)`
  deny the `git` command in both shells, so the scripts in `scripts/`
  are the only door to git.
- **The `UserPromptSubmit` hook:** it runs `scripts/hook-walkthrough.py`
  through `python`, with the script's path anchored at the project
  directory by the `${CLAUDE_PROJECT_DIR}` placeholder.

### `.claude/settings.local.json`

Gitignored and per machine. `/setup` creates it with the session
model and leaves an existing file untouched. The model can be changed
at any time with `/model` or by editing the file.

### `CLAUDE.local.md`

Gitignored, at the engine root. It carries two facts: the principal,
given as a role, and the conversation language. `/setup` copies the
template and fills it by interview, and leaves an existing file
untouched. The language of the documents is not set here; it follows
the project's own setting.

### `.gitignore` of the engine

| Entry | Effect |
|---|---|
| `.claude/settings.local.json` | the local settings stay on the machine |
| `/CLAUDE.local.md` | the instance facts stay on the machine |
| `projects/*` with `!projects/forge` | every project is a repository of its own, except the engine's own project, which is re-included; the pattern must be `projects/*`, not `projects/`, or the re-include fails |
| `/tmp/` | the principal's private scratch at the engine root |
| `__pycache__/` | Python byte-code caches |
| `Thumbs.db`, `desktop.ini`, `~$*` | Windows and office noise, including lock files of open documents |

## The git identity, outside the engine

The engine configures no git identity. Git resolves it per host from
the user's own global git configuration: one `includeIf` stanza per
host (one for `https` remotes, one for `ssh` remotes) pointing at a
`.gitconfig-<host>` file that holds `name` and `email`. Beside them
stands one global guard, `user.useConfigOnly = true`, with no global
`user.name` or `user.email`, so a repository on a host without a
stanza fails aloud instead of taking a default. A global identity that
survives defeats the guard. `/setup` offers to write these on the
user's word, never overwrites existing content, and otherwise prints
them to apply by hand.

## See also

- [Set up the forge](../start/setup.md): the command that fills the instance files.
- [About how the rules are held](../about/how-the-rules-are-held.md): why the deny rules and the hook exist.
