---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 0c0284bfcd6d9a6e
inputs:
  - .claude/skills/import-project/SKILL.md
  - scripts/forge-clone.py
  - templates/project.md
---

# Bring in an existing project

This page is for you when a project already lives in a git repository and you want to work on it in the forge. `/import-project` clones that repository into `projects/` and tells you what it found. The principal (the person whose thinking is forged) is the one who runs it.

## When to use it

Use it when the project exists as a repository at some address and is not yet on this machine.

If the project is already on this machine, do not clone it. It may sit in a repository of its own, in another one, or in none. You copy or link it into `projects/<slug>` by hand. The forge knows it from `/forge <slug>` on.

## The command

```
/import-project <git-url>
```

The name of the target directory comes from the address, so there is no slug to give. The project lands in `projects/<repository name>`.

## What happens

1. Claude requires the address. If `projects/<repository name>` already exists, it stops and reports. The script never overwrites a directory.

   You should now see either the report that the directory exists, or the go-ahead to clone.

2. On your word Claude runs `python scripts/forge-clone.py <git-url>`. The script clones the repository. It sets no commit identity of its own, because the identity is git's, resolved from your own configuration.

   You should now see the line "Cloned into projects/<repository name>".

3. Claude relays the facts the script prints:
   - the last commit
   - the origin
   - the identity git resolves for the clone
   - the project file, with its kind and language

   You should now see these lines under the clone message.

4. Claude recommends `/forge <slug>` as the first act of work. The engine does not track the project and cannot guess it, so you select it by naming it. The map that follows is described in [See where a project stands](see-where-a-project-stands.md).

   You should now see the state map of the project once you run `/forge <slug>`.

## What you have afterwards

A clone of the repository in `projects/<repository name>`. Nothing is written into the project by this command.

## If something goes wrong

- "projects/<name> already exists - never overwritten. Rename or remove it first." The target directory is taken. Rename or remove it, then run the command again.
- "Cannot derive a repository name from '<url>'." The address does not end in a name. Give the full address of the repository.
- "Clone of <url> failed." Git could not clone. The cause is in git's own output above the message, for example a wrong address or no access.
- The identity line says "none". Git has no name and e-mail to sign commits on this host. This is a different thing from the login that cloned the repository. The save script commits nothing until git resolves an identity. The ways out are the identity step of [Set up the forge](../start/setup.md), or `python scripts/forge-config.py --identity <host> <name> <email>`, or a local identity set in the clone with `git config user.name` and `user.email`. The forge writes none of these itself.
- The project line says "shape before the migration". The project has no project file and is of the shape before the migration. The script reads its kind and language from the ledger's header. The one remedy is `/migrate`; see [Migrate a project](migrate-a-project.md). If the project was written to older conventions, see also [Upgrade the engine](upgrade-the-engine.md).
- The project line says "no project file - not scaffolded by the forge". The project has neither a project file nor a ledger, so the forge did not make it. This is a fact, not a defect.

## A worked example

```
/import-project <git-url>
```

Claude runs the clone script. The script prints, in this shape:

```
Cloned into projects/<repository name>
  origin:      <git-url>
  last commit: <hash> <date> <subject>
  identity:    <name> <email> (from your git configuration)
  project:     kind thought, language en
```

Then you select the project:

```
/forge <slug>
```

where `<slug>` is the repository name.

For terms of the forge used here, see the [Glossary](../reference/glossary.md).

## See also

- [See where a project stands](see-where-a-project-stands.md): the `/forge` map that follows.
- [Migrate a project](migrate-a-project.md): what to do with a project of the shape before the migration.
- [Upgrade the engine](upgrade-the-engine.md): what to check when a project was written to older conventions.
- [Set up the forge](../start/setup.md): the identity step, when git resolves no identity for the clone.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
