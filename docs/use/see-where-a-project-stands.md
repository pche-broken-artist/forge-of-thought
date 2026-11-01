---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: ea22a7a72b33cdbb
inputs:
  - .claude/skills/forge/SKILL.md
  - .claude/skills/ledger/SKILL.md
  - templates/project.md
  - templates/ledger.md#Reports
---

# See where a project stands

Two commands tell you where a project stands: bare `/forge`, which reports the state map of one project, and `/ledger`, which gives the same report from the ledger alone. This page is for the principal, the person whose thinking is being forged, who wants to know what exists, what is stale and what waits for a decision.

## When to use it

- You open a project and want to know what is there and what to do next.
- You want the state of one project or of every project, without working on any artefact.

Both commands read. The only file they write is the ledger, the single source of truth for state, which a script makes from the documents each time it is read (see [The ledger, made from the records](../about/the-ledger.md)).

## The command

```
/forge <slug>
```

The slug is optional where Claude can infer the project from the context. To read the ledger only, for one project or for all of them:

```
/ledger <slug>
```

Bare `/ledger` reports every project.

## What happens

1. Claude makes the project's ledger with its script.
   You should now see the report begin from a fresh ledger.
2. Claude reads the ledger and lists the target states it could work.
   A target state is an artefact the project could work on next.
3. Claude reports the state map. It names, in this order:
   - the kind and the language, both from the project file, and whether the project is under git, as the status script reports it. "Not under git" is stated as a fact, never as a defect.
   - the artefacts that exist, with version and status, and the briefs with their mining state. A draft brief, or one that is `pending` or `partial`, is named as work waiting. A layer the project does not have is not reported as missing.
   - which target states can be worked from here, and for the others what is missing.
   - which renders are stale and which published files are stale. What makes a render stale is defined in the page [Ledger](../reference/ledger.md) and the glossary, not here.
   - the libraries the project needs, and whether each is cloned alongside.
   - what waits on the principal: the few live matters named in words with the ID following in brackets as an address, and the rest as a count.
   You should now see a compact map in those parts.
4. Claude recommends the natural next step in words. It is a recommendation, never a gate. Where more than one matter waits on you, it offers a walkthrough (see [Walk through a list](walk-through-a-list.md)).
   You should now see one recommended step.
5. Claude ends with the state of the engine and of the project against the origin, as the map's last word. The state is one of up to date, behind, ahead, diverged or no origin, and comes with that state's one offer. The map says it looked at the remote and runs none of the offer. For a repository that is behind, the offer is described in [Pull from the remote](pull-from-the-remote.md).
   You should now see the remote state as the last line.

A library is material, not a project waiting for a brief. For a library the map reports its sources and research and stops after the git line: no target states and no next step beyond `/ingest`.

`/ledger` follows the same report. It differs in being the door for a ledger-only reading of one project or of all of them. It also reads aloud the `unparsed:` lines of the ledger header, which name files the script could not parse, and the ledger's Reports section. The Reports section stands only when there is something to say: an ID defined twice, a closed thread touched by a later commit, or a thread cited with neither a thread file nor a closed record. Fixing these is the work of the light check (`/check light`), not of `/ledger`.

## What you have afterwards

- A fresh ledger for the project.
- A report in the conversation. Nothing else is written.

## If something goes wrong

- The slug is ambiguous: Claude asks which project you mean.
- The project is of the shape before the migration, that is, it has no project file. Claude says so as a fact and says nothing more about the project. The one remedy is `/migrate` (see [Migrate a project](migrate-a-project.md)).
- The ledger lists `unparsed:` lines or a Reports section: Claude reads them aloud. Run `/check light` to have them settled.

## A worked example

A thought project with the placeholder slug `my-project`, `/forge my-project`. The text is generic and shows the shape only.

```
my-project: a thought project, language en, a repository of its own.

Chain: brief 1.0 (mined), intent 0.4 (draft), assignment 0.1 (draft).
Can be worked from here: the solution design (the intent exists).
Cannot yet: the BRD, because the assignment is not approved.
Stale: one render, the pitch. No published file is stale.
Libraries needed: one, cloned alongside.

Waiting on you: the intent says two things about the audience that do
not fit together (see the open thread, [address]), and one assignment
item lacks an owner ([address]). Three more matters wait.

Next: settle the audience question, then the assignment. Shall we
walk through the matters that wait?

Against the origin: behind by two commits. Offer: /pull.
```

## See also

- [The ledger, made from the records](../about/the-ledger.md): what the ledger is made from and why nobody writes it.
- [Pull from the remote](pull-from-the-remote.md): the offer the map makes when a repository is behind.
- [Migrate a project](migrate-a-project.md): what to do when the map says a project is of the old shape.
- [Walk through a list](walk-through-a-list.md): how the matters waiting on the principal are worked.
- [Ledger](../reference/ledger.md): the ledger's tables and state words.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
