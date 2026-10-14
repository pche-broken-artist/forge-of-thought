---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: cba39e65301d80ba
inputs:
  - .claude/settings.json
  - .gitignore
  - templates/CLAUDE.local.md
  - .claude/skills/setup/SKILL.md
  - CLAUDE.md#What this workspace is
---

# Configuration

This page lists the files that configure one instance of the forge (one installation of the engine) and states what each holds, field by field. It is for the person who installs the forge and for the person who extends it.

Two files are shared with everyone who clones the engine. Two are local to one machine and never committed. The git identity lives outside the engine. The command that fills the local files is described in [Set up the forge](../start/setup.md). A term used here without a gloss is in the [Glossary](glossary.md).

## Overview

| File | Shared | Holds |
|---|---|---|
| `.claude/settings.json` | yes | attribution, deny rules, the per-prompt hook |
| `.claude/settings.local.json` | no (gitignored) | the session model |
| `CLAUDE.local.md` | no (gitignored) | the principal by role, the conversation language |
| `.gitignore` | yes | what git leaves out of the engine |
| the global git configuration | outside the engine | the git identity per host, the guard |

## `.claude/settings.json`

Shared by every instance. It holds three groups of settings.

### Attribution

| Field | Value | Meaning |
|---|---|---|
| `attribution.commit` | empty | a commit message carries no attribution line |
| `attribution.sessionUrl` | `false` | no session link is added |

### Deny rules

Under `permissions.deny`, Claude may not use these.

| Rule | What it blocks |
|---|---|
| `Read(~/.ssh/**)` | reading the SSH directory of the home folder |
| `Read(~/.aws/**)` | reading the AWS directory of the home folder |
| `Bash(git *)` | raw git in the Bash shell |
| `PowerShell(git *)` | raw git in the PowerShell shell |

Git is reached only through the scripts in `scripts/`. The reasons for the deny rules are in [How the rules are held](../about/how-the-rules-are-held.md).

### Hook

| Field | Value | Meaning |
|---|---|---|
| event | `UserPromptSubmit` | the hook runs at every prompt the principal sends |
| `type` | `command` | the hook is a program |
| `command` | `python` | the program is `python`, taken from the PATH |
| `args` | `${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.py` | the script it runs, found from the engine root |

## `.claude/settings.local.json`

Local to one machine and gitignored. `/setup` creates it when it is missing and leaves an existing one untouched.

| Field | Holds |
|---|---|
| `model` | the session model, which the whole forge runs on, the blind reviewers included |

`/setup` writes the strongest model the account offers. It can be changed at any time with `/model` or by editing the file.

## `CLAUDE.local.md`

Local to one machine, gitignored, at the engine root. It carries instance facts: what belongs to this installation and not to the system. `/setup` copies it from `templates/CLAUDE.local.md` and fills it by interview, the language first. An existing file is reported and not touched.

| Field | Holds |
|---|---|
| Principal | the role of whoever's thinking is being forged, for example "the CTO" |
| Conversation language | the language the working conversation runs in |

The language of the documents is not set here. It follows the project's own rule.

## `.gitignore` of the engine

Shared. Each entry names what git leaves out.

| Entry | What it keeps out |
|---|---|
| `.claude/settings.local.json` | the machine's own settings |
| `/CLAUDE.local.md` | the instance facts |
| `projects/*`, except `projects/forge` | every project, each being a repository of its own |
| `Thumbs.db`, `desktop.ini` | Windows noise |
| `~$*` | lock files of open Office documents |
| `/tmp/` | the principal's private scratch at the engine root |
| `__pycache__/` | Python byte-code caches |

## The git identity, outside the engine

The git identity is git's own and is set per host, not in the engine. The engine sets none. `/setup` offers to write it, only on the principal's word, into the global git configuration file that git reads. It never overwrites existing content and it runs no git operation. A configuration the principal declines is printed for the principal to apply by hand.

For each host, written as `<host>`:

| Part | Holds |
|---|---|
| a stanza `[includeIf "hasconfig:remote.*.url:https://<host>/**"]` | the rule for remotes addressed by https |
| a stanza `[includeIf "hasconfig:remote.*.url:git@<host>:*/**"]` | the rule for remotes addressed by ssh |
| `path` in both stanzas | the absolute path of `.gitconfig-<host>`, beside the global file |
| `.gitconfig-<host>` | `[user]` with `name` and `email`, created when missing |

The global guard is `user.useConfigOnly = true` under `[user]`. A repository on a host with no stanza then fails aloud instead of taking a default. Where the global file already carries a `user.name` or `user.email`, the guard takes effect only once that identity is removed. `/setup` offers the removal, again only on the principal's word.

## See also

- [Set up the forge](../start/setup.md): the command that fills the instance files.
- [How the rules are held](../about/how-the-rules-are-held.md): why the deny rules and the hook exist.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
