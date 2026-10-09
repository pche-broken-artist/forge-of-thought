---
generated: 2026-10-09
made: mirrored
inputs-hash: febccb88ea2c8e2c
inputs:
  - .claude/skills/import-project/SKILL.md
  - scripts/forge-clone.py
  - CLAUDE.md
---

# Bring in an existing project

This page is for a user who already has a project in a git repository and wants to work on it in the forge. It shows how to bring it in with `/import-project`, what the command reports back and what to do next.

## Run the command

Give the command the address of the repository:

```
/import-project <git-url>
```

The command asks for your word before it runs. It then clones the repository through `scripts/forge-clone.py` into `projects/<repository name>`. The name of the directory falls out of the address: the last part, without a trailing `.git`. There is no slug to give.

The script never overwrites. If `projects/<repository name>` already exists, the command stops and says so. Rename or remove the existing directory first, then run it again.

The script sets no commit identity and carries no address of its own. Git resolves the identity from your own configuration, per host.

## What it reports

When the clone is done, the command relays the facts the script prints:

- **Last commit:** the short hash, the date and the message of the newest commit.
- **Origin:** the address the clone came from.
- **Identity:** the commit identity git resolves for this clone. If git resolves none, the script says so, and the save script will report it and commit nothing until an identity is configured.
- **Ledger:** whether the project has a `ledger.md` with a `kind:` header, and which kind. A project without one was not scaffolded by the forge. That is a fact, not a defect.

Nothing is written into the imported project. The command only clones and reports.

## Start working

The command ends by recommending `/forge <slug>`, where the slug is the directory name under `projects/`. The engine does not track projects and cannot guess which one you mean, so you select the project by naming it. Run it as your first act of work on the imported project.

## See also

- [See where a project stands](see-where-a-project-stands.md): the `/forge` map that follows.
- [Upgrade the engine](upgrade-the-engine.md): what to check when a project was written to older conventions.
