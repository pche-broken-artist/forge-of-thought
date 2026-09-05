---
project: forge
type: research
topic: what good release notes look like — established projects and best practice
date: 2026-09-05
derived_from: 10-intent.md v3.34 (THR.0310; POS.0730, the release-notes recipe 0.6 and the genre skeleton); RELEASE-NOTES.md as rendered 2026-09-05
status: immutable
---

# What good release notes look like

## Question

How are release notes done well — by the projects the field holds up
as examples and by the written standards — so that the forge's own
`RELEASE-NOTES.md` stops being a story and tells a reader plainly what
was added, what changed and what disappeared (THR.0310)? Two
sub-questions the thread hands to the research: whether the Version
History row the notes are generated from must change too, and what a
"release" is for the notes when the forge releases at every `/release`
(3.34, 3.33, …) but approves a major rarely (3.0).

The facts behind the question, measured on the render of 2026-09-05:
the file is 991 lines; the Unreleased head covers intent versions
3.1 to 3.34 in eleven thematic paragraphs of 300 to 500 words each,
one of which explains in one breath a closed thread, two rejected
options, a position and a deferred check; no group says "added",
"changed" or "removed"; nothing tells a user of the engine what they
must do after a `forge-pull` (the history-companion migration of
2026-09-04, for instance, required a `/check` and a move in every
project). The recipe asks for "themes, not a row-by-row replay" and a
"narrative opening" — the render is what the recipe ordered.

Surveyed on 2026-09-05: the two written standards (Keep a Changelog
1.1.0, Common Changelog), nine established projects' release notes
read at source (Kubernetes, Rust, Django, Git, Python, Node.js,
VS Code, Stripe's API changelog, GitHub's generated notes), the
collection mechanisms behind them (Kubernetes' release-note block,
towncrier's news fragments, Django's `versionadded`), and the
commentary (Simon Willison 2022, Sophia Willows on generated
changelogs, a 2026 piece on outgrowing Keep a Changelog, vendor guides
of 2025–2026). Epistemic tags: **[C]** consensus across standards and
projects, **[P]** practice of the large projects, not stated as a
rule, **[X]** contested, **[E]** emerging.

## Key findings

### 1. The standards agree on a shape; the projects follow it more than they cite it [C]

Keep a Changelog (keepachangelog.com, 1.1.0) is the reference most
projects name. Its rules: "Changelogs are *for humans*, not machines";
an entry for every version, latest first; changes grouped by type —
`Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`; ISO
dates; an `Unreleased` section on top; every version linkable. Its
anti-patterns are as explicit as its rules: a commit-log diff is not a
changelog ("full of noise"); a changelog "documents the noteworthy
difference, often across multiple commits"; ignoring deprecations is
the worst omission; a pulled release stays in the file, marked
`[YANKED]`, "loud for a reason".

Common Changelog (common-changelog.org) is the stricter sibling, born
of the Node.js ecosystem: four groups only, in a fixed order —
`Changed`, `Added`, `Removed`, `Fixed`; breaking changes first in
each group, prefixed `**Breaking:**`; entries sorted by importance,
then latest first; imperative mood ("Add", "Remove", "Fix"); a
reference (commit, PR, issue) on every entry; "Skip content that
isn't important"; "Communicate the impact of changes". It rejects
Keep a Changelog's `Unreleased` section (finding 5).

Of the nine projects read, none follows either standard letter for
letter, and every one has the same skeleton: a dated section per
release, newest first; inside it, changes in groups; the changes
that force the reader to act set apart and first; one sentence per
change; the exhaustive log somewhere else.

### 2. Two axes of grouping — by kind of change, or by area — and the projects that group by area still cut out the compatibility section [P]

