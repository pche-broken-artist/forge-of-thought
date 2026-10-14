---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: faa7db4965842c23
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

A page of the documentation is an output: it is generated from the
files that own its matter, and it is never edited by hand. This page
is for the extender who finds a page saying something wrong, who
wants a page added or dropped, who wants the shape of every page
changed, or who is stopped by the check that runs over the pages. In
each case it says which file you change and how the page is remade.
Anything you write into a page yourself is overwritten by the next
run of `/document`.

## Before you start

The fix goes into the file that owns the matter, and the page is
regenerated from it. Where that file is a file of the forge (a
skill, an agent, a template, a script), the change is made, proved,
recorded and released as any change of the forge:
[Make a change to the forge](how-a-change-is-made.md) is the chain
it goes through. How the run itself is started and what it reports
is on [Generate the documentation](../use/generate-the-documentation.md).
The fields of an entry of the map and of a page's front-matter are
on [Documentation map](../reference/documentation-map.md). Every
term of the forge is in the [Glossary](../reference/glossary.md).

Two words this page uses. The "owning project" is the project whose
ledger the documentation map lies beside: for the engine it is
`projects/forge`, for a project it is the project itself. The
"ledger" is that project's single source of truth for state.

## The files

| Path | What it is | What a change to it does |
|---|---|---|
| `docs/<section>/<page>.md` | a page; its front-matter lists the `inputs` it was made from | nothing lasting: the next run overwrites it |
| `docs-map.md`, beside the owning project's ledger | the documentation map, one entry per page, written by the planner at every run | nothing lasting: the planner rewrites it at every run |
| `docs/README.md` | the index, derived by a script from the `line` of each entry and the `## Paths` section of the map | nothing lasting: the next run derives it again |
| the files a page's `inputs` name | the owners of the page's matter, whole files or parts named after `#` | every page naming the file or the part is remade |
| `.claude/agents/docs-writer.md` | the definition of the writer: the shape of a page and the outline of each kind | every page is remade |
| `.claude/skills/docs-contract/SKILL.md` | the contract of the two agents: what must never reach a page, the voice and the sentence | every page is remade |
| `.claude/agents/docs-planner.md` | the definition of the planner: the readers, the outline, what it reads, the rules of an entry | the map changes at the next run; a page whose entry changed is remade |
| the intent of the owning project | the reasons the pages give, and the position that says what the documentation is and for whom | the pages naming the changed item are remade |
| `recipes/readme.md`, section "Pinned facts (not rendered)" | the home of a fact of the project that no file owns yet | the planner reads it as an owner at the next run |
| `scripts/docs-state.py` | computes the state of every page from its inputs and writes the writers' tasks | a change of the forge |
| `scripts/docs-check.py` | the check of the pages | a change of the forge; what it refuses changes |
| `CLAUDE.local.md` at the engine root | the instance facts; its values are what the check refuses on a page | the check looks for the new values; the file never reaches a page |

The planner and the writers are subagents: agents Claude launches
with a task of their own, which see nothing of the conversation.

## Steps

### To change what a page says

1. Open the page and read its front-matter. The `inputs` list names
   every file, or part of a file after `#`, the page was made from.
   The owner of the wrong sentence is among them. Where the wording
   is wrong, the owner is the skill, agent, template or script that
   states it. Where the reason is wrong or missing, the owner is the
   intent of the owning project: a reason a page wants and no file
   records enters the intent in a round of its own, on the word of
   the principal (the person whose thinking the forge works on).
   You should now see one file, or one part of a file, to change.
2. Mend the matter in that file. Leave the page as it is.
   You should now see the owner saying what the page is to say.
3. Run `/document` for the engine, or `/document <slug>` for a
   project. The run hashes, for every entry of the map, the text of
   the entry, the two files the pages are made by and the content of
   every input; a part named after `#` is hashed as that part. A page
   whose hash differs from the `inputs-hash` in its front-matter is
   remade; a page whose hash is the same is kept. So the run remakes
   only the pages whose inputs, entry or generating rule changed, and
   a change elsewhere in a file leaves the pages naming only a part
   of it as they are. The state is computed, never judged.
   You should now see the run's report naming your page among the
   regenerated and the rest as kept.
4. Where the owner you mended is not among the page's inputs, do
   not add it to the map by hand: the map is written by the planner
   from the target at every run. The planner names the inputs of an
   entry from what it reads on disk, and the entry's text is hashed
   with the inputs, so a page whose entry gained an input is remade.
   You should now see the new input in the page's front-matter after
   the run.

### To change the shape every page has

1. Change `.claude/agents/docs-writer.md` for the shape of a page and
   the outline of each kind, or `.claude/skills/docs-contract/SKILL.md`
   for what must never reach a page, the voice and the sentence.
   Both are hashed with the inputs of every page.
   You should now see the rule written where it holds.
2. Start a new session before the run. The harness (the program that
   runs Claude and launches its agents) loads an agent's definition
   once per session: a change to `docs-planner.md` or
   `docs-writer.md` reaches the agents only in a new session. Within
   the session that changed one, the command passes the changed rule
   in the task and says so in its report.
   You should now see a fresh session with the new definition loaded.
3. Run `/document`. Every page is remade, because the files the pages
   are made by changed.
   You should now see every page among the regenerated.

### To change which pages exist, or who reads them

