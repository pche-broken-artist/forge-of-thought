---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 0a2c4cd86c547ec5
inputs:
  - .claude/skills/setup/SKILL.md
  - templates/CLAUDE.local.md
  - scripts/forge-status.py
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
---

# Set up the forge

`/setup` is the command you run first, once, after cloning the engine. It prepares your installation: it creates the file that holds your instance facts, sets the model Claude runs on, and offers the git identity for the hosts you push to. This page is for the person who has just cloned the forge and not yet done any other work. The course page of the teaching videos, https://pche-broken-artist.github.io/forge-of-thought/videos/, shows a first run before you make your own.

## When to use it

Run it once, before any other command, on a machine where you have just cloned the engine. What must be on the machine first is on [Install what the forge needs](install.md).

Run it from the engine root, in a Claude Code conversation started there. On a true first run no conversation language is configured yet, so Claude speaks whatever language you speak to it.

## The command

```
/setup
```

## What happens

The command has three steps. It never overwrites a file that already exists, and it runs no git operation.

1. **`CLAUDE.local.md` is created.**
   - If the file already exists, Claude reports briefly what it holds and leaves it alone.
   - Otherwise Claude copies the template to the engine root and fills it with a short interview, one question at a time.
   - It asks the conversation language first, so that every later question arrives in it.
   - It then asks who the principal is, by role. The principal is the person whose thinking is being forged, for example "the CTO".
   - The file is ignored by git and is never committed.

   You should now see `CLAUDE.local.md` at the engine root with two lines: the principal and the conversation language.

2. **The git identity is offered.** The identity is git's own, set per host. Claude asks:
   - which git hosts you will push to;
   - a name and an e-mail for each host.

   You may leave this for later, and Claude says so. Then it offers, on your word, to write the following into the global git configuration file. The status script `scripts/forge-status.py` names that file, and Claude reads it first.
   - for each host, two `includeIf` stanzas, one for the `https` form of the remote address and one for the `git@` form, each pointing to a file `.gitconfig-<host>` beside the global file;
   - the file `.gitconfig-<host>`, with your name and e-mail, where it is missing;
   - the global guard `user.useConfigOnly = true` under `[user]`, so that a repository on a host with no stanza fails aloud instead of taking a default name.

   Existing content is never overwritten. An existing stanza or guard is reported and left as it is. If the global file already carries a `user.name` or `user.email`, Claude says the guard only takes effect once that identity is removed, and offers the removal, again only on your word. If you decline, Claude prints the stanzas and the lines for you to apply by hand. These are the only edits outside the engine, and they are text files of configuration, not a git operation.

   You should now see either the stanzas written into the global git configuration file, or the printed lines to apply yourself.

3. **`.claude/settings.local.json` is created.**
   - If the file already exists, Claude reports the model it names and leaves it alone.
   - Otherwise Claude creates it with the session model set to Fable, the strongest model. A session is one running conversation with Claude.
   - The whole forge runs on this model, the blind reviewers included.
   - If your account does not list Fable in `/model`, Claude writes the strongest model your account does list and says which. This is a notice, not a question.
   - You can change the model at any time with `/model` or by editing the file.

   You should now see one sentence naming the model the session is set to.

Claude ends by pointing at the next step: `/new-project <slug>` to start a new project, or `/import-project <git-url>` to bring in an existing one.

## What you have afterwards

- `CLAUDE.local.md` at the engine root, ignored by git.
- `.claude/settings.local.json` with the session model.
- Optionally, the per-host git identity and the global guard in your global git configuration.

The files are described field by field on [Configuration](../reference/configuration.md). Why the identity is git's and why the scripts are the only door to git is on [Persistence in git](../about/persistence-in-git.md).

## If something goes wrong

- A file that exists is never replaced. If you want a fresh `CLAUDE.local.md` or `.claude/settings.local.json`, you remove the old file yourself and run the command again.
- If the global git configuration file already holds an identity of its own, the guard has no effect until you remove that identity. Claude says so and offers the removal.
- If you leave the git identity for later, nothing is written. The stanzas can be offered again by running the command with the files removed, or you can write them by hand.

## A worked example

You have just cloned the engine and start Claude from its root. All values below are placeholders.

```
/setup
```

1. Claude asks the conversation language. You answer `<language>`. It asks who the principal is. You answer `<role>`. `CLAUDE.local.md` now holds:

   ```
   - **Principal:** <role>
   - **Conversation language:** <language>
   ```

2. Claude asks which hosts you push to. You answer `<host>`, with `<name>` and `<e-mail>`. It offers to write the stanzas for `<host>` and the guard into the global git configuration file. You agree. Claude reports the file it wrote and the file `.gitconfig-<host>` it created.
3. Claude reports that `.claude/settings.local.json` was created and the session is set to Fable, changeable with `/model`.
4. Claude points at `/new-project <slug>` and `/import-project <git-url>`. To go on, follow [Get a first result](first-result.md).

## See also

- [Install what the forge needs](install.md): what must be on the machine first.
- [Get a first result](first-result.md): from a new project to a saved intent in one sitting.
- [Persistence in git](../about/persistence-in-git.md): why the identity is git's and the scripts are the only door.
- [Configuration](../reference/configuration.md): the instance files and settings, field by field.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
