---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 5252475f474ef655
inputs:
  - .claude/skills/import-project/SKILL.md
  - scripts/forge-clone.py
---

# Bring in an existing project

This page shows how to clone a project you already have into `projects/` with `/import-project`. It is for the principal (the person whose thinking is forged) who has a project in a git repository and wants to work on it here. Terms of the forge are in the [Glossary](../reference/glossary.md).

## When to use it

Use it when the project already exists as a git repository, and you want it to sit under `projects/` next to the others. For a project that does not exist yet, this page does not apply.

## The command

```
/import-project <git-url>
```

`<git-url>` is the address of the repository. The directory is not a parameter: it is `projects/<repository name>`, and the name is taken from the end of the URL (a trailing `.git` is dropped). Claude runs the clone on your word.

## What happens

1. Claude checks that you gave a URL. If the directory `projects/<repository name>` already exists, it stops and says so.

   You should now see either a clone starting or the report that the directory exists.

2. On your word, Claude runs `python scripts/forge-clone.py <git-url>`. The script clones the repository into `projects/<repository name>`. It never overwrites an existing directory. It sets no commit identity and carries no URL of its own.

   You should now see the line `Cloned into projects/<repository name>`.

3. Claude relays the facts the script prints:

   - `origin`: the address the clone came from.
   - `last commit`: the short hash, date and subject of the newest commit.
   - `identity`: the commit identity git resolves for the fresh clone, taken from your own git configuration.
   - `ledger`: whether the project has a ledger (the file that holds the project's state) and whether its header carries a `kind:` line.

   You should now see these four lines under the "Cloned into" line.

4. Claude recommends `/forge <slug>` as the first act of work. The engine does not track the project and cannot guess it, so you select the project by naming it. The `/forge` map is described in [See where a project stands](see-where-a-project-stands.md).

   You should now see Claude recommend `/forge <slug>`.

## What you have afterwards

- A clone of the repository in `projects/<repository name>`.
- The four facts above, said once.
- Nothing written into the project: the command changes no file of it.

## If something goes wrong

The script prints these messages and stops.

- `Cannot derive a repository name from '<url>'.` The URL gives no name at its end. Give the full address of the repository.
- `projects/<name> already exists - never overwritten. Rename or remove it first.` A directory of that name is already there. Rename or remove it yourself, then run the command again.
- `Clone of <url> failed.` Git could not clone the address. Check the address and your access to it.

Two lines of the report are facts, not failures:

- `identity: none resolved - forge-save will report it and skip the commit`. Git resolves no commit identity for the clone. The save script then reports this and commits nothing, until your git configuration gives one.
- `ledger: none - not scaffolded by the forge (a fact, not a defect)` or `ledger: present, no kind: header`. The project was not made by the forge, or its ledger lacks the header. If the project was written to older conventions, see [Upgrade the engine](upgrade-the-engine.md) for what to check.

## A worked example

```
/import-project https://example.com/team/my-idea.git
```

Claude asks for your word, then runs the clone. The report ends like this, with your own values in place of the placeholders:

```
Cloned into projects/my-idea
  origin:      https://example.com/team/my-idea.git
  last commit: <hash> <date> <subject>
  identity:    <name> <email> (from your git configuration)
  ledger:      present, kind: <kind>
```

Claude then recommends `/forge my-idea`.

## See also

- [See where a project stands](see-where-a-project-stands.md): the `/forge` map that follows.
- [Upgrade the engine](upgrade-the-engine.md): what to check when a project was written to older conventions.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
