---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 3bcbbfb4810a50ce
inputs:
  - .claude/skills/setup/SKILL.md
  - templates/CLAUDE.local.md
  - scripts/forge-config.py
  - scripts/forge-status.py
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
---

# Set up the forge

This page walks you through `/setup`, the first command to run after cloning the engine. It is for anyone who has just installed the forge and wants to prepare their own instance, that is, their one installation of it, before any other work.

The course page of the teaching videos, https://pche-broken-artist.github.io/forge-of-thought/videos/, shows a first run before you make your own.

Prerequisite: the machine has what the forge needs, as [Install what the forge needs](install.md) lists it. Start `claude` from the engine root, so that its instructions load.

## When to use it

Use it once, on a new machine, right after cloning the engine and before any other command. Run it again where git reads another global configuration file in another place, such as a network home at work and a local profile at home. Run on an instance that is already set up, it changes nothing that exists.

## The command

```
/setup
```

## What happens

Claude speaks whatever language you speak to it until you have named the conversation language in the first step.

1. **The instance file.** Claude copies the template to `CLAUDE.local.md` at the engine root and fills it with a short interview, one question at a time. The file is gitignored and never committed. The questions come in this order:
   - the conversation language, first, so that every later question arrives in it;
   - who the principal is, by role (the principal is whoever's thinking is being forged);
   - the principal's short handle, which stands as the author of every history record the principal decides.

   You should now see a `CLAUDE.local.md` with three lines, Principal, Conversation language and Author. If the file already exists, Claude reports briefly what it holds, touches nothing, and offers one by one only the lines the template has and the file lacks. You should now see those lines written only on your word.

2. **The git identity.** The identity is git's, kept per host, and the forge only writes it through one script. Claude first runs `python scripts/forge-config.py`, which changes nothing and shows what the global git configuration holds: the file git reads, the registration of the merge driver, the guard, a global identity and the per-host stanzas. You should now see that report.

   Claude then asks which hosts you push to, with a name and an e-mail for each. You may leave this for later. On your word it makes one call per host:

   ```
   python scripts/forge-config.py --identity <host> <name> <email>
   ```

   The call writes the per-host stanzas to the global file and an identity file beside it. A stanza or an identity file that differs from what you gave is reported and left alone. Claude offers `--replace` for it apart, again on your word. You should now see, for each host, a line saying what was written or what was left.

3. **The global guard.** On your word Claude runs `python scripts/forge-config.py --guard`. The guard makes git fail aloud in a repository that has no identity of its own, instead of taking a default. It only bites once no global name or e-mail is left. Where the script reports one, Claude says so and offers `python scripts/forge-config.py --guard --unset-identity`, which removes it, again only on your word. You should now see the guard line read `user.useConfigOnly = true`.

4. **The merge driver.** Once per machine, and once in each place where git reads another global file, Claude offers on your word the registration of the merge driver `ours` and the git settings it needs:

   ```
   python scripts/forge-config.py --register
   ```

   The option `--zdiff3` is offered apart: it adds a clearer conflict style. These settings hold for every repository on the machine. One of them, renormalize, only evens out line endings at a merge. Nothing already set is overwritten. You should now see each key reported as written or as already there. `python scripts/forge-status.py` reports the registration afterwards, as ok or as the keys missing.

5. **The session model.** Claude creates `.claude/settings.local.json` with the session model set to Fable, the strongest model, on which the whole forge runs, the blind reviewers included. A session is one running conversation with Claude. Where the account does not list Fable, Claude writes the strongest model it lists and says which. This is a notice, not a question. You can change the model at any time with `/model` or by editing the file. You should now see the file with a `model` entry. If the file already exists, Claude reports the model it names and leaves it alone.

6. **The next step.** Claude ends by pointing at `/new-project <slug>` to start a new project, or `/import-project <git-url>` to bring an existing one in.

## What you have afterwards

- `CLAUDE.local.md` at the engine root, with the conversation language, the principal's role and the author's handle.
- In the global git configuration, whatever you accepted: the per-host identity stanzas with their identity files, the guard and the merge driver registration.
- `.claude/settings.local.json` with the session model.

Git verifies the identity at your first `/import-project`, where the clone script reports the identity git resolves for the clone.

## If something goes wrong

- A stanza or an identity file differs from what you gave: the script reports it and leaves it. Accept `--replace` for that host if you want it rewritten.
- The guard seems to do nothing: a global name or e-mail still stands. Run `python scripts/forge-config.py --guard --unset-identity`.
- You decline a step that writes the global configuration: Claude prints the command for you to run by hand.
- `forge-status.py` says the registration is missing: run `/setup` again, or `python scripts/forge-config.py --register`, in the place where git reads that global file.
- The script needs git 2.36 or newer and Python 3.8 or newer on PATH.

## A worked example

```
/setup
```

Claude asks for the conversation language and you answer. It asks who the principal is and you answer with a role. It asks for the handle and you answer with a short one. Then you name one host with a name and an e-mail. Claude runs:

```
python scripts/forge-config.py --identity <host> <name> <email>
python scripts/forge-config.py --guard --unset-identity
python scripts/forge-config.py --register
```

It creates `.claude/settings.local.json` and points at `/new-project <slug>`. From there, [Get a first result](first-result.md) takes you from a new project to a saved intent in one sitting.

## See also

- [Install what the forge needs](install.md): what must be on the machine first.
- [Get a first result](first-result.md): from a new project to a saved intent in one sitting.
- [Persistence in git](../about/persistence-in-git.md): why the identity is git's, why the scripts are the only door and what the merge driver `ours` is for.
- [Configuration](../reference/configuration.md): the instance files and settings, field by field.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
