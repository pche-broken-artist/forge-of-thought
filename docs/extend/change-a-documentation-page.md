---
generated: 2026-10-10
made: derived
inputs-hash: e85e5506ca76aada
inputs:
  - .claude/skills/document/SKILL.md
  - .claude/skills/docs-contract/SKILL.md
  - .claude/agents/docs-planner.md
  - .claude/agents/docs-writer.md
  - scripts/docs-check.py
  - templates/recipe-readme.md
  - projects/forge/recipes/readme.md
---

# Change a documentation page

This page is for the extender who finds something wrong, missing or
out of date on a page of the documentation and wants it mended. It
was put together from the documentation command
(`.claude/skills/document/SKILL.md`), the contract its two agents
share (`.claude/skills/docs-contract/SKILL.md`), the definitions of
the planner and the writer (`.claude/agents/docs-planner.md`,
`.claude/agents/docs-writer.md`), the help header of the check
script (`scripts/docs-check.py`), the readme skeleton
(`templates/recipe-readme.md`) and the section "Pinned facts (not
rendered)" of the readme recipe of `projects/forge`
(`projects/forge/recipes/readme.md`).

## The one rule

A page is never edited by hand. Every page under `docs/` is
generated in one run of `/document`: the planner writes the map, the
scripts compute which pages are stale, one writer makes each stale
page, and the scripts derive the index and check the pages. The run
itself never touches a page by hand, and neither do you. What is
wrong on a page is mended in the file that owns the matter, and the
page is regenerated.

## Find the owner

1. Open the page and read its front-matter. It carries the date the
   page was generated, `made: mirrored` or `made: derived`, a hash
   of its inputs, and the list `inputs`: the files, as paths from
   the root of the target, that the writer read to make the page and
   nothing else.
2. Tell the two kinds apart. A mirrored page restates what its
   inputs say, in the reader's words: what is wrong on it is wrong
   in one of those files. A derived page puts together what no
   single file says, from evidence in several, and its opening
   paragraph names the files it was put together from.
3. Find in those files the sentence or rule the page rests on. The
   owner is a skill (a command), the definition of an artefact, a
   template, an agent, or the help header of a script. A reason the
   page gives, the why behind a rule, comes from the intent of
   `projects/forge`.

Nothing else is an owner. The renders and the README of the target
are outputs: the planner never reads them, so a fact changed there
reaches no page.

## Change what a page says

1. Change the owning file: the wording where the operating layer
   carries it (a skill, a definition, a template, an agent, a
   script's header), the reason where the forge intent carries it.
   Where the two differ, a page takes the operating layer's wording
   and the intent's reason.
2. Run `/document` (for a project, `/document <slug>`). The run asks
   nothing. It plans the map anew, recomputes the state of every
   page from the content of its inputs, and remakes only the pages
   whose inputs or whose entry changed; every other page is kept as
   it is. Each remade page is made by a writer of its own, handed a
   task file that it reads first: the page's entry, the path to
   write, the date and the hash the page is to carry.
3. Read the report at the end of the run: pages new, regenerated,
   kept and removed; the facts no file owns; what the writers left
   out because the inputs did not support it; the result of the
   check. If your change did not reach the page, the file you
   changed is not among the page's inputs: look at the front-matter
   again.

Inputs are whole files and the state is computed from their content,
so a change to any file a page lists as an input regenerates that
page, whether or not the changed sentence appears on it.

## Change which pages exist, what a page covers or who reads it

The map, `docs-map.md` beside the owning project's ledger, is not a
file to edit either: the planner writes it from the target on disk
at every run, and whatever was typed into it is written over. What
the planner plans is set by two things: its own definition, which
gives the three readers (the user, the extender, the evaluator), the
five sections of the outline and what it reads; and a position of
the forge intent, which says what the documentation is and for whom.
A change of that kind, a new section, a page cut in two, a different
reader for a page, is a change of the forge: it goes through the
chain like any other, the reason into the intent first, then the
planner's definition, then a run of `/document`.

A page that has lost its material disappears on its own: the planner
marks its entry `remove`, and the run deletes the page and says so.

## What never reaches a page

The planner and the writer share one contract. Whatever change you
make to an owning file, these never appear on a page or in the map:

- the name of a person, a company, a host, an account, an e-mail
  address, or any identifier of an instance; an example uses a
  placeholder slug in place of a real one;
- an address, except the public home of the target where the
  target's own documents name it as such;
- a document of any project but the one that owns the documentation;
- text of a skill or an agent copied as an instruction to Claude: a
  page says what a command does for the person, in the person's
  terms;
- an ID of the chain: a page gives the reason, not the ID;
- a long dash: a colon, a full stop or a spaced hyphen stands where
  one would.

A sentence that would need one of these to be said on a page is not
carried onto the page.

## A fact no file owns

A writer invents nothing: a fact a page needs and no input supports
is left out and reported. The planner lists every such fact under
"Unowned" in the map and in its report, with the page that needs it,
and the fact stays off the page until it has a home.

The home for such a fact is the section "Pinned facts (not
rendered)" that the readme skeleton gives every project's readme
recipe: optional, one bullet per fact, for facts of the project that
no file owns yet, such as prerequisites, how a tool is installed or
the public home of the repository. The README does not print them;
the planner reads them there as an owner. A pinned fact is dropped
the day a file of the project owns it. The readme recipe of
`projects/forge` fills the section today with the install facts of
the engine (what must be on the machine, how Claude Code and the
tools the scripts need are installed) and the engine's public home.

So, to give a page a fact that no file owns, add a bullet to the
pinned facts and run `/document`; once a file comes to own the fact,
move it there and remove the bullet.

## What the check refuses

The last step of every run is a mechanical check of the pages
against the map and against the rules of a page. It prints every
failure with its file and line and refuses:

- an entry of the map without its page, and a page under `docs/`
  that the map does not name (the index excepted): a page added by
  hand has no entry and fails here;
- a relative link to a Markdown file that does not resolve;
- a long dash, em or en, anywhere;
- a page that does not open with a front-matter;
- an instance fact: a value of `CLAUDE.local.md` at the engine root,
  looked for outside URLs; an e-mail address other than a
  placeholder at `example.*`; an absolute path of a machine, a drive
  letter or a user's home directory.

The check mends nothing. A page that fails is regenerated once, with
the failure named in the writer's task; a page that fails twice is
left out of the documentation and said in the report, never mended
by hand. A false hit, a common word that happens to be a value of
`CLAUDE.local.md`, is seen in the printed line, and the rule, not
the page, is adjusted.

## Changing the planner or the writer

The definitions of the two agents are loaded once per session. A
change to `.claude/agents/docs-planner.md` or
`.claude/agents/docs-writer.md` reaches the agents only in a new
session: start one before running `/document` to see its effect.
Within the session that made the change, the command passes the
changed rule in the agents' task and says so in its report.

## See also

- [Generate the documentation](../use/generate-the-documentation.md):
  running the command.
- [Documentation map](../reference/documentation-map.md): the fields
  of an entry and of a page's front-matter.
- [Make a change to the forge](how-a-change-is-made.md): the chain a
  change of the forge goes through.
