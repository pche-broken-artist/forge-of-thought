---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 5f30a52dbff08c83
inputs:
  - .claude/skills/forge/SKILL.md
  - .claude/skills/ledger/SKILL.md
  - templates/project.md
  - templates/ledger.md#Reports
---

# See where a project stands

This page is for you, the principal (the person whose thinking is being forged), when you want to know where a project stands. Bare `/forge` reports the state map of one project, and `/ledger` gives the same report from the ledger alone. Both only read: the one thing either writes is the ledger, which is made at read time.

## When to use it

- You open a project and want to know what exists, what is stale and what waits on you.
- You come back after a pause and want a recommended next step.
- You want the report for every project at once. That is `/ledger` without a slug.

## The command

```
/forge my-project
```

The slug is optional. Without it, Claude infers the project from the context and asks if that is ambiguous. For the ledger alone:

```
/ledger my-project
```

Without a slug, `/ledger` reports every project.

## What happens

1. Claude makes the project's ledger with its script. The ledger is the single record of state ([The ledger, made from the records](../about/the-ledger.md)). You should now see the map begin from a fresh ledger.
2. Claude reads the project file for the kind (`thought` or `library`) and the language of the chain's artefacts. You should now see both named.
3. Claude says whether the project is under git, as the status script reports it. This is stated as a fact and never as a defect: a project may be a repository of its own or "not under git". You should now see that line.
4. For a library, the map stops here, after its sources and research and the git line. A library is material, not a project waiting for a brief, so it has no chain, no target states and no next step beyond `/ingest`.
5. For a project with a chain, Claude reports in order:
   - the artefacts that exist, with version and status;
   - the briefs, each with its mining state, a draft or `pending` or `partial` brief named as work waiting;
   - the target states that can be worked from here, and for those that cannot yet, what is missing;
   - the stale renders and the stale published files (the state words are in [Ledger](../reference/ledger.md));
   - the libraries the project needs, and whether each is cloned alongside;
   - what waits on you: the few live matters named in words with the ID in brackets as an address, the rest as a count.

   A layer the project does not have is not reported as missing. You should now see each of these as a short block.
6. Claude recommends the natural next step in words. The recommendation is never a gate. Where more than one matter waits on you, Claude offers a walkthrough of them ([Walk through a list](walk-through-a-list.md)). You should now see one recommendation, and the offer when it applies.
7. The last word is the state of the engine and of the project against the origin, in these words: up to date, behind, ahead, diverged, or no origin. Claude gives that state's one offer, and the map runs none of it. When a repository is behind, the offer is a pull ([Pull from the remote](pull-from-the-remote.md)). You should now see the map end on that line.

## What you have afterwards

You have a report in the conversation and a fresh ledger. Nothing else is written. `/ledger` gives the same report, drawn from the ledger, for one project or for all of them.

## If something goes wrong

- The map says the project is of the shape before the migration. This is the whole report: nothing more is said of it. The project has no project file, and the one remedy is a migration ([Migrate a project](migrate-a-project.md)).
- The ledger script could not parse a file. The ledger header then carries a line beginning `unparsed:` for it. Claude reads such lines aloud.
- The ledger has a Reports section. It stands only when there is something to say: an ID defined twice, a closed thread touched by a later commit, or a thread cited with neither a thread file nor a closed record. Claude reads this section aloud too.
- Fixing these is the work of the light check (`/check light`), not of the map or of `/ledger`.

## A worked example

A generic run, with a placeholder slug and invented contents:

```
/forge my-project
```

Claude answers along these lines.

```
my-project: kind thought, language en. A repository of its own.

Artefacts
  brief   1.0  approved   mined
  intent  0.3  draft

Can be worked from here
  intent: yes
  (a layer below the intent: not yet, the intent is not approved)

Stale
  render pitch: stale
  published pitch.docx: stale

Libraries needed
  lib-shared: cloned alongside

Waiting on you
  The scope of the first release (thread) and one more thread;
  three open findings.

Next step
  Settle the open thread of scope, then iterate the intent.
  Several matters wait on you: shall I walk through them?

Origin: behind by two commits. Shall I pull?
```

The names, versions and counts here are invented. They only show the order of the blocks.

## See also

- [The ledger, made from the records](../about/the-ledger.md): what the ledger is made from and why nobody writes it.
- [Pull from the remote](pull-from-the-remote.md): the offer the map makes when a repository is behind.
- [Migrate a project](migrate-a-project.md): what to do when the map says a project is of the old shape.
- [Walk through a list](walk-through-a-list.md): how the matters waiting on the principal are worked.
- [Ledger](../reference/ledger.md): the ledger's tables and state words.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
