---
generated: 2026-10-23
version: 5.34
made: mirrored
inputs-hash: 9e644be9099d021e
inputs:
  - .claude/skills/setup/SKILL.md
  - templates/CLAUDE.local.md
  - scripts/forge-config.py
  - scripts/forge-status.py
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
---

# Set up the forge

This page walks you through `/setup`, the first command you run after
cloning the engine. It is for anyone who has just installed what the
forge needs and has not yet made a project. The course page of the
teaching videos, https://pche-broken-artist.github.io/forge-of-thought/videos/,
shows a first run before you make your own.

## When to use it

Run it once, before any other work. The prerequisites are on
[Install what the forge needs](install.md). Run it again only on a
machine where git reads a different global file (see step 3), or to
add a line your `CLAUDE.local.md` lacks.

Two words used below. The principal is whoever's thinking is being
forged. The session is one running conversation with Claude.

## The command

```
/setup
```

Start `claude` from the engine root, then type the command.

## What happens

### 1. The instance file is made

`/setup` creates `CLAUDE.local.md` at the engine root from its
template. It does so by a short interview, one question at a time.
Until you have answered the first question, Claude speaks whatever
language you speak to it.

The questions come in this order:

1. The conversation language, so that every later question arrives in
   it.
2. Who the principal is, given as a role.
3. The principal's handle, short. It stands as the author of every
   history record the principal decides.

The file is gitignored and never committed. If `CLAUDE.local.md`
already exists, `/setup` reports what it holds and touches nothing in
it. It offers only the lines the template has and the file lacks,
one by one, and writes each on your word.

You should now see `CLAUDE.local.md` at the engine root with three
lines: the principal, the conversation language and the author.

### 2. The git identity

The identity belongs to git, not to the forge, and it is kept per
host. `/setup` first shows what your global git configuration holds:

```
python scripts/forge-config.py
```

You should now see the file git reads, the state of the registration,
the guard, a global identity if there is one, and the identity
stanzas (the per-host entries) there are.

Next, name the hosts you push to, with a name and an e-mail for each.
You may leave this for later. On your word, `/setup` makes one call
per host:

```
python scripts/forge-config.py --identity <host> <name> <email>
```

The call writes the per-host stanzas and an identity file beside the
global file. A stanza or an identity file that differs from what you
gave is reported and left. `--replace` rewrites it, and `/setup`
offers it separately, again on your word.

You should now see, per host, each key reported as written, already
there or left.

Then the global guard:

```
python scripts/forge-config.py --guard
```

The guard makes a repository on a host with no identity stanza fail
aloud instead of taking a default. It bites only once no global name
or e-mail is left. Where the script reports one, `/setup` offers to
remove it:

```
python scripts/forge-config.py --guard --unset-identity
```

You should now see `user.useConfigOnly = true`, and the global name
and e-mail reported as removed if you agreed.

Git verifies the identity itself at your first `/import-project`.
It reports the identity git resolves for the clone, and says what to
do when it resolves none.

### 3. One global file per place

On a machine whose home differs by place, git reads another global
file in each place. A network home at work and a local profile at
home are two such places. `/setup` runs once in each of them, and so
does the registration in the next step.

### 4. The merge driver is registered

The registration is made once per machine, and once in each place
from step 3, on your word:

```
python scripts/forge-config.py --register
```

It sets the merge driver `ours` and the git settings it needs. Without
it, a clone silently falls back to a conflict on the derived files.
`--zdiff3` is offered apart and adds a conflict style:

```
python scripts/forge-config.py --register --zdiff3
```

These settings hold for every repository on the machine. The merge
backend is git's own default, and `renormalize` only evens line
endings at a merge. The forge has no merge driver of its own for
record files.

If you decline, `/setup` prints the commands for you to run by hand.
Nothing already set is overwritten.

You should now see each key reported as written or already there. Run
the status script afterwards to check:

```
python scripts/forge-status.py
```

You should now see `registration: ok`, or the keys that are missing.

### 5. The session model is set

`/setup` creates `.claude/settings.local.json` with the model set to
Fable, the strongest model. The whole forge runs on it, the blind
reviewers included. It says so in one sentence and does not ask. If
your account does not list Fable in `/model`, it writes the strongest
model the account lists and says which. You can change the model at
any time with `/model` or by editing the file. If the file already
exists, `/setup` reports the model it names and leaves the file
alone.

You should now see `.claude/settings.local.json` naming the model.

### 6. The next step

`/setup` ends by pointing at `/new-project <slug>` to start a project,
or `/import-project <git-url>` to bring an existing one.

## What you have afterwards

- `CLAUDE.local.md` with the principal, the conversation language and
  the author.
- The identity stanzas and files for the hosts you named, the guard
  and the registration in your global git configuration, as far as
  you agreed.
- `.claude/settings.local.json` with the session model.

## If something goes wrong

- A key that carries another value is reported and left. Only
  `--replace` for an identity, or your own edit, changes it.
- A global name or e-mail still stands: the guard does not bite. Use
  `--guard --unset-identity`.
- The registration shows keys missing in `forge-status.py`: run
  `--register` again in the place where git reads that file.
- `/import-project` says git resolves no identity: add the host with
  `--identity`.

## A worked example

```
/setup
```

1. Claude asks for the conversation language. You answer
   `<language>`.
2. It asks who the principal is. You answer `<role>`.
3. It asks for the handle. You answer `<handle>`.
4. It runs `python scripts/forge-config.py` and shows the result. You
   name one host, `<host>`, with `<name>` and `<email>`.
5. On your word it runs
   `python scripts/forge-config.py --identity <host> <name> <email>`,
   then `--guard`, and `--guard --unset-identity` where the script
   reported a global identity.
6. On your word it runs `python scripts/forge-config.py --register`.
7. It creates `.claude/settings.local.json` and tells you the model.
8. It points at `/new-project <slug>`.

## See also

- [Install what the forge needs](install.md): what must be on the machine first.
- [Get a first result](first-result.md): from a new project to a saved intent in one sitting.
- [Persistence in git](../about/persistence-in-git.md): why the identity is git's, why the scripts are the only door and what the merge driver `ours` is for.
- [Configuration](../reference/configuration.md): the instance files and settings, field by field.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.34 from the files the front-matter names; never edited by hand.
