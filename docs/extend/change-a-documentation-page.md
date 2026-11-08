---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 803db7979759208e
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

A documentation page is a generated file under `docs/`, made by
`/document` from the files that own its topic. This page is for the
extender who wants to change what a page says, which pages exist,
the shape every page has, or what the check refuses, and shows where
each change goes. The one rule behind all of them: a page is never
edited by hand. The change lands in the file that owns the matter,
and the next run of `/document` carries it onto the page.

## When to use it

- A page says something wrong or stale.
- A page is missing, or a page exists that should not.
- The readers or the outline of the documentation should change.
- The shape every page has, or the kind of content a page of one kind
  carries, should change.
- A page needs a fact that no file of the project owns.
- The check refuses a page and you want to know what to mend.

## What you do

A page is never edited by hand. The next run of `/document` writes
the page again from its owners, and a mend made on the page is gone.
Only a mend in the file that owns the matter survives, and the page
takes it at the next run. The same holds for the documentation map
(`docs-map.md` beside the owning project's ledger): the planner, the
agent that plans the pages, writes it from the target at every run.

### Find the owner

Open the page. Its front-matter lists its `inputs`, the files it was
made from, one per line, relative to the target's root. An input may
be a part of a file, named after `#`: a section by its heading or an
item by its ID. The matter you want to change is in one of those
files, and that file is where the change goes. The fields of the
front-matter and of a map entry are described on the page
[Documentation map](../reference/documentation-map.md).

A render and the README are never owners: a run does not read them
as such.

### Change what a page says

1. Change the owning file: a skill, a template, an agent file, a
   script's help header, or an item of the owning project's intent.
2. Record the change as any change of the forge is recorded; the
   chain it goes through is the page
   [Make a change to the forge](how-a-change-is-made.md).
3. Run `/document` (or `/document <slug>` for a project). It remakes
   only the pages whose inputs, entry or generating rule changed.
   Which pages those are is computed from the content of the inputs,
   never judged. A part named after `#` is hashed as that part, so
   that a change elsewhere in the same file leaves the page as it is.

### Change the shape every page has, or what a kind carries

Two files are the generating rule of every page:

- `.claude/agents/docs-writer.md`: the shape of a page (the
  front-matter, the opening paragraph, the outline of each kind, the
  closing line) and how links are made.
- `.claude/skills/docs-contract/SKILL.md`: the kinds of a page (what
  a how-to, an explanation and a reference carry), what must never
  reach a page or the map, the voice and the sentence of a page.

Both are hashed together with the inputs of every page, with their
whitespace normalised. A change of a sentence in either regenerates
every page made by the old rule. A re-wrap of the text regenerates
nothing.

One thing to know before you run: Claude Code (the harness, that is,
the program Claude runs in) loads an agent's definition once per
session (one sitting of the conversation). A change to
`.claude/agents/docs-writer.md` or `.claude/agents/docs-planner.md`
reaches the agents only in a new session. Within the session that
changed one, Claude passes the changed rule in the agent's task and
says so in its report.

### Change which pages exist, or who reads a page

The map is not a file you edit: the planner writes it from the target
at every run, and the planner's rules reach the pages through the
entries it writes. So:

- A page that should exist needs material in a file of the target: a
  section or a page with no material is left out, never left empty.
  Give the matter a home in an owning file and the planner maps it.
- A page that should go loses its material: the planner marks the
  entry `remove`, and the run deletes the page.
- The readers (the user, the extender, the evaluator), their paths
  and the five sections of the outline are owned by the planner's
  definition, `.claude/agents/docs-planner.md`, and by the position
  of the forge intent on the documentation. A change to them is a
  change to those owners.

### Give an unowned fact a home

A fact a page needs and no file supports is never guessed: the writer
leaves it out, the planner lists it under `## Unowned` in the map
with the page that needs it, and the run reports it. Its home is the
section `## Pinned facts (not rendered)` of the project's readme
recipe, made from the skeleton `templates/recipe-readme.md`: facts of
the project that no file owns yet, such as prerequisites, how a tool
is installed, or the public home of the repository, one bullet each.
The README does not print them; the planner reads them there as an
owner. A pinned fact is dropped the day a file owns it, and the
section is omitted when the project has none.

### Settle what the run filed

What a run cannot place is filed as the run's own report in
`reviews/`, named `check-documentation`, with `reviewer: the
documentation run`, in the shape of a check's report:

- the Unowned list and what did not fit, from the planner (medium);
- what a writer left out, a claim the map asked for and no input
  carried (medium);
- a disagreement of the map and an owner (medium);
- every place where a writer wanted a reason and none is recorded
  (low); the page says there that the reason is not recorded.

The ledger, the project's generated state report, reads it as any
check's report. The findings are settled by walkthrough (one item
per message, each closed with a verdict), as described on the page
[Check conformance](../use/check-conformance.md). A mend lands in
the owner, never on a page. A reason the principal (the person whose
thinking is forged, the final authority on content) wants enters the
intent in its own round and reaches the page at the next run. A run
that leaves nothing files nothing.

### What the check refuses

The check, `python scripts/docs-check.py <map> <docs-dir>`, verifies
the pages against the map and against the rules of a page, and mends
nothing. It refuses:

- an entry of the map not in state `remove` without its page, and a
  page under `docs/` that the map does not name (the index
  `README.md` excepted);
- a relative link to a `.md` file that does not resolve;
- a long dash (em or en) in the prose of a page; a code span and a
  fenced block are exempt, since a literal is copied as its owner has
  it;
