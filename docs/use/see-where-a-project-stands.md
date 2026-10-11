---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 8ad93b5fce334f99
inputs:
  - .claude/skills/forge/SKILL.md
  - .claude/skills/ledger/SKILL.md
---

# See where a project stands

This page shows how to ask for the state of a project: the bare `/forge` command prints a compact map of it, and `/ledger` prints the same report from the ledger alone. It is for you, the person who runs the forge and wants to know what exists, what is stale and what waits on the principal (the person whose thinking is being forged) before choosing the next step.

## When to use it

- You open a session and want to know where the project stands.
- You want to know which artefacts exist, at what version and status.
- You want to know what waits on the principal, or what the next step could be.
- You want to read the state of one project, or of all of them, from the ledger only (the file that is the single source of truth for state).

## The command

```
/forge my-project
```

The slug is optional. Without it, Claude infers the project from the context and asks if that is ambiguous. For a ledger-only reading:

```
/ledger my-project
```

Without a slug, `/ledger` reports every project.

## What happens

Both commands only read. They change no file.

1. Claude reads the project's ledger and lists the target states that are available.
   You should now see the report begin with the project's kind and whether it is under git. "Not under git" is stated as a fact, never as a defect.
2. For the engine and for the project, Claude says the state against the origin (the remote repository). The states are up to date, behind, ahead, diverged and no origin. Each comes with its one offer: pull, save first, save, or a merge by hand or by saving. The map says that it looked at the remote and runs none of the offers. For the pull, see [Pull from the remote](pull-from-the-remote.md).
   You should now see one line with the state and, beside it, one offer you may take or leave.
3. Claude lists the artefacts of the chain that exist, with version and status. Briefs are listed with their mining state. A draft brief, or one that is pending or partial, is named as work waiting. A layer the project does not have is not reported as missing.
   You should now see each artefact once, with its version and status.
4. Claude says which target states can be worked from here, because their inputs exist, and which cannot yet, with what is missing.
   You should now see two groups: states you can work now, and states that lack an input.
5. Claude names the renders that are stale and the published files whose state in the ledger is `stale`. What makes a render stale is the `/render` command's to say; this page does not repeat it.
   You should now see the stale renders and stale published files, or none.
6. Claude names the libraries the project needs, from the ledger's dependencies, and says whether each is cloned alongside.
   You should now see each needed library with a yes or no.
7. Claude says what waits on the principal. The few live matters are named in words, each with its ID in brackets as an address. The rest is given as a count.
   You should now see a short list in words and a number for the remainder.
8. Claude recommends the natural next step in words. The recommendation is never a gate. Where more than one matter waits on the principal, Claude offers a walkthrough of them. How a walkthrough runs is on [Walk through a list](walk-through-a-list.md).
   You should now see one recommended step and, where several matters wait, the offer of a walkthrough.

A library is material, not a project waiting for a brief. Its map reports its sources and research, from the ledger and the indexes, and stops after the git line. It has no chain, no target states and no next step beyond `/ingest`.

## What you have afterwards

You have a report in the conversation and nothing else: no file is written. The ledger's tables and state words are on [Ledger](../reference/ledger.md). A term you do not know is in the [Glossary](../reference/glossary.md).

## If something goes wrong

- The slug is ambiguous: Claude asks which project you mean.
- The ledger and reality seem to differ, for example in a version, a file on disk or an index: Claude names the discrepancy and points to the light check, `/check light`. Reconciling the ledger with reality is that check's job. `/ledger` and the map do not do it.

## A worked example

A generic map of a project with a slug `my-project`, shown in outline:

```
/forge my-project

my-project - kind: thought, under git.
Against the origin: behind. Offer: /pull.

Artefacts
- brief 00-brief.md: mined
- intent 10-intent.md: 0.4, draft
- assignment 20-assignment.md: 0.2, draft

Target states
- can be worked now: intent, assignment
- cannot yet: solution design (needs an approved assignment)

Stale
- renders: readme
- published files: none

Libraries
- lib-example: cloned alongside

Waiting on the principal
- the scope of the first release (open thread)
- the wording of the main objective (open finding)
- 3 more

Next step: settle the two named matters; shall we walk through
the five matters waiting?
```

## See also

- [Pull from the remote](pull-from-the-remote.md): the offer the map makes when a repository is behind.
- [Walk through a list](walk-through-a-list.md): how the matters waiting on the principal are worked one by one.
- [Ledger](../reference/ledger.md): the ledger's tables and state words.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
