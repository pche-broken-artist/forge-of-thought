---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 7490371474804de7
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

A documentation page is a generated file: it is made from the files
its front-matter names and is never edited by hand. This page is for
the extender who finds a page wrong, wants a page added or dropped,
or wants every page to take a different shape. It shows where each of
these changes is made and how the pages are then remade. Running the
command itself is described in
[Generate the documentation](../use/generate-the-documentation.md).

## When to use it

Use it when a page says something that is wrong or out of date.

Use it when a page is missing, or a page should no longer exist.

Use it when you want to change what every page looks like, or what
kind of content a page of each kind carries.

Use it when a fact a page needs has no file that owns it.

In every case the rule is the same. What is wrong on a page is mended
in the file that owns the matter, and the page is regenerated. The
reason a page is never edited by hand is not recorded beyond that
rule.

## What you do

1. Find the owner of what is wrong.
2. Change the owning file, as any change of the forge is made.
3. Run the documentation command:

```
/document
```

For a project in place of the engine, name its slug, for example
`/document my-project`.

The change to the owning file goes through the chain any change of
the forge goes through: see
[Make a change to the forge](how-a-change-is-made.md).

## What happens

1. **You find the owner.** Every page opens with a front-matter. Its
   `inputs` list names the files, or the parts of files, that the
   page was made from. A part is named after `#`: a section by its
   heading, or an item by its ID. The fields of the front-matter and
   of an entry of the documentation map are described in
   [Documentation map](../reference/documentation-map.md).
   Which owner to change depends on what you want to change:

   - **What a page says:** the input file, or the named part, that
     carries the matter.
   - **The shape every page has, or what kind of content a page of
     each kind carries:** the writer's definition
     (`.claude/agents/docs-writer.md`) and the documentation contract
     (`.claude/skills/docs-contract/SKILL.md`).
   - **Which pages exist, which reader a page is for, what a page is
     made from:** the planner's definition
     (`.claude/agents/docs-planner.md`), which holds the readers and
     the outline, and the target's own files, which the planner reads.
     What the documentation is and for whom is also a position of the
     forge's own intent.
   - **A fact a page needs and no file owns:** see step 5.

   You should now see one file, or one part of a file, that you will
   change.

2. **You change the owning file.** Change it and record the change as
   any change of the forge is recorded. Do not touch the page and do
   not touch the documentation map (the file `docs-map.md` that lists
   every page and what it is made from). The planner writes the map
   afresh from the target at every run, so the map is not where a
   page is changed.

   You should now see your change in the owning file and nothing
   changed under `docs/`.

3. **If you changed an agent's definition, you start a new session.**
   Claude Code (the harness, that is the program Claude runs in)
   loads an agent's definition once per session (one conversation
   with Claude, from its start to its end). A change to
   `docs-planner.md` or `docs-writer.md` reaches the agents only in a
   new session. If the command runs in the same session that made the
   change, it passes the changed rule in each writer's task and says
   so in its report.

   You should now see a fresh session, or a report that names the
   changed rule.

4. **You run `/document`.** The planner writes the map from the
   target. The script `scripts/docs-state.py` then computes, for every
   page, a hash of three things:

   - the page's entry in the map (its `state` line excepted);
   - the content of every input the entry names, a named part hashed
     as that part only;
   - the generator: the writer's definition and the documentation
     contract.

   The page carries in its front-matter the hash it was made from
   (`inputs-hash`). Where the two hashes differ, the page is
   `regenerate`; where they agree, it is `keep`; where no page exists,
   it is `new`. The state is computed, never judged. Only the pages
   whose inputs, entry or generating rule changed are remade. A change
   elsewhere in a file leaves a page as it is when the page names only
   a part of that file. A change to the writer's definition or the
   contract regenerates every page, so that no page stays made by the
   old rule. The planner's rules reach the pages through the entries
   it writes.

   You should now see the state summary, in the shape
   `entries N: new N, regenerate N, keep N; remove N; tasks written to ...`,
   with the page you meant to change among the regenerated ones.