1. A page exists because the target has material for it. The planner
   reads the target on disk at every run and writes one entry per
   page; a section or a page with no material is left out, never
   left empty; a page that lost its material is marked `remove` and
   the run deletes it. To add a page, give the target the material in
   the file that owns it; to drop a page, take the material away. An
   entry written into the map by hand does not survive the next run.
   You should now see the material in its owner, or gone from it.
2. The readers (the user, the extender, the evaluator), the path each
   reads, the five sections and the kind of content each kind of page
   carries are defined in `.claude/agents/docs-planner.md` and in a
   position of the intent of the forge's own project. To change them,
   change the planner's definition and the position; a new session is
   needed, as above. The planner's rules reach the pages through the
   entries it writes: a page whose entry changed is remade, so the
   planner's definition is not hashed with the inputs.
   You should now see the readers or the outline changed where they
   are defined.
3. The index is not a page: a script derives it from the `line` of
   each entry and the `## Paths` section of the map. It is never
   edited.
   You should now see, after the run, the index listing the pages the
   map has.

### To give a home to a fact no file owns

1. Read the run's report. Every fact a page needs and no file
   supports is listed under Unowned, with the page that needs it. The
   writer left it out; nothing is invented to fill it. Every fact in
   Unowned waits for the principal to give it a home.
   You should now see the fact and the page that wants it.
2. Give the fact a home. Where a file of the project should own it,
   write it there. Where no file does yet, the home is the section
   "Pinned facts (not rendered)" of the owning project's
   `recipes/readme.md`: one bullet per fact, such as a prerequisite,
   how a tool is installed, or the public home of the repository. The
   README does not print the section; the planner reads it as an
   owner. The bullet is dropped the day a file owns the fact, and the
   section is omitted when the project has none.
   You should now see the fact as one bullet in that section, or in
   its owner.
3. Run `/document` again. The planner names the owner in the entry,
   the entry changes, and the page is remade with the fact.
   You should now see the fact on the page and the Unowned list
   shorter.

## Prove it

For the engine:

```
/document
python scripts/docs-check.py projects/forge/docs-map.md docs
```

For a project:

```
/document <slug>
python scripts/docs-check.py projects/<slug>/docs-map.md projects/<slug>/docs
```

The run itself ends with the check; running it by hand after a
change shows the same result. The check prints every failure with
its file and line, and exits with 0 when everything holds and 1 when
anything fails. It refuses:

- a page missing: an entry of the map not in state `remove` without
  its page (`missing page: docs/...`);
- a page the map does not name, the index `README.md` excepted
  (`page not in the map: ...`);
- a relative link to a `.md` file that does not resolve
  (`broken link ...`);
- a long dash, em or en, in the prose of a page (`long dash`); a
  code span and a fenced block are exempt, since a literal is copied
  as its owner has it;
- a page that does not open with a front-matter (`no front-matter`);
- an instance fact (`instance fact (...)`): a value of
  `CLAUDE.local.md` at the engine root, every word of four letters or
  more in a value, looked for outside URLs; an e-mail address other
  than a placeholder at `example.*`; an absolute path of a machine, a
  drive letter or a user's home directory; and every pattern given
  with `--fact PATTERN`, which may be repeated.

The check mends nothing. A page that fails is regenerated once by
the run, with the failure named in the writer's task. A page that
fails twice is reported and left out of the documentation: deleted,
its entry marked `remove` in the map by hand, said aloud, never
mended by hand. A match is reported with its line, so a false hit (a
common word that happens to be a value of `CLAUDE.local.md`) is seen
and the rule in the check script, not the page, is adjusted; that is
a change of the forge like any other.

Where the fix was to an owner and the page still fails, the page is
not the place to look: a page says only what its inputs support, so
the owner, the entry or the generating rule is where the failure
comes from.

## Record and release

A change to a file of the forge is recorded and released as any
change: [Make a change to the forge](how-a-change-is-made.md). The
run records the index as one row in the Renders table of the owning
project's ledger. What a release does with the documentation is
defined in `.claude/skills/release/SKILL.md`.

## A worked example

Suppose the report of a run of `/document` for the project `<slug>`
lists under Unowned one fact: the public home of the project's
repository, wanted by a page of `start/`. The page was written
without it, and nothing was invented in its place.

You look for a file of the project that owns the fact and find none.
So you open `projects/<slug>/recipes/readme.md`, go to the section
"Pinned facts (not rendered)" and add one bullet with the public
home of the repository. The README will not print it; it is a fact
held for the documentation until a file owns it.

You run `/document <slug>`. The planner reads the recipe as an owner
and names its section among the inputs of the entry for the page of
`start/`. The entry's text changed, so the hash of that page differs
from the `inputs-hash` in its front-matter: the run remakes that one
page and keeps every other. The report names it among the
regenerated and no longer lists the fact under Unowned.

The check runs over the pages. The address stands inside a URL, and
the values of `CLAUDE.local.md` are not looked for inside a URL, so
the page passes; which addresses a page may carry is said by the
entry's `must-not`. The check prints the number of files checked and
`no failure`, and exits with 0.

The change is a change of the project, not of the forge: the recipe
is the project's own file, and it is saved with the project. Had the
fix been to a skill, an agent, a template or a script of the engine,
it would be recorded and released as any change of the forge.

## See also

- [Generate the documentation](../use/generate-the-documentation.md): running the command.
- [Documentation map](../reference/documentation-map.md): the fields of an entry and of a page's front-matter.
- [Make a change to the forge](how-a-change-is-made.md): the chain a change of the forge goes through.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
