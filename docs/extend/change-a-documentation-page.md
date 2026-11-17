---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 1bda9a87455a381e
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

A documentation page is a generated file: Claude writes it from the
files that own its topic, and nobody edits it by hand. This page is
for the extender (whoever adds to the forge or changes it). It shows
how to change what a page says, which pages exist and what the check
refuses, each time by a mend in the file that owns the matter and a
new run of the documentation command.

## When to use it

Use this page when one of these holds:

- A page says something wrong, or something that no longer holds.
- Every page should have another shape, or the pages of one kind
  should carry another kind of content.
- A page is missing, a page should go, or a page is written for the
  wrong reader.
- A page lacks a fact, and no file says it.
- The check lets something through that it should refuse, or refuses
  what it should let through.

In none of these cases is the page the place of the change. The next
run of `/document` writes a page again from its owners, and a mend
made on the page is gone. Only a mend in the file that owns the
matter survives, and the page takes it at the next run.

## What you do

You mend the owner, then you regenerate. This line, typed to Claude
as it stands, regenerates the documentation of the engine:

```
/document
```

With a slug the command regenerates the documentation of one project:
`/document my-project`, where `my-project` stands for the project's
slug. How the command runs is told in
[Generate the documentation](../use/generate-the-documentation.md).
The terms of the forge used here, such as owner, target and owning
project, are in the [Glossary](../reference/glossary.md).

Which file is the owner depends on what you want to change:

| What you want to change | Where you change it | What the next run remakes |
|---|---|---|
| What one page says | The file among the page's `inputs` that owns the matter | The pages that name the file, or the changed part of it, as an input |
| The shape every page has, or what a page of each kind carries | `.claude/agents/docs-writer.md` and `.claude/skills/docs-contract/SKILL.md` | Every page |
| Which pages exist, or who reads a page | The material of the target, or `.claude/agents/docs-planner.md` | The pages whose entry in the documentation map comes out different |
| A fact a page needs and no file owns | The section "Pinned facts (not rendered)" of the readme recipe | The pages whose entry or inputs then change |
| What the check refuses | `scripts/docs-check.py`, and the patterns the check is given | Only the pages that name the script as an input |

Every such mend is a change of the forge. It is recorded and released
the way [Make a change to the forge](how-a-change-is-made.md)
describes.

### Change what a page says

Change the owning file, then run `/document`. The run remakes only
the pages whose inputs, entry or generating rule changed. A script
decides this from content, never by judgement. For every page it
hashes three things together:

- the page's entry in the documentation map, its `state` line
  excepted;
- the content of every input the entry names: a whole file, or only
  the part named after `#`;
- the generating rule: the writer's definition and the documentation
  contract.

The script compares the result with the `inputs-hash` the page
carries in its front-matter. Where the two differ, the page gets the
state `regenerate` and is written again. Where they agree, the page
gets the state `keep` and is left as it is. A change elsewhere in a
file leaves a page as it is, where the page names only a part of that
file.

### Change the shape of every page, or what a kind of page carries

Two files hold the rule every page is made by:

