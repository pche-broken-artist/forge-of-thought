---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 47572927a9870b12
inputs:
  - .claude/skills/forge/SKILL.md
  - .claude/skills/ledger/SKILL.md
  - scripts/forge-status.py
  - templates/project.md
  - templates/ledger.md#Reports
---

# See where a project stands

The bare `/forge` command reports the state map of a project, and `/ledger` reports the same state from the ledger alone. This page is for the principal (the person whose thinking is being forged) who wants to know what a project holds, what waits on him and what to do next. The ledger is the single source of truth for state, made from the project's documents each time it is read.

## When to use it

- At the start of a session, to see where the work stands.
- Before deciding what to work on next.
- After a pull or a migration, to see the project as it is now.
- When you want the state of one project or of all of them without the recommendation: use `/ledger`.

## The command

```
/forge my-project
```

The slug is optional where the project is clear from the conversation. Where it is ambiguous, Claude asks.

For the ledger-only reading of one project:

```
/ledger my-project
```

Without a slug, `/ledger` reports every project.

## What happens

1. Claude makes the project's ledger with its script and reads it. You should now see the ledger remade, with no hand-written row anywhere.
2. Claude reports the map, compactly, in this order. You should now see each of these parts that the project has material for:
   - The kind and the language of the project, taken from its project file, and whether the project is under git, as the status script reports it. "Not under git" is stated as a fact, not as a defect.
   - The artefacts of the chain with their versions and status, and the briefs with their mining state. A draft brief, or one marked `pending` or `partial`, is named as work waiting. A layer the project does not have is not reported as missing.
   - Which target states can be worked from here, and for those that cannot yet, what is missing.
   - Which renders are stale, and which published files are stale. What makes them stale is defined on [Ledger](../reference/ledger.md) and in the render command, not here.
   - The libraries the project needs, and whether each is cloned alongside.
   - What waits on the principal: the few live matters named in words, with the ID following in brackets as an address, and the rest as a count.
3. Claude recommends the natural next step in words. The recommendation is never a gate. Where more than one matter waits on you, Claude also offers a walkthrough (a list worked one item per message, with a verdict on each). You should now see one recommended step, and the offer if several matters wait. How a walkthrough runs is on [Walk through a list](walk-through-a-list.md).
4. Claude ends with the state of the engine and of the project against the origin, from the status script run with its remote option. You should now see one of these words, as a fact, with that state's one offer:
   - up to date
   - behind
   - ahead
   - diverged
   - no origin

   Behind has its own page: [Pull from the remote](pull-from-the-remote.md).
5. From the same run, Claude says what waits on GitHub outside git: the open pull requests and the discussions that nobody of the repository has answered, one line each. You should now see those lines, or one line saying it could not read them and why. The reasons it names are these:
   - no `gh`
   - an origin that is not GitHub
   - no login
   - no network

   The offer is to look at what waits before anything is written into the project. The map says that it looked at the remote and runs none of it.

### A library

A library is material, not a project waiting for a brief. For a library the map reports its sources and its research, then the git line, and stops. There is no chain, no target state and no next step beyond `/ingest`.

### A project of the old shape

A project without a project file is of the shape before the migration. The map says so as a fact and says nothing more of it. The one remedy is the migration: see [Migrate a project](migrate-a-project.md).

### What `/ledger` adds

`/ledger` makes the ledger and gives the same report from it, as step 2 above, for one project or for all. It does not recommend and does not look at the remote. Two things in the ledger are read aloud:

- The lines `unparsed:` of its header, one for each file the script could not parse.
- The Reports section, which stands only when there is something to say. It carries what the merged files cannot say: an ID defined twice, a closed thread touched by a later commit, a thread cited with neither a thread file nor a closed record.

Fixing them is not done here. It belongs to the light check, `/check light`.

## What you have afterwards

You have a report and nothing more. The command is read-only but for the ledger, which the script writes and which is never in git. Nothing of the project changes, and the offers wait for your word.

## If something goes wrong

- Several projects fit and none is named: Claude asks which one you mean.
- The map says the project is of the shape before the migration: nothing more is reported until it is migrated.
- The last word says it could not read what waits on GitHub: the map goes on without it, and the line names the reason.
- Lines `unparsed:` or a Reports section appear: they are read aloud, and the light check fixes them.

## A worked example

You type `/forge my-project`. Claude reports a map of this shape. The wording is generic.

```
my-project: a thought project, language en, a repository of its own.

Artefacts: the brief, approved, mined; the intent, version 2.3, draft.
The assignment cannot be worked yet: it needs an approved intent.

Renders: the README is stale. No published file.
Libraries: none needed.

Waiting on you: one open thread about who the recipients are
(an address in brackets follows), and three other matters.

Next step: settle the thread about the recipients, then ask for the
assignment. Several matters wait, so I offer a walkthrough of them.

Against the origin: up to date.
On GitHub: one open pull request; no discussion waits.
Do you want to look at it before anything is written?
```

In the real map the bracket holds the matter's address; here it is left as the place a reader would see it.

## See also

- [The ledger, made from the records](../about/the-ledger.md): what the ledger is made from and why nobody writes it.
- [Pull from the remote](pull-from-the-remote.md): the offer the map makes when a repository is behind.
- [Migrate a project](migrate-a-project.md): what to do when the map says a project is of the old shape.
- [Walk through a list](walk-through-a-list.md): how the matters waiting on the principal are worked.
- [Ledger](../reference/ledger.md): the ledger's tables and state words.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
