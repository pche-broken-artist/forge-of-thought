---
generated: 2026-10-25
version: 6.1
made: mirrored
inputs-hash: 0565d38ad8857269
inputs:
  - .claude/skills/setup/SKILL.md
  - templates/CLAUDE.local.md
  - scripts/forge-config.py
  - scripts/forge-status.py
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
---

# Set up the forge

This page is for you on the first run after cloning the engine. `/setup` prepares your instance of the forge: it creates the file of facts about you, offers the git identity and the registration of the merge driver `ours`, and sets the model. Run it before any other work. The machine must be ready first, as [Install what the forge needs](install.md) describes.

## When to use it

- Once, right after cloning the engine and before any other command.
- Once more in each place where git reads a different global configuration file, such as a network home at work and a local profile at home.

## The command

```
/setup
```

Start `claude` from the engine root, so that the engine's rules and your instance file load. A term you meet here has a one-line entry in the [Glossary](../reference/glossary.md). The principal is the person whose thinking is being forged, which is you.

## What happens

1. Claude creates `CLAUDE.local.md` at the engine root, from its template, by a short interview. It asks one question at a time and speaks whatever language you speak, because no conversation language is configured yet.
   - The conversation language comes first, so that every later question arrives in it.
   - Then who the principal is, by role.
   - Then the principal's short handle. It stands as the author of every history record the principal decides.

   The file is gitignored and never committed. On an instance that already has it, `/setup` reports briefly what it holds, touches nothing, and offers only the lines the template has and the file lacks, one by one, written on your word.

   You should now see `CLAUDE.local.md` at the engine root with the three lines filled.

2. Claude shows what git already holds. It runs `python scripts/forge-config.py`, which changes nothing and reports:
   - the global git configuration file git reads
   - whether the merge driver `ours` is registered
   - whether the guard is set
   - a global identity, if one stands
   - the per-host identity stanzas

   You should now see these lines, each marked ok or missing.

3. The git identity. Git owns it, per host, and the forge sets none of it. You name the hosts you push to, with a name and an e-mail for each, or you leave it for later. On your word Claude makes one call per host:

   ```
   python scripts/forge-config.py --identity <host> <name> <email>
   ```

   The call writes two stanzas for the host in the global configuration, and an identity file beside the global file, where it is missing. A stanza or an identity file that carries another path, name or e-mail is reported and left. Only `--replace` rewrites it, and Claude offers that apart, again on your word.

   You should now see each stanza and identity file reported as written, or as already there and left.

4. The global guard:

   ```
   python scripts/forge-config.py --guard
   ```

   The guard makes a repository on a host with no identity fail aloud instead of taking a default. It bites only once no global name or e-mail is left. Where the script reports one, Claude says so and offers, on your word:

   ```
   python scripts/forge-config.py --guard --unset-identity
   ```

   You should now see `user.useConfigOnly = true` written, and the global name and e-mail removed if you agreed.

5. The registration of the merge driver `ours`, once per machine and once in each place where git reads another global file, on your word:

   ```
   python scripts/forge-config.py --register
   ```

   `--zdiff3` is offered apart and adds a clearer conflict style. These settings hold for every repository on the machine. Among them, `renormalize` only evens line endings at a merge. Nothing already set is overwritten. The forge has no merge driver of its own for record files. Why the driver `ours` is needed is explained in [Persistence in git](../about/persistence-in-git.md).

   You should now see each key written or reported as already there.

6. Claude creates `.claude/settings.local.json` with the session model set to Fable, the strongest model. The whole forge runs on it, the blind reviewers included. Where your account does not list Fable, Claude writes the strongest model the account lists and says which. This is a notice, not a question. You can change the model at any time with `/model` or by editing the file. If the file already exists, Claude reports the model it names and leaves it alone.

   You should now see the file in `.claude/`, and one sentence naming the model.

7. Claude points at the next step: `/new-project <slug>` to start a project, or `/import-project <git-url>` to bring one in. [Get a first result](first-result.md) takes a new project to a saved intent in one sitting.

If you decline a git step, Claude prints the command for you to run by hand.

## What you have afterwards

- `CLAUDE.local.md` with your language, role and handle.
- `.claude/settings.local.json` with the session model.
- In your global git configuration, as far as you agreed: identity stanzas per host, the guard and the registered merge driver.

The fields of the instance files are listed in [Configuration](../reference/configuration.md). The identity is verified by git at your first `/import-project`, which reports the identity git resolves for the clone.

To see the registration later, run:

```
python scripts/forge-status.py
```

It reports the registration as ok, or names the keys that are missing.

## If something goes wrong

- A stanza, an identity file or a key reports "carries another value" and is left. The script never overwrites it. Use `--replace` for an identity, on purpose.
- The guard is set but git still takes a default identity. A global name or e-mail still stands. Run `--guard --unset-identity`.
- `forge-status` names missing keys on a machine you already set up. Git reads another global file in this place. Run `/setup` here too.
- The scripts need Python 3.8 or newer as `python`, and git 2.36 or newer.

## A worked example

```
/setup
```

1. Claude asks for the conversation language. You answer `<language>`.
2. It asks who the principal is. You answer `<role>`.
3. It asks for your handle. You answer `<handle>`.
4. It runs `python scripts/forge-config.py` and shows the state.
5. You name one host with a name and an e-mail, and Claude runs:

   ```
   python scripts/forge-config.py --identity <host> <name> <email>
   ```

6. You accept `--guard`, and `--guard --unset-identity` because a global identity stood.
7. You accept `--register`, and decline `--zdiff3`.
8. Claude creates `.claude/settings.local.json` and says which model it set.
9. It points at `/new-project <slug>`.

The course page of the teaching videos, `https://pche-broken-artist.github.io/forge-of-thought/videos/`, shows a first run before you make your own.

## See also

- [Install what the forge needs](install.md): what must be on the machine first.
- [Get a first result](first-result.md): from a new project to a saved intent in one sitting.
- [Persistence in git](../about/persistence-in-git.md): why the identity is git's, why the scripts are the only door and what the merge driver `ours` is for.
- [Configuration](../reference/configuration.md): the instance files and settings, field by field.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.1 from the files the front-matter names; never edited by hand.
