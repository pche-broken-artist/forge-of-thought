---
generated: 2026-10-09
made: derived
inputs-hash: 497ced961a50f0f3
inputs:
  - .claude/skills/document/SKILL.md
  - .claude/agents/docs-planner.md
  - .claude/agents/docs-writer.md
  - scripts/docs-check.py
  - projects/forge/recipes/readme.md
---

# Change a documentation page

This page is for the extender who finds something wrong, missing or
out of date on a page of the generated documentation and wants to
put it right. It was put together from the documentation command
(`.claude/skills/document/SKILL.md`), the definitions of its two
agents (`.claude/agents/docs-planner.md`,
`.claude/agents/docs-writer.md`), the help header of the check
script (`scripts/docs-check.py`) and the section "Pinned facts (not
rendered)" of the readme recipe of `projects/forge`
(`projects/forge/recipes/readme.md`). It joins them into the order
of one change to a page.

## A page is never edited by hand

Nothing under `docs/` is composed by hand. Every page is made by a
writer from the files its entry in the map names, and the index is
derived from the map by a script. What is wrong on a page is mended
in the file that owns the matter, and the page is regenerated. An
edit made directly to a page is lost at the next run, because the
run remakes a page from its inputs whenever they or its entry
changed.

So a change to the documentation is always a change to something
else: to a file of the engine that the page restates, or to the map
that says which pages exist.

## Step 1: find the owner

Open the page and read its front-matter. It carries two things you
need:

- `inputs`: the files the page was made from, one per line, as
  paths relative to the target's root.
- `made`: whether the page is `mirrored` or `derived`.

A mirrored page restates what its inputs say, in the reader's
words: the wrong sentence on the page comes from one of the listed
inputs, and that input is the file to change.

A derived page puts together what no single file says, from
evidence in several. Its opening paragraph says which files it was
put together from, and the entry's `evidence` in the map says by
what reasoning. Find the file among them that carries the fact in
question.

The owner is, as a rule, the operating layer: a skill, an artefact
definition, a template, an agent, the help header of a script. A
reason, as opposed to a rule, comes from the forge intent; where
the operating layer and the intent differ, the page takes the
operating layer's wording and the intent's reason. The renders and
the README are never owners: the planner does not read them as
such.

## Step 2: change the owning file and regenerate

Change the owning file, as any change of that file is made. Then
run `/document`. The run asks no question and does this:

1. The planner reads the target on disk and writes the map anew.
2. A script computes the state of every page: it hashes the
   entry's inputs and the entry itself, compares the result with
   the `inputs-hash` the existing page carries, and marks the page
   `new`, `regenerate` or `keep`. It also lists the pages in `docs/`
   that no entry names, to be removed. The state is the script's,
   never a judgement.
3. For every page to make, the command launches one writer and
   hands it its task as a file, which the writer reads first. The
   writer reads exactly the inputs the entry names, from disk, and
   writes the page with the `inputs-hash` its task gives it. A page
   whose inputs and entry did not change is kept as it is.
4. A script derives the index from the map, and the check runs
   over every page.

You see, in the report, which pages were new, regenerated, kept
and removed; what the writers left out because the inputs did not
support it; and the check's result.

Because a page is remade only when its inputs or its entry
changed, a change to one skill regenerates the pages that name that
skill as an input and leaves the rest untouched.

## To change which pages exist, or what a page covers

The map is not a file you edit for that. The planner writes it from
the target on disk at every run, and what the planner plans is
fixed by two things: its own definition, which names the three
readers (the user, the extender, the evaluator) and the five
sections of the outline (`start/`, `use/`, `about/`, `extend/`,
`reference/`), and a position of the forge intent that says what the
documentation is and for whom.

So a change to which pages exist, to what a page covers or to who
reads it goes through the chain like any change of the forge: the
intent first where a reason changes, then the planner's definition
where the outline or the readers change, and then a run of
`/document`. The one hand-made mark in the map is the command's own:
an entry of a page that failed the check twice is marked `remove`
by hand and said aloud.

## A fact no file owns

A writer never invents. A fact a page needs that no file supports
is left out of the page and reported: the planner lists it under
`## Unowned` in the map, with the page that needs it, and the
command's report carries the list. Every fact there waits for the
owner of the documentation to give it a home; nothing is written to
fill it.

Today one home exists for facts of this kind: the section "Pinned
facts (not rendered)" of the readme recipe of `projects/forge`. It
holds the install facts (what must be on the machine, how Claude
Code is installed, what each script needs) that no engine file
carries. The README does not print them; the planner reads them
there as an owner, and the pages of the start section are where
they reach the reader. When such a fact changes, change it there
and regenerate.

## What the check refuses

After the pages are written, `scripts/docs-check.py` verifies them
against the map and the rules of a page, and prints every failure
with its file and line. It refuses:

- a page of the map that is missing, or a page in `docs/` that the
  map does not name (the index excepted);
- a relative link to a Markdown file that does not resolve;
- a long dash, em or en, anywhere on a page;
- a page that does not open with a front-matter;
- an instance fact: a value of `CLAUDE.local.md`, any e-mail
  address but a placeholder, an absolute path of a machine (a drive
  letter, a user's home directory), and any further pattern given to
  the check on its command line.

The check mends nothing. A page that fails is regenerated once with
the failure named in its task. A page that fails twice is reported
and left out of the documentation: deleted, its entry marked
`remove` in the map, said aloud, never mended by hand. A false hit,
a common word that happens to be an instance value, is seen in the
report with its line, and the rule is adjusted, not the page.

## A change to the planner or the writer

The definitions of the two agents are loaded once per session: a
change to `docs-planner.md` or `docs-writer.md` reaches the agents
only in a new session. Within the session that changed one, the
changed rule is passed in the agents' task and the report says so.
To see such a change take effect in full, start a new session and
run `/document` there.

## See also

- [Generate the documentation](../use/generate-the-documentation.md): running the command.
- [Documentation map](../reference/documentation-map.md): the fields of an entry and of a page's front-matter.
- [Make a change to the forge](how-a-change-is-made.md): the chain a change of the forge goes through.
