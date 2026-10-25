---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: b73d6da15f78e422
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

A documentation page is generated: it is made from files of the
engine or of a project, and it is never edited by hand. This page is
for the extender who finds a page wrong, wants a page added or
dropped, or wants the check to refuse something else. It shows where
each kind of change is made, so that the next run of the
documentation command carries it onto the pages. Terms of the forge
used here without a gloss are in the [Glossary](../reference/glossary.md).

## When to use it

Use it in any of these cases:

- a page says something wrong or out of date;
- the shape of every page should change;
- a page should exist that does not, or the other way round;
- the check lets through something it should refuse.

The rule behind every case is one: what is wrong on a page is mended
in the file that owns the matter, and the page is regenerated. A hand
edit lasts only until one of the page's inputs changes. Then a writer
makes the page anew from its inputs, and the edit is gone. The check
mends nothing either: a page that fails is regenerated, never mended
by hand.

## What you do

Find the owner, change it, then run the documentation command:

```
/document
```

Bare, it documents the engine. For a project, give its slug:
`/document <slug>`. Running the command is described in full on
[Generate the documentation](../use/generate-the-documentation.md).

The change itself is a change of the forge like any other. It goes
through the chain described on
[Make a change to the forge](how-a-change-is-made.md).

## What happens

1. **Find the owner.** Open the page and read its front-matter. Its
   `inputs` list names every file the page was made from, or the part
   of a file after `#` (a section by its heading, an item by its ID).
   The fields of the front-matter are listed on
   [Documentation map](../reference/documentation-map.md).
   You should now see the file, or the part of it, that says what
   the page says.

2. **Pick the kind of change.** Each kind has its own owner:

   - What one page says: the input that says it. Change that file
     or that part.
   - The shape every page has, or what kind of content a page of each
     kind carries: the writer's definition,
     `.claude/agents/docs-writer.md`, and the documentation contract,
     `.claude/skills/docs-contract/SKILL.md`. The contract owns the
     kinds of a page (how-to, explanation, reference), the voice, the
     sentence and what must never reach a page. The writer's
     definition owns the shape of a page and the outline of each
     kind.
   - Which pages exist, who reads them and in which section they
     stand: the planner's definition,
     `.claude/agents/docs-planner.md`. It owns the three readers
     (the user, the extender, the evaluator) and the outline of five
     sections. The reason behind the readers and the outline stands
     in a position of the forge's own intent.
   - A fact a page needs that no file owns: see step 5.
   - What the check refuses: the check script,
     `scripts/docs-check.py` (see "If something goes wrong").

   The documentation map (the file of one entry per page that the
   pages are made from) is written by the planner, the agent that
   plans the pages, from the target on disk at every run. A hand edit
   of the map therefore does not last.
   You should now see one file to change, and know which of the
   kinds above it is.

3. **Change the owner.** Edit the file, or the part the front-matter
   names. A page is made from its inputs only. So a fact you put in a
   file the page does not read never reaches it.
   You should now see the owning file changed, and the page itself
   untouched.

4. **Run `/document`.** The command remakes only what changed. The
   state script, `scripts/docs-state.py`, hashes each entry of the map
   together with the content of every input it names. A named part is
   hashed as that part, so a change elsewhere in the same file leaves
   the page as it is. The writer's definition and the contract are
   hashed with the inputs, so a change of either regenerates every
   page. The planner's definition is not hashed: its rules reach the
   pages through the entries it writes. Each page carries in its
   front-matter the hash it was made from, `inputs-hash`, and the two
   are compared:

   - `new`: no page at the path yet.
   - `regenerate`: the hash differs, because an input or the entry
     changed.
   - `keep`: the hash is the same, so the page is not touched.

   A page that no entry names any more is listed as `remove`.
   You should now see, in the run's report, the pages new,
   regenerated, kept and removed, with your page among the
   regenerated.

