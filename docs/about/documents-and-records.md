---
generated: 2026-10-09
made: derived
inputs-hash: 7399065258225d10
inputs:
  - CLAUDE.md
  - templates/ledger.md
  - templates/decisions.md
  - projects/forge/10-intent.md
---

# About documents and records

This page explains what the files of a project are, how they are
sorted into kinds, and why each kind behaves as it does: which files
are rewritten, which only grow, which are never touched, and where the
state of a project is kept. It is for anyone who works in a project,
anyone who extends the forge, and anyone judging whether the
arrangement holds together. It was put together from `CLAUDE.md`,
the ledger and decisions templates and the forge's own intent.

## Document and artefact

"Document" is the word for every file of a project. "Artefact" is
reserved for the documents of the chain: the brief, the intent and
whatever layers the project takes below it. These are the files the
principal composes, the reviewers read and the renders are generated
from. The distinction matters because the artefacts are the only
files whose content the principal owns outright; everything else
either records what happened to them, keeps track of where things
stand, is generated from them, or feeds them.

Every document has exactly one kind, and the kind says four things:
what the document is, who writes it, whether it carries a version,
and how it behaves over time. The kinds fall into five groups.

## The five groups

**Artefacts.** One kind, the artefact. Written by the principal with
Claude, versioned, and rewritten freely: an intent or an assignment
is not frozen in any sense the file would show. It changes between
approvals like any draft, and what a recipient holds is a particular
version reached by a link into git, not a locked file. What each
artefact is, its own definition says.

**Records.** What happened, kept so it can be read back. Two kinds
only grow: the history companion of every versioned document, one
record per change with the reason, and the decisions file, one
record per decision of the principal with its reason and date. Both
are written by the forge, never edited, and a later decision does not
correct an earlier one in place: it supersedes it with a new record
that names it. The third kind of record is a reviewer's run, a
critique, a challenge or a check report, dated and immutable from the
moment it is filed.

**State.** Where things stand right now. The ledger is the single
source of truth for state; the resource indexes catalogue what lies
in `sources/` and `research/`; the documentation map holds one entry
per page of the documentation and everything that page is made from.
All three are freely rewritten, because state is a snapshot, not a
record: the ledger and the indexes by the forge after every
operation, the map by the documentation run. The map is state of the
project that owns the documentation and is never shown to the
documentation's reader.

**Rendering.** Outputs made for an audience, and the instructions
they are made from. A recipe says how a render is made; it is
versioned, iterated by Claude with the principal, and never
approved, so it stays at 0.x for its whole life. A render is
generated from the recipe and overwritten by every `/render`; a page
of the documentation, or its index, is generated from the map and
overwritten by the documentation run. Neither a render nor a page is
ever a source of truth, and neither is edited by hand: what one
wants changed is changed in the recipe, or in the artefacts the
render draws on.

**Resources.** What came in from outside and what was looked up. A
source is external input as it arrived; research is a durable answer
to one question. Both are immutable: a source from its registration,
a research note from its creation. A functional binary, a
presentation template or a graphic, is a source like any other, so a
library's assets are resources without a kind of their own.

A library, the kind of project that shares material across others,
carries no artefacts and no records but the history companion of its
README recipe; its state and its resources behave as above.

Records, state, research and recipes are always written in English,
whatever language the project's artefacts are in, because they are
read by Claude, the reviewers and the checks and never handed to a
recipient.

## Why state lives in files

State is never kept only in the conversation. A session can end at
any point, by choice or by accident, and nothing that lived only in
the conversation survives it. So the ledger is kept current after
every operation, and `/ledger` re-orients from it when work resumes.
The same rule shapes what "written" means: when Claude reports
something as written, he names the file and the section; whatever is
carried in the conversation only is said to be nowhere yet, and he
never says nothing is lost while anything lives only there. One
project per session is the hygienic default.

## The ledger

The ledger is the single source of truth for state. Its tables cover
the briefs, the documents of the chain, the renders, the published
files, the sources, the research, the dependencies on other
repositories, the findings of critics and checks, and the challenges;
the shapes and the states they use are the reference page's. A
library's ledger keeps only the tables a library needs. The ledger's
header also carries the project's kind and the language of its
artefacts.

Two rules govern what goes in. First, resources and dependencies are
registration only: the ledger says that a source or a research note
exists and when it arrived, and what it is and is for lives in the
index of its directory, never in the ledger. Second, the ledger cites
and never copies. Under its "Waiting on principal" section, a matter
that already has an ID gets one line: the ID, a few words and its
state, with the substance left in the thread or the record it came
from. Free text is allowed only for a matter with no ID yet, and it
gets one at the next write. An unfinished conversation is saved into
its thread of the intent, never into the ledger.

A layer below the intent that a project does not have is simply
absent: the ledger has no row for it, and nothing reports it as
missing.

## Why immutability is a rule, not a mechanism

Reviews, challenges, sources and research are never edited. This is a
process rule kept by convention, not something git enforces, and the
reason is practical. Git protects nothing from a commit that rewrites
a file, so git itself cannot be the guard. The rule, on the other
hand, costs nothing to keep. A mechanism to enforce it would be one
more layer to maintain, and it still would not stop someone editing
the file by hand. So the forge states the rule and relies on it.

Corrections therefore happen downstream. A reviewer's report stays
as the reviewer wrote it; a finding it raised is settled in the
artefact, and a rejected finding or challenge is recorded as a
decision with its reason. A decision that no longer holds is not
rewritten; a later decision names it and supersedes it. A source
that turns out to be wrong is not edited; what the intent took from
it is corrected in the intent. The record of what was found, decided
or received stays readable as it was, and what changed in response
is readable beside it.

## How the files are written

Prose in every document is hard-wrapped at about 72 columns so that
git diffs stay legible: a change to one sentence shows as a change to
one or two lines, not to a whole paragraph. Tables, code blocks and
front-matter are never wrapped, because wrapping would break them.

## See also

- [Document kinds](../reference/document-kinds.md): the table of
  kinds, verbatim.
- [Ledger](../reference/ledger.md): the ledger's tables and states.
- [About versioning and history](versioning-and-history.md): the
  history companion of every versioned kind.
- [About the documentation](the-documentation.md): the map and the
  pages, the two generated kinds.
