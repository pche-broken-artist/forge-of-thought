---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - scripts/forge-status.ps1
  - .claude/agents/check-engine.md
  - projects/forge/10-intent.md
---

# Add a script

This page is for someone extending the forge who wants to add a script
to `scripts/`. It was put together from `CLAUDE.md` (Persistence,
Portability, Repository layout, Document chain and the rule that one
mechanism lives in one place), from the forge intent's position on
portability, from the help header of `scripts/forge-status.ps1` and
from the `check-engine` agent. It says how a new script is written,
where it is described and how you prove it fits.

## Before you start

- **Write it in Python.** New scripts are written in Python. The
  PowerShell scripts already in `scripts/` stand as they are and are
  rewritten to Python in time; you do not have to rewrite one to add
  yours.
- **Know why `scripts/` is special.** It is the only platform-bound
  layer of the forge, and it is the only door to git: every git
  operation, reading state included, goes through a script. For Claude
  this is enforced by the deny rules of `.claude/settings.json`. If
  your script touches git, it belongs here; nothing else may touch git.

## Steps

1. **Write the script to run unchanged on Windows, Linux and macOS.**
   - Nothing Windows-only: no `cmd`, no registry, no platform-only
     calls. Branch on the platform only where it genuinely differs.
   - Compose paths portably, never with a hard-coded separator. (The
     standing PowerShell scripts use `Join-Path` or forward slashes.)
   - Resolve external tools such as `git`, `pandoc`, `markitdown` or
     `claude` from PATH. Check that a tool is there and stop with a
     plain message if it is not: `forge-status.ps1` stops with
     `git is not installed.` before doing anything.
   - Carry no URL and no identity. No remote address, no author
     identity, no first-run initialisation: git configuration is the
     user's own.

   Portability is a writing rule, not a claim: it is held as wanted
   until the set has been verified by running it on Linux.

2. **Give it a help header that owns its facts.** The header at the top
   of the script is the one place that says what the script does, what
   it needs installed, its parameters and where its output lands.
   `forge-status.ps1` is the smallest model: a one-line synopsis, a
   description of what it does and does not change and why it exists,
   and an example of how it is run.
   - Keep the usage examples free of platform-specific paths and
     invocations: `./scripts/forge-status.ps1`, not a drive letter.

3. **List it in the layout comment of `CLAUDE.md`.** The `scripts/`
   entry of the Repository layout names every script with a few words
   of what it is for. Add yours there. Say no more than that: the facts
   stay in the header.

4. **Name it by path where a command uses it.** A command that needs
   the script cites it by its path, for example `scripts/doc2md.ps1`,
   and leaves what it needs installed and how it runs to the header.
   `CLAUDE.md` does the same: for the conversions it says that what each
   needs installed and where the output lands is the header's. A
   procedure stated in two places is a defect.

## What you see when it fits

Run `/check engine`. Among what it verifies, the engine check compares
the scripts on disk with `CLAUDE.md`: every file in `scripts/` must be
described there, in the layout comment and its governing rule, and
nothing described there may be missing on disk. A script you added but
did not list, or a listed script that is not on disk, comes back as a
finding.

## See also

- [Scripts](../reference/scripts.md): the scripts that exist.
- [About persistence in git](../about/persistence-in-git.md): why the scripts are the only door.
