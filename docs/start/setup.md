---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: abdd67f1fd11d904
inputs:
  - .claude/skills/setup/SKILL.md
  - templates/CLAUDE.local.md
  - scripts/forge-config.py
  - scripts/forge-status.py
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
---

# Set up the forge

This page shows the first run after cloning the engine: `/setup`, the command that prepares one installation of the forge for the person who will use it. It is for you if you have just cloned the engine and have not started any other work.

Before you start, the machine needs what [Install what the forge needs](install.md) lists. The forge is run by Claude, Anthropic's agent for the command line, and the person whose thinking is forged is called the principal. In this page the principal is you.

If you want to see the forge at work before you start a project of your own, the course page of the teaching videos shows one job per video: https://pche-broken-artist.github.io/forge-of-thought/videos/

## When to use it

Run `/setup` once, as the first thing after cloning, before any other command. Run it again on the same machine only where git reads a different global configuration file (for example a network home at work and a local profile at home): it is then run once in each place.

## The command

Start `claude` from the engine root, then type:

```
/setup
```

## What happens

1. **`CLAUDE.local.md` is created.** Claude copies the template `templates/CLAUDE.local.md` to the engine root and fills it by a short interview, one question at a time. It asks three things, in this order:
   - the conversation language, first, so that every later question arrives in it;
   - who the principal is, by role (whose thinking is being forged);
   - the principal's short handle, which stands as the author of every history record the principal decides.

   You should now see a file `CLAUDE.local.md` at the engine root with three lines, one for each answer. The file is ignored by git and is never committed. If the file already exists, Claude reports what it holds, changes nothing in it and only offers, one line at a time, the lines the template has and the file lacks. You should now see your existing lines unchanged.

2. **The git identity is shown.** The identity is git's own, so the forge reads and writes it only through one script. Type:

   ```
   python scripts/forge-config.py
   ```

   You should now see the global git configuration file git reads, the registration of the merge driver, the guard, any global identity, and the per-host identity stanzas. This call changes nothing.

3. **You name your hosts.** Claude asks which git hosts you will push to. For each host you give a name and an e-mail, or you leave it for later and Claude says so. On your word Claude makes one call per host:

   ```
   python scripts/forge-config.py --identity <host> <name> <email>
   ```

   The call writes the per-host stanzas into the global git configuration and an identity file beside the global file. You should now see each key reported as written, or as already there and left. A stanza or identity file that differs from what you gave is reported and left as it is. Only if you accept does Claude add `--replace` to rewrite it.

4. **The global guard is set.** On your word Claude runs:

   ```
   python scripts/forge-config.py --guard
   ```

   The guard makes a repository on a host without a stanza fail loudly instead of taking a default identity. It takes effect only once no global name or e-mail is left. Where step 2 showed a global name or e-mail, Claude offers, again on your word:

   ```
   python scripts/forge-config.py --guard --unset-identity
   ```

   You should now see `user.useConfigOnly = true` reported, and the global identity removed if you accepted.

5. **The merge driver is registered.** Once per machine, and once in each place where git reads another global file, Claude offers on your word:

   ```
   python scripts/forge-config.py --register
   ```

   This registers the merge driver `ours` and the git settings it needs. It also sets `merge.renormalize`, which only evens line endings at a merge. The settings hold for every repository on the machine. Claude offers `--zdiff3` apart, which adds one more setting for how conflicts are shown:

   ```
   python scripts/forge-config.py --register --zdiff3
   ```

   You should now see each key reported as written or as already there. Nothing already set is overwritten. Afterwards `python scripts/forge-status.py` reports the registration as ok, or names the keys still missing.

6. **The session model is set.** Claude creates `.claude/settings.local.json` with the model set to Fable, the strongest model. The whole forge runs on it, including the blind reviewers (subagents that see nothing of your conversation). Where your account does not list Fable in `/model`, Claude writes the strongest model the account lists and says which. This is a notice, not a question. You can change it at any time with `/model` or by editing the file. You should now see the file with one `model` line. If the file already exists, Claude reports the model it names and leaves it alone.

7. **Claude points to the next step.** It ends by pointing at `/new-project` to start a project, or `/import-project` to bring an existing one. [Get a first result](first-result.md) follows a new project to a saved intent in one sitting.

If you decline any of the git steps, Claude prints the commands for you to run by hand.

## What you have afterwards

- `CLAUDE.local.md` at the engine root, with the conversation language, the principal's role and the principal's handle.
- Optionally, in the global git configuration: per-host identity stanzas with an identity file for each host, the guard, and the registered merge driver `ours`.
- `.claude/settings.local.json` with the session model.
- An identity that git itself verifies at your first `/import-project`.

Why the identity is git's, why the scripts are the only door to git, and what the merge driver `ours` is for: [Persistence in git](../about/persistence-in-git.md). The instance files and settings, field by field: [Configuration](../reference/configuration.md). Every term of the forge in one line: [Glossary](../reference/glossary.md).

## If something goes wrong

- A key that carries another value is reported and left. The script never overwrites it, except an identity under `--replace`.
- A global name or e-mail still stands: the guard does not bite while it does. Run `python scripts/forge-config.py --guard --unset-identity`.
- The registration shows keys missing in `python scripts/forge-status.py`: run `python scripts/forge-config.py --register` in the place git reads.
- Git reads another global file in another place: run `/setup` once in each place.
- Your account does not list Fable: Claude writes the strongest model the account lists.

## A worked example

You have cloned the engine and started `claude` in its root.

1. You type `/setup`. Claude asks for the conversation language, then the principal's role, then your handle, and creates `CLAUDE.local.md`.
2. Claude runs `python scripts/forge-config.py`. It shows no registration, no guard and no stanza.
3. You say you push to one host. Claude runs `python scripts/forge-config.py --identity <host> <name> <email>` with the values you gave.
4. You accept the guard. Claude runs `python scripts/forge-config.py --guard`. The script reports a global name, so Claude offers `--guard --unset-identity`, and you accept.
5. You accept the registration. Claude runs `python scripts/forge-config.py --register`.
6. Claude creates `.claude/settings.local.json` with the model Fable and points you to `/new-project <slug>` or `/import-project <git-url>`.

## See also

- [Install what the forge needs](install.md): what must be on the machine first.
- [Get a first result](first-result.md): from a new project to a saved intent in one sitting.
- [Persistence in git](../about/persistence-in-git.md): why the identity is git's, why the scripts are the only door and what the merge driver `ours` is for.
- [Configuration](../reference/configuration.md): the instance files and settings, field by field.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