- **By kind** (Keep a Changelog's axis): Kubernetes — "Changes by
  Kind": Deprecation, API Change, Feature, Documentation, Bug or
  Regression, Other (Cleanup or Flake); Git — "UI, Workflows &
  Features", "Performance, Internal Implementation, Development
  Support etc.", "Fixes since v2.49"; GitHub's generated notes —
  categories mapped from PR labels (Breaking Changes, New Features,
  Other Changes).
- **By area** (the product's own map): Rust — Language, Compiler,
  Libraries, Stabilized APIs, Cargo, Rustdoc; Django — What's new by
  app (admin, auth, forms, models, …); VS Code — Agents, Chat,
  Accessibility, Editor experience, Terminal; Stripe — by product
  (Billing, Payments, Connect), each entry tagged Breaking or
  Non-breaking.

Whichever axis a project chooses, the changes that break or oblige
the reader are pulled out into a section of their own, placed first
or given its own heading: Kubernetes "Urgent Upgrade Notes" (and the
words "action required" in the note itself, a contributor rule), Rust
"Compatibility Notes", Django "Backwards incompatible changes" and
"Features deprecated", Python "Porting to Python 3.13", Node's
`(SEMVER-MAJOR)` label, Stripe's Breaking column. No project read
buries a breaking change in a narrative.

### 3. One sentence per change, from the reader's side, with a pointer [C]

The entry is a sentence, not a paragraph, and says what changed for
the reader, not how it was done: Kubernetes "Fixed a panic in the
endpoint controller when processing services with empty IPFamilies
field. (#139236, @author) [SIG Apps and Network]"; Git "A
post-processing filter for 'diff --raw' output has been introduced.";
Rust "Stabilize `if let` guards on match arms (#141295)"; Stripe
"Adds support for updating Connect parameters of an existing Payment
Link". Every one carries a pointer — a PR, a commit, a document — so
the sentence can stay short and the reader can go deeper. The tense
and mood vary (Kubernetes past tense, Common Changelog imperative,
Stripe present) and are fixed per project, never mixed.

The vendor guides of 2025–2026 (Document360, Slite, Beamer, All Days
Tech) converge on a three-part test for an entry: *what changed* in
one plain sentence, *why it matters* to the reader, *what to do* —
"Action required: yes/no; if yes, exactly what". The same test in
the contributor rules of Kubernetes: "Include a call to action if
there is anything the end user needs to do". **[C]** for the first
and third parts; the "why it matters" line is where guides for
customer-facing SaaS notes go further than the open-source projects,
which mostly let the pointer carry the why.

### 4. Highlights are a layer on top of the list, never instead of it [P]

Where a project has narrative, it is a curated head over a complete,
structured body: Python's *What's New* opens with "Summary — Release
Highlights" and refers to "the changelog" for "full details"; Node.js
gives "Notable Changes" (a hand-picked few, semver-labelled) and then
"Commits" (all of them); VS Code opens with three or four bullets of
highlights and then walks the areas; Simon Willison: "Emphasize the
highlights" so that the major themes "don't disappear amid extensive
bullet lists" — and, first of all, "Write release notes." Django, held
up by Willison as "some of the best", has almost no narrative at all:
"Major features" as short subsections, then "Minor features" by app,
then the compatibility sections, every item one to three sentences
with a link.

The forge's current render is this pattern inverted: the narrative is
the body and there is no list.

### 5. The note is written with the change, not at release time — in practice; the standards disagree on where it waits [X]

The large projects collect the sentence at the moment the change is
made, by the person who made it, in a typed slot:

- Kubernetes: a `release-note` block in every PR description ("Does
  this PR introduce a user-facing change?"); a PR without one is
  labelled `do-not-merge/release-note-label-needed`; the release
  notes are assembled from the blocks by tooling, and the kind is a
  PR label.
- towncrier (Twisted, pip, pytest, Astronomer): one "news fragment"
  file per change, typed by filename suffix (`feature`, `bugfix`,
  `removal`, `doc`), written for "those that hear it, not those that
  write it"; the changelog is compiled at release from the fragments
  and the fragments deleted. Its stated reasons: no merge conflicts
  on one shared file, and the note written while the change is fresh.
- Django: `versionadded`/`versionchanged` directives in the
  documentation, written with the change, and a release-notes file
  updated in the same commit.
- Rust: a `relnotes` label on the PR; the release team compiles.

Keep a Changelog wants the same, with the `Unreleased` section as the
waiting room: add the line when you merge, so the release is a
heading rename. Common Changelog rejects `Unreleased` outright —
"contributors can't add self-references before releases occur",
first-time contributors should not maintain the changelog, and
writing a good changelog "requires a bird's-eye view of the project"
— so the maintainer writes the section at release, from the log.
Both positions exist in the wild; the projects with many contributors
have all landed on *typed fragments written with the change, compiled
at release*, which satisfies both: the sentence is fresh, the
ordering and the pruning are done with the bird's-eye view.

Generating the notes from the commit log alone is rejected by every
source that discusses it (Keep a Changelog: "poor changelogs,
defeating their purpose"; Sophia Willows: commit messages "serve an
internal engineering audience", customers "do not care to know that
v1.3.7 was the release that added the `ProductSearchService` class";
she recommends towncrier). GitHub's generated notes are the
counter-example that proves it: they list PR titles by label and are
accepted as a floor, not as good notes.

### 6. Every release gets a section; the unit is the thing the reader can install [C]

All nine projects give every shipped version its own dated section —
patch releases included (Kubernetes v1.33.13 has the same skeleton as
v1.33.0, only shorter; Node 24.20.0 its own entry). What makes a
version a "release" is that a user can obtain it, not that it was
approved by anyone. Majors differ only in weight: a longer highlights
head, a compatibility section, sometimes a separate document (Python's
*What's New* per minor, Django's per feature release, Kubernetes' one
file per minor series).

Keep the date (Willison: "it matters a lot because you want to be
able to determine how old a release is"), link the version to its
tag or diff (both standards), and never rewrite a published section —
a correction is a new line, a pulled release a `[YANKED]` mark.

### 7. Length is controlled by pruning, not by summarising [C]

Common Changelog: "Skip content that isn't important"; Keep a
Changelog: only the "noteworthy" difference; Kubernetes: a change
with no user-facing effect gets `release-note-none` and does not
appear; towncrier: fragments of type `misc` are listed by reference
only. Nobody compresses ten changes into a paragraph; the ones that
do not matter to the reader are left out, the rest stay one line
each. Internal refactoring, documentation touch-ups and process
bookkeeping are the usual casualties.

### 8. Beyond the file: hosted pages and LLM drafts [E]

A 2026 piece (releasepad, 2026-07-09) argues that a `CHANGELOG.md`
is outgrown once the audience is outside the repository — shareable
URLs, feeds, search — and recommends keeping the file as the source
that feeds the rest. Several 2026 vendor guides describe an LLM
drafting the first pass from the typed fragments, with a human
pruning. Neither changes the shape of the notes; both assume the
structured file exists first.

## Options and trade-offs

The options concern the forge's `RELEASE-NOTES.md` (POS.0730, recipe
`recipes/release-notes.md`, genre skeleton
`templates/recipe-release-notes.md`, `/recipe release-notes`). The
reader is a user of the engine — someone who cloned it and takes
upgrades through `forge-pull` — and, for the forge's own project, the
principal looking back.

**A. Keep a Changelog shape, one section per `/release`.** Heading
`## 3.34 — 2026-09-05`, newest first; inside, fixed groups in a fixed
order — *Action required* (what a user of the engine must do in their
projects after pulling), *Added*, *Changed*, *Removed*, *Fixed* —
each entry one sentence from the user's side with a pointer (POS,
DEC, REJ, THR, a command, a script); groups that are empty are
omitted; an approved major is marked on its heading (the tag) and
gets a short highlights paragraph above its groups, nothing else. The
narrative era section disappears.
*For:* the field's consensus; a reader sees added/changed/removed at a
glance; every `forge-pull` has its own section, which is what the
puller needs; the render becomes a mechanical distillation with little
room for the story to come back.
*Against:* a section per release means 34 sections for 3.x — many of
them a line or two — and the "what the era meant" reading is lost
unless the major head carries it; a substantive change to POS.0730.

**B. Two tiers: era narrative kept, a typed list added under it.**
The current sections stay (Unreleased since the last major, one per
major); each gets, below its two-to-four-sentence opening, the same
typed groups as A, compiled across the whole span (3.1–3.34 as one
list), and the thematic paragraphs go.
*For:* the smallest change to POS.0730; the era reading survives; the
Python/Node pattern of highlights over a list.
*Against:* a span of 34 releases in one list loses *when* something
changed, which a puller needs to know ("was this already in the
release I pulled last week?"); entries must carry the release version
to compensate, which is A in disguise.

**C. Keep the narrative, tighten the prose.** Shorter paragraphs,
bold lead-ins naming the change type.
*For:* no convention changes.
*Against:* every source read rejects the paragraph as the unit; the
principal's verdict of 2026-09-04 is that the story is the problem.

**On the Version History row (THR.0310's second question).** The row
today is the developer log: 200–400 words of what changed and why,
one per version. Three ways the notes can be made from it:

1. *Row unchanged; the render agent classifies at release.* The
   isolated subagent reads the rows of the span and writes the typed
   entries. Cheap, nothing new to write; but the classification and
   the "action required" judgement are made by a model that saw
   neither the change nor the principal, at the moment the standards
   call the worst (finding 5), and the same row will classify
   differently on two renders (POS.0810).
2. *The row grows a typed tail, written by the write step with the
   change.* After the prose, a short block in the row's own cell —
   e.g. `Notes: Added … · Changed … · Removed … · Action required …`
   — one sentence per item, from the user's side, written by the same
   write step that composes the row and `last_change`. The render
   compiles the notes of the span into the groups, prunes and orders.
   This is towncrier and the Kubernetes block in the forge's own
   mechanism (one place, prime directive 10): the fragment lives in
   the row, the compilation in the recipe. Cost: one more thing the
   write step composes and the principal confirms; a convention the
   principal must decide (prime directive 2). Rows before the
   convention are compiled as in 1, once, and then frozen in the
   released sections.
3. *A separate news-fragment file per version.* towncrier literally.
   Rejected as a candidate: a second file per change beside the
   companion is a second place for one mechanism.

## Relevance to this project

The forge's render is the inversion of what every source read does:
narrative as the body, no list, no group that says added, changed or
removed, and no place where a user of the engine learns what to do
after pulling. The standards, the projects and the commentary agree
on the shape; the only contested point — whether the note is written
with the change or at release — is settled in practice by the typed
fragment compiled at release, which the forge can host inside the
Version History row.

**Recommendation:** option **A** for the shape (one dated section per
`/release`, fixed typed groups with *Action required* first, one
sentence per entry with a pointer, a highlights paragraph on approved
majors only, empty groups omitted, released sections frozen) and
row variant **2** for the source (a typed `Notes:` tail in the Version
History row, written by the write step with the change; the render
compiles, prunes and orders). Both are positions for the principal:
A rewrites POS.0730 and the recipe, the skeleton and the genre file
(THR.0310's own list); variant 2 adds a convention to the Version
History row (CLAUDE.md, Versioning & status; `templates/history.md`)
and to every write step that bumps a version — proposed through
`/forge intent`, never by fiat. If the principal wants the era
reading kept, B is the fallback, with the release version on every
entry.

Two smaller points for the same round: the recipe's audience line
("humans tracking the system's evolution") names no reader; the
projects that write well name one (the operator, the developer
upgrading). And the current Unreleased head conflates two states —
*released but not approved* (3.1–3.34 are all on `main` and pulled
by anyone) and *not yet released* — which Keep a Changelog keeps
apart; with a section per `/release` the conflation disappears, and
an `Unreleased` section is needed only if the notes are ever rendered
between releases (they are not, POS.1100).

## Sources

- Keep a Changelog 1.1.0 — https://keepachangelog.com/en/1.1.0/
- Common Changelog — https://common-changelog.org/
- Kubernetes CHANGELOG-1.33 — https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md; contributor guide on release notes — https://github.com/kubernetes/community/blob/master/contributors/guide/release-notes.md
- Rust RELEASES.md (1.98) — https://github.com/rust-lang/rust/blob/master/RELEASES.md
- Django 5.2 release notes — https://docs.djangoproject.com/en/5.2/releases/5.2/; writing documentation (versionadded) — https://docs.djangoproject.com/en/5.2/internals/contributing/writing-documentation/
- Git 2.50 release notes — https://github.com/git/git/blob/master/Documentation/RelNotes/2.50.0.adoc
- Python What's New in 3.13 — https://docs.python.org/3/whatsnew/3.13.html
- Node.js CHANGELOG_V24 (24.20.0, 2026-08-26) — https://github.com/nodejs/node/blob/main/doc/changelogs/CHANGELOG_V24.md
- VS Code release notes, September 2026 — https://code.visualstudio.com/updates
- Stripe API changelog (2026-08-26.dahlia) — https://docs.stripe.com/changelog
- GitHub, automatically generated release notes — https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes
- towncrier documentation — https://towncrier.readthedocs.io/en/stable/
- Simon Willison, "Writing better release notes", 2022-01-31 — https://simonwillison.net/2022/Jan/31/release-notes/
- Sophia Willows, "Conventional changelogs suck" — https://sophiabits.com/blog/conventional-changelogs-suck
- Releasepad, "Keep a Changelog: the format explained (and when to outgrow it)", 2026-07-09 — https://www.releasepad.io/blog/keep-a-changelog/
- Vendor guides consulted for the three-part entry test (2025–2026): Document360, Slite, Beamer, All Days Tech, Mintlify, AnnounceKit — weak sources, used only where they agree with the projects above.
