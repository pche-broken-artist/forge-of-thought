---
generated: 2026-10-10
made: mirrored
inputs-hash: c11683f1206a5d07
inputs:
  - .claude/skills/setup/SKILL.md
  - templates/CLAUDE.local.md
  - CLAUDE.md
  - scripts/forge-status.py
---

# Set up the forge

This page is for someone who has just cloned the engine. It says what
`/setup` does, the one command to run before any other work, and what
you will be asked.

## Run it once, first

Type `/setup` in the engine. It prepares your own copy of the forge in
three steps. It never overwrites a file that already exists: where one
is there, it tells you briefly what the file holds and leaves it alone.
It runs no git operation.

On a true first run the conversation language is not set yet, so
`/setup` speaks whatever language you speak to it.

## Step 1: your instance file

`/setup` creates `CLAUDE.local.md` at the engine root from its template
`templates/CLAUDE.local.md`. It fills the file by a short interview,
one question at a time:

1. the conversation language, asked first so that every later question
   arrives in it;
2. who the principal is, by role: whose thinking is being forged.

The file keeps the template's format. It is gitignored and never
committed, because who you are and what language you talk in are facts
about your instance, not about the system.

## Step 2: the session model

`/setup` creates `.claude/settings.local.json` with the session model
set to Fable, the strongest available model, on which the whole forge
runs, the blind reviewers included. You are told this in one sentence;
it is a notice, not a question. You can change the model at any time
with `/model` or by editing the file.

## Step 3: the git identity

The identity you commit under is git's own, set per host. `/setup`
closes by asking which git hosts you will push to, with a name and an
e-mail for each. You may leave this for later, and it says so.

It then offers to write two things into the global git configuration
file that git actually reads. The status script,
`scripts/forge-status.py`, names that file, and `/setup` reads it
first. Nothing is written without your word.

- For each host, the `includeIf` stanzas that pick the right name and
  e-mail by the remote's address.
- The global guard `user.useConfigOnly = true`, so that a repository on
  a host with no stanza fails aloud instead of taking a default.

Existing content is never overwritten: a stanza or guard already there
is reported and left as it is. If you decline, `/setup` prints the
stanzas and the lines for you to apply by hand. These are the only
edits outside the engine, and they are plain configuration text, not a
git operation.

## What you see at the end

`/setup` ends by pointing at the next step: `/new-project <slug>` to
start a new project, or `/import-project <git-url>` to bring an
existing one in.

## See also

- [Get a first result](first-result.md): from a new project to a saved intent in one sitting.
- [About persistence in git](../about/persistence-in-git.md): why the identity is git's and the scripts are the only door.
- [Configuration](../reference/configuration.md): the instance files and settings, field by field.