- `.claude/agents/docs-writer.md` (the writer's definition): the
  shape of a page, the outline of each kind of page, where the links
  of a page may go.
- `.claude/skills/docs-contract/SKILL.md` (the documentation
  contract): what content a how-to, an explanation and a reference
  carry, what must never reach a page, the voice, the sentence.

Both are hashed with the inputs of every page. A change of a sentence
in either regenerates every page made by the old rule. Their
whitespace is normalised before the hash is taken: a re-wrap of
either file regenerates nothing.

### Change which pages exist, or who reads a page

The documentation map holds one entry per page, with everything the
page is made from. It is the file `docs-map.md` of the owning
project, for the engine `projects/forge/docs-map.md`. The planner
(the agent that plans the documentation) writes it from the target at
every run. A lasting change is therefore not made in the map. It is
made in one of two places:

- **In the target.** The planner plans a page where the target has
  material for it: one page per job the forge has a command or a
  procedure for, one per concept, one per kind of artefact or part,
  one per kind of addition. Add the material, and the next run plans
  the page. Take the material away, and the planner marks the entry
  `remove` and the run deletes the page. A page keeps its path as
  long as it has material.
- **In the planner's definition**, `.claude/agents/docs-planner.md`.
  It holds the three readers (the user, the extender, the evaluator)
  with a path through the pages for each, the outline of five
  sections, what the planner reads and the rules of an entry. The
  readers and the outline are stated a second time in a position of
  the forge intent (`projects/forge/10-intent.md`): a change of them
  is made in both.

The planner's rules reach the pages through the entries it writes.
After a change of its definition only the pages whose entries come
out different are remade.

### Give a home to a fact no file owns

Where a page needs a fact and no file supports it, the planner lists
the fact in the `## Unowned` section of the documentation map, with
the page that needs it. The writer leaves the fact out. Nothing is
invented to fill the gap: the fact waits for the principal (the
person whose thinking is forged) to give it a home.

One home stands ready. The readme recipe, whose template is
`templates/recipe-readme.md`, may carry a section
`## Pinned facts (not rendered)`. It is for facts of the project that
no file of the project owns yet, such as:

- prerequisites;
- how a tool is installed;
- the public home of the repository.

Each fact is one bullet. The README does not print the section. The
planner reads the bullets there as an owner. A bullet is dropped the
day a file owns the fact.

### Change what the check refuses

At the end of a run a script checks the pages mechanically. It mends
nothing, and it can be run alone:

```
python scripts/docs-check.py projects/forge/docs-map.md docs
```

The check refuses:

- an entry of the documentation map, not in state `remove`, that has
  no page;
- a page in the docs directory that the map does not name (the index
  `README.md` excepted);
- a relative link to a `.md` file that does not resolve;
- a long dash, em or en, in the prose of a page (a code span and a
  fenced block are exempt, since a literal is copied as its owner has
  it);
- a page that does not open with a front-matter;
- an instance fact (a fact of one installation):
  - a value of `CLAUDE.local.md` at the engine root (every word of
    four letters or more in a value, looked for outside URLs);
  - an e-mail address that is not a placeholder at `example.*`;
  - an absolute path of a machine (a drive letter, a user's home
    directory);
  - every pattern given with `--fact`.

It prints every failure with its file and line. Its exit code is 0
when everything holds and 1 when anything fails.

What the check refuses is changed in these places:

- The checks themselves are in `scripts/docs-check.py`. The rules of
  a page they verify are given by the writer's definition.
- The instance facts are not in the script. It reads them from
  `CLAUDE.local.md` at run time. One more pattern is given on the
  command line as `--fact PATTERN`.
- Which addresses a page may carry is said by the `must-not` of the
  page's entry in the documentation map. A published address is
  public by nature, which is why the values are looked for outside
  URLs.
- A match is reported with its line. A false hit (a common word that
  happens to be a value) is seen there, and the rule is adjusted, not
  the page.

## What happens

1. **You find the owner.** Open the page and read its front-matter.
   The `inputs` list names the files the page was made from. A whole
   file is named by its path. A part of a file is named after `#`: a
   section by its heading, an item by its ID. The field `made` says
   whether the page restates its inputs (`mirrored`) or puts together
   what no single file says (`derived`). The matter you want to
   change is owned by one of the inputs. A render or the README of
   the target is never the owner: both are outputs, and a run does
   not read them as owners. The fields are listed in
   [Documentation map](../reference/documentation-map.md).
   You should now see the file, or the part of a file, that says what
   the page says.
2. **You mend the owner.** You change the wording there, as a change
   of the forge.
   You should now see the owner changed and the page still as it was.
3. **You open a new session where you changed an agent's
   definition.** The harness (Claude Code, the program Claude runs
   in) loads an agent's definition once per session (one run of
   Claude Code from its start to its end). A change of
   `.claude/agents/docs-planner.md` or `.claude/agents/docs-writer.md`
   reaches the agents only in a new session. Within the session that
   changed one, Claude passes the changed rule to the agents in their
   task and says so in its report.
   You should now see a new session open before you type the command.
4. **You type `/document`.** The planner writes the documentation map
   again, and a script computes the state of every page. Claude
   deletes the pages in state `remove` and says which. It then says
   the number of pages it is about to write and the models, and
   launches one writer per page. A writer is a subagent (an agent
   Claude launches for one job, which sees nothing of the
   conversation and reads its inputs from disk).
   You should now see a small number of pages named where you mended
   one owner, and every page named where you changed the writer's
   definition or the documentation contract.
