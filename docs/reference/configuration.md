---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 89a4586700453f76
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

This page lists the files that configure an instance of the forge and a
project, and what each holds, field by field. It is for the user who
sets up a machine and for the extender who needs to know which file
carries which setting. The principal is whoever's thinking is being
forged; the instance is one installation of the engine. Terms of the
forge are in the [Glossary](glossary.md).

The command that fills the instance files is described in
[Set up the forge](../start/setup.md).

## Overview

| File | Shared | What it configures |
|---|---|---|
| `.claude/settings.json` | yes | attribution, deny rules, the two hooks |
| `.claude/settings.local.json` | no (gitignored) | the session model |
| `CLAUDE.local.md` | no (gitignored) | the instance facts |
| `.gitignore` of the engine | yes | what the engine never tracks |
| `.gitignore` of a project | yes, copied from a template | what a project never tracks |
| `.gitattributes` of the engine | yes | how derived files merge |
| `.gitattributes` of a project | yes, copied from a template | how derived files merge, which are binary |
| `project.md` | yes, in each project | slug, kind, language |
| `pytest.ini` | yes | how the tests run |
| global git configuration | outside the engine | identity per host, guard, merge driver |

## `.claude/settings.json`

The shared settings of Claude Code for the engine. The reasons for the
deny rules and the hooks are in
[How the rules are held](../about/how-the-rules-are-held.md).

| Key | Value | Meaning |
|---|---|---|
| `attribution.commit` | empty string | the commit trailer is empty |
| `attribution.sessionUrl` | `false` | no session link is added |
| `permissions.deny` | `Read(~/.ssh/**)` | the SSH directory is never read |
| `permissions.deny` | `Read(~/.aws/**)` | the AWS directory is never read |
| `permissions.deny` | `PowerShell(git *)` | git is not run in the other shell tool |
| `hooks.UserPromptSubmit` | `python` with `scripts/hook-walkthrough.py` | runs at every prompt |
| `hooks.PreToolUse`, matcher `Bash` | `python` with `scripts/hook-git.py` | runs before every Bash tool call |

Both hooks are of type `command`, run through `python`, and take their
script from `${CLAUDE_PROJECT_DIR}/scripts/`.

## `.claude/settings.local.json`

- Gitignored.
- Created by `/setup` and never overwritten.
- Holds the session model, the one key `model`.

## `CLAUDE.local.md`

- Gitignored, at the engine root, made from `templates/CLAUDE.local.md`
  by `/setup`.
- Holds three lines:
  - **Principal**: the role of whoever's thinking is forged, not a name.
  - **Conversation language**: the language the principal talks in.
  - **Author**: the principal's short handle, signed on every record he
    decides.

## `.gitignore` of the engine

| Entry | What it keeps out of git |
|---|---|
| `.claude/settings.local.json` | the local settings |
| `/CLAUDE.local.md` | the instance facts |
| `projects/*` | every project, except the next line |
| `!projects/README.md` | the README of the directory stays tracked |
| `Thumbs.db`, `desktop.ini` | Windows noise |
| `~$*` | lock files of an open Office document |
| `__pycache__/` | Python byte-code caches |

Why `projects/` is ignored is explained in
[Projects and the engine](../about/projects-and-the-engine.md).

## `.gitignore` of a project

Copied from `templates/gitignore` as it stands when a project is
created.

| Entry | What it keeps out of git |
|---|---|
| `ledger.md` | the ledger, which is made at read time |
| `~$*` | lock files of an open Office document |

## `.gitattributes` of the engine

The engine has its own list, not a copy of the template, because its
derived files lie at its root. What the attributes do at a merge is
told in [Working together on one project](../about/working-together.md).

| Pattern | Setting | Meaning |
|---|---|---|
| `*` | `text=auto` | line endings are normalised |
| `/README.md` | `merge=ours` | taken as `ours` at a merge |
| `/RELEASE-NOTES.md` | `merge=ours` | taken as `ours` at a merge |
| `/CONTRIBUTING.md` | `merge=ours` | taken as `ours` at a merge |
| `docs/**` | `merge=ours` | taken as `ours` at a merge |

