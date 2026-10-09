---
generated: 2026-10-09
made: mirrored
inputs-hash: aa280b7b8fd93506
inputs:
  - .claude/skills/setup/SKILL.md
  - templates/CLAUDE.local.md
  - CLAUDE.md
  - scripts/forge-status.py
---

# Set up the forge

This page is for the person who has just cloned the engine. It says what
`/setup` does, the first run before any other work, and what you will be
asked and what you will see.

## What `/setup` does

Run `/setup` once, right after cloning. It has three steps and touches
two files in the engine. The third step can also touch your global git
configuration, but only on your word. It never overwrites an existing
file and it runs no git operation.

### 1. It creates `CLAUDE.local.md`

If `CLAUDE.local.md` already exists at the engine root, `/setup` tells
you briefly what it holds and leaves it alone.

Otherwise it creates the file from its template (`templates/CLAUDE.local.md`)
by a short interview, one question at a time:

1. **The conversation language.** This comes first, so that every later
   question arrives in it. On a true first run nothing is configured
   yet, so `/setup` speaks the language you speak to it.
2. **Who the principal is, by role.** The principal is the person whose
   thinking is being forged, for example "the CTO".

The file is gitignored and never committed. It holds facts about your
instance, not properties of the system.

### 2. It creates `.claude/settings.local.json`

If the file exists, `/setup` reports the model it names and leaves it
alone.

Otherwise it creates the file with the session model set to Fable. You
get one sentence about it, as a notice and not a question: Fable is the
strongest available model, the whole forge runs on it, the blind
reviewers included, and you can change it at any time with `/model` or
by editing the file.

### 3. It closes with the git identity

The git identity is git's own, set per host in your global git
configuration. The forge sets none.

`/setup` asks which git hosts you will push to, with a name and an
e-mail for each. You may leave this for later, and it says so. It then
offers to write the following into the global git configuration file,
on your word:

- for each host, a pair of `includeIf` stanzas, one for the https form
  of its remote addresses and one for the ssh form, each pointing to a
  small identity file for that host holding your name and e-mail. The
  identity file is created beside the global file if it is missing, and
  the path is written in full;
- the global guard `user.useConfigOnly = true`, so that a repository on
  a host with no matching stanza fails aloud instead of taking a
  default.

The global file is the one git actually reads. `scripts/forge-status.py`
names it, and `/setup` reads it first. Nothing in it is overwritten:
a stanza or guard that is already there is reported and left as it is.
If the file carries a global `user.name` or `user.email`, the guard only
takes effect once that identity is removed, so `/setup` says so and
offers the removal, again only on your word.

If you decline, `/setup` prints the stanzas and the lines for you to
apply by hand. These are the only edits outside the engine. They are
changes to configuration text files, not git operations.

## What comes next

`/setup` ends by pointing at the next step: start a new project with
`/new-project <slug>`, or bring an existing one with
`/import-project <git-url>`.

## See also

- [Get a first result](first-result.md): from a new project to a saved intent in one sitting.
- [About persistence in git](../about/persistence-in-git.md): why the identity is git's and the scripts are the only door.
- [Configuration](../reference/configuration.md): the instance files and settings, field by field.
