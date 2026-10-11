---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 155fef8bcde769c3
inputs:
  - .claude/skills/document/SKILL.md
  - .claude/skills/docs-contract/SKILL.md
  - .claude/agents/docs-planner.md
  - .claude/agents/docs-writer.md
  - scripts/docs-state.py
  - scripts/docs-check.py
  - templates/recipe-readme.md#Pinned facts (not rendered)
---

# Change a documentation page

A page of the documentation is a generated file: it is made from the
files of the forge that own its matter, and it is never edited by
hand. This page is for you, the extender, when a page says something
wrong, when a page should exist or disappear, when every page should
change its shape, or when the check refuses a page. It says where
the matter lives and how the page comes to be made again. A change
of the forge is decided by the principal (the person whose thinking
is forged in it); what you do here is find the owner of the matter,
change it on his word and run the command.

## When to use it

- A sentence on a page is wrong or out of date.
- A page should exist that does not, a page should go, a page covers
  the wrong topic or is written for the wrong reader.
- The shape every page has, or what every page must keep off, should
  change.
- A page needs a fact that no file of the forge owns.
- The check refuses a page.

Not to edit the page: what is wrong is mended in the file that owns
the matter, and the page is regenerated. Not to edit the
documentation map either (`docs-map.md`, beside the owning project's
ledger): the planner writes it anew from the target at every run.

## What you do

```
/document
```

Bare, the command documents the engine; `/document <slug>` documents
a project. The command runs after the change: three moves, find the
owner, change it, run. How the command runs on its own is the page
[Generate the documentation](../use/generate-the-documentation.md).

## What happens

1. **Find the owner.** Open the page. Its front-matter lists under
   `inputs` the files the page was made from and says `made:
   mirrored` or `made: derived`. A mirrored page restates what its
   inputs say in the reader's words. A derived page puts together
   what its inputs say, by the reasoning its entry in the
   documentation map gives under `evidence`. The owner of a sentence
   is among the inputs: a skill, a definition (the state file of an
   artefact), a template, an agent, the docstring of a script. An
   input may be a part of a file, named after `#`: a section by its
   heading, an item by its ID. A reason a page gives comes from the
   forge intent, that is the intent of the project that owns the
   documentation; where none is recorded the page says "the reason
   is not recorded". The fields of an entry and of a page's
   front-matter are on the page
   [Documentation map](../reference/documentation-map.md).
   You should now see the file, or the part of a file, that carries
   the words the page restates.

2. **Decide which kind of change it is, and change the owner.** The
   kinds, each with its owner:

   - What a page says: the owning file. The page follows at the next
     run. A reason the page wants and no file gives does not go into
     a skill or a template: it enters the forge intent in its own
     round, on the principal's decision.
   - The shape every page has: the writer's definition,
     `.claude/agents/docs-writer.md`, which owns the front-matter,
     the headings and the outline of each kind of page.
   - What every page must keep off, the voice and the sentence of a
     page: the contract, `.claude/skills/docs-contract/SKILL.md`.
     The contract keeps off every page the name of a person, a
     company, a host, an account, an e-mail, any identifier of an
     instance (one installation of the forge), any address but the
     public home of the target, any document of a project but the
     owning one, the text of a skill or an agent as an instruction to
     Claude, any ID of the chain, any reason the inputs do not give,
     any date of a decision or history of a rule, and any sentence of
     the generator about itself.
     The writer's definition and the contract are hashed with the
     inputs of every page, so a change of either regenerates every
     page.
   - Which pages exist, what a page covers, who reads it: the map is
     written by the planner from the target at every run, so an entry
     you add or edit in the map by hand is gone at the next run. The
     readers and the outline of the sections are in the planner's
     definition, `.claude/agents/docs-planner.md`, and in a position
     of the forge intent. Such a change goes through the chain, the
     intent first, then the planner's definition, as the page
     [Make a change to the forge](how-a-change-is-made.md) says.
   - A fact a page needs and no file of the forge owns: the run
     reports it under Unowned and the page leaves it out; nothing is
     invented to fill it. Until a file owns the fact, its home is the
     section "Pinned facts (not rendered)" of the owning project's
     readme recipe, `recipes/readme.md`, whose skeleton is
     `templates/recipe-readme.md`. One bullet per fact, such as a
     prerequisite, how a tool is installed, the public home of the
     repository. The README does not print the section; the planner
     reads it as an owner. A bullet is dropped the day a file owns
     the fact, and the section is omitted when there is none.

   Every one of these is a change of the forge, recorded and
   released as any other: the chain it goes through is on the page
   [Make a change to the forge](how-a-change-is-made.md).
   You should now see the owner changed and the page still as it was.

