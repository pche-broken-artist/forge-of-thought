---
generated: 2026-10-23
version: 5.33
made: derived
inputs-hash: 936622ceb3245650
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

A documentation page is a generated file: it is made by the
documentation command `/document` and is never edited by hand. This
page is for the extender who finds something wrong or missing on a
page, or wants a different set of pages, and needs to know which file
to change instead. It covers what a page says, the shape every page
has, which pages exist and what the check refuses. Every term of the
forge used here has one line in the [Glossary](../reference/glossary.md).

## When to use it

Use it when a page of the documentation says something you want
changed.
Use it when you want every page to have a different shape or a
different kind of content.
Use it when you want a page added, removed or written for another
reader.
Use it when the check refuses a page and you need to know why.

In every case the rule is the same.
What is wrong on a page is mended in the file that owns the matter.
The page is then regenerated from that file.
How a change of the forge is made, proved and recorded is described
in [Make a change to the forge](how-a-change-is-made.md).

## What you do

Mend the owning file, then run the documentation for the engine:

```
/document
```

For a project, name its slug:

```
/document <slug>
```

Running the command in full is described in
[Generate the documentation](../use/generate-the-documentation.md).

## What happens

1. **Find the owner.** Open the page and read its front-matter.
   Its `inputs` list names every file the page was made from, one
   per line. An input may be a part of a file, named after `#`: a
   section by its heading, or an item by its ID. The fields of the
   front-matter are listed in
   [Documentation map](../reference/documentation-map.md).
   You should now see the file, or the part of a file, that says
   what the page says.

2. **Choose what to change.** What you change depends on what you
   want different:
   - What one page says: change the owning file named in its
     `inputs`.
   - The shape every page has, or what kind of content a page of
     each kind carries: change the writer's definition
     `.claude/agents/docs-writer.md` or the documentation contract
     `.claude/skills/docs-contract/SKILL.md`. Both are hashed with
     the inputs of every page. A change to either regenerates every
     page made by the old rule.
   - Which pages exist, or which reader a page is for: change the
     planner's definition `.claude/agents/docs-planner.md`. The
     readers and the outline of five sections are set there and in
     a position of the forge's own intent. The documentation map
     (the file `docs-map.md` that lists one entry per page) is
     written by the planner from the target at every run. Its rules
     reach the pages through the entries it writes.
   - A fact a page needs and no file owns: give the fact a home in
     a file the planner reads (see below).

   You should now have the one file to change, and no page among
   them.

3. **Make the change.** Change the owning file through the chain a
   change of the forge goes through. You should now see your change
   in the owning file and nowhere in `docs/`.

4. **Regenerate.** Run `/document`. The run asks nothing. The
   planner writes the documentation map anew. The script
   `scripts/docs-state.py` then hashes every entry together with the
   content of its inputs and the two files of the generator. It
   compares the result with the `inputs-hash` each page carries in
   its front-matter. Each page gets one state:
   - `new`: no page at the path yet.
   - `regenerate`: the hash differs; an input or the entry changed.
   - `keep`: the hash is the same.

   A page is regenerated only when its inputs, its entry or the
   generating rule changed. An input named as a part is hashed as
   that part. A change elsewhere in the same file leaves the page as
   it is. You should now see your page counted under `regenerate`
   in the summary, and the pages you did not touch under `keep`.

5. **Check.** The run ends with `scripts/docs-check.py`. You should
   now see "no failure" in its result.

### A fact no file owns

A fact a page needs and no file supports is not guessed. The
planner lists it under `## Unowned` in the documentation map and in
its report. The writer leaves it out of the page. The fact waits
until the principal (the person whose thinking is forged, who has
the final word) gives it a home.

For a project fact such as a prerequisite, how a tool is installed
or the public home of the repository, the home is the section
`## Pinned facts (not rendered)` of the project's README recipe.
The skeleton of that recipe is `templates/recipe-readme.md`. Of the
section it says:

- The README does not print the section.
- The planner reads it as an owner.
- Each fact is one bullet.
- A bullet is dropped the day a file owns the fact.
- The section is omitted when the project has none.

### What the check refuses

`scripts/docs-check.py` verifies every page against the map and
against the rules of a page. It refuses:

- an entry of the map not in state `remove` that has no page;
- a page in the docs directory that the map does not name (the index
  `README.md` excepted);
- a relative link to a `.md` file that does not resolve;
- a long dash (em or en) in prose (a code span and a fenced block
  are exempt);
- a page that does not open with a front-matter;
- an instance fact.

An instance fact here is any of:

- a word of four letters or more from a value of `CLAUDE.local.md`
  at the engine root (the instance file of one installation),
  looked for outside URLs;
- an e-mail address other than a placeholder at `example.*`;
- an absolute path of a machine (a drive letter, or a user's home
  directory);
- a pattern given to the check with `--fact`.

The check mends nothing. It prints each failure with its file and
line. It exits with 1 when anything fails.

## What you have afterwards

The owning file carries the change. The pages made from it are
regenerated and carry a new `inputs-hash`. Every other page is kept
as it was. Nothing in `docs/` was written by hand.

## If something goes wrong

- **The run refuses to start.** The documentation runs on `main`
  only. It refuses a repository that is behind or diverged from its
  origin, and offers `/pull`.
- **A page fails the check.** It is regenerated once, with the
  failure named in its task. A page that fails twice is reported and
  left out of the documentation: it is deleted, its entry is marked
  `remove` in the map by hand, and this is said aloud. It is never
  mended by hand.
- **The check reports an instance fact that is only a common
  word.** The match is printed with its line. A false hit is seen
  there. The rule is adjusted, not the page.
- **An input is missing.** An input the map names and the disk does
  not have is reported as `missing input`. It is hashed as missing.
  The page is regenerated, and its writer reports the gap.
- **A change to an agent's definition has no effect.** Claude Code
  (the harness, that is the program Claude runs in) loads an
  agent's definition once per session (one sitting of Claude Code).
  An agent here is a subagent: a separate Claude that sees nothing
  of the conversation. A change to `.claude/agents/docs-planner.md`
  or `.claude/agents/docs-writer.md` reaches the agents only in a
  new session. Within the session that made the change, the changed
  rule is passed in the task, and the report says so.

## A worked example

An invented fix, traced through. Say a how-to page at
`docs/use/<job>.md` gives a wrong option for a command.

1. You open the page. Its front-matter lists
   `.claude/skills/<command>/SKILL.md` under `inputs`.
2. You find the wrong option in that skill and correct it there,
   as any change of the forge is made.
3. You run `/document`.
4. The state summary counts `docs/use/<job>.md` under
   `regenerate`: one of its inputs changed. Every page that does
   not name the skill among its inputs stays `keep`.
5. A writer remakes the page from the corrected skill.
6. The check prints "no failure".

Had you corrected the page alone, the skill would still carry the
wrong option. The page would be remade from it the next time the
skill changed.

## See also

- [Generate the documentation](../use/generate-the-documentation.md): running the command.
- [Documentation map](../reference/documentation-map.md): the fields of an entry and of a page's front-matter.
- [Make a change to the forge](how-a-change-is-made.md): the chain a change of the forge goes through.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.33 from the files the front-matter names; never edited by hand.
