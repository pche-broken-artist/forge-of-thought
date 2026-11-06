---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 6d7299dd2701e92b
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

This page lists the files that configure an instance of the forge and a project, and what each holds, field by field. It is for the user who wants to know what sits on the machine after setup and for the extender who changes one of these files. An instance is one installation of the engine. The principal is the person whose thinking is being forged.

The files fall in three groups: the files inside the engine, the files of a project, and the configuration outside the engine that `/setup` writes into git's global file. The command that fills the instance files is described in [Set up the forge](../start/setup.md).

## Files inside the engine

### `.claude/settings.json`

Shared and committed. It holds the settings of Claude Code, the agent the forge runs in.

| Key | Value | What it is |
|---|---|---|
| `attribution.commit` | `""` | The commit trailer is empty. |
| `attribution.sessionUrl` | `false` | No session link is added. |
| `permissions.deny` | `Read(~/.ssh/**)` | Reading the SSH folder is denied. |
| `permissions.deny` | `Read(~/.aws/**)` | Reading the AWS folder is denied. |
| `permissions.deny` | `PowerShell(git *)` | Git in the other shell tool is denied. |
| `hooks.UserPromptSubmit` | command `python`, argument `scripts/hook-walkthrough.py` | Runs at every prompt of the principal. |
| `hooks.PreToolUse` | matcher `Bash`, command `python`, argument `scripts/hook-git.py` | Runs before every command of the Bash tool. |

Both hook arguments are given as `${CLAUDE_PROJECT_DIR}/scripts/<name>.py`, so the hooks run from the engine root. The reason for the deny rules and the hooks is given in [How the rules are held](../about/how-the-rules-are-held.md).

### `.claude/settings.local.json`

Gitignored. It holds the session model, written by `/setup` as `{ "model": "fable" }`, or the strongest model the account lists where that one is not offered. `/setup` leaves an existing file as it is. The model can be changed with `/model` or by editing the file.

### `CLAUDE.local.md`

Gitignored, at the engine root. It is made from `templates/CLAUDE.local.md` by `/setup` and holds three lines:

| Field | What it holds |
|---|---|
| Principal | The role of the person whose thinking is being forged, not a name. |
| Conversation language | The language the working conversation runs in. |
| Author | The principal's short handle, the author of every history record he decides. |

The git identity is not kept here. It is git's, per host.

### `.gitignore` of the engine

| Entry | What it keeps out of git |
|---|---|
| `.claude/settings.local.json` | The local settings. |
| `/CLAUDE.local.md` | The instance file. |
| `projects/*` | Every project, since each is a repository of its own. |
| `!projects/forge` | The exception: the engine's own project is tracked. |
| `projects/forge/ledger.md` | The ledger of that project, made at read time. |
| `Thumbs.db`, `desktop.ini` | Windows noise. |
| `~$*` | Lock files of an open Office document. |
| `__pycache__/` | Python byte-code caches. |

The entry is `projects/*` and never `projects/`, so that the re-inclusion of `projects/forge` works.

### `.gitattributes` of the engine

The engine has its own list, not a copy of the project template, because its derived files lie at the root and under `projects/forge/`. Every path is normalised for line endings (`* text=auto`).

| Path | Attribute |
|---|---|
| `README.md` | `merge=ours` |
| `RELEASE-NOTES.md` | `merge=ours` |
| `CONTRIBUTING.md` | `merge=ours` |
| `docs/**` | `merge=ours` |
| `projects/forge/renders/**` | `merge=ours` |
| `projects/forge/published/*.md` | `merge=ours` |
| `projects/forge/published/*.pptx` | `binary` |
| `projects/forge/published/*.docx` | `binary` |

A file marked `merge=ours` keeps the side of the branch you are on at a merge and is made again afterwards. A file marked `binary` is never merged. What the attributes do at a merge is told in [Working together on one project](../about/working-together.md).

## Files of a project

### `project.md`

The project file, written once when the project is created or migrated. It has three front-matter fields.

| Field | What it holds |
|---|---|
| `project` | The slug of the project. |
| `kind` | `thought` or `library`. |
| `language` | The language of the chain's artefacts, as an ISO 639-1 code (`en` when absent). |

A fixture project also carries `fixture: true`. A project without this file is of the shape before the migration, and the one remedy is `/migrate`.

### `.gitignore` of a project

Copied from `templates/gitignore` as it stands when the project is created.

| Entry | What it keeps out of git |
|---|---|
| `ledger.md` | The ledger, made at read time. |
| `~$*` | Lock files of an open Word, PowerPoint or Excel document. |

### `.gitattributes` of a project

Copied from `templates/gitattributes`. Every path is normalised for line endings (`* text=auto`).

| Path | Attribute |
|---|---|
| `renders/**` | `merge=ours` |
| `README.md` | `merge=ours` |
| `RELEASE-NOTES.md` | `merge=ours` |
| `CONTRIBUTING.md` | `merge=ours` |
| `docs/**` | `merge=ours` |
| `published/*.md` | `merge=ours` |
| `published/*.pptx` | `binary` |
| `published/*.docx` | `binary` |

## Configuration outside the engine

`/setup` writes this into the global configuration of git, on the principal's word and only through `scripts/forge-config.py`. The script reads and writes through `git config --global`, so it lands in the file git itself reads and names no path to it. A key that already carries the asked value is reported and left. A key that carries another value is reported and left, unless `--replace` is given for an identity. The settings hold for every repository on the machine. Where git reads another global file in each of several places, the configuration is made once in each. The script needs git 2.36 or newer. The reason for the merge driver and the guard is given in [Persistence in git](../about/persistence-in-git.md).

Run bare, `python scripts/forge-config.py` shows what is there and changes nothing.

### The identity per host

Written by `python scripts/forge-config.py --identity <host> <name> <email>`. For one host it writes two stanzas and an identity file.

| Key | Value |
|---|---|
| `includeIf.hasconfig:remote.*.url:https://<host>/**.path` | `.gitconfig-<host>` |
| `includeIf.hasconfig:remote.*.url:git@<host>:*/**.path` | `.gitconfig-<host>` |

The path is relative to the global file, so the identity file `.gitconfig-<host>` always lies beside the file that includes it. It holds `user.name` and `user.email`, written where the file is missing. A stanza with another path and an identity file with another name or e-mail are reported and left, and `--replace` rewrites them.

### The guard

Written by `python scripts/forge-config.py --guard`.

| Key | Value | What it does |
|---|---|---|
| `user.useConfigOnly` | `true` | Git refuses to guess an identity. |

The guard bites only once no global `user.name` or `user.email` is left. `--unset-identity` removes them.

### The registration of the merge driver `ours`

Written by `python scripts/forge-config.py --register`.

| Key | Value | What it is for |
|---|---|---|
| `merge.ours.driver` | `true` | The driver that takes our side at a merge. |
| `merge.renormalize` | `true` | Line endings are normalised at a merge. |
| `rebase.backend` | `merge` | The apply backend ignores drivers. |
| `rerere.enabled` | `true` | A convenience: git reuses a resolution it has seen. |
| `merge.conflictStyle` | `zdiff3` | Only with `--zdiff3`: the conflict is shown with its common ancestor. |

## See also

- [Set up the forge](../start/setup.md): the command that fills the instance files.
- [How the rules are held](../about/how-the-rules-are-held.md): why the deny rules and the hooks exist.
- [Persistence in git](../about/persistence-in-git.md): what the merge driver `ours` and the git hook are for.
- [Working together on one project](../about/working-together.md): what the attributes do at a merge.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
