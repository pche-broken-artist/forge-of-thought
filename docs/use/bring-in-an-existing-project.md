---
generated: 2026-10-23
version: 5.34
made: mirrored
inputs-hash: 6a8442c686ad3491
inputs:
  - .claude/skills/import-project/SKILL.md
  - scripts/forge-clone.py
  - templates/project.md
---

# Bring in an existing project

This page shows how to clone a project that already lives in a git repository into `projects/` with `/import-project`. It is for the principal (the person whose thinking is forged) who has a project elsewhere and wants to work on it here.

## When to use it

- The project is in a git repository that you can reach by a URL.
- The project is not yet on this machine.

If the project is already on this machine, nothing is cloned. See "A project already on this machine" below.

## The command

```
/import-project <git-url>
```

## What happens

1. Claude requires the URL. The target directory is `projects/<repository name>`, and the name is taken from the end of the URL. There is no slug parameter. If that directory already exists, Claude stops and reports it.

   You should now see the URL accepted and the target directory named, or the stop.

2. On your word, Claude runs `python scripts/forge-clone.py <git-url>`. The script clones the repository into the target directory. It never overwrites an existing directory. It sets no commit identity and carries no URL of its own.

   You should now see the output of git's clone, then the line "Cloned into projects/<repository name>".

3. Claude relays the facts the script prints:

   - `origin`: the address the clone came from.
   - `last commit`: the short hash, the date and the subject of the newest commit.
   - `identity`: the name and e-mail that git resolves for the fresh clone, taken from your git configuration.
   - `project`: what the project file says, as described below.

   You should now see these four lines.

4. Claude recommends `/forge <slug>` as the first act of work. The forge does not track the project and cannot guess it, so the project is selected by naming it. The `/forge` map is described in [See where a project stands](see-where-a-project-stands.md).

   You should now see the recommendation to run `/forge <slug>`.

### Reading the identity line

When git resolves no name and e-mail for the clone, the line says `none`. That means git has no identity to sign commits with on this host. The login that cloned the repository is a different thing. The save script commits nothing until git resolves an identity.

The script names two ways out:

- Run `/setup`. Its identity step is described in [Set up the forge](../start/setup.md).
- Run `python scripts/forge-config.py --identity <host> <name> <email>`.

The script also names a third, local to this one repository: set `user.name` and `user.email` with `git config` in the clone. The forge writes no identity itself.

### Reading the project line

The project file records the project's kind and language.

- With a project file, the line reads `kind <kind>, language <language>`, and `fixture` is added for a fixture project.
- Without a project file but with a ledger, the project is of the shape before the migration. The line gives the kind and language from the ledger's header and says to run `/migrate`. That is the one remedy. See [Migrate a project](migrate-a-project.md).
- With neither a project file nor a ledger, the line says the project was not scaffolded by the forge. That is a fact, not a defect.

## What you have afterwards

- A clone at `projects/<repository name>`, with its own git history and its origin.
- Nothing written into the project: the command only clones.
- A report of the last commit, the origin, the identity and the project file.

## A project already on this machine

A project that is already on this machine is not cloned. It may be in a repository of its own, in another one's, or in none. You copy or link it into `projects/<slug>` by hand. The forge knows it from `/forge <slug>` on.

If the project was written to older conventions, check [Upgrade the engine](upgrade-the-engine.md) for what to look at.

## If something goes wrong

The messages come from the script.

- `Cannot derive a repository name from '<url>'.` The end of the URL gave no name. Give the full address of the repository.
- `projects/<name> already exists - never overwritten. Rename or remove it first.` A directory of that name is in `projects/`. Rename or remove it, then run the command again.
- `Clone of <url> failed.` Git could not clone. Git's own message stands above this line. Fix the cause it names, such as the address or your access, and run the command again.
- `identity: none ...` The clone has no commit identity. See "Reading the identity line".
- `project: shape before the migration ... run /migrate`. See "Reading the project line".
- `project: no project file - not scaffolded by the forge (a fact, not a defect)`. Nothing to fix.

## A worked example

You have a repository of a project called `my-idea`. You type:

```
/import-project <git-url>
```

Claude asks for your word and runs the script. The script prints something of this shape:

```
Cloned into projects/my-idea
  origin:      <git-url>
  last commit: a1b2c3d 2026-01-15 <subject of the commit>
  identity:    <name> <<email>> (from your git configuration)
  project:     kind thought, language en
```

You should now see `projects/my-idea` on disk. Claude recommends `/forge my-idea`, and you run it to see the state of the project.

## See also

- [See where a project stands](see-where-a-project-stands.md): the `/forge` map that follows.
- [Migrate a project](migrate-a-project.md): what to do with a project of the shape before the migration.
- [Upgrade the engine](upgrade-the-engine.md): what to check when a project was written to older conventions.
- [Set up the forge](../start/setup.md): the identity step, when git resolves no identity for the clone.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.34 from the files the front-matter names; never edited by hand.
