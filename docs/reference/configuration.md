---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 248790b2e3857c29
inputs:
  - .claude/settings.json
  - .gitignore
  - templates/CLAUDE.local.md
  - .claude/skills/setup/SKILL.md
  - CLAUDE.md#What this workspace is
---

# Configuration

This page lists the files that configure one instance of the forge and what each holds, field by field. It is for the user who sets up an instance and for the extender who needs to know which file carries which setting. The command that fills the instance files is described in [Set up the forge](../start/setup.md). Terms of the forge are explained in the [Glossary](glossary.md).

## Overview

| File | Shared | Holds | Made by |
|---|---|---|---|
| `.claude/settings.json` | yes | attribution, deny rules, the prompt hook | the engine |
| `.claude/settings.local.json` | no (gitignored) | the session model | `/setup` |
| `CLAUDE.local.md` | no (gitignored) | the principal and the conversation language | `/setup`, from its template |
| `.gitignore` | yes | what git leaves out of the engine | the engine |
| the git identity | outside the engine | name and e-mail per host, and the guard | `/setup`, on the user's word |

## `.claude/settings.json`

The shared settings of the engine, the same on every instance.

| Field | Value | What it does |
|---|---|---|
| `attribution.commit` | empty | adds no attribution line to a commit |
| `attribution.sessionUrl` | `false` | adds no session link to what is written |
| `permissions.deny` | `Read(~/.ssh/**)` | Claude may not read the SSH folder of the home directory |
| `permissions.deny` | `Read(~/.aws/**)` | Claude may not read the AWS folder of the home directory |
| `permissions.deny` | `Bash(git *)` | Claude may not run raw git in the Bash shell; git is reached only through the scripts of `scripts/` |
| `permissions.deny` | `PowerShell(git *)` | the same rule for the PowerShell shell |
| `hooks.UserPromptSubmit` | one command hook | runs before each prompt of the principal (the person whose thinking is forged) is handled |

The hook runs `python` with one argument, `${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.py`. The placeholder `${CLAUDE_PROJECT_DIR}` stands for the project directory of the session, so the same line works on every machine. The script repeats the walkthrough rule at every prompt so that it holds in a long conversation. Why the deny rules and the hook exist is told in [How the rules are held](../about/how-the-rules-are-held.md).

## `.claude/settings.local.json`

Gitignored, so it belongs to one machine.

| Field | Holds |
|---|---|
| `model` | the model the session runs on; the whole forge, the isolated reviewers included, runs on it |

`/setup` creates the file when it is missing and leaves an existing one untouched. The model can be changed at any time with `/model` or by editing the file.

## `CLAUDE.local.md`

Gitignored, at the engine root. `/setup` copies it from `templates/CLAUDE.local.md` and fills it by interview, and it leaves an existing file untouched. It holds the facts of the instance, which are not properties of the system.

| Field | Holds |
|---|---|
| Principal | the role of the person whose thinking is being forged (for example "the CTO"), never a name needed by the system |
| Conversation language | the language the working conversation runs in; the language of the documents follows the project, not this field |

## `.gitignore` of the engine

| Entry | What it leaves out |
|---|---|
| `.claude/settings.local.json` | the local settings of one machine |
| `/CLAUDE.local.md` | the instance facts |
| `projects/*` | every project, because each is a repository of its own |
| `!projects/forge` | re-includes the engine's own project; the pattern is `projects/*` and never `projects/` so that the re-include works |
| `/tmp/` | private scratch at the engine root |
| `Thumbs.db`, `desktop.ini` | Windows file-manager noise |
| `~$*` | lock files of open office documents |
| `__pycache__/` | Python byte-code caches, which the documentation scripts create |

## The git identity

This is not a file of the engine. Git reads it from the global git configuration of the user, per host, and the forge sets none by itself. `/setup` offers to write it on the user's word, reads the file first and never overwrites existing content.

| Part | Holds |
|---|---|
| Stanza for HTTPS remotes | `[includeIf "hasconfig:remote.*.url:https://<host>/**"]` with `path` set to the absolute path of `.gitconfig-<host>` |
| Stanza for SSH remotes | `[includeIf "hasconfig:remote.*.url:git@<host>:*/**"]` with the same `path` |
| `.gitconfig-<host>` | `[user]` with `name` and `email` for that host, created beside the global file when missing |
| Guard | `user.useConfigOnly = true` under `[user]`, so that a repository on a host without a stanza fails aloud instead of taking a default |

The `path` is absolute because `~` may mean different things to git and to the shell. The guard only takes effect once a `user.name` or `user.email` in the global file is removed. If the user declines, `/setup` prints the stanzas and the lines to apply by hand.

## See also

- [Set up the forge](../start/setup.md): the command that fills the instance files.
- [How the rules are held](../about/how-the-rules-are-held.md): why the deny rules and the hook exist.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