5. **Give an unowned fact a home.** When the planner needs a fact
   for a page and no file supports it, it lists the fact under
   `## Unowned` in the documentation map, with the page that needs
   it. The writer leaves the fact out, and the run reports it.
   Nothing is invented to fill it. For a fact no file of the project
   owns yet (a prerequisite, how a tool is installed, the public home
   of the repository), the home is the section
   `## Pinned facts (not rendered)` of the project's readme recipe,
   whose skeleton is `templates/recipe-readme.md`. The README does not
   print these facts; the planner reads them there as an owner. Each
   is one bullet, dropped the day a file owns the fact.
   You should now see the fact gone from the Unowned list of the next
   run and present on the page that needed it.

## What you have afterwards

The owning file carries the change, and every page made from it is
regenerated in the same run. Pages whose inputs did not change are
kept as they were. Where a page wanted a reason that no input
records, the run lists the place. The page itself says "the reason
is not recorded".

## If something goes wrong

**The check fails.** After writing, the run checks every page with
`scripts/docs-check.py`. It refuses:

- an entry of the map (not marked `remove`) without its page, and a
  page in the documentation folder that the map does not name (the
  index `README.md` excepted);
- a relative link to a `.md` file that does not resolve;
- a long dash (em or en) in the prose of a page; a code span and a
  fenced block are exempt, since a literal is copied as its owner has
  it;
- a page that does not open with a front-matter;
- an instance fact (a value of one installation): a value of the
  instance file at the engine root, an e-mail address other than a
  placeholder at `example.*`, an absolute path of a machine (a drive
  letter, a user's home directory), and every `--fact` pattern given.

To change what the check refuses, change `scripts/docs-check.py`.
Every failure is printed with its file and line, so a false hit (a
common word that happens to be a value) can be seen. Then the rule is
adjusted, not the page.

**A page fails twice.** A page that fails the check is regenerated
once, with the failure named in its task. A page that fails twice is
reported and left out of the documentation. It is deleted and its
entry marked `remove` in the map, said aloud, never mended by hand.
Mend the owner and run again.

**A changed agent definition seems to have no effect.** The harness
(Claude Code, the program Claude runs in) loads an agent's definition
once per session (one continuous conversation with Claude). A change
to `.claude/agents/docs-planner.md` or `.claude/agents/docs-writer.md`
therefore reaches the agents only in a new session. The agents are
subagents: separate runs of Claude that see only their task. Within
the session that made the change, the run passes the changed rule in
the task and says so in its report. Start a new session to be sure.

**An input is missing.** An input the map names and the disk does
not have is reported by the state script and hashed as missing. The
page is regenerated, and its writer reports the gap.

**The run refuses to start.** For the engine, the command runs on
`main` only. A repository behind or diverged from its remote is
refused.

## A worked example

Say a how-to page of a project with the slug `<slug>` spells a
command with an argument the command no longer takes.

1. The page's front-matter lists among its `inputs` the command's
   skill, `.claude/skills/<command>/SKILL.md`.
2. You open that part of the skill and find the old argument still
   written there: the skill is the owner, and the mistake is its.
3. You correct the skill, as a change of the forge, and run:

   ```
   /document <slug>
   ```

4. The state script hashes the skill anew. Every page whose entry
   names that skill now has a hash that differs from its
   `inputs-hash` and is marked `regenerate`. Every other page is
   `keep`.
5. A writer remakes each regenerated page from its inputs, the
   corrected skill among them. The check passes, and the page spells
   the command as the skill now does.

The flow of the fix, in short:

```
page wrong
  -> front-matter `inputs` names the owner
  -> change the owner (not the page)
  -> /document
  -> state script: hash differs -> regenerate
  -> writer remakes the page -> check
```

## See also

- [Generate the documentation](../use/generate-the-documentation.md):
  running the command.
- [Documentation map](../reference/documentation-map.md): the fields
  of an entry and of a page's front-matter.
- [Make a change to the forge](how-a-change-is-made.md): the chain a
  change of the forge goes through.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
