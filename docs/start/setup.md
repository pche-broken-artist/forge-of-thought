---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 4f8fde32f998364a
inputs:
  - .claude/skills/setup/SKILL.md
  - templates/CLAUDE.local.md
  - scripts/forge-status.py
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
---

# Set up the forge

`/setup` is the first command to run after cloning the forge: it prepares your instance, that is your own installation of the engine, through a short interview and a few files. This page is for the person who has just cloned the engine and installed what it needs, and who has not yet started any work.

The forge calls the person whose thinking is being forged "the principal". On your own instance that is you, or the role you name.

## When to use it

Run it once, on the first start in a fresh clone, before any other work. Run it again on another machine, or on an instance that lacks a line the template has gained since. Before you start, the machine needs what [Install what the forge needs](install.md) lists.

Start `claude` from the engine root, so that the instance file is loaded.

## The command

```
/setup
```

## What happens

Claude speaks whatever language you speak to it, because the conversation language is not configured yet. It asks one question at a time.

1. **The instance file `CLAUDE.local.md`.** Claude copies the template to the engine root and fills it by interview. It asks three things, in this order:
   - the conversation language, first, so that every later question arrives in it;
   - who the principal is, by role (whose thinking is being forged);
   - the principal's short handle, which stands as the author of every history record the principal decides.

   You should now see a `CLAUDE.local.md` at the engine root with those three lines filled. The file is never committed, because git ignores it.

   If the file already exists, Claude reports what it holds and touches nothing. It only offers the lines the template has and the file lacks, one by one, and writes each on your word.

2. **The git identity.** Git owns the identity, not the forge. Claude asks which git hosts you will push to, with a name and an e-mail for each. You may leave this for later.

   Then it offers to write the following into the global git configuration file that git actually reads. `python scripts/forge-status.py` names that file, and Claude reads it first.
   - for each host, two `includeIf` stanzas (one for `https://<host>/**` URLs, one for `git@<host>:*/**` URLs), each pointing to a `.gitconfig-<host>` file by an absolute path;
   - the `.gitconfig-<host>` file with your `name` and `email`, created when missing;
   - the global guard `user.useConfigOnly = true`, so that a repository on a host without a matching stanza fails aloud instead of taking a default identity.

   The path is absolute because the global file follows the home directory, and the home directory may differ from place to place. A `~` path is then found from one place and not from the other. Where the global file already carries such a stanza with a `~` path, Claude reports it and offers to make the path absolute.

   Where the global file already holds a `user.name` or `user.email`, the guard only takes effect once that identity is removed. Claude says so and offers the removal, again only on your word.

   Existing content is never overwritten: an existing stanza or guard is reported and left. If you decline, Claude prints the lines for you to apply by hand.

   You should now see the stanzas and the guard in the global file, or the printed lines in the conversation.

3. **The merge drivers, once per machine.** On your word, Claude registers in the same global file what the forge needs to merge its records correctly. `python scripts/forge-status.py` first says whether the registration is there. Claude reads the file, reports every key that already has its value and leaves it, and offers every other key:
   - `[merge "ours"]` with `driver = true`, and `[merge]` with `renormalize = true`;
   - `[rebase]` with `backend = merge`, because the apply backend ignores drivers;
   - `[rerere]` with `enabled = true`, a convenience;
   - `[merge]` with `conflictStyle = zdiff3`, offered apart.

   These settings hold for every repository on the machine. The merge backend is git's own default, and renormalize only evens out line endings at a merge. If you decline, Claude prints the lines for you to apply by hand.

   You should now see `registration: ok` when you run `python scripts/forge-status.py`, or the names of the keys still missing.

4. **The session model.** Claude creates `.claude/settings.local.json` with the model set to Fable, the strongest model. The whole forge runs on it, the blind reviewers included. It tells you so in one sentence, as a notice and not a question. If your account does not list Fable in `/model`, Claude writes the strongest model the account lists and says which. You can change it at any time with `/model` or by editing the file.

   You should now see a `.claude/settings.local.json` that names the model. If the file already exists, Claude reports the model it names and does not touch it.

5. **The next step.** Claude points you at `/new-project <slug>` to start a project, or `/import-project <git-url>` to bring an existing one.

## What you have afterwards

- `CLAUDE.local.md` at the engine root, with the conversation language, the principal and the author handle.
- `.claude/settings.local.json`, with the session model.
- Optionally, in the global git configuration: the per-host identity stanzas, the guard and the merge registration.

`/setup` never overwrites an existing file and runs no git operation. The only edits outside the engine are to configuration text files, and each is made on your word.

To see what the registration looks like at any time, run:

```
python scripts/forge-status.py
```

## If something goes wrong

- `registration: missing ...` in the output of `forge-status`: the listed keys are not set. Run `/setup` again, or apply the printed lines by hand. Without the registration, a clone silently falls back to a conflict at a merge.
- `registration: the forge-records driver leads nowhere`: a registered driver points at a script that does not exist. Run `/setup` again.
- `global git config: none yet`: git has no global file yet and creates it at its first write. This is not an error.
- A repository on a host without a stanza fails aloud when it commits. This is the guard working: add the host's stanza and identity.

## A worked example

Placeholders stand where your own values go.

```
/setup
```

1. Claude asks for the conversation language. You answer `<language>`.
2. Claude asks who the principal is. You answer `<role>`.
3. Claude asks for the short handle. You answer `<handle>`.
4. Claude asks for the git hosts. You answer `<host>`, with `<name>` and `<e-mail>`.
5. Claude offers the stanzas and the guard for `<host>`. You accept.
6. Claude offers the merge registration. You accept, and decline `conflictStyle = zdiff3`.
7. Claude tells you the session model is set, and points at `/new-project <slug>`.

Then `python scripts/forge-status.py` shows `registration: ok`.

The course page of the teaching videos, https://pche-broken-artist.github.io/forge-of-thought/videos/, shows a first run before you make your own.

## See also

- [Install what the forge needs](install.md): what must be on the machine first.
- [Get a first result](first-result.md): from a new project to a saved intent in one sitting.
- [Persistence in git](../about/persistence-in-git.md): why the identity is git's, why the scripts are the only door and what the merge settings are for.
- [Configuration](../reference/configuration.md): the instance files and settings, field by field.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
