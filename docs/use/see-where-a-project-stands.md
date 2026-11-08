---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: f0eb325bb13c29d0
inputs:
  - .claude/skills/forge/SKILL.md
  - .claude/skills/ledger/SKILL.md
  - scripts/forge-status.py
  - templates/project.md
  - templates/ledger.md#Reports
---

# See where a project stands

This page shows how to ask where a project stands: the bare `/forge` command reports the state map of one project, and `/ledger` reports the same from the ledger alone. It is for the principal (the person whose thinking is being forged) who comes back to a project and wants to know what exists, what waits and what to do next.

## When to use it

- You open a project and want its state before you decide what to work on.
- You want to know what waits on you.
- You want to know whether the project is behind or ahead of its origin, or whether something waits on GitHub.
- You want a ledger-only reading of one project or of all of them: use `/ledger`.

## The command

```
/forge <slug>
```

Replace `<slug>` with the slug of the project. Where the context makes the project clear, the slug may be left out. Where it is ambiguous, Claude asks.

For the ledger-only reading:

```
/ledger <slug>
```

With no slug, `/ledger` reports every project.

## What happens

1. Claude makes the project's ledger with its script. The [ledger](../about/the-ledger.md) is the record of state, made from the documents whenever it is read, so nobody writes it.

   You should now see the report open from a freshly made ledger, not from a stale copy.

2. Claude reads the project file and the git state, and reports the kind (thought or library), the language, and whether the project is under git. The git state comes from the status script and is stated as a fact: a repository of its own, or "not under git". Not being under git is a property of the project, not a defect.

   You should now see the kind, the language and the git line first.

3. For a library, the report stops here, after its sources and research and the git line. A library is material, not a project waiting for a brief, so it has no chain, no target states and no next step beyond `/ingest`.

   You should now see for a library only its material and the git line.

4. For a thought project, Claude lists the artefacts that exist, with version and status. The briefs are listed with their mining state, and a draft brief, or one marked `pending` or `partial`, is named as work waiting. A layer the project does not have is not reported as missing.

   You should now see each existing artefact with its version and status.

5. Claude says which target states can be worked from here and which cannot yet, and what is missing for those.

   You should now see the states you can start, and for the others the missing input.

6. Claude names the stale renders and the stale published files. What makes one stale is defined in the [Ledger](../reference/ledger.md) reference and by `/render`, not here.

   You should now see the stale outputs by name, or none.

7. Claude lists the libraries the project needs, from the ledger's dependencies, and whether each is cloned alongside.

   You should now see each needed library with a yes or no for being cloned beside the project.

8. Claude reports what waits on the principal. The few live matters are named in words, each with its ID following in brackets as an address, and the rest are given as a count.

   You should now see a few matters in plain sentences and a count of the others.

9. Claude recommends the natural next step in words. The recommendation is never a gate. Where more than one matter waits on you, it offers a [walkthrough](walk-through-a-list.md) of them, which works the matters one at a time.

   You should now see one recommended step and, if several matters wait, the offer of a walkthrough.

10. The last word of the map is the state of the engine and of the project against the origin, from the status script run with `--remote`. It is one of:
    - up to date
    - behind
    - ahead
    - diverged
    - no origin

    Each state comes with its one offer. Where a repository is behind, the offer leads to [Pull from the remote](pull-from-the-remote.md).

    From the same run the map says what waits on GitHub outside git: the open pull requests and the discussions nobody of the repository has answered, one line each. Where it cannot read them, it gives one line saying why. The reasons are:
    - no `gh`
    - an origin that is not GitHub
    - no login
    - no network

    The offer is to look at it before anything is written into the project. The map says it looked at the remote and runs none of it.

    You should now see the remote line, and under it the GitHub line or its one-line reason.

For the forge's own project the status script shows two repositories, the engine and the project beside it, because `forge` names the whole in the commands of git. See [Projects and the engine](../about/projects-and-the-engine.md).

A project of the shape before the migration is said to be so and nothing more is reported. Go to [Migrate a project](migrate-a-project.md).

## What you have afterwards

You have a report in the conversation. The only file written is the ledger, which the script makes and git never keeps. Nothing else is changed, pulled or merged.

`/ledger` reads aloud two things that the map does not stress: the lines the ledger script could not parse (the `unparsed:` lines of the ledger header) and the ledger's Reports section. That section stands only when there is something to say, such as an ID defined twice. Fixing them belongs to the light check, `/check light`.

## If something goes wrong

- The project has no project file: it is of the old shape. The map says so and stops. Run `/migrate` as [Migrate a project](migrate-a-project.md) describes.
- The GitHub line says it could not be read: the line gives the reason. The rest of the map is not affected.
- The ledger header has `unparsed:` lines or a Reports section: use `/ledger` and then `/check light` to fix them.

## A worked example

You type:

```
/forge <slug>
```

A map of a generic thought project, in the shape you would read:

```
Kind: thought. Language: en. Under git: a repository of its own.
Artefacts: the brief (mined), the intent (version 2.0, approved).
No layer below the intent; none is missing.
States you can work from here: the assignment. Not yet: none.
Stale renders: the README. Published files: none stale.
Libraries needed: none.
Waiting on you: an open thread on who owns the rollout (its address),
a critic finding on the Purpose section (its address), and four more.
Next step: settle the thread on the rollout; a walkthrough of the
matters is on offer.
Remote: behind by two commits; /pull is the offer.
GitHub: one open pull request; nothing unanswered in discussions.
```

You should now see what exists, what waits, what to do next and the state against the origin.

## See also

- [The ledger, made from the records](../about/the-ledger.md): what the ledger is made from and why nobody writes it.
- [Pull from the remote](pull-from-the-remote.md): the offer the map makes when a repository is behind.
- [Migrate a project](migrate-a-project.md): what to do when the map says a project is of the old shape.
- [Walk through a list](walk-through-a-list.md): how the matters waiting on the principal are worked.
- [Projects and the engine](../about/projects-and-the-engine.md): why `forge` names the engine and the forge's own project beside it.
- [Ledger](../reference/ledger.md): the ledger's tables and state words.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