5. **A fact with no owner is reported, not invented.** Where a page
   needs a fact that no file supports, the planner lists it under
   `## Unowned` in the map, with the page that needs it. The writer
   leaves the fact out, and the command's report lists it. The fact
   waits for the principal (the person whose thinking is forged and
   who has the final word on content) to give it a home. One home is
   the section "Pinned facts (not rendered)" of the project's readme
   recipe, made from the skeleton `templates/recipe-readme.md`:

   - it is optional and is left out when the project has no such
     facts;
   - it holds facts no file of the project owns yet, such as
     prerequisites, how a tool is installed, or the public home of the
     repository;
   - it holds one bullet per fact;
   - the README does not print it, but the planner reads it as an
     owner;
   - a fact is dropped from it the day a file owns the fact.

   You should now see the fact gone from the Unowned list at the next
   run, and on the page that needed it.

6. **The pages are checked.** After the pages and the index are
   written, `scripts/docs-check.py` checks them against the map and
   the rules of a page. It refuses:

   - an entry of the map not marked `remove` that has no page;
   - a page in the documentation directory that the map does not name
     (the index `README.md` excepted);
   - a relative link to a `.md` file that does not resolve;
   - a long dash (em or en) in prose, code spans and fenced blocks
     exempt;
   - a page that does not open with a front-matter;
   - an instance fact: a value of the instance file of the
     installation, an e-mail address other than a placeholder at
     `example.*`, an absolute path of a machine, or any pattern given
     to it with `--fact`.

   The check mends nothing. A page that fails is regenerated once with
   the failure named in its task.

   You should now see `N files checked, no failure`.

## What you have afterwards

The owning file carries the change, recorded as any change. The pages
made from it are regenerated and every other page is kept as it was.
The index is derived again from the map, and the owning project's
ledger (the state report made from the documents at read time) is
remade from the index's provenance.

## If something goes wrong

- **The command refuses to run.** It runs on `main` only, and refuses
  a repository that is behind or diverged from its origin. Bring the
  repository up to date first.
- **The page you changed is listed as `keep`.** Its hash did not
  change: the file you changed is not among its inputs, or the change
  fell outside the part the page names. Look again at the page's
  `inputs`.
- **The summary prints `missing input: ... (named by ...)`.** The map
  names a file or a part the disk does not have. The page is
  regenerated and its writer reports the gap.
- **A page fails the check twice.** It is reported and left out of the
  documentation: the page is deleted and its entry marked `remove` in
  the map by hand, said aloud. It is never mended by hand. Mend the
  owner of what failed and run the command again.
- **A false hit of the instance-fact rule.** A match is reported with
  its line. Where a common word happens to be a value of the instance
  file, the rule is adjusted, not the page.
- **A changed agent rule did not show.** The agent's definition was
  loaded before the change. Start a new session (step 3).

## A worked example

An invented fix, traced through. A page under `docs/use/<job>.md`
tells you to type an option that the command no longer takes.

1. You open the page. Its front-matter lists
   `.claude/skills/<command>/SKILL.md` among its inputs.
2. You correct the option in that skill, and record the change as any
   change of the forge.
3. You run `/document`. The state script finds the page's hash
   changed, because one of its inputs changed. It reports that page,
   and any other page that names the same file or part, as
   `regenerate`, and every other page as `keep`.
4. A writer remakes the page from the corrected skill. The index is
   derived again, and the check prints `N files checked, no failure`.
5. The page now gives the right option, and no page was touched by
   hand.

Had you instead changed a rule in the writer's definition, step 3
would have reported every page as `regenerate`, since the generator
is hashed with every page's inputs.

## See also

- [Generate the documentation](../use/generate-the-documentation.md):
  running the command.
- [Documentation map](../reference/documentation-map.md): the fields
  of an entry and of a page's front-matter.
- [Make a change to the forge](how-a-change-is-made.md): the chain a
  change of the forge goes through.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
