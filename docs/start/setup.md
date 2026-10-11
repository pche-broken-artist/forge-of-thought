---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 7fb2c24a171e8a31
inputs:
  - .claude/skills/setup/SKILL.md
  - templates/CLAUDE.local.md
  - scripts/forge-status.py
---

# Set up the forge

`/setup` is the first command to run after cloning the engine: it prepares your own instance of the forge, and this page is for the person who has just cloned it. It asks a few questions, writes two small files, and offers a third piece of configuration that lives outside the engine. The tools it relies on are listed in [Install what the forge needs](install.md), which comes first.

A term you meet here is explained in the [Glossary](../reference/glossary.md). The principal is the person whose thinking is being forged, and Claude is the assistant that works with the principal.

## When to use it

Run it once, before any other work, on a machine where the engine was just cloned. It is safe to run again: it never overwrites an existing file, and it runs no git operation.

## The command

```
/setup
```

## What happens

There are three steps.

1. **`CLAUDE.local.md` is created.** If the file already exists at the engine root, `/setup` reports briefly what it holds and leaves it alone. Otherwise it copies the template and fills it by a short interview, one question at a time:
   - the conversation language first, so that every later question arrives in it
   - who the principal is, by role (for example "the CTO")

   The file is gitignored and never committed. You should now see `CLAUDE.local.md` at the engine root with the two answers in it.

2. **`.claude/settings.local.json` is created.** If the file already exists, `/setup` reports the model it names and leaves it alone. Otherwise it writes the session model, `fable`, the strongest model. The whole forge runs on this one model, the blind reviewers included. Where your account does not offer Fable, `/setup` writes the strongest model the account lists and says which one. This is a notice, not a question. You can change the model at any time with `/model` or by editing the file. You should now see one sentence naming the model the session is set to.

3. **The git identity is offered.** The identity is git's own, not the forge's. `/setup` asks which git hosts you will push to, with a name and an e-mail for each. You may leave this for later, and it says so. It then offers to write, on your word, the configuration into the global git configuration file that git actually reads. The file is named by `scripts/forge-status.py`, which `/setup` reads first. Existing content is never overwritten: an existing stanza or guard is reported and left as it is. The offer holds:
   - per host, two `includeIf` stanzas, one for `https://<host>/**` remote URLs and one for `git@<host>:*/**` remote URLs
   - an absolute path in each stanza, to a file `.gitconfig-<host>` beside the global file, created with your `name` and `email` when it is missing
   - the global guard `user.useConfigOnly = true` under `[user]`, so that a repository on a host with no stanza fails aloud instead of taking a default

   If the global file already carries a `user.name` or `user.email`, `/setup` says that the guard only bites once that identity is removed, and offers the removal, again only on your word. If you decline, it prints the stanzas and the lines for you to apply by hand. These are the only edits outside the engine, and they are configuration text files, not a git operation. You should now see either the written stanzas reported, or the printed lines in front of you.

`/setup` ends by pointing at the next step: `/new-project <slug>` to start a project, or `/import-project <git-url>` to bring in an existing one.

## What you have afterwards

- `CLAUDE.local.md` at the engine root, with the conversation language and the principal
- `.claude/settings.local.json`, with the session model
- optionally, per-host identity stanzas and the guard in your global git configuration

The instance files and settings are described field by field in [Configuration](../reference/configuration.md). The reason the identity is git's and the scripts are the only door to git is explained in [Persistence in git](../about/persistence-in-git.md).

## A worked example

You run `/setup` on a fresh clone. The answers are placeholders.

```
/setup
```

- Conversation language: `<language>`
- Principal: `<role>`
- Git host: `<host>`, name `<name>`, e-mail `<e-mail>`

You accept the offer to write the configuration. Afterwards the global git configuration holds the two stanzas for `<host>` and the guard:

```
[includeIf "hasconfig:remote.*.url:https://<host>/**"]
    path = <absolute path>/.gitconfig-<host>
[includeIf "hasconfig:remote.*.url:git@<host>:*/**"]
    path = <absolute path>/.gitconfig-<host>
[user]
    useConfigOnly = true
```

The file `.gitconfig-<host>` beside it holds `[user]` with `name = <name>` and `email = <e-mail>`.

## See also

- [Install what the forge needs](install.md): what must be on the machine first.
- [Get a first result](first-result.md): from a new project to a saved intent in one sitting.
- [Persistence in git](../about/persistence-in-git.md): why the identity is git's and the scripts are the only door.
- [Configuration](../reference/configuration.md): the instance files and settings, field by field.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
