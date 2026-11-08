---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: b580d9d60d4fa750
inputs:
  - .claude/skills/setup/SKILL.md
  - templates/CLAUDE.local.md
  - scripts/forge-config.py
  - scripts/forge-status.py
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
---

# Set up the forge

`/setup` is the first command you run after cloning the engine. It
prepares your instance: it writes the file that says who you are to
Claude, it helps you set the git identity and the git settings the
forge relies on, and it chooses the model of the session. This page
is for you, the person who has just installed the forge and has not
yet made a project. The course page of the teaching videos,
`https://pche-broken-artist.github.io/forge-of-thought/videos/`, shows
a first run before you make your own.

## When to use it

Run it once, before any other work, on every machine where you use the
forge. Run it from the engine root, where Claude was started. On an
instance that is already set up it is safe to run again: it touches
nothing that exists.

## The command

```
/setup
```

Before you start, the machine needs what [Install what the forge
needs](install.md) lists.

## What happens

1. **`CLAUDE.local.md` is created.** Claude copies the template to the
   engine root and fills it with a short interview, one question at a
   time. The first question is the conversation language, so that
   every later question arrives in it. The second is who the principal
   is, by role (the principal is the person whose thinking is being
   forged). The third is the principal's short handle, which stands as
   the author of every history record he decides. The file is
   gitignored and never committed. If the file already exists, Claude
   reports briefly what it holds, changes nothing, and offers one by
   one only the lines the template has and the file lacks.
   You should now see `CLAUDE.local.md` at the engine root with the
   three lines filled.

2. **The git identity is shown.** The identity is git's own, so
   Claude first runs `python scripts/forge-config.py`, which changes
   nothing and prints what the global git configuration holds: the
   file git reads, the registration of the merge driver, the guard, a
   global identity if there is one, and the per-host stanzas.
   You should now see those lines, each marked as present or missing.

3. **You name your hosts.** Claude asks which git hosts you push to
   and, for each, a name and an e-mail. You may leave this for later.
   On your word Claude makes one call per host:

   ```
   python scripts/forge-config.py --identity <host> <name> <email>
   ```

   The call writes the per-host stanzas into the global git
   configuration and the identity file beside it. A stanza or an
   identity file that differs from what you gave is reported and left.
   Only if you accept `--replace` for it does the script rewrite it.
   You should now see, for each host, the stanzas and the identity
   file reported as written or as already there.

4. **The guard is set.** On your word Claude runs `--guard`, which
   makes git refuse to commit in a repository whose host has no
   identity, instead of taking a default. The guard bites only once no
   global name or e-mail is left. Where the script reports one, Claude
   says so and, on your word, runs `--guard --unset-identity`.
   You should now see `user.useConfigOnly = true` reported, and any
   global name or e-mail reported as removed.

5. **Each place git reads is set up.** Where git reads a global file
   in another place (a network home at work, a local profile at
   home), `/setup` runs once in each.

6. **The merge driver `ours` is registered.** Once per machine, and
   once in each such place, on your word, Claude runs:

   ```
   python scripts/forge-config.py --register
   ```

   It registers the merge driver `ours` and the git settings it needs.
   `--zdiff3` is offered apart. These settings hold for every
   repository on the machine, and the renormalize setting only evens
   out line endings at a merge. Nothing already set is overwritten.
   You should now see each key reported as written or as already
   there.

7. **The session model is chosen.** Claude creates
   `.claude/settings.local.json` with the session model set to Fable,
   the strongest model, on which the whole forge runs, the reviewers
   that see nothing of the conversation included. Where your account
   does not list Fable, Claude writes the strongest model it lists and
   says which. It tells you in one sentence and does not ask. You can
   change the model at any time with `/model` or by editing the file.
   If the file already exists, Claude reports the model it names and
   leaves it alone.
   You should now see the file and a sentence naming the model.

8. **Claude points at the next step.** It ends by pointing at
   `/new-project <slug>` for a new project or `/import-project
   <git-url>` for an existing one.

## What you have afterwards

- `CLAUDE.local.md` with your language, role and handle, never
  committed.
- In the global git configuration, as far as you agreed: a stanza
  pair and an identity file per host, the guard, and the registration
  of the merge driver.
- `.claude/settings.local.json` with the session model.

The fields of these files are in [Configuration](../reference/configuration.md).
Why the identity is git's, why the scripts are the only door to a
write, and what the merge driver `ours` is for is in [Persistence in
git](../about/persistence-in-git.md).

## If something goes wrong

- If you decline a step, Claude prints the commands so that you can
  run them by hand.
- To check the registration afterwards, run
  `python scripts/forge-status.py`. It reports it as ok or names the
  keys that are missing.
- The identity is verified by git at your first `/import-project`,
  which reports the identity git resolves for the clone and says what
  to do when it resolves none.
- A stanza or identity file that differs is left as it is until you
  accept `--replace`.

## A worked example

You start Claude in the engine root and type `/setup`. Claude asks in
which language to talk, and you answer. It asks whose thinking is
being forged, and you give your role. It asks for your handle, and
you give a short one. It runs `python scripts/forge-config.py` and
shows that nothing is registered and no stanza exists. You name one
host with a name and an e-mail, and Claude runs:

```
python scripts/forge-config.py --identity <host> <name> <email>
```

You agree to the guard and to the removal of the global identity, so
Claude runs `python scripts/forge-config.py --guard --unset-identity`.
You agree to the registration, so it runs
`python scripts/forge-config.py --register`. It writes
`.claude/settings.local.json`, tells you the model, and points you at
`/new-project <slug>`.

## See also

- [Install what the forge needs](install.md): what must be on the machine first.
- [Get a first result](first-result.md): from a new project to a saved intent in one sitting.
- [Persistence in git](../about/persistence-in-git.md): why the identity is git's, why the scripts are the only door and what the merge driver `ours` is for.
- [Configuration](../reference/configuration.md): the instance files and settings, field by field.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
