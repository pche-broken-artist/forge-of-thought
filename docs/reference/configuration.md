---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: ba15024fcd980d8e
inputs:
  - .claude/settings.json
  - .gitignore
  - .gitattributes
  - templates/gitattributes
  - templates/project.md
  - templates/CLAUDE.local.md
  - .claude/skills/setup/SKILL.md
  - CLAUDE.md#What this workspace is
---

# Configuration

This page lists the files that configure an instance of the forge and
a project in it, and what each holds, field by field. It is for the
person who installs the forge and for the one who extends it. The
principal is the person whose thinking is being forged. A session is
one running conversation with Claude.

The command that fills the instance files is described in
[Set up the forge](../start/setup.md).

## Overview

| File | Where | Shared in git | Holds |
|---|---|---|---|
| `.claude/settings.json` | engine | yes | attribution, deny rules, the prompt hook |
| `.claude/settings.local.json` | engine | no | the session model |
| `CLAUDE.local.md` | engine root | no | the principal, the conversation language, the author handle |
| `.gitignore` | engine | yes | what git leaves out |
| `.gitattributes` | engine | yes | how derived and binary files merge |
| `templates/gitattributes` | engine | yes | the template of a project's own `.gitattributes` |
| `project.md` | each project | yes | slug, kind, language |
| global git configuration | outside the engine | no | git identity per host, the guard, the merge settings |

## .claude/settings.json

Shared by every instance. It holds three groups of settings.

`attribution`:

- `commit`: an empty string, so no trailer is added to a commit message.
- `sessionUrl`: `false`, so no session address is added.

`permissions.deny`: paths and commands Claude may not use.

- `Read(~/.ssh/**)`: the secure-shell key folder.
- `Read(~/.aws/**)`: the cloud credentials folder.
- `Bash(git *)`: raw git in the Bash shell.
- `PowerShell(git *)`: raw git in the PowerShell shell.

`hooks.UserPromptSubmit`: one command hook, run at every prompt.

- `command`: `python`
- `args`: `${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.py`

Why the deny rules and the hook exist is told in
[How the rules are held](../about/how-the-rules-are-held.md).

## .claude/settings.local.json

Gitignored, so it differs per machine. `/setup` creates it when it is
missing and does not touch it when it exists. It holds one field,
`model`: the model of the session. `/setup` writes the strongest model
the account offers. It can be changed at any time with `/model` or by
editing the file.

## CLAUDE.local.md

Gitignored, at the engine root. `/setup` copies it from
`templates/CLAUDE.local.md` and fills it by interview. It holds three
lines:

- **Principal**: the role of the principal, that is whose thinking is
  being forged.
- **Conversation language**: the language the working conversation
  runs in.
- **Author**: the principal's short handle. It is the author of every
  history record the principal decides, and the key of the
  principal's block of IDs.

These are facts of the instance, not properties of the system.

## .gitignore of the engine

Entries, in the order of the file:

- `.claude/settings.local.json`: the local settings.
- `/CLAUDE.local.md`: the instance facts.
- `projects/*` with `!projects/forge`: every project is a repository
  of its own and is left out, except the forge project. The pattern is
  `projects/*` and not `projects/`, so that the re-include works.
- `projects/forge/ledger.md`: the ledger of the forge project, which
  is made at read time and never kept in git.
- `/tmp/`: private scratch at the engine root.
- Operating system noise (`Thumbs.db`, `desktop.ini`), Office lock
  files (`~$*`) and Python byte-code caches (`__pycache__/`).

## .gitattributes of the engine

The engine's own list, not a copy of the template, because its derived
files lie at the root and under `projects/forge/`.

| Pattern | Attribute | Meaning |
|---|---|---|
| `*` | `text=auto` | line endings are normalised so files do not fight between machines |
| `README.md`, `RELEASE-NOTES.md`, `CONTRIBUTING.md` | `merge=ours` | derived, taken as ours at a merge and made again |
| `docs/**` | `merge=ours` | as above |
| `projects/forge/renders/**` | `merge=ours` | as above |
| `projects/forge/published/*.md` | `merge=ours` | as above |
| `projects/forge/published/*.pptx`, `projects/forge/published/*.docx` | `binary` | published files, never merged |

## templates/gitattributes

The template a project's own `.gitattributes` is copied from. Its paths
lie at the project root.

| Pattern | Attribute | Meaning |
|---|---|---|
| `*` | `text=auto` | line endings are normalised |
| `renders/**` | `merge=ours` | derived, taken as ours at a merge and made again |
| `README.md`, `RELEASE-NOTES.md`, `CONTRIBUTING.md` | `merge=ours` | as above |
| `docs/**` | `merge=ours` | as above |
| `published/*.md` | `merge=ours` | as above |
| `published/*.pptx`, `published/*.docx` | `binary` | published files, never merged |

What the attributes and the merge settings are for is told in
[Persistence in git](../about/persistence-in-git.md).

## project.md

The project file, in the root of each project. It is written once, at
the creation of the project, by `/new-project` or by the migration.
It is merged as text. It has three front-matter fields:

| Field | Value | Meaning |
|---|---|---|
| `project` | the slug | the name of the project |
| `kind` | `thought` or `library` | whether the project has a chain or only shares material |
| `language` | an ISO 639-1 code, such as `en` | the language of the chain's artefacts |

A fixture project also carries `fixture: true`. A project without the
file has the shape from before the migration, and the one remedy is
`/migrate`.

## Configuration outside the engine

`/setup` can write these into the global git configuration, which git
itself reads. It asks first, reads the file first, never overwrites
existing content, and reports and leaves what is already there. If the
user declines, it prints the lines to apply by hand. It runs no git
operation.

Git identity, per host. The identity is git's own, not the forge's.

- Two `includeIf` stanzas per host, one for `https://<host>/**` and
  one for `git@<host>:*/**`, both with `hasconfig:remote.*.url`.
- Each stanza has `path = <absolute path>/.gitconfig-<host>`. The path
  is absolute and the file lies in the local profile.
- The file `.gitconfig-<host>` is created with `[user]` `name` and
  `email` when missing.

The guard:

- `user.useConfigOnly = true` under `[user]`, so a repository on a host
  with no stanza fails aloud instead of taking a default. It only bites
  once a global `user.name` or `user.email` is removed.

The registration of the merge settings, once per machine. They hold for
every repository on the machine.

- `[merge "ours"]` with `driver = true`: makes `merge=ours` work.
- `[merge]` with `renormalize = true`: evens line endings at a merge.
- `[rebase]` with `backend = merge`: the apply backend ignores drivers.
- `[rerere]` with `enabled = true`: a convenience.
- `[merge]` with `conflictStyle = zdiff3`: offered apart.

## See also

- [Set up the forge](../start/setup.md): the command that fills the instance files.
- [How the rules are held](../about/how-the-rules-are-held.md): why the deny rules and the hook exist.
- [Persistence in git](../about/persistence-in-git.md): what the merge settings and the attributes are for.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
