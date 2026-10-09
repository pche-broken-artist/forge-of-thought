---
generated: 2026-10-09
made: derived
inputs:
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/save/SKILL.md
  - .claude/skills/import-project/SKILL.md
  - CLAUDE.md
  - projects/forge/recipes/readme.md
---

# Get a first result

This page takes you, in one sitting, from nothing to a saved intent
for a new idea: three commands, run from the engine root. It is for
someone who has the forge set up and wants to see it work once
before reading further. It was put together from the readme recipe's
Quickstart, the skills of `/new-project`, `/save` and
`/import-project`, the definitions of the brief and the intent, and
the Persistence section of `CLAUDE.md`.

## Start the project

1. Run `/new-project my-idea`.

   The forge creates `projects/my-idea/` with its files: the ledger,
   the decisions record, the empty `sources/` and `research/` with
   their indexes, and the recipes for the project's README and
   release notes. It writes files only and runs no git.

2. When asked, paste or dictate your brief: your idea put together,
   what you want and why.

   The forge stores it as `00-brief.md`. If you pasted it whole, it
   asks whether the text is finished; say yes and it is approved at
   once. If it is not finished, it stays a draft and you can go on
   working it with `/forge brief`. Approval happens only on your
   explicit word.

   At the end the forge proposes the next step, `/forge intent`, and
   reminds you that the project is not under git yet.

## Forge the first intent

3. Run `/forge intent`.

   With no intent yet, your brief is consolidated into the first one:
   what you hold, kept as positions. This runs as an interview, one
   question per message. Your answers are carried in the
   conversation; nothing is written one answer at a time.

4. At the end of the round, say `write`.

   Before writing, the forge reflects back what it understood, so the
   write confirms rather than surprises. On your confirmation it
   creates `10-intent.md` as version 0.1, with its history beside it
   and the open threads in `threads.md`, and names what changed and
   what stays open.

## Save it

5. Run `/save`.

   The forge runs the `light` check, then proposes a one-line commit
   message for you to confirm or adjust, and commits and pushes. A
   finding of the check does not hold the save up unless you ask for
   it to be fixed.

A project is a git repository of its own: initialising it
(`git -C projects/my-idea init -b main`, then a remote if you want
one) is your one-off act, and until then "not under git" is a fact,
not an error; `/save` names such a project and leaves it alone.

## If the project already exists

To bring in a project that already lives in a git repository, run
`/import-project <git-url>`. It clones the project into `projects/`,
under the repository's name, and reports the last commit, the
origin and the commit identity git resolves. Then run
`/forge <slug>`, the slug being the repository's name: the engine
does not track the project, so you select it by naming it before
any work.

## See also

- [Start a project](../use/start-a-project.md): the full job of starting a project, thought or library.
- [Forge the intent](../use/forge-the-intent.md): the full job of iterating the intent.
- [Save your work](../use/save-your-work.md): what a save does and asks.
