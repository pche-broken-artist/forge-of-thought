---
generated: 2026-10-23
version: 5.34
made: mirrored
inputs-hash: a1ef25625afe7b49
inputs:
  - .claude/settings.json
  - .gitignore
  - .gitattributes
  - templates/gitattributes
  - templates/project.md
  - templates/CLAUDE.local.md
  - .claude/skills/setup/SKILL.md
  - scripts/forge-config.py
  - CLAUDE.md#What this workspace is
---

# Configuration

This page lists the files that configure an instance of the forge and a project, and the settings outside the engine that the setup command writes, with what each holds field by field. It is for the person who installs the forge and for the one who extends it. Terms of the forge are in the [Glossary](glossary.md); the command that fills the instance files is described in [Set up the forge](../start/setup.md).

The "principal" is the person whose thinking is being forged. An "instance" is one installation of the engine on one machine.

## Overview

| File | Shared | Holds |
|---|---|---|
| `.claude/settings.json` | yes | attribution, deny rules, two hooks |
| `.claude/settings.local.json` | no | the session model |
| `CLAUDE.local.md` | no | the principal, the conversation language, the author handle |
| `.gitignore` | yes | what the engine's repository leaves out |
| `.gitattributes` | yes | how paths merge, which are binary |
| `templates/gitattributes` | yes | the template a project's own `.gitattributes` is copied from |
| `project.md` | in the project | slug, kind, language |
| global git configuration | no, outside the engine | identity per host, the guard, the merge driver registration |

## `.claude/settings.json`

Shared by every instance. Fields:

- `attribution.commit`: an empty string, so a commit carries no trailer.
- `attribution.sessionUrl`: `false`, so no session link is added.
- `permissions.deny`: three rules.
  - `Read(~/.ssh/**)`: the SSH directory is never read.
  - `Read(~/.aws/**)`: the AWS directory is never read.
  - `PowerShell(git *)`: git is not run through the other shell tool, so the hook on Bash is not bypassed.
- `hooks.UserPromptSubmit`: a hook (a command that Claude's host program runs at a fixed moment) that runs at every prompt, command `python` with the argument `${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.py`.
- `hooks.PreToolUse`: a hook with the matcher `Bash`, command `python` with the argument `${CLAUDE_PROJECT_DIR}/scripts/hook-git.py`.

Why the deny rules and the hooks exist is in [How the rules are held](../about/how-the-rules-are-held.md).

## `.claude/settings.local.json`

Gitignored, per machine. It holds the session model as `{ "model": "<model>" }`. `/setup` creates it where it is missing and leaves an existing one untouched. It can be changed at any time with `/model` or by editing the file.

## `CLAUDE.local.md`

At the engine root, gitignored, created by `/setup` from `templates/CLAUDE.local.md`. It holds the instance facts, which are not properties of the system. Fields:

- `Principal`: the role of the person whose thinking is being forged, for example "the CTO".
- `Conversation language`: the language the working conversation runs in; the language of the documents follows the project's `language`.
- `Author`: the principal's short handle, the author of every history record the principal decides.

## `.gitignore` of the engine

Entries:

- `.claude/settings.local.json`: the session model, per machine.
- `/CLAUDE.local.md`: the instance facts.
- `projects/*` with `!projects/forge`: every project is a repository of its own, except the forge project, which the engine tracks. The pattern is `projects/*` and not `projects/` so that the re-inclusion works.
- `projects/forge/ledger.md`: the ledger (the state of a project, made at read time) of the forge project is never in git.
- `Thumbs.db`, `desktop.ini`: Windows noise.
- `~$*`: lock files of open Office documents.
- `/tmp/`: private scratch at the engine root.
- `__pycache__/`: Python byte-code caches.

## `.gitattributes`

The engine's own file and the template `templates/gitattributes`, which a project's file is copied from, differ only in their paths. The engine's carries the prefix `projects/forge/` on the paths below the project; the template's does not.

| Setting | Paths in a project | Meaning |
|---|---|---|
| `* text=auto` | all | line endings are normalised |
| `merge=ours` | `renders/**`, `README.md`, `RELEASE-NOTES.md`, `CONTRIBUTING.md`, `docs/**`, `published/*.md` | taken as `ours` at a merge and made again |
| `binary` | `published/*.pptx`, `published/*.docx` | never merged |

The engine's own file lists `README.md`, `RELEASE-NOTES.md`, `CONTRIBUTING.md` and `docs/**` at its root and the other paths under `projects/forge/`. What the attributes do at a merge is in [Working together on one project](../about/working-together.md).

## `project.md`

The project file, at the root of a project. It is written once, when the project is created or migrated. Front-matter fields:

- `project`: the slug.
- `kind`: `thought` or `library`.
- `language`: the language of the chain's artefacts, as an ISO 639-1 code (default in the template: `en`).

A fixture project (a project made to test the forge) also carries `fixture: true`. A project without this file is of the shape before the migration, and `/migrate` is the one remedy.

## Configuration outside the engine

`/setup` offers these settings, one call at a time and on the principal's word, through `scripts/forge-config.py`. The script reads and writes only through `git config --global`, so a change lands in the file git itself reads. A key that already carries another value is reported and left, unless `--replace` is given for an identity. Bare `python scripts/forge-config.py` shows what is there and changes nothing. It needs Python 3.8 or newer and git 2.36 or newer.

### Identity per host

Call: `python scripts/forge-config.py --identity <host> <name> <email>`. It writes two stanzas and one identity file.

- `includeIf.hasconfig:remote.*.url:https://<host>/**.path`: set to `.gitconfig-<host>`.
- `includeIf.hasconfig:remote.*.url:git@<host>:*/**.path`: set to `.gitconfig-<host>`.
- `.gitconfig-<host>`: the identity file, beside the global file, because the path is relative to it. It holds `user.name` and `user.email`.

### The guard

Call: `python scripts/forge-config.py --guard`.

- `user.useConfigOnly`: `true`, so a repository on a host with no identity stanza fails aloud instead of taking a default. It bites only once no global `user.name` or `user.email` is left; `--unset-identity` removes them.

### Registration of the merge driver `ours`

Call: `python scripts/forge-config.py --register`. These keys hold for every repository on the machine.

- `merge.ours.driver`: `true`, the driver `ours`.
- `merge.renormalize`: `true`, which evens line endings at a merge.
- `rebase.backend`: `merge`, because the apply backend ignores drivers.
- `rerere.enabled`: `true`, a convenience.
- `merge.conflictStyle`: `zdiff3`, written only with `--zdiff3`.

The forge has no merge driver of its own for record files; they merge as text. What the driver `ours` and the git hook are for is in [Persistence in git](../about/persistence-in-git.md).

## See also

- [Set up the forge](../start/setup.md): the command that fills the instance files.
- [How the rules are held](../about/how-the-rules-are-held.md): why the deny rules and the hooks exist.
- [Persistence in git](../about/persistence-in-git.md): what the merge driver `ours` and the git hook are for.
- [Working together on one project](../about/working-together.md): what the attributes do at a merge.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.34 from the files the front-matter names; never edited by hand.
