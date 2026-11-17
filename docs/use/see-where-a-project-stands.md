---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: f5dd0f2adcea7415
inputs:
  - .claude/skills/forge/SKILL.md
  - .claude/skills/ledger/SKILL.md
  - scripts/forge-status.py
  - templates/project.md
  - templates/ledger.md#Reports
---

# See where a project stands

This page shows how to ask Claude where a project stands: the bare `/forge` command reports a map of the project, and `/ledger` gives the same report from the ledger alone. It is for the principal (whoever's thinking is being forged) who opens a project and wants to know what is there and what waits.

## When to use it

- You open a project and want to know what exists and what waits on you.
- You want the state of one project or of all of them, without working any artefact.
- You want to know whether the project is behind its origin before you write into it.

## The command

```
/forge [slug]
```

`/ledger [slug]` gives the same report; with no slug it reports every project.

## What happens

1. Claude makes the project's ledger with its script, then reads it. The ledger is [made from the records](../about/the-ledger.md) at read time, and nobody writes it. For the report on `/ledger` it makes the ledger of one project, or of every project when you name none.

   You should now see the report begin.

2. Claude reports the state map, in this order:
   - the project's kind and language, from the project file, and whether it is under git, as the status script reports it. "Not under git" is stated as a fact, not as a defect.
   - the artefacts that exist, with version and status, and the briefs with their mining state. A draft brief, or one marked `pending` or `partial`, is named as work waiting. A layer the project does not have is not reported as missing.
   - which target states can be worked from here, and for those that cannot, what is missing.
   - which renders are stale and which published files are stale. What stale means is defined elsewhere, and the map only points at it.
   - which libraries the project needs and whether each is cloned alongside.
   - what waits on the principal. Of the open threads, those something waits on and the high ones are named in words, with the ID following in brackets as an address. The rest are given as a count by priority. The full list is the one `/thread` gives, see [Set a matter aside as a thread](set-a-matter-aside.md). Of whatever else waits, Claude names the few live matters in words and gives the rest as a count.

   You should now see the matters in words, the others only as counts.

3. Claude recommends the natural next step in words. A recommendation is never a gate. Where more than one matter waits on you, it offers a walkthrough, one item per message (see [Walk through a list](walk-through-a-list.md)).

   You should now see one recommendation and, where several matters wait, the offer of a walkthrough.

4. Claude ends with the state of the engine and of the project against the origin, from one run of `python scripts/forge-status.py --remote`. The state is one of these:
   - up to date
   - behind
   - ahead
   - diverged
   - no origin

   Each state comes with its one offer. When a repository is behind, the offer is described in [Pull from the remote](pull-from-the-remote.md).

   From the same run Claude relays what waits on GitHub outside git: the open pull requests and the discussions nobody of the repository has answered, one line each. If the script could not read them, the one line says so and says why: no `gh`, an origin that is not GitHub, no login, or no network. The offer is to look at it before anything is written into the project. The map says it looked at the remote and runs none of it.

   You should now see the state against the origin as the last word of the report.

## Special cases

- **A library.** A library is material, not a project waiting for a brief. The report gives its sources and research and stops after the git line. It has no chain, no target states and no next step beyond `/ingest`.
- **The forge's own project.** For it the status script shows two repositories, the engine and the project beside it, because `forge` names the whole in the commands of git. See [Projects and the engine](../about/projects-and-the-engine.md).
- **A project of the shape before the migration.** The map says so and nothing more. See [Migrate a project](migrate-a-project.md).

## What you have afterwards

Nothing is written into the project. The only file the command writes is the ledger, which is never in git. You have a report you can act on, and the ledger's tables and state words are in [Ledger](../reference/ledger.md).

## If something goes wrong

- The ledger script could not parse a file. The ledger's header carries a line `unparsed:` for it. Claude reads these lines aloud.
- The ledger has a Reports section. It stands only when something is found: an ID defined twice, a closed thread touched by a later commit, or a thread cited with neither a thread file nor a closed record. Claude reads this section aloud too.
- Fixing these is the work of the light check, `/check light`, not of the map or of `/ledger`.
- The status line about GitHub says it could not read. The map goes on without it. The causes are listed in step 4.

## A worked example

A generic map of a thought project, as Claude might say it. The brackets stand where a reader would see an ID.

```
/forge my-project

my-project is a thought project in English, in its own git repository.

Artefacts: the brief 1.0 (approved, mined), the intent 0.4 (draft).
Can be worked from here: the intent. Not yet: the layers below it,
because the intent is not approved.
Stale: one render, the README. No published file is stale.
Libraries: one needed, cloned alongside.

Waiting on you:
- The thread on how the pilot is measured, which the next intent
  round waits on (a bracketed ID stands here).
- The thread on the reporting rhythm, set high (a bracketed ID
  stands here).
- Three more open threads: two medium, one low.
- Of whatever else waits: one finding of the last critique, and two
  more matters as a count.

Next step: take up the thread on measurement, since the intent
waits on it. Several matters wait; shall we walk through them?

Last word: the engine is up to date; the project is behind its
origin by two commits. The offer is /pull. On GitHub: one open pull
request, one discussion nobody has answered.
```

## See also

- [The ledger, made from the records](../about/the-ledger.md): what the ledger is made from and why nobody writes it.
- [Set a matter aside as a thread](set-a-matter-aside.md): the full list of the open threads, and how a thread is born and taken up.
- [Pull from the remote](pull-from-the-remote.md): the offer the map makes when a repository is behind.
- [Migrate a project](migrate-a-project.md): what to do when the map says a project is of the old shape.
- [Walk through a list](walk-through-a-list.md): how the matters waiting on the principal are worked.
- [Projects and the engine](../about/projects-and-the-engine.md): why `forge` names the engine and the forge's own project beside it.
- [Ledger](../reference/ledger.md): the ledger's tables and state words.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
