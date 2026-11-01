---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: db6db8236a234766
inputs:
  - .claude/skills/forge/SKILL.md
  - .claude/skills/ledger/SKILL.md
  - templates/project.md
  - templates/ledger.md#Reports
---

# See where a project stands

Bare `/forge` reports the state map of a project, and `/ledger` gives the same report from the ledger alone. This page is for the user who wants to know, at the start of a session or after a pause, what a project holds and what waits on the principal (the person whose thinking is being forged).

## When to use it

- You open a project and want to know what exists, at what version, and what to do next.
- You want the state of one project, or of all of them, without working on any artefact.

The ledger is the forge's single record of state, made at read time from the project's documents. It is [described on its own page](../about/the-ledger.md).

## The command

```
/forge my-project
```

The slug is optional when the project is clear from context. For a reading of the ledger only, one project or all:

```
/ledger my-project
```

## What happens

1. Claude makes the project's ledger with its script.
   You should now see the ledger rebuilt, with nothing written by hand.
2. Claude reads the ledger and lists the target states it can work (the artefact definitions).
   You should now see the report begin.
3. Claude reports the map, compactly:
   - the kind and the language, both from the project file, and whether the project is under git, as the status script reports it. "Not under git" is stated as a fact, not as a defect;
   - the artefacts that exist, with version and status, and the briefs with their mining state. A draft brief, or one that is `pending` or `partial`, is named as work waiting. A layer the project does not have is not reported as missing;
   - which target states can be worked from here, and for those that cannot yet, what is missing;
   - which renders are stale and which published files are stale. What stale means is on the [Ledger](../reference/ledger.md) page;
   - which libraries the project needs, and whether each is cloned alongside;
   - what waits on the principal: the few live matters named in words with the ID in brackets as an address, and the rest as a count.

   You should now see the map of the project.
4. Claude recommends the natural next step in words. This is a recommendation, never a gate. Where more than one matter waits on the principal, it also offers a [walkthrough](walk-through-a-list.md), which works the matters one at a time.
   You should now see a recommended step and, where it applies, the offer.
5. The last word of the map is the state of the engine and of the project against the origin (the remote): up to date, behind, ahead, diverged or no origin. It comes with that state's one offer, for example [a pull](pull-from-the-remote.md) when the repository is behind. The map says it looked at the remote and runs none of it.
   You should now see the remote state as the final line.

## A library

A library is material, not a project waiting for a brief. The map reports its sources and research and stops after the git line. It names no chain, no target states and no next step beyond `/ingest`.

## A project of the old shape

A project without a project file is of the shape before the migration. The map says so as a fact and says nothing more of it. The one remedy is a migration, described in [Migrate a project](migrate-a-project.md).

## What `/ledger` adds

`/ledger [slug]` makes the ledger and gives the same report from it, for one project or for all. It is read-only except for the ledger file the script writes.

Two things it reads aloud:

- the `unparsed:` lines of the ledger header, which name files the script could not parse;
- the Reports section, which stands only when there is something to say: an ID defined twice, a closed thread touched by a later commit, or a thread cited with neither a thread file nor a closed record.

Fixing them is not done here. It belongs to the light check (`/check light`).

## What you have afterwards

You have a spoken picture of the project and a recommended next step. Nothing is changed except the ledger, which is never kept in git.

## A worked example

A generic map for a project `my-project`, shortened:

```
my-project: kind thought, language en, own repository.

Artefacts:
  brief   00-brief.md   mined
  intent  10-intent.md  version 1.3, draft

Can be worked from here: assignment (the intent exists).
Cannot yet: none named.

Stale: one render (readme). No stale published files.
Libraries needed: lib-shared, cloned alongside.

Waiting on you: the choice of an owner for the open
question on scope (THR.0010), and two other matters.

Next step: settle the scope question, then write the
assignment. Two or more matters wait: shall we walk
through them?

Against the origin: behind by two commits.
Offer: /pull.
```

Terms used here are defined in the [Glossary](../reference/glossary.md).

## See also

- [The ledger, made from the records](../about/the-ledger.md): what the ledger is made from and why nobody writes it.
- [Pull from the remote](pull-from-the-remote.md): the offer the map makes when a repository is behind.
- [Migrate a project](migrate-a-project.md): what to do when the map says a project is of the old shape.
- [Walk through a list](walk-through-a-list.md): how the matters waiting on the principal are worked.
- [Ledger](../reference/ledger.md): the ledger's tables and state words.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
