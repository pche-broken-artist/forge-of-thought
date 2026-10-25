---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 6d9bdefc0795a0f5
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

This page lists the files that configure an instance of the forge and a project, and what each holds, field by field. It is for the user who sets up a machine and for the extender who needs to know which file carries which setting. Values of a real instance are not shown: a placeholder stands where one would be.

Two words are used throughout. The principal is the person whose thinking is being forged. Claude is the model that works with the principal.

## Overview

| File | Shared | Holds | Written by |
|---|---|---|---|
| `.claude/settings.json` | yes | attribution, deny rules, two hooks | part of the engine |
| `.claude/settings.local.json` | no | the session model | `/setup` |
| `CLAUDE.local.md` | no | the principal, the conversation language, the author handle | `/setup` |
| `.gitignore` | yes | what git leaves out of the engine | part of the engine |
| `.gitattributes` | yes | the merge ways of the engine's own paths | part of the engine |
| `templates/gitattributes` | yes | the merge ways a project's own file is copied from | part of the engine |
| `project.md` | in the project | slug, kind, language | `/new-project` |
| the global git configuration | outside the engine | identity per host, the guard, the merge driver `ours` | `scripts/forge-config.py`, called by `/setup` |

## `.claude/settings.json`

The shared settings of Claude Code for the engine. It is committed.

| Key | Value | Meaning |
|---|---|---|
| `attribution.commit` | empty string | no trailer is added to a commit message |
| `attribution.sessionUrl` | `false` | no session address is added |
| `permissions.deny` | `Read(~/.ssh/**)` | Claude may not read the SSH folder of the user |
| `permissions.deny` | `Read(~/.aws/**)` | Claude may not read the AWS folder of the user |
| `permissions.deny` | `PowerShell(git *)` | Claude may not run git in the PowerShell tool, the other shell tool |
| `hooks.UserPromptSubmit` | command `python`, argument `${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.py` | runs at every prompt of the principal |
| `hooks.PreToolUse` | matcher `Bash`, command `python`, argument `${CLAUDE_PROJECT_DIR}/scripts/hook-git.py` | runs before every Bash call |

The first hook repeats the rules of the walkthrough at every prompt. The second hook stands between Claude and git: it denies a write to git and names the script to use. The reasons for the rules and the hooks are on [How the rules are held](../about/how-the-rules-are-held.md). What the hook and the scripts are for in git is on [Persistence in git](../about/persistence-in-git.md).

## `.claude/settings.local.json`

The settings of one machine. It is gitignored. `/setup` creates it where it is missing and leaves it alone where it exists.

| Key | Value | Meaning |
|---|---|---|
| `model` | the strongest model the account offers | the model of the session, on which the whole forge runs, the blind reviewers included |

The model can be changed at any time with `/model` or by editing the file. A session is one run of Claude Code from start to end.

## `CLAUDE.local.md`

The facts of one instance, at the engine root. It is gitignored. `/setup` copies `templates/CLAUDE.local.md` here and fills it by interview. It holds three lines.

| Field | Holds |
|---|---|
| `Principal` | the role of the person whose thinking is being forged, such as "the CTO" |
| `Conversation language` | the language in which the working conversation runs |
| `Author` | the short handle of the principal, written as the author of every record he decides, such as `JDo` |

The language of the documents of a project is not set here. It is the `language` of the project file.

## `.gitignore`

The engine's list of what git leaves out.

| Entry | Left out |
|---|---|
| `.claude/settings.local.json` | the machine's settings |
| `/CLAUDE.local.md` | the instance facts |
| `projects/*` | every project, each a repository of its own |
| `!projects/forge` | re-includes the engine's own project |
| `projects/forge/ledger.md` | the ledger of the engine's own project, made at read time |
| `__pycache__/` | Python byte-code caches |

The entry is `projects/*` and never `projects/`, because only then can the re-include work. The file also lists operating-system and office-program noise.

## `.gitattributes` of the engine

The ways of merging by path for the engine's own files. It is not a copy of the template below, because the engine's derived files lie at the root and under `projects/forge/`.

