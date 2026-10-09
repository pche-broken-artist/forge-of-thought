---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/new-project/SKILL.md
  - CLAUDE.md
  - templates/ledger.md
---

# Start a project

This page is for someone who wants to open a new project in the
forge. It shows how `/new-project <slug>` creates one, what it
creates for each of the two kinds, and the one thing you do yourself
afterwards: put the project under git.

## Choose the kind and the language

A project has one of two kinds, declared as `kind:` in the header of
its ledger:

- **thought** (the default): a project with a chain of documents,
  from the brief and the intent onward.
- **library**: material shared across projects, with no chain. Its
  slug starts with `lib-`.

The command infers a library from the `lib-` prefix or from your
words, and asks when that is unclear.

A project also declares the language of its chain documents as
`language:` in the same header. It is English unless you name
another; the command asks when your words leave it open. This is the
language of the project's documents, not the language you talk to
Claude in.

## Start a thought project

1. Run `/new-project <slug>`. The slug is lowercase with hyphens and
   no spaces. If `projects/<slug>/` already exists, the command stops
   and reports; it never overwrites.
2. The command creates the structure, files only:
   - `sources/`, `reviews/`, `challenges/` and `research/`, empty
     except for `sources/00-INDEX.md` and `research/00-INDEX.md`,
     which are catalogues with their header filled and no entries;
   - `ledger.md`, filled with the slug, `kind: thought`, the language
     and today's date, and with the brief as a 0.1 draft row, pending;
   - `decisions.md`, with the slug filled and no records yet;
   - `recipes/readme.md` and `recipes/release-notes.md`, each with its
     history companion. Their renders are made later, at a release,
     not by this command.
3. The command then asks you to paste or dictate the founding brief
   at once, and hands it to `/forge brief`. How the brief is
   composed is the brief page's matter.
4. It does not create the intent or any layer below it. Each of these
   is born from its own first `/forge <state>`, so `10-intent.md`
   appears when you first run `/forge intent`.
5. It updates the ledger and proposes the next step: `/forge intent`
   to start the elicitation interview.

A `logo.png` in the project root, used as the repository avatar, is
yours to supply. It is optional; the command mentions it once and
does not ask for it.

## Start a library

A library is named with the `lib-` prefix. The command creates only:

- `ledger.md` with `kind: library`, reduced to the tables a library
  keeps (renders, sources, dependencies, research, and what waits on
  you);
- `sources/00-INDEX.md` and `research/00-INDEX.md`;
- `recipes/readme.md` with its history companion. The README is the
  library's catalogue of what it holds.

There is no brief, no decisions file, no reviews or challenges and no
release notes. The command finishes by proposing `/ingest` for the
first documents.

## Put the project under git yourself

The command never runs git. A new project starts "not under git",
which is a property and not a defect, and the command tells you so
once at the end. Putting it under git is a one-off act that is yours:

```
git -C projects/<slug> init -b main
```

Add a remote afterwards if you want one. The commit identity is
git's own, resolved on each machine from your git configuration; the
forge sets none. Once the project is a repository, the forge's
scripts can save it.

## See also

- [Write a brief](write-a-brief.md): composing the founding brief.
- [Share material through a library](share-material-through-a-library.md): what a library is for and how it is used.
- [About projects and the engine](../about/projects-and-the-engine.md): why a project is a repository of its own that the engine does not know.