- a page that does not open with a front-matter;
- an instance fact: a value of `CLAUDE.local.md` at the engine root
  (every word of four letters or more in a value, looked for outside
  URLs), an e-mail address other than a placeholder at `example.*`,
  an absolute path of a machine (a drive letter, a user's home
  directory), and every `--fact PATTERN` given on the command line.

The script carries no name, address or host of its own: the instance
facts it looks for are read from `CLAUDE.local.md` at run time. A
match is reported with its line, so that a false hit (a common word
that happens to be a value) is seen and the rule, not the page, is
adjusted. A page that fails is regenerated once with the failure
named in its task; a page that fails twice is left out of the
documentation, never mended by hand.

## What happens

After the owner is changed and recorded, `/document` runs in one go
and asks nothing. How it is started and what it says are on the page
[Generate the documentation](../use/generate-the-documentation.md).
The run, from your change's point of view:

1. The planner reads the target on disk and writes the map, one
   entry per page. You should now see the planner's report: the
   counts of pages per section, the Unowned list and what did not
   fit.
2. `python scripts/docs-state.py <map> <docs-dir> --tasks
   tmp/docs-tasks` hashes every entry with the content of its inputs
   and the generating rule, compares the hash with the `inputs-hash`
   of the page on disk, and sets the entry's state: `new`,
   `regenerate` or `keep`. You should now see one summary line,
   `entries N: new ..., regenerate ..., keep ...; remove ...; tasks
   written to ...`, and the page you changed the owner of among the
   regenerated.
3. The pages listed as `remove` are deleted and said aloud. You
   should now see each one named.
4. One writer per task makes its page alone, from its entry and the
   inputs read from disk, and writes the page with the hash its task
   gave it. You should now see the writers' reports: what the inputs
   did not support, and every place a reason was wanted.
5. `python scripts/docs-index.py <map> <docs-dir>` derives the index.
   You should now see `docs/README.md` remade.
6. `python scripts/docs-check.py <map> <docs-dir>` verifies the
   pages. You should now see `N files checked, no failure`.
7. The owning project's ledger is remade, the run is reported (pages
   new, regenerated, kept and removed, the check's result), and what
   the run could not place is filed in `reviews/`. You should now see
   the report, and the path of the filed report where there is one.

## What you have afterwards

- The owning file changed, with its change recorded.
- The page remade from its owners, carrying the new `inputs-hash` in
  its front-matter; every other page as it was.
- The map with the state of every entry set by the script.
- The ledger remade, its Renders table reading the index's
  provenance.
- Where the run could not place something: a report in `reviews/`,
  waiting for a walkthrough.

## If something goes wrong

- `/document` refuses to run: it runs on `main` only, and a
  repository behind or diverged from its origin is refused.
- `missing input: <path> (named by <page>)` from the state script:
  the map names an input the disk does not have, a file or a part.
  The page is regenerated and its writer reports the gap. The owner
  was moved or the part renamed; the planner's next run names it
  anew once the target has it.
- `missing page: <path>` or `page not in the map: <path>` from the
  check: the pages under `docs/` and the map disagree. A page the map
  does not name is removed by the run; a page the map names and the
  run did not write is a writer that failed.
- `<page>: broken link <target>`: a link on the page points to a
  page that does not exist. Links come from the entry's `links`, so
  the entry and the target page disagree.
- `<page>:<line>: long dash`: the owner's prose carries a long dash
  outside a code span, or the writer wrote one. The page is
  regenerated once with the failure named.
- `<page>:<line>: instance fact (<pattern>): <line>`: a value of the
  instance reached a page. The page is regenerated once; where the
  hit is a common word that happens to be a value, the rule is
  adjusted, not the page.
- `<page>: no front-matter`: the page does not open with its
  front-matter. The page is regenerated once.
- A page fails the check twice: it is reported and left out of the
  documentation (deleted, its entry marked `remove` in the map by
  hand, said aloud).
- You changed the writer's or the planner's definition and the pages
  came out by the old rule: the definition is loaded once per
  session. Start a new session, or have the changed rule passed in
  the task.
- You changed an owner and the page kept its state `keep`: the page's
  inputs name a part of the file, and your change lies elsewhere in
  it; or the file you changed is not among the page's inputs at all.
  Read the page's front-matter and the entry's `inputs`.

## A worked example

A page of `docs/use/` says that a command takes an argument it no
longer takes. The fix, traced through:

1. You open `docs/use/<job>.md`. Its front-matter lists one input,
   `.claude/skills/<command>/SKILL.md`. That skill is the owner.
2. You correct the argument line in `.claude/skills/<command>/SKILL.md`
   and record the change as any change of the forge.
3. You run `/document`. The planner writes the map; the state script
   prints `entries 60: new 0, regenerate 1, keep 59; remove 0; tasks
   written to tmp/docs-tasks`. One task, for `docs/use/<job>.md`: the
   skill's content changed, so its hash changed; nothing else did.
4. One writer makes the page anew from the entry and the skill, and
   its report says nothing was left out.
5. The index is derived; the check prints `60 files checked, no
   failure`.
6. The ledger is remade. The run reports one page regenerated and
   files nothing, since nothing was left to place.

Had you corrected the sentence on `docs/use/<job>.md` instead, the
page's hash would still have matched its unchanged inputs, the entry
would have stayed `keep` at this run, and the next change to the
skill, or to the generating rule, would have written the page again
with the wrong argument back.

## See also

- [Generate the documentation](../use/generate-the-documentation.md):
  running the command.
- [Documentation map](../reference/documentation-map.md): the fields
  of an entry and of a page's front-matter.
- [Make a change to the forge](how-a-change-is-made.md): the chain a
  change of the forge goes through.
- [Check conformance](../use/check-conformance.md): how a report's
  findings are settled by walkthrough.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
