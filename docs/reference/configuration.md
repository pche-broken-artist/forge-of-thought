---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: ac6ad4592db7521a
inputs:
  - .claude/settings.json
  - .gitignore
  - .gitattributes
  - templates/gitattributes
  - templates/gitignore
  - templates/project.md
  - templates/CLAUDE.local.md
  - pytest.ini
  - .claude/skills/setup/SKILL.md
  - scripts/forge-config.py
  - CLAUDE.md#What this workspace is
---

# Configuration

This page lists the files that configure an instance of the forge and a project, and what each holds, field by field. It is for the user who sets up an instance and for the extender who changes how the forge is held together. The principal (whoever's thinking is being forged) is named in these files by role, never by name. Terms of the forge are in the [Glossary](glossary.md).

## Overview

| File | Where | In git | What it configures |
|---|---|---|---|
| `.claude/settings.json` | engine | yes | attribution, deny rules, two hooks |
| `.claude/settings.local.json` | engine | no | the session model |
| `CLAUDE.local.md` | engine root | no | the instance facts |
| `.gitignore` | engine | yes | what the engine's repository never holds |
| `.gitignore` | each project | yes | what a project's repository never holds |
| `.gitattributes` | engine | yes | the merge ways of the engine |
| `.gitattributes` | each project | yes | the merge ways of a project |
| `project.md` | each project | yes | slug, kind, language |
| `pytest.ini` | engine | yes | how the tests run |
| the global git configuration | outside the engine | not applicable | identity per host, guard, merge driver |

The two files `/setup` fills in the engine are `CLAUDE.local.md` and `.claude/settings.local.json`; the command is described in [Set up the forge](../start/setup.md).

## .claude/settings.json

The shared settings of Claude Code for the engine. The reasons for the deny rules and the hooks are in [How the rules are held](../about/how-the-rules-are-held.md).

| Key | Value | Meaning |
|---|---|---|
| `attribution.commit` | empty string | a commit carries no trailer added by Claude Code |
| `attribution.sessionUrl` | `false` | no session link is added |
| `permissions.deny` | `Read(~/.ssh/**)` | Claude may not read the SSH directory of the user |
| `permissions.deny` | `Read(~/.aws/**)` | Claude may not read the AWS directory of the user |
| `permissions.deny` | `PowerShell(git *)` | Claude may not run git in the PowerShell tool |
| `hooks.UserPromptSubmit` | `python` with `scripts/hook-walkthrough.py` | runs at every prompt of the principal |
| `hooks.PreToolUse`, matcher `Bash` | `python` with `scripts/hook-git.py` | runs before every command in the Bash tool |

Both hooks are of type `command`. The script path is built from `${CLAUDE_PROJECT_DIR}`.

## .claude/settings.local.json

The settings of one machine. It is gitignored. `/setup` creates it where it is missing and leaves an existing one untouched. It holds one key, `model`, the model the session runs on; it can be changed with `/model` or by editing the file.

## CLAUDE.local.md

The instance facts. It is gitignored and lies at the engine root. `/setup` copies it from `templates/CLAUDE.local.md` and fills it by interview. It has three lines:

| Field | Holds |
|---|---|
| Principal | the role of the person whose thinking is forged, such as "the CTO" |
| Conversation language | the language the working conversation runs in |
| Author | the principal's short handle, written as the author of every history record he decides |

The language of the documents is not set here. It is the `language` of the project file.

## .gitignore of the engine

Entries, in the order of the file:

| Entry | Keeps out of git |
|---|---|
| `.claude/settings.local.json` | the local Claude Code settings |
| `/CLAUDE.local.md` | the instance facts |
| `projects/*` | every project, since each is a repository of its own |
| `!projects/forge` | re-includes the engine's own project |
| `projects/forge/ledger.md` | the ledger of the engine's own project, made at read time |
| `Thumbs.db`, `desktop.ini` | file-system noise of Windows |
| `~$*` | lock files of an open Office document |
| `__pycache__/` | Python byte-code caches |

## .gitignore of a project

Copied from `templates/gitignore` by `/new-project` as it stands.

| Entry | Keeps out of git |
|---|---|
| `ledger.md` | the ledger, made at read time |
| `~$*` | lock files of an open Office document |

## .gitattributes of the engine and of a project

The engine has its own list, since its derived files lie at the root and under `projects/forge/`. A project's list is copied from `templates/gitattributes`. What the attributes do at a merge is in [Working together on one project](../about/working-together.md), and the merge driver `ours` is explained in [Persistence in git](../about/persistence-in-git.md).

| Pattern | Attribute | Where | Meaning |
|---|---|---|---|
| `*` | `text=auto` | both | line endings are normalised between machines |
| `/README.md` | `merge=ours` | both | taken as ours at a merge, made again afterwards |
| `/RELEASE-NOTES.md` | `merge=ours` | both | the same |
| `/CONTRIBUTING.md` | `merge=ours` | both | the same |
| `docs/**` | `merge=ours` | both | the same |
| `renders/**` | `merge=ours` | project | the same |
| `published/*.md` | `merge=ours` | project | the same |
| `projects/forge/renders/**` | `merge=ours` | engine | the same |
| `projects/forge/published/*.md` | `merge=ours` | engine | the same |
| `published/*.pptx`, `published/*.docx` | `binary` | project | never merged |
| `projects/forge/published/*.pptx`, `projects/forge/published/*.docx` | `binary` | engine | never merged |

The three root files are anchored with a leading slash. A bare name would match at every depth and, on a case-insensitive file system, in every case.

## project.md

The project file, at the root of a project. It is written once at creation, by `/new-project` or by the migration, and never by a round of work. It is merged as text. It has front-matter with these fields:

| Field | Holds |
|---|---|
| `project` | the slug of the project |
| `kind` | `thought` or `library` |
| `language` | the language of the chain's artefacts, as an ISO 639-1 code; `en` in the template |
| `fixture` | `true` on a test fixture project only |

A project without this file is of the shape before the migration. The one remedy is `/migrate`.

## pytest.ini

How the tests run, from the engine root with `python -m pytest`. What the tests serve is in [The tests](../about/the-tests.md).

| Key | Value | Meaning |
|---|---|---|
| `testpaths` | `tests` | the directory pytest collects from |
| `pythonpath` | `scripts` | the scripts lie on the import path, so the shared modules import directly |

## The configuration outside the engine

`/setup` writes the global git configuration on the user's word, through `scripts/forge-config.py` and nowhere else. The script goes through `git config --global`, so it writes the file git itself reads. A key that already carries a value is left and reported. The script needs Python 3.8 or newer and git 2.36 or newer. Run bare, it changes nothing and shows what is there.

### Identity per host

Written by `python scripts/forge-config.py --identity <host> <name> <email>`.

| Key or file | Value |
|---|---|
| `includeIf "hasconfig:remote.*.url:https://<host>/**"` `.path` | `.gitconfig-<host>` |
| `includeIf "hasconfig:remote.*.url:git@<host>:*/**"` `.path` | `.gitconfig-<host>` |
| `.gitconfig-<host>`, key `user.name` | the name given |
| `.gitconfig-<host>`, key `user.email` | the e-mail given |

The path is relative to the global file, so the identity file lies beside it. A stanza with another path and an identity file with another name or e-mail are left; `--replace` rewrites them.

### The guard

Written by `--guard`.

| Key | Value | Meaning |
|---|---|---|
| `user.useConfigOnly` | `true` | a repository with no identity of its own fails aloud instead of taking a default |

The guard bites only once no global `user.name` or `user.email` is left. `--unset-identity` removes them.

### The registration of the merge driver ours

Written by `--register`. The keys hold for every repository the configuration serves.

| Key | Value | Meaning |
|---|---|---|
| `merge.ours.driver` | `true` | the merge driver `ours` |
| `merge.renormalize` | `true` | needed by the driver |
| `rebase.backend` | `merge` | the apply backend ignores drivers |
| `rerere.enabled` | `true` | a convenience |
| `merge.conflictStyle` | `zdiff3` | only with `--zdiff3` |

## See also

- [Set up the forge](../start/setup.md): the command that fills the instance files.
- [How the rules are held](../about/how-the-rules-are-held.md): why the deny rules and the hooks exist.
- [Persistence in git](../about/persistence-in-git.md): what the merge driver `ours` and the git hook are for.
- [Working together on one project](../about/working-together.md): what the attributes do at a merge.
- [The tests](../about/the-tests.md): what the test configuration serves.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
