---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 15bc9095eec8b1ff
inputs:
  - .claude/skills/forge/SKILL.md
  - .claude/skills/ledger/SKILL.md
  - templates/project.md
  - templates/ledger.md#Reports
---

# See where a project stands

This page shows how to ask Claude where a project stands, with the bare `/forge` command or with `/ledger`, and what each answer tells you. It is for the principal (whoever's thinking is being forged) who opens a project and wants to know what exists, what is stale and what waits for a decision.

## When to use it

Use it at the start of a working session, after a pause, or before you decide what to work on next. The answer is read-only: it changes nothing in the project except the ledger, which is made fresh each time. The ledger is the single record of a project's state, made from the project's own records at the moment it is read (see [The ledger, made from the records](../about/the-ledger.md)).

## The command

```
/forge my-project
```

The slug is optional when the conversation already makes the project clear. If it is ambiguous, Claude asks which project you mean. To read only the ledger, for one project or for all of them:

```
/ledger my-project
```

## What happens

1. Claude makes the project's ledger with its script, then reads it. You should now see Claude report from a ledger that is current as of this moment.
2. Claude reports the map in this order. You should now see each of these lines:
   - The project's kind and language, read from the project file, and whether the project is under git. Not being under git is stated as a fact, not as a defect.
   - The chain artefacts that exist, with version and status. The briefs are listed with their mining state, that is how far the intent has absorbed them. A draft brief, or one whose mining is `pending` or `partial`, is named as work waiting. A layer the project does not have is not reported as missing.
   - Which target states can be worked from here, and for those that cannot yet, what is missing.
   - Which renders are stale, and which published files are stale. What makes a render stale is defined by the `/render` command, not here.
   - Which libraries the project needs, and whether each is cloned alongside it.
   - What waits on the principal: the few live matters named in words with the ID in brackets as an address, and the rest as a count.
3. Claude recommends the natural next step in words. The recommendation is never a gate. Where more than one matter waits on you, Claude also offers a walkthrough, which means working the items one at a time with a verdict on each (see [Walk through a list](walk-through-a-list.md)). You should now see one recommendation and, where it applies, the offer.
4. The last word of the map is the state of the engine and of the project against the origin (the remote repository), taken from a status script run with `--remote`. It is one of: up to date, behind, ahead, diverged, no origin. Each state comes with its one offer. For a repository that is behind, that offer is described in [Pull from the remote](pull-from-the-remote.md). The map only says it looked at the remote; it runs none of the offers. You should now see the state of the engine and of the project as the final line.

## Special cases

- A library is material, not a project waiting for a brief. For a library the map reports its sources and research, gives the git line, and stops. There is no chain, no target state and no next step beyond `/ingest`.
- A project of the shape before the migration is said to be so, and nothing more is reported against it. The remedy is in [Migrate a project](migrate-a-project.md).

## What `/ledger` adds

`/ledger` makes the ledger and gives the same report from it, for one project or for all of them. It is the door for reading the ledger alone.

Claude reads aloud two things that the ledger script may leave in it:

- The `unparsed:` lines of the ledger header, which name files the script could not parse.
- The Reports section, which stands only when there is something to say: an ID defined twice, a closed thread touched by a later commit, or a thread cited with neither a thread file nor a closed record.

Fixing them is not the map's work. It belongs to the light check, run with `/check light`.

## What you have afterwards

You have a spoken picture of the project and a recommendation for the next step. Nothing is written except the ledger, which is never kept in git. The tables and state words behind the report are listed on the reference page [Ledger](../reference/ledger.md).

## If something goes wrong

- If Claude cannot tell which project you mean, it asks. Give the slug.
- If the map says the project is of the shape before the migration, run the migration described in [Migrate a project](migrate-a-project.md).
- If the report ends with lines named `unparsed:` or with a Reports section, those are things the ledger script could not settle. Run `/check light` to have them fixed.

## A worked example

A generic map for a thought project with the placeholder slug `my-project`, in outline:

```
Project my-project: thought, language en, under git.

Artefacts: brief 1.0 approved (mined), intent 0.4 draft.
Work from here: intent can be worked now; assignment cannot yet,
the intent is not approved.
Stale: one render (the README); no published file stale.
Libraries: none needed.
Waiting on you: two open threads (the first on the scope of the
pilot) and 3 further matters.

Next: settle the pilot-scope thread. Two matters wait on you:
shall we walk through them?

State against the origin: behind by 1 commit. Offer: /pull.
```

The names, versions and counts here are invented to show the shape. Terms used on this page are explained in the [Glossary](../reference/glossary.md).

## See also

- [The ledger, made from the records](../about/the-ledger.md): what the ledger is made from and why nobody writes it.
- [Pull from the remote](pull-from-the-remote.md): the offer the map makes when a repository is behind.
- [Migrate a project](migrate-a-project.md): what to do when the map says a project is of the old shape.
- [Walk through a list](walk-through-a-list.md): how the matters waiting on the principal are worked.
- [Ledger](../reference/ledger.md): the ledger's tables and state words.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
