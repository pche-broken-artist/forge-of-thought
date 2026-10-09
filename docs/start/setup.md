---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/setup/SKILL.md
  - templates/CLAUDE.local.md
  - CLAUDE.md
  - scripts/forge-status.ps1
---

# Set up the forge

This page is for someone who has just cloned the engine. It says what
`/setup` does for you, which you run once, before any other work.

## What you do

Open the engine in Claude Code and type:

```
/setup
```

On a true first run nothing is configured yet, so the conversation
runs in whatever language you speak to Claude. The command works in
three steps. It never overwrites an existing file and runs no git
operation.

## Step 1: your instance file

`/setup` creates `CLAUDE.local.md` at the engine root from its
template, `templates/CLAUDE.local.md`, by a short interview, one
question at a time:

1. The conversation language, asked first so that every later
   question arrives in it.
2. Who the principal is, by role: whose thinking is being forged, for
   example "the CTO".

The file is gitignored and never committed. If it already exists,
`/setup` tells you briefly what it holds and leaves it alone.

## Step 2: the session model

`/setup` creates `.claude/settings.local.json` with the session model
set to Fable. It tells you so in one sentence: Fable is the strongest
available model, and the whole forge, including the blind reviewers,
runs on it. You can change it at any time with `/model` or by editing
the file. If the file already exists, `/setup` reports the model it
names and leaves it alone.

## Step 3: the git identity

The git identity is git's own, not the forge's. `/setup` closes by
asking which git hosts you push to, with a name and an e-mail for
each. You may leave this for later; it says so.

Then it offers, on your word, to write two things into the global git
configuration file that git actually reads (`scripts/forge-status.ps1`
reports which file that is):

- for each host, `includeIf` stanzas that pick the name and e-mail
  for repositories whose remote is on that host;
- the global guard `user.useConfigOnly = true`, so that a repository
  on a host with no stanza fails aloud instead of taking a default.

If the global file already carries a `user.name` or `user.email`, the
guard only takes effect once that identity is removed. `/setup` says
so and offers the removal, again only on your word.

It never overwrites what is already in the file, and it reports and
leaves any stanza or guard that is there. If you decline, it prints
the stanzas and lines for you to apply by hand. These are the only
edits outside the engine, and they are plain configuration text, not
a git operation.

## What you see at the end

`/setup` points at the next step: start a new project with
`/new-project <slug>`, or bring an existing one with
`/import-project <git-url>`.

## See also

- [Get a first result](first-result.md): from a new project to a
  saved intent in one sitting.
- [About persistence in git](../about/persistence-in-git.md): why
  the identity is git's and the scripts are the only door.
- [Configuration](../reference/configuration.md): the instance files
  and settings, field by field.
