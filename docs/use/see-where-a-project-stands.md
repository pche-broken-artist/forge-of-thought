---
generated: 2026-10-23
version: 5.34
made: mirrored
inputs-hash: 9492665e48044d16
inputs:
  - .claude/skills/forge/SKILL.md
  - .claude/skills/ledger/SKILL.md
  - templates/project.md
  - templates/ledger.md#Reports
---

# See where a project stands

This page shows how to ask where a project stands and how to read the answer. It is for the principal, the person whose thinking is forged, who wants to know what exists, what is stale and what waits for a decision before choosing the next step.

## When to use it

- You open a project and want its state in one report.
- You want the state of every project at once.
- You want to know what waits on you before you start working.

## The command

```
/forge my-project
```

Without a slug, Claude infers the project from the context and asks if that is ambiguous. For a ledger-only reading of one project or of all of them, type:

```
/ledger my-project
```

## What happens

1. Claude makes the project's ledger with its script.
   The ledger is the report of state, made from the project's documents at the time it is read (see [The ledger, made from the records](../about/the-ledger.md)).
   You should now see the map begin; nothing in the project has been changed but the ledger file.
2. Claude reads the ledger and lists the target states that can be worked.
3. Claude reports the state map, compactly:
   - The kind of the project and its language, both from the project file, and whether the project is under git, as the status script reports it. "Not under git" is stated as a fact, not a defect.
   - The artefacts that exist, each with version and status, and the briefs with their mining state. A draft brief, or one marked `pending` or `partial`, is named as work waiting. A layer the project does not have is not reported as missing.
   - Which target states can be worked from here, and for the others what is missing.
   - Which renders are stale and which published files are stale. This page does not define staleness; the [Ledger](../reference/ledger.md) reference gives the state words.
   - The libraries the project needs, and whether each is cloned alongside.
   - What waits on you: the few live matters named in words with the ID in brackets, and the rest as a count.

   You should now see a report in that order.
4. Claude recommends the natural next step in words. The recommendation is never a gate. Where more than one matter waits on you, it offers a walkthrough (see [Walk through a list](walk-through-a-list.md)).
   You should now see a recommendation, and the offer where several matters wait.
5. Claude ends with the state of the engine and of the project against the origin, as the status script reports it: up to date, behind, ahead, diverged or no origin. It says it looked at the remote, gives that state's one offer, and runs none of it. A repository that is behind gets the offer described in [Pull from the remote](pull-from-the-remote.md).
   You should now see the last line say how each repository stands to its origin.

### A library

A library is material, not a project waiting for a brief. Its map reports its sources and research and stops after the git line. It has no chain, no target states and no next step beyond `/ingest`.

### What `/ledger` adds

`/ledger [slug]` makes the ledger and gives the same report from it, for one project or for all. It is read-only but for the ledger file the script writes. Two things in the ledger are read aloud:

- The `unparsed:` lines of its header, one for each file the script could not parse.
- Its Reports section, which stands only when there is something to say: an ID defined twice, a closed thread touched by a later commit, or a thread cited with neither a thread file nor a closed record.

Fixing what these name belongs to the light check (`/check light`), not to `/ledger`.

## What you have afterwards

You have a report in the conversation and a freshly made ledger file. Nothing else is written. The ledger is never written by hand and is not kept in git.

## If something goes wrong

- The map says the project is of the shape before the migration. It says so and nothing more. The one remedy is `/migrate`; see [Migrate a project](migrate-a-project.md).
- The slug is ambiguous. Claude asks which project you mean.
- The ledger has `unparsed:` lines or a Reports section. Claude reads them aloud; run the light check to fix them.

## A worked example

A generic map for a thought project with the placeholder slug `my-project`. The figures are made up to show the shape.

```
my-project: kind thought, language en, a repository of its own.

Artefacts
- brief 00-brief: mined
- intent 10-intent: version 0.4, draft
- assignment: not yet written (a layer the project may not need)

Can be worked from here: intent, assignment.

Stale: one render (readme); no published files.

Libraries: lib-shared, cloned alongside.

Waiting on you: two open threads, the question of the audience
(THR.NNNN) and the scope of the first phase (THR.NNNN); three
more matters in all.

Next: settle the audience, then the scope. Shall I walk you
through the five matters?

Origin: the project is behind its origin by one commit;
the engine is up to date. Pull is the offer.
```

## See also

- [The ledger, made from the records](../about/the-ledger.md): what the ledger is made from and why nobody writes it.
- [Pull from the remote](pull-from-the-remote.md): the offer the map makes when a repository is behind.
- [Migrate a project](migrate-a-project.md): what to do when the map says a project is of the old shape.
- [Walk through a list](walk-through-a-list.md): how the matters waiting on the principal are worked.
- [Ledger](../reference/ledger.md): the ledger's tables and state words.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.34 from the files the front-matter names; never edited by hand.
