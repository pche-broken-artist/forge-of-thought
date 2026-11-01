---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 2da7cd662002ea64
inputs:
  - .claude/skills/import-project/SKILL.md
  - scripts/forge-clone.py
  - templates/project.md
---

# Bring in an existing project

This page shows how to clone a project you already have into `projects/` with `/import-project`, for the principal (the person whose thinking is forged) who has a project repository elsewhere and wants to work on it here. Terms of the forge are in the [Glossary](../reference/glossary.md).

## When to use it

Use it when the project lives in a git repository that is not yet on this machine, and you have its address.

If the project is already on this machine, do not use it. A project that sits in a repository of its own, in another repository or in none is not cloned. See "A project already on this machine" below.

## The command

```
/import-project <git-url>
```

`<git-url>` is the address of the repository. There is no slug to give: the project is placed in `projects/<repository name>`, and the name is taken from the end of the address (without a trailing `.git`).

## What happens

1. Claude requires the address. If `projects/<repository name>` already exists, it stops and says so.

   You should now see either a request for the address or the report that the directory exists.

2. On your word, Claude runs `python scripts/forge-clone.py <git-url>`. The script clones the repository into `projects/<repository name>`. It never overwrites an existing directory.

   You should now see the output of the clone, then the line "Cloned into projects/<repository name>".

3. Claude relays the facts the script prints:
   - the origin, that is the address the clone came from
   - the last commit
   - the identity git resolves for the clone
   - the project file, with its kind and language

   You should now see these facts stated one after the other.

4. Claude reads the identity line for you. Git signs commits with a name and an e-mail it resolves from your own configuration. If it resolves none, Claude says in plain words what that means: git has no name and e-mail to sign commits on this host, and the login that cloned the repository is a different thing. The save script then commits nothing until git resolves one. The ways out are the identity step of [Set up the forge](../start/setup.md), or `python scripts/forge-config.py --identity <host> <name> <email>`. The forge writes no identity of its own.

   You should now see either your name and e-mail, or the plain statement that none is resolved.

5. Claude reads the project line for you:
   - With a project file, you see the kind and the language of the project.
   - Without one, the project is of the shape before the migration. The one remedy is `/migrate`; see [Migrate a project](migrate-a-project.md).
   - With neither a project file nor a ledger (the ledger being the file that holds a project's state), the project was not made by the forge. That is a fact, not a defect.

   You should now see which of the three cases your project is.

6. Claude recommends `/forge <slug>` as the first act of work. The engine does not track the project and cannot guess it, so you select it by naming it. `<slug>` is the repository name.

   You should now see the recommendation to run `/forge <slug>`.

## What you have afterwards

- A clone of the repository in `projects/<repository name>`.
- Nothing written into it. `/import-project` clones and reports; it changes no file of the project.
- The facts above in the conversation, so that you know what to do next: set up an identity, migrate, or start.

Start work by selecting the project with `/forge <slug>`. The map that follows is described in [See where a project stands](see-where-a-project-stands.md). If the project was written to older conventions, see also [Upgrade the engine](upgrade-the-engine.md) for what to check.

## A project already on this machine

`/import-project` is for cloning. A project already on this machine is brought in by hand: copy it or link it into `projects/<slug>`. The forge knows it from `/forge <slug>` on.

## If something goes wrong

The script stops with one of these messages.

- `Cannot derive a repository name from '<git-url>'.` The address ends in nothing the script can use as a name. Give the full address of the repository.
- `projects/<repository name> already exists - never overwritten. Rename or remove it first.` A directory of that name is already in `projects/`. Rename or remove it, then run the command again.
- `Clone of <git-url> failed.` Git could not clone the address. The text git printed above this line says why.

The identity line is not an error, but it needs action. When it reads "none - git resolves no user.name/user.email for this repository", the save script commits nothing until you act. It names three ways out:
- run `/setup`
- run `python scripts/forge-config.py --identity <host> <name> <email>`
- set a local identity in the clone with git's `user.name` and `user.email` settings

## A worked example

The repository is at `https://example.com/team/my-idea.git`.

```
/import-project https://example.com/team/my-idea.git
```

Claude asks for your word and runs the script. The script prints something like this:

```
Cloned into projects/my-idea
  origin:      https://example.com/team/my-idea.git
  last commit: <hash> <date> <subject>
  identity:    <name> <email> (from your git configuration)
  project:     kind thought, language en
```

The project is now in `projects/my-idea`. Claude recommends:

```
/forge my-idea
```

## See also

- [See where a project stands](see-where-a-project-stands.md): the `/forge` map that follows.
- [Migrate a project](migrate-a-project.md): what to do with a project of the shape before the migration.
- [Upgrade the engine](upgrade-the-engine.md): what to check when a project was written to older conventions.
- [Set up the forge](../start/setup.md): the identity step, when git resolves no identity for the clone.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
