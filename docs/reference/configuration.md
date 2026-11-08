---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 671d081fcdec66bc
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

This page lists the files that configure an instance of the forge and a project, and what each holds, field by field. It is for the user who fills the instance files and for the extender who changes them. The command that fills the instance files is described in [Set up the forge](../start/setup.md). Terms of the forge are defined in the [Glossary](../reference/glossary.md).

In this page the principal is the person whose thinking is being forged. The ledger is the state report made from the documents at read time. A hook is a program that Claude Code, the agent the forge runs in, calls at a fixed moment of its work.

| File | Shared | Holds |
|---|---|---|
| `.claude/settings.json` | yes | attribution, deny rules, two hooks |
| `.claude/settings.local.json` | no | the session model |
| `CLAUDE.local.md` | no | the principal, the conversation language, the author handle |
| `.gitignore` of the engine | yes | what the engine never tracks |
| `.gitignore` of a project | yes | what a project never tracks |
| `.gitattributes` of the engine | yes | the derived files taken as `ours` at a merge |
| `.gitattributes` of a project | yes | the same for a project, and the binary files |
| `project.md` | yes | slug, kind, language, fixture flag |
| `pytest.ini` | yes | how the tests run |
| the global git configuration | no | identity per host, guard, merge driver registration |

## `.claude/settings.json`

The shared settings of the engine.

- `attribution.commit`: an empty string, so that a commit carries no trailer.
- `attribution.sessionUrl`: `false`.
- `permissions.deny`: three rules.
  - `Read(~/.ssh/**)`: the SSH directory is never read.
  - `Read(~/.aws/**)`: the AWS directory is never read.
  - `PowerShell(git *)`: git is not run in the other shell tool.
- `hooks.UserPromptSubmit`: one hook, run with `python` on `scripts/hook-walkthrough.py`, at every prompt.
- `hooks.PreToolUse`: one hook with the matcher `Bash`, run with `python` on `scripts/hook-git.py`, before every call of the Bash tool.

Both hook paths start with `${CLAUDE_PROJECT_DIR}`. Why the deny rules and the hooks exist is explained in [How the rules are held](../about/how-the-rules-are-held.md).

## `.claude/settings.local.json`

The local settings of one machine, ignored by git and created by `/setup`. It holds the session model under the key `model`. `/setup` leaves an existing file untouched.

## `CLAUDE.local.md`

The instance facts, at the engine root, ignored by git and created by `/setup` from `templates/CLAUDE.local.md`. It has three lines.

- `Principal`: the role of the principal, whose thinking is being forged.
- `Conversation language`: the language the working conversation runs in.
- `Author`: the principal's short handle, the author of every record he decides.

The git identity is not kept here; git holds it per host.

## `.gitignore` of the engine

What the engine never tracks:

- `.claude/settings.local.json` and `/CLAUDE.local.md`: the instance files.
- `projects/*`, but not `projects/README.md`: every project is a repository of its own. See [Projects and the engine](../about/projects-and-the-engine.md).
- `Thumbs.db` and `desktop.ini`: Windows noise.
- `~$*`: the lock files of an open Office document.
- `__pycache__/`: the byte-code caches of Python.

The `tmp/` folder has its own `.gitignore` and is not listed here.

## `.gitignore` of a project

The template `templates/gitignore`, copied by `/new-project` as it stands.

- `ledger.md`: the ledger is made at read time and never enters git.
- `~$*`: the lock files of an open Office document.

## `.gitattributes` of the engine

The engine keeps its own list, not a copy of the template, because its derived files lie at the root. Each derived file is made again after a merge, so a merge takes it as `ours`.

- `* text=auto`: line endings are normalised.
- `/README.md merge=ours`
- `/RELEASE-NOTES.md merge=ours`
- `/CONTRIBUTING.md merge=ours`
- `docs/** merge=ours`

The three root files are anchored with a leading slash. A bare name would match at every depth, and with `core.ignorecase` in every case, `recipes/readme.md` among them. See [Working together on one project](../about/working-together.md) for what the attributes do at a merge.

## `.gitattributes` of a project

The template `templates/gitattributes`, which a project's own file is copied from.

- `* text=auto`: line endings are normalised.
- `renders/** merge=ours`
- `/README.md merge=ours`
- `/RELEASE-NOTES.md merge=ours`
- `/CONTRIBUTING.md merge=ours`
- `docs/** merge=ours`
- `published/*.md merge=ours`
- `published/*.pptx binary`
- `published/*.docx binary`

The root files are anchored for the same reason as in the engine. The published designed files are binary and never merged. What the merge driver `ours` and the git hook are for is explained in [Persistence in git](../about/persistence-in-git.md).

## `project.md`

The project file, written once when a project is created, by `/new-project` or by the migration. It has a front-matter of three fields and a fourth that only a fixture carries.

- `project`: the slug of the project.
- `kind`: `thought` or `library`.
- `language`: the language of the chain's artefacts, as an ISO 639-1 code.
- `fixture`: `true` in a test fixture project, absent elsewhere.

A project without this file has the shape from before the migration, and the one remedy is `/migrate`.

## `pytest.ini`

How the tests run, from the engine root with `python -m pytest`.

- `testpaths = tests`: the test path.
- `pythonpath = scripts`: the scripts on the import path, so that the shared modules import directly.

A script with a hyphen in its name is loaded through the `load_script` fixture of `tests/conftest.py`. What the configuration serves is explained in [The tests](../about/the-tests.md).

## The global git configuration

Outside the engine, `/setup` writes the global git configuration on the user's word, only through `scripts/forge-config.py`. The script writes to the file git itself reads, and it names no path to it. A key that already carries the value asked is left. A key that carries another value is reported and left, unless `--replace` is given for an identity. The script needs Python 3.8 or newer and git 2.36 or newer.

### Identity per host

`python scripts/forge-config.py --identity <host> <name> <email>` writes two stanzas for one host, each with `path = .gitconfig-<host>`:

- `includeIf "hasconfig:remote.*.url:https://<host>/**"`
- `includeIf "hasconfig:remote.*.url:git@<host>:*/**"`

The path is relative to the global file, so the identity file lies beside the file that includes it. The identity file `.gitconfig-<host>` holds `[user]` with `name` and `email`, and is written where it is missing.

### The guard

`python scripts/forge-config.py --guard` writes `user.useConfigOnly = true`. It takes effect only once no global `user.name` or `user.email` is left. `--unset-identity` removes them.

### The merge driver registration

`python scripts/forge-config.py --register` writes the keys below. They hold for every repository the configuration serves.

- `merge.ours.driver = true`: the merge driver `ours`.
- `merge.renormalize = true`
- `rebase.backend = merge`: the apply backend ignores drivers.
- `rerere.enabled = true`: a convenience.

`--zdiff3` adds `merge.conflictStyle = zdiff3`.

The bare run, `python scripts/forge-config.py`, changes nothing. It shows the file git reads, the registration, the guard, a global identity and the identity stanzas.

## See also

- [Set up the forge](../start/setup.md): the command that fills the instance files.
- [How the rules are held](../about/how-the-rules-are-held.md): why the deny rules and the hooks exist.
- [Persistence in git](../about/persistence-in-git.md): what the merge driver `ours` and the git hook are for.
- [Working together on one project](../about/working-together.md): what the attributes do at a merge.
- [Projects and the engine](../about/projects-and-the-engine.md): why `projects/` is gitignored but for its README.
- [The tests](../about/the-tests.md): what the test configuration serves.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
