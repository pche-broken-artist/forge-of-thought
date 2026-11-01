---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: b66902ae92bfaeb5
inputs:
  - .claude/skills/document/SKILL.md
  - .claude/skills/docs-contract/SKILL.md
  - .claude/agents/docs-planner.md
  - .claude/agents/docs-writer.md
  - scripts/docs-state.py
  - scripts/docs-check.py
  - templates/recipe-readme.md#Pinned facts (not rendered)
  - projects/forge/10-intent.md#POS.1450
---

# Change a documentation page

A page of the documentation is a generated file: `/document` writes
it from the files that own its topic, and a run of the command writes
it again whenever those files change. This page is for the extender
who finds something wrong on a page, or wants a page that does not
exist, or wants every page shaped differently, and needs to know
which file to change so that the change survives the next run.

## When to use it

Use this page whenever you want the documentation to say something
else, and never reach for the page itself. A page is never edited by
hand. The next run of `/document` writes the page again from its
owners, and a mend made on the page is gone. Only a mend in the file
that owns the matter survives, and the page takes it at the next run.

The same holds for four different wishes, each with its own owner:

- what one page says: the files its front-matter names as `inputs`;
- the shape every page has, or what kind of content a page of each
  kind carries: the writer's definition and the documentation
  contract;
- which pages exist, who reads them and in what order: the planner's
  definition and the position of the forge intent that defines the
  documentation;
- what the check refuses: the check script and, for the values it
  reads, the instance file.

## What you do

Mend the owner, then run the command, bare for the engine or with a
slug for a project:

```
/document
/document <slug>
```

The command asks nothing. It runs on `main` only and refuses a
repository that is behind or diverged from its origin. How the run
proceeds as a whole is on [Generate the
documentation](../use/generate-the-documentation.md).

## What happens

1. **Find the owner.** Open the page and read its front-matter. The
   `inputs` list names every file, or every named part of a file,
   the page was made from; a part is written after `#`, a section
   by its heading or an item by its ID. The paths are relative to
   the target's root: the engine root for the engine's documentation,
   the project's directory for a project's. The fields of the
   front-matter are on [Documentation
   map](../reference/documentation-map.md). You should now see the
   one file, or the one part of a file, whose wording the page
   restates.

2. **Mend the owner.** Change that file where the matter stands, as
   any change of the forge is made: the chain a change goes through
   is on [Make a change to the forge](how-a-change-is-made.md). Where
   the owner is a skill, a template, an agent or a script, change its
   wording; where the owner is the forge intent, the reason the page
   wants enters the intent in its own round. You should now see the
   mend in the owning file and nothing changed under `docs/`.

3. **Run `/document`.** The planner, an isolated subagent (an agent
   that sees nothing of the conversation and reads every input from
   disk), reads the target on disk and writes the documentation map
   anew at every run, one entry per page. A script then hashes, for
   every entry, the entry's own text together with the content of
   every input it names, a part hashed as that part, and compares the
   result with the `inputs-hash` the page carries. The entry's state
   is set from the comparison alone: `new` where no page exists,
   `regenerate` where the hash differs, `keep` where it is the same.
   Only the pages in state `new` or `regenerate` are written again,
   each by one writer that reads its entry and its inputs from disk
   and nothing else. You should now see the command say which pages
   are new, regenerated, kept and removed.

4. **Read the check's result.** A script checks the pages against
   the map and against the rules of a page and prints every failure
   with its file and line. A page that fails is regenerated once
   with the failure named in its task. A page that fails twice is
   reported and left out of the documentation: deleted, its entry
   marked `remove` in the map, said aloud, never mended by hand. You
   should now see the check's result in the command's report, and
   the page you wanted changed carrying a new `inputs-hash` and the
   wording of the mended owner.

5. **Read the run's report.** What the run could not place is filed
   as a check's report in the owning project's `reviews/`, under the
   name `YYYY-MM-DD-check-documentation` completed as every report's
   name is, with `reviewer: the documentation run`. It holds one
   finding per matter: a fact a page needs and no file owns, a
   disagreement between the map and an owner, a claim the map asked
   for and no input carried, each as medium; a reason a page wanted
   and no file records, as low. The ledger (the project's state
   report, made at read time) reads it as any check's report, and
   the findings are settled by walkthrough (one item per message,
   each closed with a verdict), as [Check
   conformance](../use/check-conformance.md) describes; a mend lands
   in the owner, never on a page. A run that leaves nothing files
   nothing. You should now see either a new report in `reviews/`, or
   none.

### To change the shape of every page

The shape of a page, its front-matter, its headings per kind, the
voice and the sentence, and what must never reach a page, are owned
by two files: the writer's definition
(`.claude/agents/docs-writer.md`) and the documentation contract
(`.claude/skills/docs-contract/SKILL.md`). The state script hashes
both together with the inputs of every entry, with their whitespace
normalised: every run of whitespace, line breaks included, is
collapsed to one space before hashing. So a change of a sentence in
either file regenerates every page made by the old rule, and a
re-wrap of either file regenerates nothing.

### To change which pages exist or who reads them

