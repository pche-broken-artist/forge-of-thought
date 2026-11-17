---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 9048aa9831573ea4
inputs:
  - .claude/skills/import-project/SKILL.md
  - scripts/forge-clone.py
  - templates/project.md
  - projects/forge/10-intent.md#POS.1980
---

# Bring in an existing project

This page shows how to clone a project you already have into `projects/` with `/import-project`. It is for anyone who has a project repository elsewhere, such as a colleague's or their own on another machine, and wants to work on it in the forge.

## When to use it

Use `/import-project` when the project lives in a git repository you can reach by a URL and is not yet on this machine.

If the project is already on this machine, do not clone it. See "A project already on this machine" below.

## The command

```
/import-project <git-url>
```

## What happens

1. Claude requires the URL. The target is `projects/<repository name>`, and the name is taken from the end of the URL, so there is no slug to give. If that directory exists, Claude stops and says so.

   You should now see the target named, or the stop reported.

2. On your word Claude runs the clone script, `python scripts/forge-clone.py <git-url>`. The script never overwrites an existing directory. It sets no commit identity of its own: the identity is the one git resolves from your own configuration for that host.

   You should now see git's clone output and the line "Cloned into projects/<repository name>".

3. Claude relays the facts the script prints:

   - the origin of the clone
   - the last commit (short hash, date, subject)
   - the identity git resolves for the clone, or "none"
   - the project file with its kind and language

   You should now see these four lines.

4. If the identity is "none", Claude says what it means. Git has no name and e-mail to sign commits on this host. The login that cloned the repository is a different thing. The save script commits nothing until git resolves an identity. The way out is the identity step of [Set up the forge](../start/setup.md), that is `/setup`, or this command:

   ```
   python scripts/forge-config.py --identity <host> <name> <email>
   ```

   You should now see the identity either resolved or named as the one thing left to settle.

5. If the project has no project file, the script says it is of the shape before the migration. The one remedy is `/migrate`; see [Migrate a project](migrate-a-project.md). A project with neither a project file nor a ledger (the ledger is the file of the project's state, made at read time) was not made by the forge. That is a fact, not a defect.

   You should now see either the kind and language from the project file, or the shape named.

6. Claude recommends `/forge <slug>` as the first act of work. The engine does not track the project and cannot guess it, so you select it by naming it.

   You should now see the recommendation. The map that `/forge <slug>` prints is described in [See where a project stands](see-where-a-project-stands.md).

## What you have afterwards

- A clone of the repository in `projects/<repository name>`, with its own git history and origin.
- Nothing written into the project: the command only clones.
- A report of the commit identity and of the project's shape.

If the project was written to older conventions, [Upgrade the engine](upgrade-the-engine.md) says what to check. Why every project is a repository of its own is explained in [Projects and the engine](../about/projects-and-the-engine.md).

## A project already on this machine

`/import-project` only clones. A project that is already on this machine is not cloned, whether it sits in a repository of its own, in another's or in none. You copy or link it into `projects/<slug>` by hand. The forge knows it from `/forge <slug>` on.

## The forge's own project

The forge's own project is brought in the same way by whoever develops the engine. Its repository is named `forge`, so that it lands in `projects/forge` without a rename. A user never needs it.

## If something goes wrong

The script stops with one of these messages.

- `projects/<name> already exists - never overwritten. Rename or remove it first.` The target directory exists. Rename or remove it, or choose another repository.
- `Cannot derive a repository name from '<url>'.` The end of the URL gives no name. Give the URL of the repository itself.
- `Clone of <url> failed.` Git could not clone. The reason is in git's own output above the message.
- `identity:    none - git resolves no user.name/user.email for this repository ...` This is not a failure of the clone. Set the identity as step 4 describes. The message also offers a local setting, `git -C '<target>' config user.name/user.email`.
- `project:     no project file - not scaffolded by the forge (a fact, not a defect)` The project was not made by the forge. Nothing is wrong with the clone.

For the terms used here, see the [Glossary](../reference/glossary.md).

## A worked example

You have a repository at `<git-url>` whose last path segment is `my-idea`.

```
/import-project https://example.com/team/my-idea.git
```

Claude asks for your word, then runs the clone script. The report reads like this:

```
Cloned into projects/my-idea
  origin:      https://example.com/team/my-idea.git
  last commit: <hash> <date> <subject>
  identity:    <name> <<email>> (from your git configuration)
  project:     kind thought, language en
```

The identity is resolved and the project has its project file, so nothing is left to settle. Claude recommends the next act:

```
/forge my-idea
```

## See also

- [See where a project stands](see-where-a-project-stands.md): the `/forge` map that follows.
- [Migrate a project](migrate-a-project.md): what to do with a project of the shape before the migration.
- [Upgrade the engine](upgrade-the-engine.md): what to check when a project was written to older conventions.
- [Projects and the engine](../about/projects-and-the-engine.md): why every project, the forge's own among them, is a repository of its own.
- [Set up the forge](../start/setup.md): the identity step, when git resolves no identity for the clone.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
