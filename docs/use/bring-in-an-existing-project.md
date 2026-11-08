---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: a84b7e9cf39ddca7
inputs:
  - .claude/skills/import-project/SKILL.md
  - scripts/forge-clone.py
  - templates/project.md
---

# Bring in an existing project

This page shows how to clone a project you already have into `projects/` with `/import-project`. It is for the principal (the person whose thinking is forged) who has a project in a git repository and wants to work on it in the forge.

## When to use it

Use it when the project lives in a git repository that is not yet on this machine. If the project is already on this machine, see "A project already on this machine" below.

## The command

```
/import-project <git-url>
```

## What happens

1. Claude requires the URL. The target is `projects/<repository name>`, and the name is taken from the URL, so there is no slug to give. If that directory already exists, Claude stops and reports it, and nothing is overwritten.

   You should now see the target named, or the stop reported.

2. On your word, Claude runs the clone script (`scripts/forge-clone.py`) with the URL. The script clones the repository into `projects/<repository name>`.

   You should now see git's own clone output, then the line "Cloned into projects/<repository name>".

3. Claude relays the facts the script prints:
   - origin: the address the clone came from.
   - last commit: its short hash, date and subject.
   - identity: the name and e-mail git resolves for the clone from your own git configuration.
   - project: the kind and the language from the project file.

   You should now see these four lines.

4. Where git resolves no identity, Claude says what that means. Git has no name and e-mail to sign commits on this host. The login that cloned the repository is a different thing. The save script commits nothing until git resolves an identity. The script names two ways out: run `/setup`, or run `python scripts/forge-config.py --identity <host> <name> <email>`. The identity step of setup is on the page [Set up the forge](../start/setup.md). The forge writes no identity itself.

   You should now see the identity line say "none", and the ways out.

5. Where the project has no project file, the script says so instead. If the project has a ledger, it is of the shape before the migration: the kind and language are then read from the ledger's header, and the one remedy is `/migrate`. See [Migrate a project](migrate-a-project.md). If it has neither a project file nor a ledger, the forge did not make it. That is a fact, not a defect.

   You should now see the project line name the shape, or say there is no project file.

6. Claude recommends `/forge <slug>` as the first act of work. The engine does not track the project and cannot guess it, so you select the project by naming it.

   You should now see the recommendation to run `/forge <slug>`.

## What you have afterwards

The project stands in `projects/<repository name>` as a clone with its origin set. Nothing is written into it: the command only clones. Work starts when you select it with `/forge <slug>`, which shows the state map. See [See where a project stands](see-where-a-project-stands.md). A project written to older conventions may need more: see [Upgrade the engine](upgrade-the-engine.md).

## A project already on this machine

A project already on this machine is not cloned. This holds whether it sits in a repository of its own, in another repository or in none. You copy it or link it into `projects/<slug>` by hand. The forge knows it from `/forge <slug>` on.

## If something goes wrong

- "Cannot derive a repository name from '<url>'." The URL ends with no name. Give the URL of the repository itself.
- "projects/<name> already exists - never overwritten. Rename or remove it first." A directory of that name is already in `projects/`. Rename or remove it, then run the command again.
- "Clone of <url> failed." Git could not clone the address. Check the URL and your access to it.
- Identity "none": git resolves no `user.name` and `user.email` for the repository. The save script commits nothing until it does. Run `/setup`, or `python scripts/forge-config.py --identity <host> <name> <email>`, or set a local identity in the clone with git.
- Project "shape before the migration": run `/migrate`.
- Project "no project file - not scaffolded by the forge": a fact, not a defect. The project was not made by the forge.

For the terms used here, see the [Glossary](../reference/glossary.md).

## A worked example

```
/import-project https://example.com/team/my-idea.git
```

The script clones into `projects/my-idea` and prints:

```
Cloned into projects/my-idea
  origin:      https://example.com/team/my-idea.git
  last commit: <hash> <date> <subject>
  identity:    <name> <<email>> (from your git configuration)
  project:     kind thought, language en
```

You then run `/forge my-idea` to select the project.

## See also

- [See where a project stands](see-where-a-project-stands.md): the `/forge` map that follows.
- [Migrate a project](migrate-a-project.md): what to do with a project of the shape before the migration.
- [Upgrade the engine](upgrade-the-engine.md): what to check when a project was written to older conventions.
- [Set up the forge](../start/setup.md): the identity step, when git resolves no identity for the clone.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
