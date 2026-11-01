---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 52a4fc38555823e6
inputs:
  - .claude/skills/setup/SKILL.md
  - templates/CLAUDE.local.md
  - scripts/forge-config.py
  - scripts/forge-status.py
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
---

# Set up the forge

This page is for you on the first run after cloning the engine. `/setup` prepares your instance: it writes two local files and, on your word, the global git configuration. It asks one question at a time and never overwrites what already exists. The principal is whoever's thinking is being forged; that is usually you. The course page of the teaching videos, https://pche-broken-artist.github.io/forge-of-thought/videos/, shows a first run before you make your own.

## When to use it

Run it once, before any other work, after the machine has what the forge needs (see [Install what the forge needs](install.md)). Run it again on a machine where git reads another global file in another place, such as a network home at work and a local profile at home: `/setup` runs once in each place.

## What you do

Start `claude` from the engine root and type:

```
/setup
```

## What happens

1. **`CLAUDE.local.md` is created.** Claude copies the template to the engine root and fills it by a short interview, one question at a time. The conversation language comes first, so that every later question arrives in it. You should now see the next question in your own language.
   - Conversation language: the language the working conversation runs in.
   - Principal: who is being forged, named by role (for example "the CTO").
   - Author: the principal's short handle. It stands as the author of every history record the principal decides.

   You should now see a file `CLAUDE.local.md` in the engine root. It is gitignored and never committed.

   If the file already exists, `/setup` reports briefly what it holds and touches nothing. It offers only the lines the template has and the file lacks, one by one, and writes them on your word.

2. **The git identity is shown.** The identity is git's own, kept per host. Claude runs `python scripts/forge-config.py`, which changes nothing and reports the file git reads, the registration of the merge driver, the guard, a global identity and the per-host stanzas. You should now see one line for each of these.

3. **You name your hosts.** You name the git hosts you push to, with a name and an e-mail for each, or you leave it for later. On your word, Claude makes one call per host:

   ```
   python scripts/forge-config.py --identity <host> <name> <email>
   ```

   The call writes the per-host stanzas to the global git file and an identity file beside it. You should now see each key reported as written. A stanza or an identity file that differs (another path, another name or e-mail) is reported and left. Only `--replace`, offered apart and on your word, rewrites it.

4. **The global guard is set.** On your word, Claude runs `python scripts/forge-config.py --guard`. The guard makes git fail aloud in a repository with no identity, instead of taking a default. It acts only once no global name or e-mail is left. Where the script reports one, Claude says so and offers:

   ```
   python scripts/forge-config.py --guard --unset-identity
   ```

   You should now see `user.useConfigOnly = true` reported, and the global name and e-mail removed if you agreed.

5. **The merge driver `ours` is registered.** This is done once per machine and once in each place where git reads another global file, on your word. Claude runs:

   ```
   python scripts/forge-config.py --register
   ```

   It writes the merge driver `ours` and the settings it needs: `merge.renormalize` (it evens line endings at a merge and nothing more), `rebase.backend merge` and `rerere.enabled`. `--zdiff3` is offered apart and adds a clearer conflict style. These settings hold for every repository on the machine. You should now see each key reported as written or as already there. A key that carries another value is left. Why the registration matters is explained in [Persistence in git](../about/persistence-in-git.md).

6. **The session model is set.** If `.claude/settings.local.json` exists, Claude reports the model it names and leaves the file alone. Otherwise it creates the file with the model set to Fable, the strongest model, on which the whole forge runs, the blind reviewers included. Where your account does not list Fable, Claude writes the strongest model it does list and says which. This is a notice, not a question. You can change the model at any time with `/model` or by editing the file. You should now see the file `.claude/settings.local.json`.

7. **The next step is named.** `/setup` ends by pointing at `/new-project <slug>` to start a project, or `/import-project <git-url>` to bring an existing one.

If you decline a git step, Claude prints the command for you to run by hand. Nothing already set is overwritten.

## What you have afterwards

- `CLAUDE.local.md` at the engine root, gitignored.
- `.claude/settings.local.json` with the session model.
- On your word, the per-host identity stanzas and identity files, the guard and the registration in the global git configuration.

Run `python scripts/forge-status.py` to see the registration reported, as ok or with the keys missing. Git itself verifies the identity at your first `/import-project`. The files are described field by field in [Configuration](../reference/configuration.md).

## If something goes wrong

- A key is reported as carrying another value and left: this is intended. Only an identity can be rewritten, with `--replace`.
- The guard is set but git still commits with a default name: a global name or e-mail still stands. Run `--guard --unset-identity` on your word.
- `forge-status` says the registration is missing keys: run `python scripts/forge-config.py --register` in that place.
- The identity differs between your two places: git reads another global file there, so run `/setup` once in each.

## A worked example

You have just cloned the engine and installed the prerequisites. You type `/setup`. Claude asks for the conversation language and you answer. It asks who the principal is and you answer "the CTO". It asks for your handle and you answer `<handle>`. It shows the git state and you name one host with `<name>` and `<email>`. Claude runs:

```
python scripts/forge-config.py --identity <host> <name> <email>
python scripts/forge-config.py --guard --unset-identity
python scripts/forge-config.py --register
```

It creates `.claude/settings.local.json` and ends by pointing at `/new-project <slug>`. Continue with [Get a first result](first-result.md).

## See also

- [Install what the forge needs](install.md): what must be on the machine first.
- [Get a first result](first-result.md): from a new project to a saved intent in one sitting.
- [Persistence in git](../about/persistence-in-git.md): why the identity is git's, why the scripts are the only door and what the merge driver `ours` is for.
- [Configuration](../reference/configuration.md): the instance files and settings, field by field.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
