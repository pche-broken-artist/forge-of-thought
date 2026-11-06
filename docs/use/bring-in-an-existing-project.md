---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 90e580bed0a7e30d
inputs:
  - .claude/skills/import-project/SKILL.md
  - scripts/forge-clone.py
  - templates/project.md
---

# Bring in an existing project

This page shows how to clone a project you already have into `projects/` with `/import-project`. It is for the principal (the person whose thinking is forged) who has a project in a git repository and wants to work on it in this forge. Terms of the forge are one line each in the [Glossary](../reference/glossary.md).

## When to use it

- The project lives in a git repository that you can reach by a URL, and it is not yet on this machine.
- The project is already on this machine: then you do not clone it. See "A project already on this machine" below.

## The command

```
/import-project <git-url>
```

Replace `<git-url>` with the address of the repository. The directory is named after the repository, so there is no slug to give.

## What happens

1. Claude requires the URL and works out the target, `projects/<repository name>`, from it. If that directory already exists, Claude stops and says so. The script never overwrites it.
   You should now see either the target named, or the report that the directory exists.
2. On your word Claude runs the clone script, `python scripts/forge-clone.py <git-url>`. The script clones the repository into the target. It sets no commit identity and carries no URL of its own.
   You should now see git's own clone output, then the line "Cloned into projects/<repository name>".
3. Claude relays the facts the script prints:
   - `origin`: the address the clone came from.
   - `last commit`: the short hash, the date and the subject of the newest commit.
   - `identity`: the name and e-mail git resolves for the fresh clone, taken from your git configuration.
   - `project`: the project file, with its kind and language.
   You should now see these four lines under the "Cloned into" line.
4. Claude reads the facts to you in plain words. The project file line says one of three things:
   - The project has a project file: the line gives its kind (`thought` or `library`) and its language.
   - The project has no project file but has a ledger: it is of the shape before the migration. The line gives the kind and language read from the ledger's header. The one remedy is `/migrate`, described in [Migrate a project](migrate-a-project.md).
   - The project has neither a project file nor a ledger: it was not made by the forge. This is a fact, not a defect.
   You should now see which of the three holds for this project.
5. Claude recommends `/forge <slug>` as the first act of work. The engine does not track the project and cannot guess it, so you select the project by naming it. The map that follows is described in [See where a project stands](see-where-a-project-stands.md).
   You should now see the recommendation to run `/forge` with the repository name as the slug.

## What you have afterwards

- A clone of the repository in `projects/<repository name>`, with its own git history and its origin as it was.
- Nothing written into the project: the command clones and does nothing more.
- Your facts for the next step: the identity git resolves, and the shape of the project.

## A project already on this machine

`/import-project` only clones. A project that is already on this machine is not cloned, whether it sits in a repository of its own, inside another repository or in none. You copy it or link it into `projects/<slug>` by hand. The forge knows it from `/forge <slug>` on.

## If something goes wrong

- **The directory exists.** The script prints "projects/<repository name> already exists - never overwritten. Rename or remove it first." Rename or remove the old directory yourself, then run the command again.
- **No repository name can be taken from the URL.** The script prints "Cannot derive a repository name from '<git-url>'." Give the URL in a form that ends in the repository name.
- **The clone fails.** The script prints "Clone of <git-url> failed." Git's own output above that line says why.
- **Git resolves no identity.** The `identity` line reads "none". This means git has no name and e-mail to sign commits on this host. The login that cloned the repository is a different thing. The save script commits nothing until git resolves an identity. The ways out are the identity step of the setup, described in [Set up the forge](../start/setup.md), or this command, with the placeholders replaced:
  ```
  python scripts/forge-config.py --identity <host> <name> <email>
  ```
  The script names a third way, a local identity set with git in the project's own directory. The forge writes no identity itself.
- **The project has no project file.** The line says the shape is that of before the migration. Run `/migrate`.
- **The project was written to older conventions.** What to check after a change of engine is in [Upgrade the engine](upgrade-the-engine.md).

## A worked example

You have a project in a repository at `<git-url>`, and its name is `<repository name>`.

You type:

```
/import-project <git-url>
```

Claude asks for your word, then runs the script. The output ends like this:

```
Cloned into projects/<repository name>
  origin:      <git-url>
  last commit: <hash> <date> <subject>
  identity:    <name> <<email>> (from your git configuration)
  project:     kind thought, language en
```

Claude tells you the project has a project file, that its kind is `thought` and its language English, and that git will sign commits as the identity shown. It recommends `/forge <repository name>`. You run it and see the state map of the project.

## See also

- [See where a project stands](see-where-a-project-stands.md): the `/forge` map that follows.
- [Migrate a project](migrate-a-project.md): what to do with a project of the shape before the migration.
- [Upgrade the engine](upgrade-the-engine.md): what to check when a project was written to older conventions.
- [Set up the forge](../start/setup.md): the identity step, when git resolves no identity for the clone.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
