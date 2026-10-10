---
generated: 2026-10-10
made: derived
inputs-hash: 666fa98860034429
inputs:
  - CLAUDE.md
  - templates/ledger.md
  - templates/decisions.md
  - projects/forge/10-intent.md
---

# About documents and records

This page explains what the files of a project are, how they are
grouped by kind and why each group behaves as it does: which files
are rewritten, which only grow and which are never touched again. It
is for anyone who uses the forge, extends it or judges it, and it was
put together from `CLAUDE.md`, the ledger and decisions skeletons in
`templates/` and the forge's own intent; the table of kinds itself
stands on the reference page linked at the end.

## Document and artefact

"Document" is the word for every file of a project. "Artefact" is
reserved for the documents of the chain: the ones the principal
composes with Claude, the reviewers read and the renders are
generated from. The boundary is authorship: an artefact is composed,
a render is generated from artefacts. An article the principal
writes is a layer of the chain; its translation is a render.

Every document has exactly one kind, and the kind says four things
about it: what it is, who writes it, whether it is versioned, and how
it behaves over time. Behaviour is the point of the grouping. A file
that may be rewritten at will, a file that may only be appended to
and a file that must never change are three different promises, and
the kind tells the reader which promise a file carries before he
opens it.

## The five groups

**Artefacts.** The documents of the chain: the brief, the intent and
whatever layers the project takes below it. Which artefacts exist is
the listing of the forge's state definitions, one per artefact; they
are listed nowhere else. Artefacts are versioned and rewritten
freely between approvals: an assignment is not frozen in any sense
the file would show, and what the recipients hold is a version
reached by a link into git, not a locked file.

**Records.** What happened, kept so that it can be read back. The
history companion of every versioned document records what changed
and why; the decisions file records the principal's decisions with
their reasons. Both are append-only: a record, once written, is
never edited, and a later decision supersedes an earlier one by a
new record that names it. Reviews and challenges, one dated reviewer
run each, are immutable from creation. The forge writes the history
and the decisions; a reviewer agent writes its own report.

**State.** Where things stand now. The ledger is the single source of
truth for state; the resource indexes catalogue what lies in
`sources/` and `research/` and what it is for; the documentation map
holds one entry per page of the documentation with everything the
page is made from. All three are freely rewritten, because their
value is in being current, not in being a record. The map is state
of the project that owns the documentation and is never shown to the
documentation's reader.

**Rendering.** Outputs for an audience and the instructions that make
them. A recipe says how a render is made; it is versioned, iterated
and never approved, since it is a tool and not a record of thinking.
A render is generated from the recipe and overwritten by every
`/render`; a page of the documentation, or its index, is generated
from the map and overwritten by every documentation run. No render
and no page is ever a source of truth or edited by hand: what is
wanted differently is changed in the recipe or the map and
regenerated.

**Resources.** What came in from outside and what was found out. A
source is external input as it arrived, immutable from its
registration; a research note is the durable answer to one question,
immutable from creation. A functional binary, such as a presentation
template or a graphic, is a source too, so a library's assets are
resources without a kind of their own.

A library carries no artefacts and no records except the history
companion of its readme recipe; the other groups are unchanged.

## Why state lives in files

State lives in files, never only in the conversation. The reason is
simple: a session can be ended at any point without loss, and the
next one re-orients from the ledger. This is why "written" means a
file and nothing else. Whenever Claude reports something as written,
it names the file and section; whatever is carried in the
conversation only is said to be nowhere yet, and nothing is said to
be safe while any of it lives only in the conversation.

## The ledger

The ledger is the single source of truth for state. It holds tables
for the briefs, the documents of the chain, the renders, the
published files, the sources, the research, the dependencies on
other repositories, the findings of critics and checks, the
challenges, and a short list of what waits on the principal. For
resources and dependencies it is registration only: what a source or
a research note is and is for lives in the index of its directory,
and a library document cited by path carries no version because its
owner maintains it.

Two rules keep the ledger useful. It is kept current after every
operation, so that it can be trusted as a snapshot. And it cites and
never copies: a matter that has an ID gets one line, the ID, a few
words and its state, while its substance stays in the thread or the
record it belongs to; free text is allowed only for a matter with no
ID yet, which gets one at the next write; an unfinished conversation
is saved into its thread of the intent, never into the ledger. A
layer below the intent that the project does not have is not
missing: it gets no row, and neither the state map nor the checks
say anything of it.

The ledger's header carries the project's kind, `thought` or
`library`, and the language of its artefacts. A library's ledger
keeps only the tables a library needs.

## Decisions

The decisions file is one record per decision of the principal, each
numbered in the global ID sequence, newest last, with the decision,
the reason including what was weighed against it, and the date. A
rejected finding or challenge is a decision too, and the ledger
points to the record that rejected it. Because the file is
append-only, a decision is never silently revised: changing one's
mind is a new record that names the old.

## Why immutability is a rule and not a mechanism

Immutability of documents is a process rule, enforced by convention,
not by git. Three reasons stand behind this. Git protects nothing
from a commit that rewrites a file, so a repository gives no
guarantee that a convention does not already give. The rule costs
nothing to keep. And a mechanism would be one more layer to maintain
that still would not stop a hand edit. The same holds for the
append-only records: the promise is kept by the people and the
commands that write them, and a breach is something a check reports,
not something the tooling prevents.

## Why corrections happen downstream

Reviews, challenges, sources and research are never edited: a source
from its registration, the others from creation. A review is one
dated run of a reviewer; a source is input as it arrived; a research
note is the answer that was found on its date. Edited, each would
stop being what it is. So a correction is made where the matter is
actually worked: a finding's state changes in the ledger, a rejected
one is answered by a decision, an accepted challenge is mended in
the artefact that needs it, and a wrong source is answered by what
the principal chooses to take from it into the intent, with
provenance. The original stays as evidence of what was there.

## Prose at about 72 columns

Prose in every document is hard-wrapped at about 72 columns so that
git diffs stay legible: a change to one sentence shows as a change
to a line or two, not to a whole paragraph. Tables, code blocks and
front-matter are never wrapped, because a line break inside them
would change their meaning.

## See also

- [Document kinds](../reference/document-kinds.md): the table of
  kinds, verbatim.
- [Ledger](../reference/ledger.md): the ledger's tables and states.
- [About versioning and history](versioning-and-history.md): the
  history companion of every versioned kind.
- [About the documentation](the-documentation.md): the map and the
  pages, the two generated kinds.