The map is not edited: the planner writes it from the target at
every run. What the planner plans, the three readers and their
order, the five sections of the outline and what each holds, the
rules of an entry, is owned by the planner's definition
(`.claude/agents/docs-planner.md`) and by the position of the forge
intent that defines the documentation. The planner's rules reach
the pages through the entries it writes: the entry's text is part of
the hash, so an entry the planner words differently regenerates its
page, and an entry it words the same leaves its page as it is.

### To give a home to a fact no file owns

A fact a page needs and no file supports is not invented: the
planner lists it under `## Unowned` in the map, the writer leaves it
out, and the run files it as a finding. Such a fact waits for the
principal (whoever's thinking is being forged, the one who decides)
to give it a home. The readme recipe of the owning project has a
section for exactly this, `## Pinned facts (not rendered)`, whose
skeleton is `templates/recipe-readme.md`: facts of the project that
no file owns yet, such as prerequisites, how a tool is installed or
the public home of the repository, one bullet each. The README does
not print them; the planner reads them there as an owner. A fact is
dropped from the section the day a file owns it.

### A changed agent reaches the next session

Claude Code, the harness the forge runs in (the program that loads
the commands, the skills and the agents), loads an agent's definition
once per session. A change to `.claude/agents/docs-planner.md` or
`.claude/agents/docs-writer.md` reaches the planner or the writers
only in a new session. Within the session that changed one of them,
the changed rule is passed in the agents' task and the run's report
says so.

## What you have afterwards

The owning file carries the mend; the page carries the owner's new
wording and a new `inputs-hash`; the pages whose inputs did not
change are untouched, byte for byte; the map carries every entry's
state as the script set it; the owning project's ledger is remade,
its Renders table reading the index's provenance; and where the run
could not place something, a check's report lies in `reviews/` for
a walkthrough.

## If something goes wrong

- **The check prints a failure with a file and a line.** What it
  looks for: every entry of the map not in state `remove` has its
  page, and no page lies under `docs/` that the map does not name
  (the index `README.md` excepted); every relative link to a `.md`
  file resolves; no long dash, em or en, in the prose of any page,
  a code span and a fenced block exempt; every page opens with a
  front-matter; no instance fact, that is the values of
  `CLAUDE.local.md` at the engine root (every word of four letters or
  more in a value, looked for outside URLs), any e-mail address but a
  placeholder at `example.*`, any absolute path of a machine (a
  drive letter, a user's home directory), and every `--fact` pattern
  the run was given. The exit code is 0 when everything holds and 1
  when anything fails. The check mends nothing: the command
  regenerates the failing page once, with the failure named in its
  task.
- **A page fails twice.** It is reported and left out of the
  documentation: deleted, its entry marked `remove` in the map, said
  aloud. Mend the owner that produced the failing text, or the entry
  it comes from through the planner's rules, and run `/document`
  again.
- **The check reports a false hit.** A common word that happens to
  be a value of the instance file is reported with its line so that
  it is seen; the rule, not the page, is adjusted.
- **An input the map names is not on disk.** A file or a part that
  was renamed or removed is reported by the state script and hashed
  as missing; the page is regenerated and its writer reports the
  gap, which the run files as a finding. Restore the name the map
  expects, or let the planner's next map name the new one.
- **The run refuses to start.** `/document` runs on `main` only and
  refuses a repository behind or diverged from its origin; it offers
  the pull. It never runs on Claude's own judgement.
- **Your mend did not reach the page.** The page's `inputs-hash`
  did not change because none of its inputs changed: the mend landed
  in a file, or in a part of a file, the entry does not name. Read
  the front-matter again and mend the named owner, or, where the
  entry names the wrong owner, raise it as a disagreement of the map
  and the owner so that the planner's rules are mended.
- **The agents behave as before your change to them.** The agent's
  definition was loaded at the start of the session. Start a new
  session and run `/document` again.

## A worked example

An invented fix, traced through. A how-to of `use/` says that a
command takes an optional slug, and the slug was dropped from the
command a round ago.

1. You open `docs/use/<job>.md` and read its front-matter. Its
   `inputs` list names `.claude/skills/<command>/SKILL.md`, whole.
   That skill is the owner.
2. You do not touch the page. You correct the skill's wording where
   it describes the arguments, and you record and release the change
   as any change of the forge.
3. You run `/document`. The planner writes the map again; the entry
   of the page is worded as before, since the skill's description did
   not change. The state script hashes the entry together with the
   skill's content: the content changed, the hash differs from the
   `inputs-hash` on the page, the entry is set to `regenerate`. Every
   other page whose inputs did not change is `keep`. One writer
   remakes the one page from the mended skill.
4. The check passes. The command reports one page regenerated, the
   rest kept, and the check's result. The page now says what the
   skill says, and carries the new hash.
5. Had the skill been silent on why the slug was dropped, the page
   would say that the reason is not recorded, the writer would
   report the place, and the run would file it as a low finding in
   `reviews/`. The reason, where the principal wants one, enters the
   intent in its own round and reaches the page at the next run.

## See also

- [Generate the documentation](../use/generate-the-documentation.md): running the command.
- [Documentation map](../reference/documentation-map.md): the fields of an entry and of a page's front-matter.
- [Make a change to the forge](how-a-change-is-made.md): the chain a change of the forge goes through.
- [Check conformance](../use/check-conformance.md): how a report's findings are settled by walkthrough.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
