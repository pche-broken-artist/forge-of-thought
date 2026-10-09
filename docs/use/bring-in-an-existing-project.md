---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/import-project/SKILL.md
  - scripts/forge-clone.ps1
  - CLAUDE.md
---

# Bring in an existing project

This page is for someone who already has a project in a git
repository and wants to work on it in the forge. It shows how to
bring the repository in and what to do first.

## Bring it in

Run the command with the address of the repository:

```
/import-project <git-url>
```

The command clones the repository through `scripts/forge-clone.ps1`
into `projects/<repository name>`. The name of the directory comes
from the address, so there is no slug to give. The clone runs on your
word.

An existing directory of that name is never overwritten. If
`projects/<repository name>` is already there, the command stops and
says so; rename or remove the directory first, then run it again.

## What you are told

When the clone is done, the command relays the facts the script
reports:

- the last commit of the project;
- the origin, the address the clone came from;
- the commit identity git resolves for the clone. The forge sets no
  identity: it is git's, resolved from your own configuration, per
  host. If git resolves none, the line says so, and `forge-save`
  will report it and commit nothing in that project until one is
  resolved;
- whether the project has a ledger with a `kind:` header. A project
  without one is not defective; its absence is only a fact you are
  told.

## What it leaves alone

The command writes nothing into the project. The clone is exactly
what the repository held.

## Start work

Select the project by naming it:

```
/forge <slug>
```

The engine does not keep track of projects and cannot guess which one
you mean, so selecting it by its name is the first act of work.

## See also

- [See where a project stands](see-where-a-project-stands.md): the
  `/forge` map that follows.
- [Upgrade the engine](upgrade-the-engine.md): what to check when a
  project was written to older conventions.
