---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: da131105060ffc4d
inputs:
  - .claude/settings.json
  - .gitignore
  - .gitattributes
  - templates/gitattributes
  - templates/gitignore
  - templates/project.md
  - templates/CLAUDE.local.md
  - .claude/skills/setup/SKILL.md
  - scripts/forge-config.py
  - CLAUDE.md#What this workspace is
---

# Configuration

This page lists the files that configure an instance of the forge (one installation of the engine) and a project, and what each holds, field by field. It is for the user who sets an instance up and the extender who changes how it is configured. The command that fills the instance files is described in [Set up the forge](../start/setup.md).

## Overview

| File | Where it lives | In git | Holds |
|---|---|---|---|
| `.claude/settings.json` | the engine | yes | attribution, deny rules, two hooks |
| `.claude/settings.local.json` | the engine | no | the session model |
| `CLAUDE.local.md` | the engine root | no | the principal, the conversation language, the author handle |
| `.gitignore` of the engine | the engine root | yes | what the engine never tracks |
| `.gitignore` of a project | the project root | yes | the ledger and Office lock files |
| `.gitattributes` of the engine | the engine root | yes | merge and binary rules by path |
| `.gitattributes` of a project | the project root | yes | the same, from a template |
| `project.md` | the project root | yes | slug, kind, language |
| global git configuration | outside the engine | not applicable | identity per host, the guard, the merge driver `ours` |

## `.claude/settings.json`

The shared settings of the engine. Claude Code (the program that runs Claude) reads it.

- `attribution.commit`: an empty string, so no trailer is appended to a commit message.
- `attribution.sessionUrl`: `false`, so no session link is added.
- `permissions.deny`: three rules.
  - `Read(~/.ssh/**)`: Claude may not read the SSH folder.
  - `Read(~/.aws/**)`: Claude may not read the AWS folder.
  - `PowerShell(git *)`: Claude may not run git in the other shell tool.
- `hooks.UserPromptSubmit`: runs `scripts/hook-walkthrough.py` through `python` at every prompt of the principal (the person whose thinking is forged).
- `hooks.PreToolUse`: runs `scripts/hook-git.py` through `python` before every use of the Bash tool.

Why the deny rules and the hooks exist is said in [How the rules are held](../about/how-the-rules-are-held.md). What the git hook is for is said in [Persistence in git](../about/persistence-in-git.md).

## `.claude/settings.local.json`

Gitignored. `/setup` creates it when it is missing and leaves it untouched when it exists.

- `model`: the model of the session (one working run of Claude). It is set to the strongest model the account offers. It can be changed with `/model` or by editing the file.

## `CLAUDE.local.md`

Gitignored, at the engine root. `/setup` copies `templates/CLAUDE.local.md` and fills it by interview. It holds three lines:

- `Principal`: the role of the one whose thinking is being forged.
- `Conversation language`: the language the working conversation runs in. The language of the documents is set by the project, not by this line.
- `Author`: the principal's short handle, written as the author of every history record the principal decides.

## `.gitignore` of the engine

- `.claude/settings.local.json`: the local settings.
- `/CLAUDE.local.md`: the instance facts.
- `projects/*` with `!projects/forge`: every project is a repository of its own, except the engine's own project, which is re-included.
- `projects/forge/ledger.md`: the ledger of the engine's own project, made at read time.
- `Thumbs.db` and `desktop.ini`: Windows noise.
- `~$*`: lock files of an open Office document.
- `__pycache__/`: Python byte-code caches.

## `.gitignore` of a project

Copied as it stands from `templates/gitignore` when a project is created.

- `ledger.md`: the ledger, made at read time and never in git.
- `~$*`: lock files of an open Office document (Word, PowerPoint, Excel).

## `.gitattributes` of the engine

Its own list, not a copy of the template, because its derived files lie at the root and under `projects/forge/`.

- `* text=auto`: line endings are normalised.
- `merge=ours` (the file of the current branch is taken at a merge and made again): `README.md`, `RELEASE-NOTES.md`, `CONTRIBUTING.md`, `docs/**`, `projects/forge/renders/**` and `projects/forge/published/*.md`.
- `binary`: `projects/forge/published/*.pptx` and `projects/forge/published/*.docx`.

## `.gitattributes` of a project

The file a project's own is copied from is `templates/gitattributes`.

- `* text=auto`: line endings are normalised.
- `merge=ours`: `renders/**`, `README.md`, `RELEASE-NOTES.md`, `CONTRIBUTING.md`, `docs/**` and `published/*.md`.
- `binary`: `published/*.pptx` and `published/*.docx`.

What the attributes do at a merge is said in [Working together on one project](../about/working-together.md). The record files carry no rule here, so git merges them as text.

## `project.md`

The project file, written once when the project is created or migrated. It has front-matter with three fields and no body.

- `project`: the slug of the project.
- `kind`: `thought` or `library`.
- `language`: the language of the chain's artefacts, as an ISO 639-1 code. It is `en` when the file gives none.

A fixture project (a project made for testing) also carries `fixture: true`. A project without this file has the shape from before the migration, and the one remedy is `/migrate`.

## The global git configuration

`/setup` writes these keys outside the engine, only on the user's word, and only through `scripts/forge-config.py`. The script writes into the file git itself reads, so it names no path. A key that already carries another value is reported and left, unless `--replace` is given for an identity. Bare `python scripts/forge-config.py` shows what is there and changes nothing.

### Identity per host

One call per host: `python scripts/forge-config.py --identity <host> <name> <email>`. It writes two stanzas and one identity file.

- `includeIf.hasconfig:remote.*.url:https://<host>/**.path`: `.gitconfig-<host>`.
- `includeIf.hasconfig:remote.*.url:git@<host>:*/**.path`: `.gitconfig-<host>`.
- The identity file `.gitconfig-<host>` lies beside the global file, because the path is relative to it. It holds `user.name` and `user.email`.

This needs git 2.36 or newer.

### The guard

`python scripts/forge-config.py --guard` writes `user.useConfigOnly = true`. A repository on a host with no identity then fails aloud instead of taking a default. It takes effect only once no global `user.name` or `user.email` is left. `--unset-identity` removes them.

### The merge driver `ours`

`python scripts/forge-config.py --register` writes four keys. They hold for every repository the configuration serves.

- `merge.ours.driver = true`: registers the merge driver `ours`.
- `merge.renormalize = true`: renormalises line endings at a merge.
- `rebase.backend = merge`: the apply backend ignores merge drivers.
- `rerere.enabled = true`: git remembers how a conflict was resolved. This is a convenience.

`--zdiff3` adds `merge.conflictStyle = zdiff3`. What the driver and the git hook are for is said in [Persistence in git](../about/persistence-in-git.md).

## See also

- [Set up the forge](../start/setup.md): the command that fills the instance files.
- [How the rules are held](../about/how-the-rules-are-held.md): why the deny rules and the hooks exist.
- [Persistence in git](../about/persistence-in-git.md): what the merge driver `ours` and the git hook are for.
- [Working together on one project](../about/working-together.md): what the attributes do at a merge.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
