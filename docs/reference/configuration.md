---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/settings.json
  - templates/CLAUDE.local.md
  - .claude/skills/setup/SKILL.md
  - CLAUDE.md
  - projects/forge/40-solution-design.md
---

# Configuration

This page lists the files that configure an instance of the forge and
what each holds. It is for the user who sets an instance up and for
the extender who changes what is shared.

## Files in the engine

| File | Shared | Holds |
|---|---|---|
| `.claude/settings.json` | yes | the settings below |
| `.claude/settings.local.json` | no, gitignored | the session model |
| `CLAUDE.local.md` | no, gitignored | the principal and the conversation language |
| `.gitignore` | yes | the pattern for projects |

### `.claude/settings.json`

- `attribution`: the commit text is empty and `sessionUrl` is false,
  so nothing is appended to a commit.
- `permissions.deny`: reading `~/.ssh/**` and `~/.aws/**` is denied,
  as is raw `git`, in both shells (`Bash(git *)` and
  `PowerShell(git *)`); the scripts in `scripts/` are the only door
  to git.
- `hooks.UserPromptSubmit`: one hook runs
  `scripts/hook-walkthrough.ps1` through `pwsh` with `-NoProfile
  -File`, the script path anchored by `${CLAUDE_PROJECT_DIR}` so it
  does not depend on the working directory.

### `.claude/settings.local.json`

Gitignored. Holds the session model, which the whole forge runs on,
reviewers included. `/setup` creates it when missing and never
overwrites it; it can be changed with `/model` or by editing the
file.

### `CLAUDE.local.md`

Gitignored, at the engine root. Created by `/setup` from
`templates/CLAUDE.local.md` and holds two facts:

- **Principal**: the role, whose thinking is being forged.
- **Conversation language**: the language the working conversation
  runs in; the language of the documents is set elsewhere, by the
  project's ledger header.

### `.gitignore`

The pattern for projects is `projects/*` with `projects/forge`
re-included (`!projects/forge`). The pattern must be `projects/*`,
not `projects/`, or the re-inclusion does not work. Every other
project is a git repository of its own.

## Outside the engine

### Git identity

The identity is git's, set per host in the user's global git
configuration, never in the engine and never per repository:

- one `includeIf` stanza per host, for `https` and for `git@`
  remotes, pointing to an absolute path of a `.gitconfig-<host>` file
  that holds `[user]` `name` and `email`;
- the guard `user.useConfigOnly = true`, with no global `user.name`
  or `user.email`, so a repository on a host with no stanza fails
  aloud; a surviving global identity defeats the guard.

`/setup` offers to write these, on the user's word, and never
overwrites existing content.

## See also

- [Set up the forge](../start/setup.md): the command that fills the
  instance files.
- [About how the rules are held](../about/how-the-rules-are-held.md) -
  why the deny rules and the hook exist.