5. **The run derives the index and checks the pages.** A script
   derives the index from the documentation map, and the check runs
   over the pages. A page that fails is regenerated once, with the
   failure named in its task.
   You should now see the check's result: nothing, or every failure
   with its file and line.
6. **Claude reports.** The report counts the pages new, regenerated,
   kept and removed, and gives the check's result.
   You should now see your page among the regenerated, with the date
   of the run under `generated` and a new `inputs-hash` in its
   front-matter.
7. **The run files what it could not place.** Three kinds of matter
   are filed, one finding per matter:
   - a fact with no owner, and a disagreement of the documentation
     map and an owner, both with the severity medium;
   - a claim the map asked for and no input carried, which the writer
     left out;
   - a reason a page wanted and no file records, with the severity
     low.

   The report is filed as a check's report,
   `reviews/YYYY-MM-DD-check-documentation.md`, with the documentation
   run named as its reviewer. Its findings are settled by walkthrough
   (the findings worked one at a time with the principal), as
   [Check conformance](../use/check-conformance.md) tells. A mend
   lands in the owner, never on a page.
   You should now see the report in `reviews/` of the owning project,
   where the run could not place something.

## What you have afterwards

- The owner mended: the one place where the matter is said.
- The page regenerated from it, with a new `generated` date and a new
  `inputs-hash`.
- Every other page that draws on the same owner regenerated with it,
  and all the rest untouched.
- The index derived again from the documentation map.
- Where the run could not place something, a dated report in
  `reviews/` with one finding per matter.

## If something goes wrong

- **The command refuses to run.** `/document` runs on `main` only. It
  refuses a repository that is behind its origin or has diverged from
  it.
- **The page did not change.** The state is computed, never judged: a
  page whose inputs did not change is not regenerated. Read the
  page's `inputs` again. A change outside the part a page names after
  `#` leaves the page as it is.
- **A change of an agent's definition had no effect.** The definition
  is loaded once per session. Open a new session and run the command
  again.
- **An input is missing.** An input the documentation map names and
  the disk does not have, a file or a part, is reported and hashed as
  missing. The page is regenerated, and its writer reports the gap.
- **A page fails the check.** It is regenerated once with the failure
  named in its task. A page that fails twice is reported and left out
  of the documentation: the page is deleted, its entry is marked
  `remove` in the documentation map, and Claude says so. The page is
  never mended by hand.
- **The check reports a false hit.** The reported line shows it. The
  rule is adjusted, not the page.
- **A page says "the reason is not recorded".** The inputs give no
  reason, and a page carries none of its own making. The run files
  the place as a finding. The mend is the reason written into the
  owner.
- **You mended a page by hand.** The mend is gone when the run writes
  the page again. Make the same mend in the owner.

## A worked example

The fix is invented. A how-to page says that a command takes a
project's slug as its argument, and you know that the command takes
none.

1. You open the page. Its front-matter reads:

   ```
   ---
   generated: <date of the last run>
   version: <version>
   made: mirrored
   inputs-hash: 0a1b2c3d4e5f6071
   inputs:
     - .claude/skills/<command>/SKILL.md
     - templates/<name>.md#<Section>
   ---
   ```

2. You read the two inputs. The skill of the command still names the
   argument. The page mirrors its owner faithfully: the mistake is in
   the skill.
3. You mend the skill, as a change of the forge.
4. A skill is not an agent's definition, and the session you are in
   will do. You type `/document`.
5. The script hashes every entry with its inputs. The hash of this
   page no longer agrees with its `inputs-hash`, and the page gets
   the state `regenerate`. One other page names the same skill as an
   input and gets `regenerate` too. Every other page gets `keep`.
6. Claude says that it will write two pages, launches a writer for
   each, derives the index and runs the check.
7. The report says: no page new, two regenerated, the rest kept, none
   removed, the check without a failure. The page now says what the
   mended skill says, and its front-matter carries the date of the
   run and a new hash:

   ```
   generated: <date of this run>
   inputs-hash: 9f8e7d6c5b4a3920
   ```

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

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
