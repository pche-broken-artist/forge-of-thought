---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 1feec2ed6a7fc323
inputs:
  - .claude/skills/setup/SKILL.md
  - templates/CLAUDE.local.md
  - scripts/forge-config.py
  - scripts/forge-status.py
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
---

# Set up the forge

This page is for you on the first run after cloning the engine. It says what `/setup` asks, what it writes and what you see at each step. Run it before any other work. The machine must already have what the forge needs, as [Install what the forge needs](install.md) says.

A word on terms. The principal is the person whose thinking is being forged, usually you. A session is one running conversation with Claude. The full list of the forge's terms is the [Glossary](../reference/glossary.md).

## When to use it

Use it once on a new machine, with `claude` started from the engine root so that the engine's instructions load. Use it again in a clone that already has the instance file, if you want only to see what is missing: it touches nothing that exists.

## The command

```
/setup
```

## What happens

1. **The instance file.** Claude creates `CLAUDE.local.md` at the engine root from its template and fills it by a short interview, one question at a time. You should now see the first question arrive in the language you speak.
   - The conversation language comes first, so that every later question arrives in it.
   - Then who the principal is, by role (for example "the CTO").
   - Then the principal's short handle. It stands as the author of every history record you decide.

   The file is gitignored and never committed. On an instance that already has it, `/setup` reports briefly what the file holds, changes nothing, and offers one by one the lines of the template that the file lacks. You should now see a `CLAUDE.local.md` with three lines: Principal, Conversation language and Author.

2. **The git identity.** The identity is git's own, kept per host, and the forge only writes it through `scripts/forge-config.py`. First Claude runs the script bare:

   ```
   python scripts/forge-config.py
   ```

   You should now see what the global git configuration holds: the file git reads, the registration of the merge driver, the guard, a global identity if there is one, and the per-host stanzas. The bare run changes nothing.

   Then you name the git hosts you push to, with a name and an e-mail for each. You may leave this for later. On your word Claude makes one call per host:

   ```
   python scripts/forge-config.py --identity <host> <name> <email>
   ```

   You should now see the two stanzas of that host and its identity file reported as written. The identity file lies beside the global file. A stanza or an identity file that already carries another path, name or e-mail is reported and left. Claude offers `--replace` for it apart, and it runs only if you accept.

3. **The guard.** On your word Claude runs:

   ```
   python scripts/forge-config.py --guard
   ```

   You should now see `user.useConfigOnly = true` written, so that a repository on a host with no identity fails aloud instead of taking a default. The guard bites only once no global name or e-mail is left. Where the script reports one, Claude says so and offers, again on your word:

   ```
   python scripts/forge-config.py --guard --unset-identity
   ```

   You should now see the global name and e-mail removed.

4. **The merge driver `ours`.** Once per machine, on your word, Claude registers the merge driver `ours` and the git settings it needs:

   ```
   python scripts/forge-config.py --register
   ```

   You should now see each key reported as written, or as already there. The option `--zdiff3` is offered apart and adds a more legible conflict style. These settings hold for every repository on the machine. The setting `merge.renormalize` only evens line endings at a merge. Nothing already set is overwritten. The reason for the driver is in [Persistence in git](../about/persistence-in-git.md).

   Afterwards this reports the registration as "ok", or names the keys missing:

   ```
   python scripts/forge-status.py
   ```

5. **The session model.** Claude creates `.claude/settings.local.json` with the session model set to Fable, the strongest model. The whole forge runs on it, the blind reviewers included. If the account does not list Fable in `/model`, Claude writes the strongest model the account does list and says which. This is a notice, not a question. You should now see the file with a `model` entry. You can change it at any time with `/model` or by editing the file. If the file already exists, Claude reports the model it names and leaves it alone.

6. **The next step.** Claude ends by pointing at `/new-project <slug>` to start a project, or `/import-project <git-url>` to bring an existing one. The way on from there is [Get a first result](first-result.md).

## What you have afterwards

- `CLAUDE.local.md` at the engine root, gitignored.
- `.claude/settings.local.json` with the session model.
- Where you agreed, the per-host stanzas and identity files, the guard and the registration of the merge driver, all in git's global configuration.

The fields of these files are in [Configuration](../reference/configuration.md).

## If something goes wrong

- Where git reads another global file in another place (a network home at work, a local profile at home), the configuration is made once in each place. Run `/setup` once in each. `python scripts/forge-status.py` says where the registration is missing.
- A key that carries a value other than the one asked is reported and left, never overwritten. Only an identity can be replaced, with `--replace`.
- If you decline a step, Claude prints the commands for you to run by hand.
- The identity is verified by git at the first `/import-project`. If git resolves none for the clone, that command says what to do.
- The script needs Python 3.8 or newer and git 2.36 or newer on PATH.

## A worked example

On a new machine you start `claude` in the engine root and type `/setup`. Claude asks for the language, and you answer "English". It asks who the principal is, and you answer "the head of a team". It asks for the handle, and you answer `<handle>`. Claude shows the bare output of `python scripts/forge-config.py`: no registration, no guard, no stanzas. You name one host, `<host>`, with `<name>` and `<email>`. Claude runs `python scripts/forge-config.py --identity <host> <name> <email>`, then `--guard`, then `--register`. It writes `.claude/settings.local.json` and says the session is set to Fable. It ends by offering `/new-project <slug>`.

The course page of the teaching videos, https://pche-broken-artist.github.io/forge-of-thought/videos/, shows a first run before you make your own.

## See also

- [Install what the forge needs](install.md): what must be on the machine first.
- [Get a first result](first-result.md): from a new project to a saved intent in one sitting.
- [Persistence in git](../about/persistence-in-git.md): why the identity is git's, why the scripts are the only door and what the merge driver `ours` is for.
- [Configuration](../reference/configuration.md): the instance files and settings, field by field.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
