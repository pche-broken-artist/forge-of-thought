---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 11132e02b5be4791
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

A documentation page is a generated file, and you never edit it by
hand. This page is for the extender who finds a page wrong, wants a
page that does not exist, or wants to change what the check refuses.
It shows where each kind of change is made and how the page is then
remade.

## When to use it

Use it when a page says something wrong or out of date. Use it when
every page should take a different shape. Use it when a page is
missing, should go, or is meant for a different reader. Use it when
the check refuses a page and you want to know why.

In every case the rule is the same. What is wrong is mended in the
file that owns the matter. The page is then regenerated.

## What you do

Mend the owning file, then run the documentation command for the
target. For the engine, bare:

```
/document
```

For a project, with its slug:

```
/document <slug>
```

How the command runs in full is on
[Generate the documentation](../use/generate-the-documentation.md).

## What happens

1. **Find the owner.** Open the page and read its front-matter. Its
   `inputs` list names every file, or part of a file, the page was
   made from. A part is named after `#`: a section by its heading,
   or an item by its ID. The fields of the front-matter are listed on
   [Documentation map](../reference/documentation-map.md).
   You should now see the file and the section that carry the wrong
   sentence.

2. **Choose where the change goes.** The kind of change decides the
   file:
   - What one page says: the owning file from the page's `inputs`.
   - The shape every page has: the writer's definition,
     `.claude/agents/docs-writer.md`.
   - What kind of content a how-to, an explanation or a reference
     carries, and what a mirrored and a derived page are: the
     documentation contract, `.claude/skills/docs-contract/SKILL.md`,
     section "The kinds of a page".
   - Which pages exist, which section holds them, and which reader
     each is for: the planner's definition,
     `.claude/agents/docs-planner.md`, under "The readers" and "The
     outline". What the documentation is and for whom is also a
     position of the forge's own intent.
   - What the check refuses: the check script, `scripts/docs-check.py`.

   You should now know the one file you will change.

3. **Make the change as any change of the forge.** The change is
   recorded and released like every other change. The chain it goes
   through is on [Make a change to the forge](how-a-change-is-made.md).
   You should now see the owning file changed and its record written.

4. **Run `/document`.** The planner (a subagent, that is a separate
   Claude agent that sees nothing of your conversation) reads the
   target on disk and writes the documentation map afresh at every
   run. The documentation map is the file of one entry per page that
   the pages are made from, `docs-map.md` beside the owning
   project's ledger (the ledger is the file that holds the state of a
   project). Then `scripts/docs-state.py` computes the state of each
   page. It hashes the entry's text together with the content of
   every input the entry names, a part being hashed as that part. It
   also hashes the writer's definition and the contract with the
   inputs. The result is compared with the `inputs-hash` the page
   carries. You should now see a summary that names each page as
   `new`, `regenerate`, `keep` or `remove`.

5. **The pages are remade.** Only the pages marked `new` or
   `regenerate` are written again, one writer each. A page whose
   inputs did not change is not regenerated. You should now see the
   changed page carry your correction, and the pages you did not
   touch left as they were.

6. **The check runs.** `scripts/docs-check.py` verifies the pages
   against the map and against the rules of a page. You should now
   see the check pass, or a failure printed with its file and line.

Which change reaches which pages:

- A change to one input regenerates the pages that name that input.
  A change elsewhere in a file leaves a page that names only one part
  of it as it is.
- A change to the writer's definition or to the contract regenerates
  every page, because a page made by the old rule is stale.
- A change to the planner's definition reaches the pages through the
  entries the planner writes. A page is regenerated where its entry
  changed.

## What you have afterwards

The page says what its owner now says. Its front-matter carries the
new `inputs-hash`. Nothing on the page was touched by hand, so the
next run keeps it until an owner changes again.

## If something goes wrong

**A fact has no owner.** A page may need a fact that no file
supports. The planner then lists it under `## Unowned` in the
documentation map, and the writer leaves it out. The command's report
names it, and it waits for the principal (the person whose thinking
is forged, with the final word on content) to give it a home. Nothing
is invented to fill it. For a fact of a project that no file owns
yet, the home is the section "Pinned facts (not rendered)" of the
project's readme recipe, made from `templates/recipe-readme.md`. The
README does not print these facts. The planner reads them there as an
owner. Prerequisites, how a tool is installed and the public home of
the repository are the kinds of fact the section holds. A fact is
dropped from it the day a file owns it.

**A writer wanted a reason and none is recorded.** The page says "the
reason is not recorded" and the command's report lists the place. The
reason enters the intent in its own round, where the principal wants
one.

**The check refuses a page.** It refuses a page for these causes:

- An entry of the map that is not `remove` has no page, or a page
  lies in the documentation that the map does not name. The index
  `README.md` is excepted.
- A relative link to a `.md` file does not resolve.
- A long dash (em or en) stands in the prose. A code span and a
  fenced block are exempt.
- The page does not open with a front-matter.
- The page carries an instance fact. The check looks for the values
  of `CLAUDE.local.md` at the engine root, every word of four letters
  or more, outside URLs. It also looks for an e-mail address other
  than a placeholder at `example.*`, an absolute path of a machine
  (a drive letter or a user's home directory), and every pattern
  given with `--fact`.

The check mends nothing. A page that fails is regenerated once, with
the failure named in its task. A page that fails twice is reported
and left out of the documentation: it is deleted, its entry is marked
`remove` in the map by hand, and this is said aloud. It is never
mended by hand. A match is reported with its line. When the hit is
false (a common word that happens to be a value), the rule is
adjusted, not the page.

**The command refuses to run.** It runs on `main` only. It refuses a
repository that is behind or diverged from its origin. The way out it
offers is `/pull`.

**A change to an agent's definition seems to have no effect.** Claude
Code loads an agent's definition once per session (one conversation
in Claude Code, from its start to its close). A change to
`.claude/agents/docs-planner.md` or `.claude/agents/docs-writer.md`
reaches the agents only in a new session. Within the session that
made the change, the command passes the changed rule in the task and
says so in its report.

## A worked example

Suppose a page of the engine's documentation, `docs/use/<job>.md`,
says that a command takes an option it does not take.

1. You open the page. Its front-matter names
   `.claude/skills/<command>/SKILL.md` among its `inputs`.
2. You read that skill and find the wrong sentence there: the page
   repeated it faithfully.
3. You mend the sentence in the skill, as a change of the forge, with
   its record.
4. You run `/document`. The state script finds that the skill's
   content changed. It marks every page that names that skill as
   `regenerate`, and the rest as `keep`.
5. One writer remakes `docs/use/<job>.md` from the mended skill. The
   check passes.

The page now agrees with its owner, and neither the page nor the map
was edited by hand.

## See also

- [Generate the documentation](../use/generate-the-documentation.md):
  running the command.
- [Documentation map](../reference/documentation-map.md): the fields
  of an entry and of a page's front-matter.
- [Make a change to the forge](how-a-change-is-made.md): the chain a
  change of the forge goes through.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
