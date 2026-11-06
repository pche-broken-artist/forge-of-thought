---
project: forge
title: Office temporary files kept out of git
author: PCHe
version: 0.2
status: draft
---

<!-- Only this header is fixed; the text below it is free-form. The
rules: its definition, `.claude/skills/forge/states/brief.md`; the
history companion:
templates/history.md. -->

# Office temporary files kept out of git

When someone opens an Office document in a project, for instance in
`published/`, the application leaves a temporary file beside it.
Such files must never reach git, in any repository the forge works
with.

## What is wanted

The forge keeps these files out of git globally, on each machine,
through git's global ignore — not repository by repository. It is
set up by `/setup`, once per machine, the way the merge driver
`ours` is registered, and `forge-status` says when it is missing,
so that a colleague's clone is covered the same way without anyone
having to remember it.

Why globally: one setting covers every repository on the machine,
the forge's projects and any other, with nothing to add to each
project and nothing for `/new-project` to remember.

## What is ignored

The temporary files of office applications, nothing more:
- Office lock files, `~$*`;
- Word's temporary files, `~WRL*.tmp`;
- LibreOffice lock files, `.~lock.*#`.

(remark: the last two patterns are from knowledge, not verified.)

## Still open

- The line in each project's own `.gitignore` as well, travelling
  with the repository as a safeguard: not decided. Today the engine's
  `.gitignore` carries `~$*`, agentic-platform carries it by hand,
  the other projects do not.
