---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 5f69123d0c166213
inputs:
  - .claude/skills/import-project/SKILL.md
  - scripts/forge-clone.py
  - templates/project.md
  - projects/forge/10-intent.md#POS.1980
---

# Bring in an existing project

This page shows how to clone a project you already have into `projects/` with `/import-project`. It is for you when the project lives in a git repository and is not yet on this machine. The principal is whoever's thinking is being forged.

## When to use it

Use it when the project exists as a git repository somewhere else and you want it on this machine. Cloning is the only thing the command does: nothing is written into the project.

If the project is already on this machine, do not use the command. It may sit in a repository of its own, in another one or in none. Copy or link it into `projects/<slug>` by hand. The forge knows it from `/forge <slug>` on.

## The command

```
/import-project <git-url>
```

The directory is `projects/<repository name>`. The name is taken from the URL, so the command has no slug parameter.

## What happens

1. Claude requires the URL. It stops and says so if the target directory already exists.

   You should now see either the target `projects/<repository name>` named, or a report that the directory exists.

2. On your word, Claude runs the clone script, `python scripts/forge-clone.py <git-url>`. The script never overwrites an existing directory. It sets no commit identity and carries no URL of its own.

   You should now see git's own clone output, then the line "Cloned into projects/<repository name>".

3. Claude relays the facts the script prints:
   - the origin of the clone
   - the last commit
   - the commit identity git resolves for the clone
   - the project file, with its kind and language

   You should now see a block of four lines, one for each fact.

4. If git resolves no identity, the script says so, and Claude puts it in plain words. Git has no name and e-mail to sign commits on this host. The login that cloned the repository is a different thing. The save script commits nothing until git resolves an identity. The way out is the identity step in [Set up the forge](../start/setup.md), or this line:

   ```
   python scripts/forge-config.py --identity <host> <name> <email>
   ```

   You should now see, after a fix, your name and e-mail on the identity line when the clone is read again.

5. Claude recommends `/forge <slug>` as the first act of work. The engine does not track the project and cannot guess it, so you select it by naming it. The map that follows is described in [See where a project stands](see-where-a-project-stands.md).

   You should now see the state map of the project.

## What you have afterwards

- A clone of the repository in `projects/<repository name>`, with its own history and its origin.
- Nothing changed inside it.

What the project line says about the project:

- With a project file: the kind and the language.
- Without a project file but with a ledger: the project is of the shape before the migration. The one remedy is `/migrate`, described in [Migrate a project](migrate-a-project.md). A project written to older conventions may need more checks; see [Upgrade the engine](upgrade-the-engine.md).
- With neither a project file nor a ledger: the forge did not make the project. This is a fact, not a defect.

Every project, the forge's own among them, is a repository of its own. The reason is given in [Projects and the engine](../about/projects-and-the-engine.md).

The forge's own project is brought in the same way by whoever develops the engine. Its repository is named `forge`, so it lands in `projects/forge` without a rename. A user never needs it.

## If something goes wrong

The script prints these messages:

- "projects/<name> already exists - never overwritten. Rename or remove it first." The target directory is taken. Rename or remove the existing one, then run the command again.
- "Cannot derive a repository name from '<url>'." The URL ends in nothing the script can use as a name. Give the URL of the repository itself.
- "Clone of <url> failed." Git could not clone. Its own message stands above this line.
- "identity: none - git resolves no user.name/user.email for this repository". The message names three ways out: `/setup`, the `forge-config.py --identity` line above, or a local identity set with `git -C '<target>' config user.name/user.email`. The save script commits nothing until one of them is done.
- "project: shape before the migration ... run /migrate". The project has no project file. Run `/migrate`.
- "project: no project file - not scaffolded by the forge (a fact, not a defect)". Nothing is wrong; the project was made elsewhere.

Git must be on PATH, or the script stops before cloning.

## A worked example

You have a repository you want to work on. Its URL is `<git-url>`, and the repository is named `my-idea`.

```
/import-project <git-url>
```

Claude asks for your word and you give it. The script clones into `projects/my-idea` and prints:

```
Cloned into projects/my-idea
  origin:      <git-url>
  last commit: <hash> <date> <subject>
  identity:    <name> <<email>> (from your git configuration)
  project:     kind thought, language en
```

Claude then recommends `/forge my-idea`. You run it and the state map of the project opens.

## See also

- [See where a project stands](see-where-a-project-stands.md): the `/forge` map that follows.
- [Migrate a project](migrate-a-project.md): what to do with a project of the shape before the migration.
- [Upgrade the engine](upgrade-the-engine.md): what to check when a project was written to older conventions.
- [Projects and the engine](../about/projects-and-the-engine.md): why every project, the forge's own among them, is a repository of its own.
- [Set up the forge](../start/setup.md): the identity step, when git resolves no identity for the clone.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