3. **Run `/document`.** One run, no question asked. The planner, a
   subagent (an agent Claude launches apart from the conversation,
   which sees nothing of it), reads the target on disk and writes
   the map. A script then hashes every entry of the map together
   with the content of each input the entry names, a part as that
   part, and with the generator (the writer's definition and the
   contract), and compares the result with the `inputs-hash` in the
   front-matter of the page at the entry's path. No page at the path
   is `new`; a page with a differing hash is `regenerate`; a page
   with the same hash is `keep`. A page under `docs/` that no entry
   names is removed. Only a `new` or `regenerate` page gets a writer,
   one subagent per page, which reads its inputs from disk and
   writes the page with the hash it was given. The index is derived
   from the map and the check runs over the pages.
   You should now see the state line, in the shape
   `entries N: new a, regenerate b, keep c; remove d; tasks written to tmp/docs-tasks`,
   the check's closing line `N files checked, no failure`, and
   Claude's report: the pages new, regenerated, kept and removed; the
   Unowned list and what did not fit; what the writers left out;
   every place where a writer wanted a reason and none is recorded;
   the check's result.

## What you have afterwards

- The page regenerated from the changed owner, with a new
  `inputs-hash` in its front-matter.
- Every other page that names the changed file or part among its
  inputs regenerated too; every page whose inputs did not change
  kept as it was.
- The map written anew by the planner and the index `docs/README.md`
  derived from it.
- A row for the index in the Renders table of the owning project's
  ledger (the project's one record of its state).
- A change of the forge to record and release as any other.

## If something goes wrong

The check prints every failure with its file and line, and mends
nothing. What it refuses:

- `missing page: docs/...`: an entry of the map not in state
  `remove` has no page.
- `page not in the map: docs/...`: a page lies under `docs/` that
  the map does not name; the index is excepted.
- `<page>: broken link <target>`: a relative link to a `.md` file
  that does not resolve.
- `<page>:<line>: long dash`: an em or en dash in the prose of a
  page; a code span and a fenced block are exempt, since a literal
  is copied as its owner has it.
- `<page>: no front-matter`: the page does not open with one.
- `<page>:<line>: instance fact (...)`: a value of `CLAUDE.local.md`
  at the engine root (every word of four letters or more in a value,
  looked for outside URLs), an e-mail address other than a
  placeholder at `example.*`, an absolute path of a machine (a drive
  letter, a home directory), or a pattern given to the check with
  `--fact`.

A page that fails is regenerated once, with the failure named in its
task. A page that fails twice is reported and left out of the
documentation: deleted, its entry marked `remove` in the map by
hand, said aloud, never mended by hand. A false hit (a common word
that happens to be a value of the instance) is seen with its line,
and the rule is adjusted, not the page.

Other signs:

- `missing input: <path> (named by <page>)`: the map names an input
  the disk does not have, a file or a part. The page is regenerated
  and its writer reports the gap.
- `no entries found in the map`: the map holds no entry, and the
  state script stops.
- A change to the planner's or the writer's definition has no
  effect. The harness (the program that runs Claude and its agents)
  loads an agent's definition once per session (one conversation
  with Claude, from its start to its end): the change reaches the
  agents in a new session. Within the session that made the change,
  Claude passes the changed rule in the agents' task and says so in
  its report.
- A page says "the reason is not recorded" where you wanted a
  reason: no input gives it. It enters the forge intent in its own
  round, on the principal's decision, and the page follows at the
  next run.

## A worked example

An invented fix, traced through. A page of `use/` says that a
command asks for confirmation before it writes, and the command no
longer does.

1. You open `docs/use/<job>.md`. Its front-matter reads:

   ```
   ---
   generated: 2026-10-11
   version: 5.3
   made: mirrored
   inputs-hash: 0123456789abcdef
   inputs:
     - .claude/skills/<command>/SKILL.md
   ---
   ```

   The page is mirrored, and its one input is the skill of the
   command: the sentence restates a step of that skill.

2. You open `.claude/skills/<command>/SKILL.md` and find the step
   that still says the question. You change the wording of the step,
   on the principal's word, and record the change as any change of
   the forge. The page stays untouched.

3. You run `/document`. The state line reads
   `entries 80: new 0, regenerate 2, keep 78; remove 0; tasks written to tmp/docs-tasks`:
   the page of the job, and one other page that names the same skill
   among its inputs, are made again; the other seventy-eight are
   kept. Two writers run. The check closes with
   `81 files checked, no failure` (eighty pages and the index), and
   Claude's report lists the two pages regenerated, nothing left
   out, no reason wanted.

4. You open `docs/use/<job>.md` again: a new `inputs-hash`, the
   sentence gone, the rest as it was. The change of the skill and
   the regenerated pages are saved and released together, as any
   change of the forge.

## See also

- [Generate the documentation](../use/generate-the-documentation.md): running the command.
- [Documentation map](../reference/documentation-map.md): the fields of an entry and of a page's front-matter.
- [Make a change to the forge](how-a-change-is-made.md): the chain a change of the forge goes through.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