The three root files are anchored with a leading slash. A bare name
matches at every depth and, with `core.ignorecase`, in every case.

## `.gitattributes` of a project

Copied from `templates/gitattributes`.

| Pattern | Setting | Meaning |
|---|---|---|
| `*` | `text=auto` | line endings are normalised |
| `renders/**` | `merge=ours` | taken as `ours` at a merge |
| `/README.md` | `merge=ours` | taken as `ours` at a merge |
| `/RELEASE-NOTES.md` | `merge=ours` | taken as `ours` at a merge |
| `/CONTRIBUTING.md` | `merge=ours` | taken as `ours` at a merge |
| `docs/**` | `merge=ours` | taken as `ours` at a merge |
| `published/*.md` | `merge=ours` | taken as `ours` at a merge |
| `published/*.pptx` | `binary` | never merged |
| `published/*.docx` | `binary` | never merged |

## `project.md`

The project file, at the root of each project.

| Field | Value | Meaning |
|---|---|---|
| `project` | the slug | the project's name |
| `kind` | `thought` or `library` | the kind of project |
| `language` | an ISO 639-1 code, `en` in the template | the language of the chain's artefacts |
| `fixture` | `true` | present only in a test fixture project |

## `pytest.ini`

How the tests run, from the engine root with `python -m pytest`. What
they serve is told in [The tests](../about/the-tests.md).

| Key | Value | Meaning |
|---|---|---|
| `testpaths` | `tests` | where the tests are |
| `pythonpath` | `scripts` | the shared modules import directly |

## Configuration outside the engine

`/setup` writes the global git configuration through
`scripts/forge-config.py`, which uses `git config --global` alone, so
that the change lands in the file git itself reads. It needs Python 3.8
or newer and git 2.36 or newer. A key that already carries a value is
reported and left, never overwritten, unless `--replace` is given for
an identity. Why the merge driver and the git hook exist is told in
[Persistence in git](../about/persistence-in-git.md).

| Call | What it writes |
|---|---|
| no arguments | nothing; it shows the registration, the guard, a global identity and the identity stanzas |
| `--identity <host> <name> <email>` | the identity of one host |
| `--guard` | the guard |
| `--register` | the registration of the merge driver `ours` |

### The identity of a host

`--identity` writes two stanzas to the global file and one identity
file.

| Key or file | Value |
|---|---|
| `includeIf "hasconfig:remote.*.url:https://<host>/**"` | `path = .gitconfig-<host>` |
| `includeIf "hasconfig:remote.*.url:git@<host>:*/**"` | `path = .gitconfig-<host>` |
| `.gitconfig-<host>` | `[user]` with `name` and `email` |

The path is relative to the global file, so the identity file lies
beside the file that includes it. A stanza with another path and an
identity file with another name or e-mail are reported and left.
`--replace` rewrites them.

### The guard

| Key | Value | Meaning |
|---|---|---|
| `user.useConfigOnly` | `true` | a repository on a host with no stanza fails instead of taking a default identity |

The guard bites only once no global `user.name` or `user.email` is
left. `--unset-identity` with `--guard` removes them.

### The merge driver `ours`

| Key | Value | Meaning |
|---|---|---|
| `merge.ours.driver` | `true` | the driver `ours` itself |
| `merge.renormalize` | `true` | a setting the driver needs |
| `rebase.backend` | `merge` | the apply backend ignores drivers |
| `rerere.enabled` | `true` | a convenience |
| `merge.conflictStyle` | `zdiff3` | only with `--zdiff3` |

These keys hold for every repository the configuration serves. On a
machine where git reads another global file in each place, the call is
made once in each.

## See also

- [Set up the forge](../start/setup.md): the command that fills the instance files.
- [How the rules are held](../about/how-the-rules-are-held.md): why the deny rules and the hooks exist.
- [Persistence in git](../about/persistence-in-git.md): what the merge driver `ours` and the git hook are for.
- [Working together on one project](../about/working-together.md): what the attributes do at a merge.
- [Projects and the engine](../about/projects-and-the-engine.md): why `projects/` is gitignored but for its README.
- [The tests](../about/the-tests.md): what the test configuration serves.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
