---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 68fe9e2d1023ce5a
inputs:
  - .claude/skills/forge/SKILL.md
  - .claude/skills/ledger/SKILL.md
---

# See where a project stands

The bare `/forge` command reports the state map of a project: what exists, what can be worked next and what waits on the principal (the person whose thinking is being forged). This page is for anyone who wants that picture before deciding what to do. `/ledger` gives the same report from the ledger alone.

## When to use it

- At the start of work, to see where a project stands.
- After a break, to find what is waiting.
- When you want the report without Claude looking at anything but the ledger (the single file that records the state of a project; see [Ledger](../reference/ledger.md)).

## The command

```
/forge my-project
```

The slug is optional where Claude can tell the project from context. If it cannot, it asks which project you mean.

The ledger-only reading:

```
/ledger my-project
```

Without a slug, `/ledger` reads every project.

## What happens

Claude reads the project's ledger and lists the target states that exist. It then reports the following, in this order.

1. The kind of the project and whether it is under git.
   - A project not under git is stated as a fact, never as a defect.
   - For the engine and for the project, Claude also says the state against the origin: up to date, behind, ahead, diverged or no origin.
   - Each state comes with its one offer: `/pull`, `/save` first, `/save`, or a merge by hand or by `/save`. See [Pull from the remote](pull-from-the-remote.md) for the case of a repository that is behind.
   - The map says that it looked at the remote. It runs none of the offers.

   You should now see the kind, the git line and the state against the origin.

2. The artefacts that exist, with their version and status.
   - Briefs are listed with their mining state.
   - A draft brief, or one marked `pending` or `partial`, is named as work waiting.
   - A layer the project does not have is not reported as missing.

   You should now see one line per artefact with version and status.

3. The target states, split in two.
   - Those that can be worked from here, because their inputs exist.
   - Those that cannot yet, with what is missing.

   You should now see both groups, the second with its reason.

4. The stale renders and the stale published files.
   - A published file is stale when the ledger's Published table says `stale`.
   - What makes a render stale is defined by `/render`, not here.

   You should now see the stale ones named, or nothing where none is stale.

5. The libraries the project needs, from the ledger's Dependencies table, and whether each is cloned alongside.

   You should now see each library with its cloned state.

6. What waits on the principal, from the ledger.
   - The few live matters are named in words, with the ID in brackets as an address.
   - The rest are given as a count.

   You should now see the live matters and a count of the others.

7. A recommended next step, in words. It is a recommendation, never a gate. Where more than one matter waits on the principal, Claude also offers a walkthrough of them. See [Walk through a list](walk-through-a-list.md).

   You should now see one recommendation, and the offer where there is a list.

A library is material, not a project waiting for a brief. Its map reports the sources and the research, from the ledger and the indexes, and stops after the git line. It has no chain, no target states and no next step beyond `/ingest`.

## What you have afterwards

You have a report and nothing else. Neither command changes a file. The map offers `/pull` or `/save` but runs neither.

The `/ledger` report is read from the ledger only. If Claude notices a mismatch between the ledger and reality while reporting, it names it and points to `/check light`. Reconciling the ledger with versions, files on disk and indexes is the job of that check.

## If something goes wrong

- Claude asks which project you mean: the slug was ambiguous. Name the slug.
- Claude names a discrepancy between the ledger and reality: run `/check light`, which is where it is reconciled.
- A term in the report is unfamiliar: the [Glossary](../reference/glossary.md) gives every term of the forge in one line.

## A worked example

The slug and everything in the report are generic.

```
/forge my-project
```

Claude reports, in words close to these:

```
my-project is a thought project, under git. Against the origin it is
behind; the offer is /pull. I looked at the remote and ran nothing.

Artefacts: brief 1.0 approved, mined; intent 0.4 draft.

Can be worked from here: intent. Cannot yet: assignment, because the
intent is not approved.

Stale: the render "overview". No published file is stale.

Libraries: one needed, cloned alongside.

Waiting on you: two matters, one about the scope of the intent and
one about a rejected direction; no others.

Next: settle the two matters, then approve the intent. I can walk
you through the two, one at a time. Shall I?
```

## See also

- [Pull from the remote](pull-from-the-remote.md): the offer the map makes when a repository is behind.
- [Walk through a list](walk-through-a-list.md): how the matters waiting on the principal are worked.
- [Ledger](../reference/ledger.md): the ledger's tables and state words.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
