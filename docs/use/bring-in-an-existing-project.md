---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 6603046be4e4500d
inputs:
  - .claude/skills/import-project/SKILL.md
  - scripts/forge-clone.py
---

# Bring in an existing project

This page shows how to bring a project you already have, kept in a git repository, into the `projects/` directory of the engine with `/import-project`. It is for you, the principal (the person whose thinking is forged), when the project exists elsewhere and you want to work on it here.

## When to use it

Use it when the project already lives in a git repository and `projects/` does not yet hold it. A project that is new is scaffolded instead, and this command does not do that.

## The command

```
/import-project <git-url>
```

Replace `<git-url>` with the address of your repository. Claude asks for your word before it runs the clone.

## What happens

1. Claude requires the address. The target directory is `projects/<repository name>`, and the name is taken from the address, so there is no slug to give. If that directory already exists, Claude stops and reports.

   You should now see the target named, or the stop reported.

2. On your word, Claude runs the clone script, `scripts/forge-clone.py`, with the address. The script clones the repository into the target directory and never overwrites a directory that exists. It sets no commit identity of its own: the identity is the one git resolves from your own configuration.

   You should now see git's clone output and the line "Cloned into projects/<repository name>".

3. Claude relays the facts the script prints:
   - the origin: the address the clone came from
   - the last commit: its short hash, date and subject
   - the identity: the name and e-mail git resolves for the clone; if git resolves none, the save script will report it and commit nothing
   - the ledger: whether the project has a ledger with a `kind:` header; its absence is a fact, not a defect

   You should now see these four lines, each with its fact.

4. Claude recommends `/forge <slug>` as the first act of work. The engine does not track projects and cannot guess which one you mean, so you select the project by naming it.

   You should now see the recommendation to select the project.

Nothing is written into the imported project by this command.

## What you have afterwards

A clone of your repository in `projects/<repository name>`, with its own history and its origin untouched. Work starts when you select it with `/forge <slug>`, where the slug is the repository name.

## If something goes wrong

- The directory `projects/<repository name>` already exists: the script stops with "projects/<name> already exists - never overwritten. Rename or remove it first." Rename or remove the existing directory, then run the command again.
- A repository name cannot be read from the address: the script stops with "Cannot derive a repository name from '<address>'." Give the full address of the repository.
- The clone fails: the script stops with "Clone of <address> failed." Check the address and your access to the repository.
- Git is not on your path: the script cannot run, because it needs Python 3.8 or newer and git.
- The identity line says "none resolved": the clone is fine, but the save script will report the missing identity and commit nothing until your git configuration provides one.

## A worked example

You run:

```
/import-project <git-url>
```

Claude asks for your word, you give it, and the script prints, for a repository named `my-idea`:

```
Cloned into projects/my-idea
  origin:      <git-url>
  last commit: <hash> <date> <subject>
  identity:    <name> <e-mail> (from your git configuration)
  ledger:      present, kind: thought
```

Claude then recommends `/forge my-idea`. If the ledger line had said "none - not scaffolded by the forge", the project would still be imported, and that line would be the fact to know about it. The map that `/forge` shows is described in [See where a project stands](see-where-a-project-stands.md). If the project was written to older conventions, [Upgrade the engine](upgrade-the-engine.md) says what to check.

## See also

- [See where a project stands](see-where-a-project-stands.md): the `/forge` map that follows.
- [Upgrade the engine](upgrade-the-engine.md): what to check when a project was written to older conventions.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
