---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 7c7779ea13c4bf10
inputs:
  - .claude/skills/setup/SKILL.md
  - templates/CLAUDE.local.md
  - scripts/forge-config.py
  - scripts/forge-status.py
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
---

# Set up the forge

`/setup` is the first command you run after cloning the engine. It
prepares your installation: it writes the file that holds the facts of
your instance, offers the git identity and the global git settings the
forge needs, and sets the model Claude runs on. This page is for
anyone who has just installed the forge and is about to run it for the
first time.

The page uses one word that needs a gloss. The principal is the person
whose thinking is being forged (the
[Glossary](../reference/glossary.md) has every term of the forge in one
line).

## When to use it

Run `/setup` once, before any other work, on a fresh clone. Run it
again on a machine where git reads its global configuration from
another place, for example a network home at work and a local profile
at home. Run it in each such place.

Install first what the forge needs: see
[Install what the forge needs](install.md).

## The command

```
/setup
```

Start `claude` from the engine root, then type the command.

## What happens

1. **`CLAUDE.local.md` is created.** Claude copies the template to the
   engine root and fills it by a short interview, one question at a
   time. The first question is the conversation language, so that every
   later question arrives in it. The second is who the principal is, by
   role. The third is the principal's short handle. The handle stands as
   the author of every history record the principal decides.
   The file is gitignored and never committed. If the file already
   exists, Claude reports what it holds and touches nothing. It only
   offers the lines the template has and the file lacks, one by one, and
   writes each on your word.
   You should now see `CLAUDE.local.md` at the engine root with three
   lines: Principal, Conversation language and Author.

2. **The git identity is shown.** The identity is git's own, kept per
   host. Claude runs `python scripts/forge-config.py`, which changes
   nothing and shows what the global git configuration holds: the file
   git reads, the registration of the merge driver, the guard, a global
   identity and the per-host stanzas.
   You should now see those lines, each marked as present or missing.

3. **You name your hosts.** You say which git hosts you push to, with a
   name and an e-mail for each. You may leave this for later.
   On your word, Claude makes one call per host:

   ```
   python scripts/forge-config.py --identity <host> <name> <email>
   ```

   The call writes the two stanzas of that host in the global git
   configuration. It also writes an identity file beside the global
   file, holding the name and the e-mail. A stanza or an identity file
   that differs from what you gave is reported and left as it is. Only
   `--replace`, offered apart and again on your word, rewrites it.
   You should now see each stanza and the identity file reported as
   written, or as already there and left.

4. **The global guard is set.** On your word, Claude runs
   `python scripts/forge-config.py --guard`. The guard makes git fail
   aloud on a host with no identity, instead of taking a default one. It
   only bites once no global name or e-mail is left. Where the script
   reports one that survives, Claude offers
   `python scripts/forge-config.py --guard --unset-identity`, again only
   on your word.
   You should now see `user.useConfigOnly = true` reported as written or
   already there.

5. **The merge driver is registered.** Once per machine, and once in
   each place where git reads another global file, Claude offers
   `python scripts/forge-config.py --register`. Add `--zdiff3` apart if
   you want it. The settings hold for every repository on the machine,
   not only for the forge. The line endings are only evened at a merge,
   which is all that `renormalize` does. A setting that already carries
   another value is reported and left, never overwritten.
   You should now see each setting reported as written or already
   there.

6. **`.claude/settings.local.json` is created.** If the file is missing,
   Claude creates it with the session model set to Fable, the strongest
   model. The whole forge runs on it, the blind reviewers included. A
   session is one run of Claude from start to end. Where your account
   does not list Fable, Claude writes the strongest model it lists and
   says which. You can change the model at any time with `/model` or by
   editing the file. If the file already exists, Claude reports the
   model it names and does not touch it.
   You should now see the model named in a one-sentence notice.

7. **Claude points at the next step.** It ends by pointing at
   `/new-project <slug>` to start a project, or
   `/import-project <git-url>` to bring in an existing one.
   You should now see both commands named.

## What you have afterwards

- `CLAUDE.local.md` at the engine root, with your language, your role
  and your handle.
- Per-host identity stanzas and identity files in the global git
  configuration, where you gave a host.
- The guard and the registration of the merge driver, where you agreed.
- `.claude/settings.local.json` with the session model.

The identity is verified by git itself at your first
`/import-project`. The registration is reported afterwards by
`python scripts/forge-status.py`: "ok", or the keys that are missing.
The files and settings are described field by field in
[Configuration](../reference/configuration.md). Why the identity is
git's, why the scripts are the only door to a write of git and what the
merge driver is for is explained in
[Persistence in git](../about/persistence-in-git.md).

The course page of the teaching videos shows a first run before you
make your own:
https://pche-broken-artist.github.io/forge-of-thought/videos/

## If something goes wrong

- **You decline a step.** The commands are printed for you to run by
  hand.
- **The script reports "carries another value, left".** Nothing is
  overwritten. For an identity, review the value shown and add
  `--replace` if you want it replaced.
- **The guard does not bite.** A global name or e-mail still stands.
  Run `python scripts/forge-config.py --guard --unset-identity`.
- **The registration is reported missing by `forge-status`.** Run
  `python scripts/forge-config.py --register`, in each place where git
  reads another global file.
- **`/model` does not list Fable.** Claude writes the strongest model
  your account lists and says which.

## A worked example

Placeholder values stand for yours.

```
/setup
```

Claude asks, one by one: the conversation language, the principal's
role and the handle. It then runs
`python scripts/forge-config.py` and shows the state. You answer that
you push to one host:

```
python scripts/forge-config.py --identity <host> <name> <email>
python scripts/forge-config.py --guard --unset-identity
python scripts/forge-config.py --register
```

Each call reports what it wrote. Claude creates
`.claude/settings.local.json`, tells you the model, and points at
`/new-project <slug>`. For the next step, see
[Get a first result](first-result.md).

## See also

- [Install what the forge needs](install.md): what must be on the
  machine first.
- [Get a first result](first-result.md): from a new project to a saved
  intent in one sitting.
- [Persistence in git](../about/persistence-in-git.md): why the identity
  is git's, why the scripts are the only door and what the merge driver
  `ours` is for.
- [Configuration](../reference/configuration.md): the instance files and
  settings, field by field.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
