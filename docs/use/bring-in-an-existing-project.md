---
generated: 2026-10-10
made: mirrored
inputs-hash: 278982851bb48f74
inputs:
  - .claude/skills/import-project/SKILL.md
  - scripts/forge-clone.py
  - CLAUDE.md
---

# Bring in an existing project

This page is for a user who already has a project in a git repository
and wants to work on it in the engine. It shows how to bring the
project in with `/import-project` and what you see afterwards.

## Steps

1. Run `/import-project <git-url>` with the address of the
   repository. The address is required.
2. The project goes into `projects/<repository name>`. The name is
   taken from the end of the address, so there is no slug to give. If
   that directory already exists, the command stops and says so. An
   existing directory is never overwritten: rename or remove it
   first.
3. On your word the command runs `python scripts/forge-clone.py
   <git-url>`, which clones the repository. Git is reached through
   this script only.
4. Read the facts the script reports and the command relays to you.
5. Select the project with `/forge <slug>`.

For example, the script's own help shows addresses of the form
`https://example.com/team/my-idea.git`, which gives the project
`projects/my-idea`.

## What you see

After the clone the script reports four facts.

| Fact | What it tells you |
|---|---|
| origin | the address the clone came from |
| last commit | the newest commit: short hash, date and message |
| identity | the commit identity git resolves for the fresh clone, taken from your own git configuration |
| ledger | whether the project has a `ledger.md` with a `kind:` header, and the kind if it has |

Two of these need a word.

- **Identity.** The engine sets no commit identity and carries none.
  If git resolves none for the clone, the report says so, and the
  save script will report the missing identity and commit nothing
  until one is resolved.
- **Ledger.** A project without a ledger, or with a ledger that has
  no `kind:` header, was not scaffolded by the forge. That is stated
  as a fact, not a defect.

Nothing is written into the imported project by this command.

## Start working

The engine does not track projects and cannot guess which one you
mean. The project is selected by naming it: run `/forge <slug>`,
where the slug is the directory name under `projects/`. That gives
you the map of where the project stands.

If the project was written to older conventions, see the page on
upgrading the engine for what to check.

## See also

- [See where a project stands](see-where-a-project-stands.md): the `/forge` map that follows.
- [Upgrade the engine](upgrade-the-engine.md): what to check when a project was written to older conventions.