| Pattern | Attribute |
|---|---|
| `*` | `text=auto` |
| `README.md`, `RELEASE-NOTES.md`, `CONTRIBUTING.md` | `merge=ours` |
| `docs/**` | `merge=ours` |
| `projects/forge/renders/**` | `merge=ours` |
| `projects/forge/published/*.md` | `merge=ours` |
| `projects/forge/published/*.pptx`, `projects/forge/published/*.docx` | `binary` |

`text=auto` normalises line endings so that files do not fight between machines. `merge=ours` takes the local version at a merge, and the file is made again afterwards. `binary` means the file is never merged. What the attributes do at a merge is on [Working together on one project](../about/working-together.md).

## `templates/gitattributes`

The file a project's own `.gitattributes` is copied from. The patterns are those of the engine's list, relative to the project root.

| Pattern | Attribute |
|---|---|
| `*` | `text=auto` |
| `renders/**` | `merge=ours` |
| `README.md`, `RELEASE-NOTES.md`, `CONTRIBUTING.md` | `merge=ours` |
| `docs/**` | `merge=ours` |
| `published/*.md` | `merge=ours` |
| `published/*.pptx`, `published/*.docx` | `binary` |

## `project.md`

The project file, at the root of a project. It is written once, at the creation of the project by `/new-project` or by the migration, and never by a round of work.

| Field | Holds |
|---|---|
| `project` | the slug of the project |
| `kind` | `thought` or `library` |
| `language` | the language of the artefacts of the chain, as an ISO 639-1 code such as `en` |

A fixture project, one made for testing, also carries `fixture: true`. A project without this file is of the shape before the migration. The one remedy is `/migrate`.

## The global git configuration

Outside the engine, `/setup` writes to the global git configuration of the user, on his word. It writes only through `scripts/forge-config.py`, which uses `git config --global` and so lands in whichever file git itself reads. A key that already carries the value asked is left. A key that carries another value is reported and left. Only `--replace` for an identity rewrites. Where git reads a different global file in each of several places, the configuration is made once in each. The command `/setup` is described on [Set up the forge](../start/setup.md).

Run bare, the script changes nothing and reports what is there.

### Identity per host

Call: `python scripts/forge-config.py --identity <host> <name> <email>`

| Key | Value |
|---|---|
| `includeIf.hasconfig:remote.*.url:https://<host>/**.path` | `.gitconfig-<host>` |
| `includeIf.hasconfig:remote.*.url:git@<host>:*/**.path` | `.gitconfig-<host>` |

The path is relative to the global file, so the identity file lies beside the file that includes it. The script then writes that file, where it is missing, with these keys:

| Key | Value |
|---|---|
| `user.name` | `<name>` |
| `user.email` | `<email>` |

A stanza that carries another path, an absolute one among them, and an identity file that carries another name or e-mail are reported and left. git 2.36 or newer is needed, because of `hasconfig`.

### The guard

Call: `python scripts/forge-config.py --guard [--unset-identity]`

| Key | Value | Meaning |
|---|---|---|
| `user.useConfigOnly` | `true` | git fails aloud in a repository whose host has no identity, instead of taking a default |

The guard bites only when no global `user.name` or `user.email` is left. `--unset-identity` removes them.

### The merge driver `ours`

Call: `python scripts/forge-config.py --register [--zdiff3]`

| Key | Value | Meaning |
|---|---|---|
| `merge.ours.driver` | `true` | the driver that keeps the local version of a file at a merge |
| `merge.renormalize` | `true` | line endings are normalised at a merge |
| `rebase.backend` | `merge` | the apply backend ignores drivers |
| `rerere.enabled` | `true` | git remembers how a conflict was settled, a convenience |
| `merge.conflictStyle` | `zdiff3` | only with `--zdiff3`; the style in which a conflict is shown |

These keys hold for every repository the configuration serves. Without the registration, an unregistered clone falls back to a conflict. What the driver is for is on [Persistence in git](../about/persistence-in-git.md).

## See also

- [Set up the forge](../start/setup.md): the command that fills the instance files.
- [How the rules are held](../about/how-the-rules-are-held.md): why the deny rules and the hooks exist.
- [Persistence in git](../about/persistence-in-git.md): what the merge driver `ours` and the git hook are for.
- [Working together on one project](../about/working-together.md): what the attributes do at a merge.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
