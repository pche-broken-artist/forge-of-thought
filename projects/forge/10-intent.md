---
version: 3.47
date: 2026-09-06
status: draft
last_change: 3.47 (2026-09-06): the intent swept by the position rule of POS.0120 (CHL.0180) — every position read, nineteen cut to stance, reason and citations and nine more trimmed, the story of each left to the history rows that already carry it; nothing decided, nothing changed in substance.
project: forge
audience: principal + Claude only
---

# Forge of Thought — Intent

## Essence

**Forge of Thought** is a place for forging thoughts — a workshop
where thought is tempered and shaped. It began as one CTO's tool for
briefing his direct reports; that origin is now an instance fact, not the
system. Anyone can be the principal, the subject matter is deliberately
unconstrained — process redesign, platform initiatives, organisational
topics, anything — and the recipients of an assignment may be teams,
colleagues, or the principal's future self.

The primary ambition is the full chain: from a raw idea all the way to a
deck ready for realisation, growing layer by layer — assignment, then a
BRD, then solution architecture, up to implementation-ready specification
including integration. **Version 1 deliberately ends at the assignment.**
Every design decision below is made with that growth in mind, which is
why files and IDs are numbered with gaps and why the name says thought,
not assignment.

The engine runs in Claude Code. Claude acts as the principal's cognitive
extension: it owns structure, order and process discipline, while every
decision about content remains the principal's. Isolated AI
reviewers, deliberately blind to the working conversation, provide
adversarial pressure from different angles.

The design constraint that shapes almost everything: an assignment must
carry the complete in-scope substance of the intent, written as well and
as precisely as it can be. Nothing is omitted for brevity's sake; length
is whatever fidelity requires. What keeps it an assignment rather than a
solution is the kind of content, never the amount.

## Positions

### Collaboration model
- **POS.0005** Forge of Thought is a general-purpose engine, not bound
  to one person or one management relationship. "Principal" means
  whoever's thinking is being forged; "recipients" means whoever
  receives the assignment. PCHe (CTO) is the engine's author and its
  first principal (POS.0990); who the principal of an instance is lives
  in `CLAUDE.local.md` (POS.0950).
- **POS.0010** Claude is the principal's cognitive extension, not a
  supplier. Claude owns structure, order and document hygiene; the
  principal owns content and every decision.
- **POS.0020** Claude's default under uncertainty is to ask, never to
  assume. Beyond answering, Claude actively elicits: helping the
  principal extract what he has not yet articulated is part of the job.
- **POS.0030** Claude never introduces a new convention, prefix or
  section unilaterally: propose, wait for a decision, then write it down.
- **POS.0040** Many iterations are the normal mode. Intent and
  assignments may grow or change substantially between versions.
- **POS.0050** For key topics Claude researches current best practice
  rather than inventing. Outside inspiration is a legitimate input;
  durable findings are stored in `research/`, not left in chat.
- **POS.0060** The forge as a system dictates only the output
  language: all documents are written in English; the single
  exception is the briefs (`00-brief*.md`), stored verbatim in
  whatever language they were written. The working-conversation
  language is per-instance configuration, not a system rule: it is
  set in `CLAUDE.local.md` (POS.0950) and read from there by every
  command — never written into the operating layer, and never
  presented outward. The README and other outward-facing renders
  state only the output-language rule.
- **POS.0070** Claude's contribution to content is to criticise,
  challenge, inspire and lay out options; the composition is the
  principal's. He assembles what the forge offers into his own
  positions and decisions — nothing enters the content because
  Claude proposed it, only because the principal took it up.
  "Cognitive extension" (POS.0010) means an amplifier of the
  principal's thinking, never its substitute.

### Working methods
The named ways a working conversation runs. They are the forge's
vocabulary of collaboration: each has a name so that command
definitions and the README can refer to it and the principal can
invoke it in a word. None is a command — a command has one input and
starts on demand; a method applies whenever its situation arises,
whatever produced it. Some are new positions here; others name a
position that already stands elsewhere.

- **POS.0850 Walkthrough.** Any list of items that need the principal's
  decision — critique findings, challenges, the differences between two
  requirement sets, open threads, TBC items before a handover — is
  worked one item at a time, in order of weight. For each item Claude
  first gives its recommendation with a one-sentence reason; the
  principal decides in a word or with a counter-proposal; "leave it
  open" is a legitimate verdict, not a failure. A table asking for every
  verdict at once is never put in front of the principal. The next
  message opens with one line acknowledging the verdict and then
  carries the next item, nothing else. A check whether
  Claude has understood an item fully is an item of its own. An
  elicitation interview runs the same way: one question per message, the
  answer acknowledged before the next question is asked. A questionnaire
  of several questions at once is the table of verdicts in another coat
  and is never put in front of the principal. Verdicts are carried in
  the conversation and written once at the round's end (POS.0190):
  findings and challenges change state in the ledger, an overruled
  finding or rejected challenge becomes a DEC record with its reason, a
  fix becomes an iteration of the artefact it concerns, an accepted
  challenge must change the intent. Whatever produces a list ends by
  offering a walkthrough — `/critique`, `/challenge`, the `/forge` map,
  a comparison made on request — and the principal may call for one at
  any moment. `/resolve`, a per-verdict door, is retired without
  alias; its write-up rules live here.
- **POS.0860 Propose, never decide.** Claude criticises, challenges,
  inspires and lays out options; the principal composes (POS.0010,
  POS.0070). Nothing enters content because Claude proposed it.
- **POS.0870 Elicitation interview.** Claude draws out by questions
  what the principal has not yet articulated, rather than filling gaps
  by assumption (POS.0020); the heart of `/forge intent`.
- **POS.0880 Draft early.** An early draft is an elicitation tool,
  not an output: concrete text sharpens the principal's reaction
  (POS.0150).
- **POS.0890 Reflect back.** Before anything is written, Claude
  restates what it understood the principal to have said, so that the
  write is a confirmation and not a surprise; the companion of
  write-once-per-round (POS.0190).
- **POS.0900 Intent-first.** A change of substance goes into the
  intent and propagates from there; only wording is fixed downstream
  directly (POS.0140).
- **POS.0910 Recommend, do not push.** Every option Claude lays out
  comes with its recommendation and reason, stated once; a declined
  recommendation is not re-argued unless new facts appear.

### Document chain
- **POS.0100** Files in the chain are numbered in tens (`00-brief.md`,
  `10-intent.md`, `20-assignment.md`) so later layers — a BRD
  (`30-brd.md`), a solution design — can be added without renaming
  anything that exists.
- **POS.0110** A brief is an intent that is composed and then locked.
  It is the principal's own text — the birthplace of one whole of
  thinking — free-form: any structure the principal finds useful
  (prose, headings, tables, use cases), no required content and no
  IDs; only a minimal YAML header (project, title, date, author,
  version, status, last_change). It holds thoughts to be processed, not
  decisions: they may be changed, reworked or dropped when mined, and
  only the intent turns them into positions. No structure is
  *required* because a required one would force premature tidiness and
  destroy the diagnostic value of how the idea was actually dumped —
  but none is forbidden either, and a summary the principal orders
  into a brief is stored as shown, never re-narrated. A brief has two
  states: *draft* while it is being composed, and *approved* (version
  1.0) once the principal locks it; immutability runs from the lock,
  not from the file's creation. Three origins are equally legitimate
  and the forge does not distinguish them: the brief arrives finished
  from outside and is locked on arrival; it is begun outside and
  finished with Claude in the forge; or it is born in the forge from
  the first word. `/forge brief [name]` is the door for the latter
  two, and it runs under the principal's moderation: he says what is
  being explored and steers; Claude's role is to clarify where he is
  terse or unclear — never to add content of its own — and to
  correlate the thought with reality throughout, offering best
  practice, projects and standards that solve the same thing ("are we
  reinventing the wheel?") through `/research` and `/ingest`, which
  Claude proposes and the principal times. The aim of a brief is a
  thought clear enough to be checked against what exists or to draw
  inspiration from it; what such a check contributes enters the brief
  only by the principal's word — the brief stays his text, not a
  literature review. `/new-project` creates `00-brief.md` at scaffold
  time with the pre-filled header; the principal's verbatim text
  completes it. A locked brief is the provenance anchor of its whole:
  the record against which later drift is measured. The draft state
  and the forge-born brief decided 2026-08-27 (history 2.12–2.13).
- **POS.0920** A project may have more than one brief, and the ledger
  tracks how far each is mined. The founding brief is `00-brief.md`;
  every later whole of thinking that would otherwise land in the
  intent as a batch of unproven positions is born as
  `00-brief-<name>.md` — same header, same states, same rules. A
  locked brief is mined into the single intent: positions cite the
  brief as provenance; a whole that dies on the way leaves the brief
  locked and one REJ in the intent with the reason, so the trace
  survives either way. The ledger's Briefs table carries one row per
  brief — version, status and a mining state `pending | partial |
  mined | dropped` with a free-text note (what remains for *partial*,
  the REJ for *dropped*); "how much" is a judgement recorded in that
  note and in the provenance of the positions, never a metric.
  `/forge` shows pending and partial briefs as next steps, `/forge
  intent` offers them for mining, `/check` compares the table with the
  directory. Rationale: a big new whole needs a place where the
  thought can be tempered before it enters the trunk — like a git
  branch — without a new document kind; THR was wrong for it (a
  thread is a question, not a body of work), and a working space with
  positions before the merge (a branch document) was judged heavy for
  now (THR.0170). Closes THR.0110 (opened 0.8, 2026-08-02).
- **POS.0120** `10-intent.md` is the working document: the consolidated
  *current* state of the principal's intent. Not an append-only log; it
  is rewritten for coherence each round, with changes recorded in its
  Version History. It exists because chat context dies and anything of
  value must live in a file: it is the document to read when returning to
  a project after weeks, instead of excavating old conversations.
  A position is a stance with its reason and its citations, dated
  once. How it was reached — trials, measurements, counts, findings
  settled, what others do — is the history row's, the ledger's or a
  research note's, never the position's (CHL.0180, 2026-09-06; the
  intent measured against this rule once, before 4.0, THR.0240).
- **POS.0130** `20-assignment.md` is the distilled handover document for
  the recipients: complete, precise, structured, self-contained,
  versioned. It carries the whole in-scope substance of the intent —
  nothing is left out for the sake of brevity, and a silent omission is
  a defect; leaving a matter out is legitimate only as an explicit
  delegation (a DEL or TBC item). There is no size target in either
  direction: length is whatever fidelity requires, and the defect is
  excess of the wrong kind (solving instead of assigning), never length
  as such (the size targets dropped 2026-08-08 and 2026-08-15, history
  1.12 and 1.15: the goal is to have it right, not short). The name "assignment"
  was kept deliberately after considering alternatives; it does not
  preclude further layers below it.
- **POS.0140** Substance changes go intent-first and then propagate to
  the assignment; wording-only fixes may edit the assignment directly. If
  the principal dictates substance straight into the assignment, the
  corresponding intent update is proposed in the same step.
- **POS.0150** Drafting early is a legitimate elicitation tool, not a
  violation of sequence. Concrete text sharpens critique.
- **POS.0160** Supporting documents (the kinds: POS.1080): `decisions.md` (append-only, DEC),
  `ledger.md` (single source of truth for state, freely rewritten),
  `reviews/`, `challenges/`, `research/` (all immutable, dated); the
  resource indexes are POS.0840's.
- **POS.0170** Feedback from recipients has no channel of its own. The
  principal processes it and feeds conclusions back through
  `/forge intent`.
- **POS.0180** External inputs (transcripts, offers, documents,
  standards) live in `sources/` per project: immutable once registered,
  plain slug filenames, each in one form — text, or a functional
  binary (POS.1040).
  They may arrive at any stage of a project's life — before the brief
  as material for writing it, during intent work, or after. Origin
  dates are metadata, not ceremony: recorded best-effort in the ledger
  (content | file | ingested) and never demanded from the principal.
  The principal may drop files into `sources/` manually at any time;
  `/ingest` without arguments sweeps the directory: it registers new
  files and reports files changed since registration (modification
  time against the ledger date) with a question — what to do with
  each. The meaning depends on the project's kind (POS.0960): in a
  `thought` project a changed source is a breach of immutability to
  be settled (a new version beside it, or knowingly accepted); in a
  `library` project it is the normal case — the extract is
  regenerated, the ledger date moved, the index entry corrected.
  `/ingest`
  stores, registers and catalogues — nothing more. Registration does
  not imply intake: what a source is for is individual — a standard to
  verify against, inspiration, a meeting record, material to absorb —
  and is recorded as free-text Role in the directory's `00-INDEX.md`
  (POS.0840), taken from the principal in a sentence when he offers
  one, never demanded; the ledger row is registration only. The
  principal alone directs how and when a source is used, in whatever
  work he chooses. When source content does enter the intent, it is
  his explicit act, cited with provenance to the file; what someone
  said in a meeting is never silently promoted to the principal's own
  position. A set of related files — a downloaded site with its index,
  a document with attachments — may live as a subdirectory
  `sources/<slug>/`: one source, one ledger entry, immutable as a
  whole from registration. File-level detail is not lost: provenance
  in the intent cites individual files by path, and the bundle's index
  or extract lists its contents. If a bundle's files ever need
  separate fates, a file may be split out to its own ledger row — the
  ledger is freely rewritten. Isolated files stay directly in
  `sources/` as before. Every bundle carries a `00-INDEX.md`
  catalogue in the shape POS.0840 owns; `/ingest` creates it at
  registration when the bundle lacks one and validates a supplied one
  against the contents, origin dates best effort, never asked for.
  Text extracts are produced by
  `scripts/doc2md.ps1` (engine: markitdown, installed separately),
  never by ad-hoc parsing — no Python PDF reading, no manual
  transcription. `/ingest` runs the script file by file on every
  binary the principal chooses to convert (POS.1040), in bundles as
  well as for isolated files; the output is `sources/<slug>.md`, the
  source itself.
- **POS.0840** Resources have an index. Every `sources/` and
  `research/` directory carries a `00-INDEX.md` (the resource index):
  a light catalogue so that Claude — and the principal — know what
  resources exist and what they are for without re-reading the files.
  It is a working aid, not a record of thinking: it tracks nothing (no
  processing state, no positions) and is an automatic input of no
  command. `/forge`, `/critique` and the challengers do not confront
  the chain with the material on their own; a contradiction between
  the intent and a source is not a finding, because the source may be
  a counter-example, a mere inspiration or a record of what someone
  else said. Claude reaches for a file by its own judgement or when
  the principal asks ("check the assessment against the requirements
  in file X"). Each entry has fixed fields in free text — for sources
  *What / Origin / Role / Use for*, for research *Question / Answer in
  short / Consult when*; Role is free text with recurring examples (a
  standard to verify against, inspiration, a counter-example, a
  meeting record), never a fixed vocabulary. The ledger holds
  registration only — a Sources table and a Research table, no content
  columns — so that nothing is described in two places. A bundle keeps
  its own `00-INDEX.md` inside and appears in the top index as one
  entry pointing into it: two levels, never deeper, and the top index
  never repeats the bundle's contents. The bundle index is the same
  catalogue one level down: a YAML header (bundle, project, date,
  origin), one paragraph saying what the whole is and why it entered
  sources, and one entry per file in the same fields;
  `templates/index-bundle.md` is the full skeleton `/ingest` creates
  the file from, its entry carried verbatim from `templates/index.md`.
  One shape for every index, because Role and Use for are what an
  index is for and a table does not carry them (decided 2026-09-04,
  history 3.23). The index is freely rewritten like the ledger while
  the files under it stay immutable. `/ingest` and `/research` write
  the entry when they place the file (the bare `/ingest` sweep fills
  gaps), `/new-project` scaffolds both indexes from
  `templates/index.md`, and the `light` check verifies index against
  directory — a file without an entry or an entry without a file.
- **POS.0190** Artefacts are written once per iteration round, not once
  per answer — and this holds for any working conversation over the
  intent or open items (a `/forge intent` interview, a thread sweep,
  resolving findings), whatever the entry door. Answers are carried in
  the conversation and reflected back; at the round's natural end
  Claude asks whether to write and writes on the principal's
  confirmation — one version bump and one Version History row however
  many answers the round contained. The principal may at any moment
  order a write of whatever is agreed so far. Writing after every
  exchange buries the substantive change under changelog churn and
  makes the Version History unreadable.
- **POS.0710** A project may spawn renders: audience-specific outputs
  generated from the chain — a pitch for the group, an architecture
  picture, an executive summary, the repository README. A render is
  never edited by hand; the iterated thing is its **recipe**
  (`recipes/<recipe>.md`): inputs (one artefact or several), audience,
  instructions and the literal output template in one file, versioned
  by the house scheme and composed conversationally with the
  principal. `/render <recipe>` regenerates the output mechanically
  into `renders/<recipe>.md` — or the recipe's optional `output:`
  path — undated, overwritten freely, history in git. Every render
  opens with YAML front-matter provenance citing the recipe and every
  input with their versions; the ledger's Renders table mirrors it. A
  render assigns nothing and is not part of the chain: the artefacts
  remain the sole source of truth. The boundary between the two is
  authorship, not audience: a chain artefact is composed by the
  principal (Claude proposes, the principal composes), a render is
  generated from artefacts — an article the principal writes is a
  layer of the chain, its translation is a render. Visible YAML provenance was chosen
  over an invisible comment deliberately: provenance is control
  information, the audience rarely meets raw Markdown, and GitLab does
  not display front-matter. Dated hand-made editions of the earlier
  derivative convention remain in place as legacy history. Recipes are
  tools, not records of thinking: they carry a version and an updated
  date in front-matter — enough for a render to cite — and no status
  field, because a recipe is never approved and stays 0.x for life.
  Being versioned, a recipe keeps its Version History in the companion
  like every versioned kind (POS.0310); the companion records what
  changed in the recipe at its own grain, the substantive turns live
  in the intent. Recipes are deliberately loose: the template fixes the
  structure and what information appears where, never the wording — a
  presentation recipe says what belongs on a slide, not its phrasing
  or its placement on a picture. Each rendering re-derives the words
  from the current inputs; fixing the text in the template would turn
  the recipe into the render and make the inputs meaningless. A
  render may also serve as an input of another render — a deck slide
  citing an architecture picture as `render: <file>` — provided the
  citing recipe declares it among its Inputs, so provenance and
  staleness track the dependency.
- **POS.0720** README.md is a render of the forge project. Its recipe lives
  at `projects/forge/recipes/readme.md` with `output:` pointing at the
  repository root; the natural inputs are this intent and CLAUDE.md.
  README.md is never edited by hand: content fixes go into the recipe
  or the inputs, and the file is regenerated: a process change is
  complete only once the intent is updated and the README re-rendered.
- **POS.0730** Release notes are a log of releases, not a story.
  `RELEASE-NOTES.md` in the repository root is a render (`/render
  release-notes`, recipe `recipes/release-notes.md`) for one reader:
  the user of the engine who has cloned it and takes upgrades through
  `forge-pull`. One section per release of the engine — every
  `/release` (POS.1100), the version being the intent's, 3.12 as much
  as 3.0 — newest first, headed `<version> — <date>`; inside it fixed
  groups in a fixed order — *Action required* (what the user must do
  in their projects after pulling), *Added*, *Changed*, *Removed*,
  *Fixed*, *Rejected* (a direction dropped, with its REJ or DEC) —
  one sentence per change from the user's side with a pointer (a
  position, a decision, a command, a script), empty groups omitted, a
  release that changes nothing for the user carrying that one line.
  An approved major is headed "approved", opens with two to four
  sentences of highlights and names its tag among them where one
  exists; no other narrative, and no Unreleased section — nothing is
  unreleased at the moment of a render, which only `/release` runs.
  At a major the minors since the previous major are folded into it:
  the major's section carries every Notes line of the span in the six
  groups, a line superseded by a later minor dropped so that only the
  final state remains, and the sections of those minors disappear
  from the file — the house scheme's own reading of a major ("the
  next approved version, incorporating all changes since") and the
  field's folding of pre-releases into the final release; the detail
  per version stays in the history companion. Between majors every
  release keeps its section. The sections are compiled, not
  distilled: every line comes from the Notes block of the intent's
  Version History rows (POS.0310), pruned and ordered by the render,
  never classified by it. Released sections are carried over verbatim
  from the previous edition and never change retroactively; only
  factual corrections ordered by the principal touch one, through the
  recipe. A thought project's release notes work the same way from
  the Notes of all its chain artefacts but the brief — intent,
  assignment, later layers — for the recipients tracking it (genre
  skeleton `templates/recipe-release-notes.md`, `/recipe
  release-notes`). Reason: a reader wants to see plainly what was
  added, changed and removed — the shape the written standards and
  the established projects share (research
  `2026-09-05-good-release-notes.md`), and the one the forge's first
  render had inverted. Decided 2026-09-05 by walkthrough, closing
  THR.0310 (history 3.35–3.38, where the migration of the whole
  history is recorded).
- **POS.0810** Regenerated renders pass under the principal's eyes.
  Regeneration is stochastic: the same inputs never guarantee the
  same words, so an unreviewed regeneration is an unreviewed edit of
  an outward-facing document. Two light defences, neither of them a
  gate (POS.0430): a recipe pins load-bearing wording as fixed
  text — what is pinned regenerates verbatim (a title, a claim, a
  fixed line) while everything else re-derives freely — and a
  `/release` that regenerated renders reports in its summary
  what materially changed in them, so the principal rules on the
  delta before the release commit without reading a full diff. A render is
  regenerated only by `/release` (POS.1100) or by the principal's
  explicit `/render`; Claude never regenerates on its own judgement — it
  reports staleness and offers (decided 2026-08-30). Only the README and the
  release notes have a freshness rule — the next `/release` regenerates
  them; every other render is as stale as the principal lets it be,
  and `/check` says nothing about it (POS.0570).
- **POS.0960** A project has a kind, `kind: thought | library`, declared
  in the YAML header of its ledger, default `thought` — today's projects
  unchanged. The rules of a kind live in the engine; the project carries
  only the data marker, and its optional `CLAUDE.md` stays polish, never
  kind rules (that would copy the engine into the project).
  `/new-project` scaffolds by kind, the `/forge` map reads a library as
  material rather than as a project waiting for a brief, `/check`
  requires no chain of a library and reports a project that is not a
  repository — with the one-line way to initialise it — as a fact, never
  as a defect (POS.0940). "Chain" was considered as a kind name and
  dropped: nothing could be pictured under it.
- **POS.0970** A library is a project of kind `library` — no chain: a
  ledger, `sources/` and `research/` with their indexes,
  `recipes/readme.md` and the README it renders (POS.1000) — a
  collection of documents used across projects, prefix `lib-`, its own
  repository and therefore its own visibility. Nothing is redefined:
  `/ingest` by file or link, or an upload and a sweep, registration and
  index as everywhere. Two kinds of material exist: a thought project's
  sources are inputs as of a date and immutable; a library's documents
  are maintained by an owner who is also their author — overwrite, or a
  new version beside, is the owner's choice (a deck template's previous
  version is irrelevant; a requirement-writing convention may usefully
  say "supports v1 and v2"). Another project cites a library document by
  path. The citation is a cross-repository dependency taken knowingly:
  only someone with both repositories can read it, the assignment is
  self-contained anyway, the version in the citation is a visible,
  unguarded pin, and a check is added when it hurts. The library is not
  a condition of publication: the intention is decided, the
  implementation comes with the first library.

### Structure and style of an assignment
- **POS.0200** Structured items with stable IDs beat prose, even at very
  high abstraction. Narrative is confined to Purpose & Context and
  Objective.
- **POS.0210** An assignment assigns; it does not solve. What keeps a
  document an assignment is the kind of content, never its amount.
  The formerly enumerated ban — stakeholder matrices, RACI, impact
  analyses, MECE decompositions, tables of contents — originated in
  one early case and is not a universal rule: any such apparatus may
  appear where the principal judges it part of setting direction; it
  is the recipients' machinery only when it belongs to executing
  delivery. (THR.0120 closed by this decision, 2026-08-17.)
- **POS.0220** IDs use the format `PREFIX.NNNN` with three-letter
  prefixes, numbered in tens, each new group starting at the next
  hundred. IDs are global and stable, never renumbered; items may move
  between groups freely. Groups are plain headings with no IDs, no
  metadata and no lifecycle; depth is capped at two levels.
- **POS.0230** Prefix vocabulary, aligned with the group BRD standard
  where an equivalent exists: REQ, OOS, CON, ASM, DEL, TBC, SCR in the
  assignment; POS, THR, REJ in the intent; FND, CHL, DEC internally. No
  universal standard for prefixes exists; this is a house convention
  derived from the group's own.
- **POS.0240** Every assignment carries a Terms section listing the
  prefixes and any domain terms it actually uses, so it can be forwarded
  without oral tradition. Defined Terms are capitalised in item text.
- **POS.0250** Requirements are written as shall / shall not, in full
  correct UK English sentences, one idea per item, each written once.
  Would, could, should, might, may and MoSCoW wording are not used.
- **POS.0260** No priorities and no priority column. Everything in an
  assignment is essential; an exception carries a note reading
  *optional*.
- **POS.0270** Testability is recommended, never required. Assignments
  are deliberately high-level; delegating concretisation through a DEL
  item is a legitimate outcome, and the critic reports untestable wording
  as a recommendation, not a finding.
- **POS.0280** Success criteria are wanted but not compulsory. Delegating
  them to the recipients as a deliverable ("define success criteria and
  return") is a legitimate outcome, not a defect.
- **POS.0290** An item must not depend on an external link to be
  understood, agreed or later tested. Negative mandates (out of scope,
  do-not) rank equally with positive ones. FR / NFR markers may appear in
  item text where they help; they are never part of the ID.

### Versioning and state
- **POS.1080** A project's documents fall into five groups and
  thirteen kinds, and the kind determines what a document is, who
  writes it, whether it is versioned and how it behaves. "Document" is
  the word for every file of a project; "artefact" is reserved for the
  documents of the chain — the ones the principal composes, the
  reviewers read and the renders are generated from. The table is the
  one page from which all of this is read, in the intent, in CLAUDE.md
  and in the README alike:

  | Group | Kind | Meaning | Written by | Versioned | Behaviour |
  |---|---|---|---|---|---|
  | artefacts | brief | the idea as the principal wrote it | principal | yes | locked at 1.0, then immutable |
  | artefacts | intent | current understanding for principal and Claude: positions, threads, rejections | Claude, principal composes | yes | rewritten freely |
  | artefacts | assignment | the direction handed to the recipients, self-contained | Claude, principal composes | yes | rewritten freely |
  | artefacts | later artefacts (BRD, RFP, article…) | further layers, each derived from the one above | Claude, principal composes | yes | rewritten freely |
  | records | history | what changed in a versioned document, and why | forge | — | append-only |
  | records | decisions | the principal's decisions with reasons | forge | — | append-only |
  | records | review, challenge | one dated reviewer run | reviewer agent | — | immutable |
  | state | ledger | single source of truth for state | forge | — | freely rewritten |
  | state | index | catalogue of a resource directory | forge | — | freely rewritten |
  | rendering | recipe | how a render is made | Claude, principal iterates | yes | iterated, never approved |
  | rendering | render | audience-specific output, never a source of truth | generated | — | overwritten by /render |
  | resources | source | external input as it arrived | external, /ingest | — | immutable |
  | resources | research | durable answer to one question | Claude, /research | — | immutable |

  Every versioned kind keeps its Version History in an append-only
  companion `<file>.history.md` (POS.0310); an integer version is
  approved, and a recipe never is. A functional binary — a `.potx`
  template, a graphic — is a source (POS.1040), so a library's assets
  fall under resources without a kind of their own; a library carries
  no artefacts and no records, the other groups unchanged. The
  assignment is not "frozen" in any sense the file would show: it is
  rewritten freely between approvals like the intent, and what the
  recipients hold is a version reached by a link into git — the word
  was dropped because it described the handover, not the document.
  Decided 2026-09-04 (history 3.23).
- **POS.0300** Versioning follows the group BRD convention: integers
  denote signed-off versions. Drafts run 0.1, 0.2 …; 1.0 is approved;
  1.1, 1.2 … are changes made after approval, not yet approved
  themselves; 2.0 is the next approved version. Status in front-matter
  (`draft | in_review | approved | superseded`) must agree with the
  number. A major of the forge intent closes a set of features the
  principal names — 4.0 closes the engine's operating layer: the git
  doors, the release notes, the contracts, the skills layout, the
  checks — and passes more than a minor before its tag: every check,
  `single-source-of-truth` included, both critic lenses and one
  challenge, their findings settled or deferred by his word. The word
  closes the major; the test says what the word attests (CHL.0190,
  2026-09-06).
- **POS.0310** Every versioned document keeps its Version History
  (Version | Modification | Author | Date — human-readable, what changed
  and why) in an append-only companion `<file>.history.md` beside it,
  never in its body: the body is the current state, the companion the
  record. One rule without exception — brief, intent, assignment, every
  later artefact and the recipe alike; a brief that arrives finished
  has one row, a brief born in the forge one per round. The document's
  front-matter carries version, date, status and a machine-written
  `last_change:` line summarising the newest row, written by the same
  write step that appends the row, never by hand, so the two cannot
  drift. The row of a chain artefact other than the brief — the
  intent, the assignment, every later layer — closes with a **Notes**
  block: after the prose, one line per change that reaches the reader
  of the release notes, each opening with its group (Action required,
  Added, Changed, Removed, Fixed, Rejected) and carrying a pointer, or
  the one line "nothing for the reader"; written with the row, by
  whoever made the change, so that the release notes (POS.0730) are
  compiled from fresh lines and never classified afterwards. A Notes
  line has two sides, in this order: what changed — the fact, with its
  pointer — and then, after "For you:", what it means for the reader:
  what they can now do, must do or can no longer do. Neither side
  alone is a line: a fact without its consequence describes the
  system, a consequence without its fact loses what changed, and no
  recipe can supply a missing side, since the render compiles and does
  not rewrite. The brief has no Notes (its history is a draft and a
  lock, mined into the intent's rows), nor has a recipe (a tool, not
  the project's content). The row in the companion is the single
  primary: the commit messages `/save` and `/release` draft and the
  release notes are derivations by mechanism, which POS.1070 permits —
  a record rendered twice is not a procedure stated twice. The
  companion is part of its document: not a row of the ledger, handed
  over with it by the link into git, read by a reviewer that needs the
  document's trajectory and by nobody who needs its current state —
  every command and isolated agent that loads the document is spared
  a history that had grown to 40 % of this intent. A Version History
  table in the body of a document is a `/check` finding, fixed by
  moving it into the companion — that is how a project migrates to
  this convention (POS.0820), on the principal's word, project by
  project, each saved by its own `/save`; a colleague's project meets
  the rule at its next `/check` after `forge-pull`. Decided
  2026-09-04, closing THR.0260 (history 3.21; research
  `2026-09-03-version-history-placement.md`, whose split by kind the
  principal rejected as two rules for one thing); the Notes block and
  its two sides 2026-09-05 with THR.0310 (history 3.35–3.37; research
  `2026-09-05-good-release-notes.md`).
- **POS.0320** Immutable documents (a locked brief, reviews, challenges,
  sources, research) are never edited — a brief from its lock, a source
  from its registration, the others from creation; corrections happen
  downstream.
- **POS.0330** State lives in files, never only in conversation. A
  session can be ended at any point without loss; `/ledger` re-orients
  from the ledger. One project per session is the hygienic default.
- **POS.0820** Artefacts do not expire with the conventions.
  Conventions evolve continuously and `/check` measures against the
  current ones — but an artefact remains valid under the conventions
  it was written to: nonconformance of a finished or dormant project
  is a fact to report, never a defect to chase. Bringing a project
  to newer conventions is an explicit migration decision of the
  principal, made per project and never assumed.

### Review
- **POS.0400** Isolated kinds of review of one shape: the critic
  (document quality, findings FND) and the challenger (substance of the
  thinking, challenges CHL). Both run as isolated subagents on the
  session model that never see the working conversation — that blindness
  is the source of their value; both are invoked by hand by the
  principal, `/critique <lens>` and `/challenge <persona>`; both produce
  an immutable dated report and ledger rows; both are settled by
  walkthrough (POS.0850). The challenger has personas, the critic has
  lenses: one agent file each, the shared behaviour of the kind
  preloaded from one contract skill (POS.1120), only the Lens section
  its own (the engine check guards the preload, POS.1120). Both take
  an optional target, an artefact named
  as `/forge` names it (`brief`, `brief-<name>`, `intent`, `assignment`,
  later layers as they come); without one, the whole chain, so that
  one file or one transition can be reviewed alone (2026-09-03). Neither runs at a save; `/release` offers `critique essence` once,
  in a sentence, and runs no reviewer on its own — the one lens that
  guards what a release publishes, the drift of the chain (decided
  2026-09-05 at the THR.0220 round, POS.1100).
- **POS.0410** The critic has two lenses, because one critic hunted
  formalities and never guarded the chain (history 3.10). `clarity`
  reads each artefact on its own: ambiguity, internal contradiction,
  duplication, scope hygiene, Requirement style, the advisory
  checklist. `essence` reads the chain: for every adjacent pair
  (brief → intent, intent → assignment, every later layer) it first
  distils, blind, the essence of the downstream artefact in a few
  sentences, then the upstream's the same way, and compares —
  substance lost without a trace (REJ, DEC, DEL, TBC, the ledger's
  mining state), substance added without provenance, meaning shifted,
  provenance that does not hold; a finding is a difference of
  essences, not of texts, and the report carries both distillations.
  A target narrows `clarity` to that artefact and `essence` to that
  artefact against its parent — a transition is addressed by its
  downstream artefact, since every layer has exactly one parent, so
  no arrow is ever typed. Regression against resolved findings is
  every lens's first step over its own reports, the retired single
  critic's reports divided between them by category; FND IDs stay one
  global sequence; each run produces a delta report (new / verified
  resolved / still open / newly obsolete). Untestable wording and
  missing delivery-stage apparatus are findings of no lens. Decided
  2026-09-03.
- **POS.0420** `/challenge <persona> [artefact]` reviews the thinking
  through a chosen persona — one isolated agent per persona
  (`challenger-<persona>`), each defined by the blind spots it exists to
  find. The target may be any artefact of the chain, the whole chain
  when none is named — each challenge then names the artefact it
  concerns: the challenger reads the whole chain for context and
  challenges the substance of the target. The contract is
  invariant whatever the persona: no stake in the principal being right;
  unstated assumptions, whether the stated objective is the real
  problem, second-order effects, organisational reality, failure modes,
  missing dimensions, the serious counter-case; three to seven sharp
  challenges, each with a severity (dealbreaker | major | minor, ordered
  by it — a fatal flaw is never buried among cosmetics), a falsifiable
  "what would change my mind" and an epistemic status (consensus |
  active debate | emerging practice | my judgement); no fabrication — a
  precise "I don't know" beats an invented figure, and anything
  reconstructed from memory is flagged. The contract has one
  owner, the skill `challenger-contract` (POS.1120): every persona file
  names it in its front-matter and writes only its own Lens — who it is
  to the principal and which blind spots it exists to find
  (POS.1120 for the guard of the preload).
  The first persona is `cto` (CTO register);
  further personas — a strategist, a business analyst — are created from
  the lens-file skeleton by the principal's decision when first needed, and only
  where their blind spots genuinely differ: personas that would say the
  same things in different words are noise. Bare `/challenge` lists the
  roster and recommends a fit for the project's subject. Challenge files
  carry the persona in their name (`YYYY-MM-DD-challenge-<persona>.md`);
  the CHL sequence stays global per project.
- **POS.1120** The shared behaviour of a kind of reviewer is a contract
  skill, preloaded — never a copy. Each kind — the critic, the
  challenger, check (POS.0540), whatever comes after — owns one skill
  `.claude/skills/<kind>-contract/SKILL.md` (`critic-contract`,
  `challenger-contract`, `check-contract`; the suffix because `check/`
  is the command, POS.1130), named in the front-matter (`skills:`) of
  every lens, persona or check file of that kind, which then carries
  its front-matter and its Lens section and nothing else; Claude Code
  injects the whole skill at launch. One skill per kind, because the
  shared texts differ almost whole; the few sentences common to all
  stay in each contract in its own words — three contracts and no
  common skill, reopened only if a fourth kind repeats them. A
  contract is addressed to every lens of its kind, never a template
  with placeholders: it opens with what the contract owns (conduct,
  subject, way of working, report shape, ledger step) and what the
  lens file owns (what it reads, what it goes after, its categories,
  its own report sections), and carries the overlap rule — a lens is
  a specialisation, never a replacement: it may make a rule stricter,
  never rename, drop or duplicate one; the protocol changes in the
  contract — because the contract lands after the lens's own text and
  the agent must know which yields. The contract never names a lens;
  the lens file does. The skill is `user-invocable: false` (out of the
  `/` menu; its description stays in the session's context —
  `disable-model-invocation` would also forbid the preload) with a
  description saying it is preloaded. `templates/critic.md`,
  `templates/challenger.md` and `templates/check.md` are the skeletons
  of a lens file; the engine check verifies that every skill an agent
  names exists, since a missing one is skipped silently. Facts of the
  mechanism: the skill arrives at the end of the first user message,
  after the task, not in the system prompt; a headless `--agent` run
  preloads nothing, so reviewers run as subagents only. Decided
  2026-09-06 after a trial (history 3.40), built and confirmed on
  every kind the same day (3.41–3.46). Closes THR.0270.
- **POS.0430** Nothing blocks. There are no hard quality gates;
  checklists and findings are advisory and the principal alone decides
  what is published.
- **POS.0440** Every finding and challenge is either fixed or explicitly
  overruled with a recorded reason (DEC). Overruling and parking are
  legitimate outcomes; silently ignoring is not. An accepted challenge
  must change the intent, otherwise it was not accepted.
- **POS.0450** An artefact is best challenged before the next layer is
  first derived from it — the intent before the first assignment, one
  day a BRD before the solution design — while accepted challenges are
  still cheap to absorb. Whether it runs again later — after a draft,
  before approval — is left to the judgement of whoever is running the
  process; no rule prescribes it. (THR.0040 → DEC.0020, generalised
  from "before the first draft" when the challenger was opened to any
  artefact; the reasoning of the decision is unchanged.)
- **POS.0790** Isolation is not independence. The author, the critic
  and the challengers share one model family; what that family
  systematically cannot see, none of them will find, and agreement
  between the reviewers is therefore never treated as validation —
  it only means the artefact is consistent under one set of priors.
  The calibration point lies outside: review by humans or by a
  different model family, invited at the principal's discretion —
  independent different-family challengers are planned (POS.0800).
  External human review of the forge by experienced practitioners
  has already taken place and shaped it through the ordinary door,
  like any other input. A challenge may inspire, but supplied
  content follows POS.0070 — nothing enters the intent because a
  reviewer wrote it, only because the principal composed it — and an
  accepted challenge may change the intent by subtraction as readily
  as by addition (POS.0440 read accordingly).
- **POS.0800** Independent challengers will be built: challenger
  personas running on a different model family than the author's,
  composed by the principal in Microsoft AI Foundry and invoked from
  the forge over a CLI link, so that `/challenge` can send in a lens
  with genuinely different priors. The direction is decided; the
  mechanics are designed when taken up.

### Operating environment
- **POS.0500** The engine is one git repository, `forge-of-thought`
  (POS.0990), full name **Forge of Thought** in documents: the universal
  core in the root (`CLAUDE.md` for the agent, `README.md` for humans,
  `templates/`, `scripts/`, `.claude/`) together with `projects/forge`,
  the system's own project. User projects live under `projects/<slug>/`
  as git repositories of their own, ignored by the engine (POS.0940); a
  per-project `CLAUDE.md` is polish only where genuinely needed.
- **POS.0510** Commands are entry points into phases, not the only
  permitted door; the core rules apply in ordinary conversation too.
- **POS.0520** Protection relies on Claude Code's permission system,
  not an OS-level sandbox: commands and file operations run under
  permission prompts and allowlists, shared deny rules in
  `.claude/settings.json` block sensitive paths (`~/.ssh`, `~/.aws`),
  and web access is approved per domain on first use. OS-level
  sandboxing was tried on 2026-08-04 and deliberately dropped: it is
  unavailable on Windows, where enforcing it meant no shell at all.
- **POS.0530** This work is reasoning-heavy and token-light, so the
  strongest available model tier is the default — the session model,
  chosen once, with no per-agent pins (POS.0930).
- **POS.0540** Mechanical conformance runs on the same mechanism as
  the critic and the challenger (POS.1120): its own contract skill,
  one agent per kind of check, a roster, a run by hand. Whether it is
  called a review is not decided and does not matter to the
  mechanism, which takes further kinds as they come. The checks and
  their composition are POS.1140's. Read-only and advisory: they report and
  propose, the principal decides what is fixed. They check
  conformance, never substance or document quality — that remains the
  critic's and the challenger's territory.
- **POS.0550** The engine is persisted in git with a remote of its own,
  `main` the released line, branches allowed and left to git
  (POS.1110); every user project is likewise a repository with
  whatever remote and visibility its owner gives it. The scripts in
  `scripts/` are the only door to git — reading state included, no
  exceptions; how many there are is whatever the door needs, never a
  rule. The scripts that serve the engine and every project that is a
  repository (`projects/<slug>/.git`): `forge-save.ps1`
  (stage–commit–push; bare, the engine and every project with changes,
  each its own commit; with a slug, that repository — `forge` meaning
  the engine; auto-generated commit message unless given; remote
  changes reconciled by rebase; without an origin, commit and a note;
  `-Tag <name>` sets a tag on the commit and pushes it, POS.1100; never
  `git add -f`, never `git clean`), `forge-pull.ps1` (fast-forward
  only, refuses over unsaved work; bare, the engine — which is the
  upgrade — and every project with a remote; with a slug, one),
  `forge-status.ps1` (engine and every project: unsaved changes, the
  branch it is on, last commit, origin or "not under git"; changes
  nothing), `forge-clone.ps1` (brings an existing project in,
  POS.1060: clones a repository into `projects/<repository name>`,
  never overwriting, and sets that repository's local commit identity
  only when given `-Name` and `-Email`) and `forge-branch.ps1`
  (creates a branch or switches to one, `main` included, bare reports
  the branch and lists the branches, and nothing else, POS.1110). No
  remote is configured anywhere in the forge: git carries that
  information itself. Immutability of documents remains a process rule
  enforced by convention, not by git.
- **POS.0570** The project's full conformance — the `project` check,
  for the engine `engine` too — and the renders belong to the release,
  the `light` check to the save. `/release` (POS.1100) runs the checks
  POS.1140 composes for it and settles their findings with the
  principal before the release commit: fixed, or explicitly accepted;
  deferred findings are recorded in the ledger under "Waiting on
  principal". The recommended procedure, never a gate: nothing blocks
  (POS.0430). `/release` then renders what POS.1100 names,
  unconditionally, with no staleness test. The renders come after the
  check and its walkthrough, not before: a render made from the
  settled sources is current by construction, whereas one made before
  it goes stale whenever a finding bumps the intent. `/save` runs the
  `light` check only (POS.1100, POS.1140): the full check cost minutes
  and a walkthrough at every save. The staleness of any other render
  is the principal's business alone: the `/forge` map shows it,
  `/check` never reports it, since a render is regenerated only on his
  word (POS.0810). The check at the release rather than the save
  decided 2026-09-05 (history 3.33), the order check-then-render the
  same day (history 3.30), the light check 2026-09-06 (history 3.44),
  the staleness rule 2026-09-04 (history 3.23).
- **POS.1100** Save and release are two commands. `/save` runs the
  `light` check (POS.1140) and then commits and pushes on whatever
  branch is checked out, through `forge-save`, no render: a message
  proposed and confirmed, the script run, seconds. `/release` runs on
  `main` only and refuses elsewhere, naming the branch: the checks
  POS.1140 composes, with their walkthrough (POS.0570); the README and
  release notes from the settled sources (POS.0730, POS.1000,
  POS.0810); the release commit "release <intent version>" and, at an
  approved major, the tag `v<major>` — both `/save` run by `/release`
  with the release message, not a second procedure (POS.1070). Named
  without a slug it asks which repository, never sweeps; it offers
  `critique essence` once and runs no reviewer on its own (POS.0400).
  The release number is the intent's version (POS.0730). Tags:
  `v<major>` at every release of an approved major, proposed by
  `/release` and confirmed by word — a rule of the procedure, not a
  gate in the script; any other tag on request, `/save -Tag` or
  `/release -Tag`, on a branch as well, the name free, `v<intent
  version>` proposed when none is given; the script pushes the tag
  with the commit and keeps it without an origin. Only the major's tag
  has a fixed name, so `/check` and the release notes can rely on it:
  an integer is a released major, anything else a snapshot. Why two:
  the renders cost minutes and over a hundred thousand tokens at every
  save, and the two-speed save had existed in practice for weeks; with
  the renders at the release only, the README on `main` is current at
  every release and stale in between visibly (the `/forge` map), never
  silently. Decided 2026-09-05 (history 3.33); closes THR.0220;
  alternatives REJ.0160, REJ.0170.
- **POS.1110** Branches are voluntary and belong to git. Whoever wants
  one gets it through one forge command — `forge-branch <name>` creates
  the branch or switches to it, `forge-branch main` switches back — and
  never types git; merge, rebase and conflicts stay git's, by hand or by
  merge request, and `forge-status` reports the current branch. Nothing
  forces a branch: whoever does not use them works on `main`, saves and
  now and then releases, and sees none of this. The forge's only
  knowledge of a merge is that `/release` runs on `main` after it and
  its checks find what two branches broke — the known hole, left
  until it happens: two parallel branches taking the same next free ID.
  The boundary against the wrapper of git the principal does not want:
  the script does creation and switching, which only change where the
  next commit lands, and nothing that rewrites history. Grounded in a
  colleague's practice (history 3.33); the forge stays a single-user
  tool per instance, more people means more instances and
  coordination by git (bearing on THR.0090). Decided 2026-09-05 with
  POS.1100.
- **POS.0580** Work on the chain is invoked by target state, never by
  verb: `/forge <state>` (`/forge intent`, `/forge assignment`) —
  knowing the name of the target artefact is knowing the command, with
  nothing to memorise as layers are added. Bare `/forge` reports the
  map: which artefacts exist at what versions, which states can be
  worked from here, which renders are stale, and a recommended next
  step. Mechanics: a thin dispatcher (`.claude/skills/forge/SKILL.md`)
  plus one definition file per state
  (`.claude/skills/forge/states/<state>.md`, a supporting file of the
  dispatcher, POS.1130), each declaring its own
  inputs — so the chain is a star, not a fixed line: a future layer
  branches from any artefact by adding one file, the dispatcher
  untouched. `/clarify` and `/draft` were retired without aliases on
  2026-08-15.
- **POS.0590** Everything the forge produces is Markdown, renders
  included: a presentation is a `.md` saying what is on each slide
  (mermaid for pictures). The forge still ends at content, but it
  carries one delivery-format tool at its edge: `scripts/md2pptx.ps1`
  (POS.0740) turns a Markdown deck render into a `.pptx`. The
  Markdown render remains the sole source of truth; the `.pptx` is a
  generated output of second order — regenerated at will, never
  edited by hand. All other format conversion stays outside the
  forge, as git is for persistence.
- **POS.0740** `scripts/md2pptx.ps1` generates a PowerPoint file from
  a Markdown deck definition through headless Claude Code
  (`claude -p`) with Anthropic's official pptx skill (plugin
  `document-skills` from the `anthropics/skills` marketplace,
  installed separately per user, as markitdown is for `doc2md`). The
  conversion is done by a model, never by a deterministic converter,
  because deck definitions are deliberately free-form and may
  themselves contain instructions for the LLM — slide content,
  speaker notes, diagrams to redraw as native shapes, visual
  directions. Template handling: `-Template <path>` names a `.potx`
  file by path — typically a document of a library project
  (POS.0970), e.g. `projects/lib-<name>/sources/<name>.potx`; without
  the parameter Claude designs the visual style itself. There is no
  default template and no bare-name lookup. The output defaults to the input's directory
  and basename with a `.pptx` extension, so a deck generated from
  `renders/<recipe>.md` lands as `renders/<recipe>.pptx`, tracked in
  git like any render output; `-Out` overrides. The headless run's
  model is chosen by `-Model`, default opus; a presentation recipe
  may recommend one in its Build instructions.
- **POS.0770** Recipe composition may be guided by genre:
  `/recipe <genre>` mirrors the `/forge` star (POS.0580) — a thin
  dispatcher (`.claude/skills/recipe/SKILL.md`) plus one definition file
  per genre (`.claude/skills/recipe/genres/<genre>.md`, a supporting
  file of the dispatcher, POS.1130) carrying the
  elicitation checklist, with the genre's canonical skeleton in
  `templates/recipe-<genre>.md` extending the base recipe shape,
  never replacing it. Bare `/recipe` lists the roster; a recipe
  outside any genre stays legitimate, composed conversationally from
  `templates/recipe.md`; naming an existing recipe iterates it
  through the same lens. The first genre is `presentation` — a
  slide-by-slide deck definition whose render `md2pptx.ps1` turns
  into a PowerPoint file — distilled from the first deck recipe;
  its interview covers audience and register, the one
  message, inputs (including renders as picture sources), dramaturgy,
  speaker notes and traceability citations, on-slide density, diagram
  policy, language, vocabulary discipline, confidentiality, and the
  Build instructions copied verbatim into the render for the
  deck-builder LLM. The genre is named "presentation" rather than
  "deck" for company-wide legibility at rollout.
- **POS.0830** The forge runs beyond Windows. `scripts/` is the only
  platform-bound layer, and its scripts are written to run unchanged
  on Linux and macOS: they are PowerShell 7, which is itself
  cross-platform (`pwsh`, one install on a non-Windows machine), and
  they use nothing Windows-only — paths composed with `Join-Path` or
  forward slashes, no `cmd`, registry or Windows-only cmdlets,
  `$IsWindows` only where the platform genuinely differs, external
  tools (`git`, `markitdown`, `claude`) resolved from PATH, and usage
  examples in the scripts' help free of Windows-specific paths and
  invocations. Instance facts are out of the scripts: no remote URL,
  no author identity, no first-run initialisation — git configuration
  is the user's (POS.0950). Portability is verified by running the set on Linux
  (WSL suffices); until then it is a writing rule, not a claim.
- **POS.0940** Mechanism of the engine/projects split. The engine is a
  clone; the projects are nested git repositories in a gitignored
  `projects/*` with `projects/forge` re-included (`!projects/forge`; the
  pattern must be `projects/*`, not `projects/`, or the re-include fails
  silently). The engine does not know the projects: the scripts
  recognise a project by the presence of `projects/<slug>/.git` —
  without it, status reports "not under git" and save and pull skip it;
  with it, they commit and push to its origin. `git init` and the remote
  are the user's one-off act: `/new-project` and `/spinoff` create files
  only and never touch git, and a project starting "not under git" is a
  property, not a defect. A project without a repository, or with a
  repository and no origin, is a legitimate shape — a sensitive project
  kept local; the second keeps the history the renders and recipes rely
  on, the first does not. Upgrade is `forge-pull` on the engine — a
  fast-forward of `main`; the engine receives the git tag `v<major>` at
  every release of an approved major of this intent, and any tag on
  request (POS.1100). A project records no engine version: `/check`
  measures it against the current conventions. That is the whole
  migration path of any instance, the principal's and a third party's
  alike: after `forge-pull`, `/check project` on each project says what
  the conventions changed, the release notes' Action required lines say
  what to do, and Claude migrates on the user's word; no migration tool
  exists, knowingly (DEC.0100). Verified by test (research
  `2026-08-29-git-engine-projects-separation.md`); shapes rejected:
  REJ.0150. Decided 2026-08-29 (history 2.21); closes THR.0130.
- **POS.0950** The engine carries no instance facts. Who the principal
  is (by role) and what language the conversation runs in live in
  `CLAUDE.local.md` at the engine root — gitignored, created from
  `templates/CLAUDE.local.md` and filled by `/setup` on a new machine
  (POS.1050); the root is where Claude Code looks for it, and
  everything there reaches every subagent, the isolated reviewers
  included (THR.0240). Therefore only what must be always-on and is
  harmless in a public report lives there; the git identities —
  names, e-mail addresses, hosts — live beside it in
  `identities.local.md`, gitignored, loaded by nobody, read by path
  by the three commands that set an identity (`/setup`,
  `/new-project`, `/import-project`), and every reviewer contract
  forbids instance facts in a report (CHL.0170; the split of an
  existing instance file is the user's act on the release notes'
  word). The session model lives in `.claude/settings.local.json`
  (POS.0930). `CLAUDE.md` names the principal and the conversation
  language only as things that exist, never by value; the artefact
  language stays English (THR.0180). The scripts carry no URL and no
  identity (POS.0830). The commit identity is a property of the
  project, not of the host: set locally in every repository (`git
  config user.name` / `user.email`) at its creation or import,
  proposed by the command layer from the roster in
  `identities.local.md` — matched by the origin's host, an offer,
  never a rule — and set on the principal's word; no per-host
  `includeIf`, since the host is only a correlate of the identity
  and fails where one host serves two roles, and a file outside the
  engine is beyond its boundary. The one global guard, offered by
  `/setup` (POS.1050), is `user.useConfigOnly = true` with no global
  `user.name`/`user.email`: a commit in a repository with no local
  identity then fails aloud instead of silently taking a default (a
  surviving global identity defeats the guard, and `/setup` says
  so). A user's own configuration — per-host includes included —
  remains his business and a legitimate way to resolve an identity.
  `forge-save` checks that git resolves an identity for the
  repository and, where it resolves none, reports it with the command
  to set one and commits nothing until it is. Decided 2026-08-30
  (history 3.0), the identity model 2026-09-01 (history 3.6–3.8), the
  identities file 2026-09-06 (history 3.46). Resolves the scripts
  part of THR.0090.
- **POS.0930** One model for the whole forge. Every command, chain
  state and reviewer runs on the session model; the reviewer agents
  declare `model: inherit` explicitly, so that the strongest model the
  forge runs on is a decision and never an accident of a pin that has
  aged. Speed is bought with context, not with weaker models:
  `/render` generates in an isolated subagent that sees only the
  recipe and its inputs, never the working conversation — the same
  principle as the reviewers', applied to a mechanical job — and a
  command's `effort:` remains the lever for routine turns should one
  ever need it. Per-command pinning to a faster model is rejected for
  now: the routine commands are a small share of the work and slow for
  the size of the context they carry, not for the model, and every pin
  is a convention to keep. A per-recipe `model:` is deferred until a
  recipe is genuinely mechanical: in a test a smaller model loosened
  pinned wording, dropped prescribed elements and leaned on the
  previous render instead of the recipe — the drift POS.0810 guards
  against (history 2.13). The session model is chosen in one
  deliberate place, `.claude/settings.local.json` — an instance
  preference, gitignored (POS.0950). The one exception is
  `scripts/md2pptx.ps1`: a headless run has no session model, so the
  script needs a default of its own (`-Model`, POS.0740) — an
  explicit parameter, not an aged pin. The same lever carries the
  checks: every check executes its own definition in an isolated
  subagent that sees only the files, returning the report for the
  walkthrough in the session, and `/release` launches its renders in
  parallel (which command renders what is POS.1100's); the working
  conversation is spent on verdicts, not on reading. Decided
  2026-08-27 (history 2.13), the isolation of checks and renders
  2026-09-02 (history 3.10); closes THR.0160.
- **POS.1070** One mechanism lives in one place and is used from
  there. Whatever the forge already has a procedure for — a command,
  a skill, a script, an agent — is invoked through that procedure
  whenever its situation arises, never re-described ad hoc:
  `/release` regenerates the README and release notes through
  `/render` and ends by running `/save`, git is touched through the
  scripts in `scripts/` (POS.0550), reviews run through the reviewer
  agents. A command that needs another's mechanism references it by
  path and adds nothing of its own to how it runs; the rules of a
  mechanism — isolation, wrapping, provenance, what may be read — are
  written once, in its own definition. Restating a procedure in a
  second place is a defect: the two copies drift, and the copy without
  a rule silently loses it. The `single-source-of-truth` check carries
  the standing rule — a restated procedure, a reviewer file restating
  what its contract skill owns (POS.1120), a direct operation where a
  script, command or agent exists — over the whole operating layer,
  run on the principal's word and never at a release on its own
  (POS.1140), so that the rule costs a release nothing and the sweep
  is honest when it runs. Where a shape had no owner at all, it gets
  a skeleton rather than a second description: the bundle catalogue
  (`templates/index-bundle.md`), the library reduction of the ledger
  (`templates/ledger.md`'s header). Raised by the principal
  2026-09-02 after a render made outside `/render` arrived unwrapped
  (history 3.10).
- **POS.1090** The harness enforces the principal's word where it
  can. A command that writes, scaffolds, commits or regenerates —
  `/save`, `/release`, `/spinoff`, `/setup`, `/new-project`,
  `/import-project`, `/ingest`, `/render` — carries
  `disable-model-invocation: true` in its
  front-matter, so that Claude cannot start it on his own judgement:
  the principal invokes it by slash, or asks in words and Claude
  follows the command's definition read by path, as the dispatchers
  do. The state and genre files behind `/forge` and `/recipe` carried
  the same field while they were registered as commands; since
  POS.1130 they are supporting files registered as nothing and need
  no guard. Maps, reports and rosters (`/forge`, `/ledger`, `/check`,
  `/critique`, `/challenge`, `/research`, `/recipe`)
  stay model-invocable, since Claude is meant to propose them. The
  guarantee of Step by step (CLAUDE.md, Working methods) thereby
  rests on the harness as well as on CLAUDE.md, and the descriptions of the guarded
  commands leave the always-on context. Decided 2026-09-05 at the
  walkthrough of the harness critique (FND.0210, FND.0190).
- **POS.1130** The commands are skills. Every command lives as
  `.claude/skills/<name>/SKILL.md`; `.claude/commands/` no longer
  exists. The state files of `/forge` and the genre files of `/recipe`
  are supporting files of their dispatcher
  (`.claude/skills/forge/states/<state>.md`,
  `.claude/skills/recipe/genres/<genre>.md`): read by path, registered
  as nothing, carrying a description and no registration field. The
  reviewers' contracts (POS.1120) are skills of the same directory,
  not user-invocable. "Command" stays the word for what the user
  invokes by slash; "skill" names the file shape, commands and
  contracts alike. Grounds: in Claude Code custom commands have been
  merged into skills — a command file and a skill of one name create
  the same `/name` and work the same way, existing command files keep
  working, skills are the recommended form — and a skill adds what
  this layer wants: supporting files without registration, `context:
  fork` with an agent type (set aside, POS.1140), named `arguments`.
  No context gain: a command's body and a skill's alike load only
  when invoked, so THR.0240 is untouched. A skill shadows a command of
  the same name, so a migration is whole, never partial. Every
  `argument-hint` is quoted: a front-matter with CRLF line endings and
  an unquoted hint of two bracketed items fails to parse, and the
  harness then shows the body's first line as the description.
  Decided and migrated 2026-09-06 (history 3.43); closes THR.0330,
  resolving FND.0260.
- **POS.1140** Check runs on the reviewer mechanism — POS.0540 decided
  it, this is the shape. One command `/check <check> [slug]`, bare the
  roster; one contract skill `check-contract` — conformance only,
  read-only, findings only with `file:line`, the rule's owner and one
  fix, ranked by severity; a report returned to the session, nothing
  filed and no ID sequence, since a check's findings are settled at
  the walkthrough and recorded by the session where they change
  something; one agent per check, `check-<name>`, front-matter and
  Lens only, from `templates/check.md`; the roster open, a new check
  one file. The first checks, each owning one concern and none
  another's: `project` — structure, IDs, assignment style, language,
  immutables, recipes and renders; `light` — front-matter against the
  companion, the ledger against the files, dependencies, resource
  indexes, fit for a save; `engine` — the core against itself and the
  forge intent, the rename sweep; `single-source-of-truth` — the
  whole operating layer for restatements and direct operations
  (POS.1070), the honest sweep, expensive by design, run on the
  principal's word before a major or after a round on the operating
  layer, never by `/release` on its own, a project on request. A rule
  an older position attributes to `/check` as one procedure belongs
  to the check that owns its concern by this list — bookkeeping,
  ledger, dependencies and indexes to `light`, structure, recipes and
  renders to `project` — never to two. Composition is the caller's
  and checks never call each other: `/save` runs `light`; `/release`
  runs `light` and `project`, for the engine `engine` too, launched
  at once; anything else is the principal's word. The engine is
  checked as `/check engine`, the forge project as `/check project
  forge`; `/check-forge` is gone. The word for a check's variants is
  "check" — the light check, the project check — the mechanism's name
  serving for its members. `context: fork` is set aside: the field
  fixes the agent type in a skill's front-matter, so it cannot serve
  a dispatcher that chooses an agent by argument; the isolation stays
  what `/critique` and `/challenge` do — the Agent tool with the
  target path and nothing else (POS.0930). Decided 2026-09-06 by
  walkthrough of THR.0290 and built the same day (history 3.44); the
  `/research` point stays in THR.0290.

### Naming
- **POS.0600** The system is named **Forge of Thought**: thoughts are
  the raw material — of whatever kind, nothing is presumed about them —
  and forged assignments are the product. Chosen with the full-chain
  vision in mind (assignment → BRD → architecture → full realisation
  deck); "Assignment Studio" was dropped because it named only the first
  segment and only the first audience. Repository `forge-of-thought`
  (POS.0990), slug `forge` for the system's own project under
  `projects/`, full name in documents; the short form "Forge" is
  expected in daily speech.
- **POS.0610** Project slugs are lowercase and hyphenated on disk;
  display names may differ. Programme naming is used where a family of
  initiatives is expected: FLOW (Future Lean Operating Way), first
  instance FLOW:BA → slug `flow-ba`. Names must be legible to the
  audience, not only to the principal.
- **POS.0620** The README subtitle is "*A workshop where thought is
  tempered and shaped.*" Any subtitle or one-line description must
  present the forge as a place and space where thoughts are forged; it
  must not name the assignment as the goal, because the assignment is
  only where version 1 of the chain happens to end. "Forging thoughts
  into assignments" was dropped for exactly that reason; "A forge for
  thought" was dropped as a tautology of the name.

### Growth path
- **POS.0700** The principal intends to keep extending the engine
  downward: thoughts are forged as far as he needs them taken. The BRD
  layer is certain to come; solution architecture and integration are
  intended; a strategy layer is possible if it proves to make sense.
  Which layers are added, and in what order, is open — possibly all of
  these, possibly none yet. Nothing is approved for construction: the
  mechanics of a layer (commands, agents, reviewer calibration) are
  designed when that layer is actually taken up, not in advance. An
  earlier `/elaborate` mechanics proposal was withdrawn as premature.
  The layers below the assignment grow in the same project, by the
  same principal's hand, when he chooses to take his own thought
  further — a BRD as his next layer, not as someone else's
  deliverable. What a recipient does with an assignment in his own
  instance is his own forge run: the assignment becomes his brief, by
  his hand today (an assignment is self-contained for exactly that),
  by a command of its own only when that day comes (THR.0090). The
  chain never spans two principals (CHL.0140, 2026-09-06).
- **POS.0760** The forge is split into a public engine and user projects
  in repositories of their own. The engine — the core together with
  `projects/forge` — is public and contains nothing sensitive and no
  instance facts (POS.0950, POS.0980); users keep their projects
  wherever they choose and are themselves responsible for what those
  contain and where they live, generated decks carrying corporate
  branding included. Decided on 2026-08-29 from
  `00-brief-public-engine.md`; the mechanism is POS.0940.
- **POS.0780** The forge is a general tool for forging thoughts, and
  a forge run ends where its owner is satisfied: the outcome is an
  artefact the principal stands behind — nothing further. An intent
  may be immaterial and carry no delivery at all; the chain's
  mechanics are domain-agnostic — the same machinery that forges a
  platform assignment would forge a D&D campaign: an intent of the
  story, then materials rendered for the DM. Sponsorship, funding,
  adoption and delivery outcomes are outside the forge's scope and
  outside its sight. The door stays open, not closed: the forge may
  one day feed a delivery chain, and experience from use flows back
  through the ordinary door — the principal, via `/forge intent`
  (POS.0170) — as input like any other; whether a delivery side
  would be grown layers of the forge or a separate framework is
  deliberately undecided (THR.0140). The forge itself is developed
  at the principal's discretion and pace, by his needs and by the
  feedback its company rollout returns: direction may be named
  (POS.0700), destinations and deadlines are not.
- **POS.0980** Publication. The engine is the principal's to publish: it
  was built outside any work assignment and lived on the company's git
  only because it carried work information not yet separated. The
  audience, in order: rollout in the company first, at the same time a
  public project around which a community may form, and a showcase of
  the principal's work; the split also lets access be granted per
  project, where before a collaborator had to be on everything. The
  boundary for the public `projects/forge`: nothing company-specific by
  name — no company name, no URLs, no e-mail addresses, no content of
  the company projects; the slugs of the company projects stay, since
  that projects of those names exist and travelled the chain is a
  process fact, not content (THR.0210 draws the line); a
  forbidden-term list is no guard, since a grep catches names, not
  content. Before publication the forge project was rewritten within
  that boundary **including its immutable documents** — immutability
  knowingly broken, once, recorded in the ledger and nowhere in the
  files; the brief was rewritten into English before its lock for the
  same reason, a one-time yield of POS.0060. The public repository
  starts with a fresh history of one commit (DEC.0080); the full
  record stays on the company host, archived read-only, with a notice
  naming the new homes and the tag `pre-split` as its last complete
  state. Until a public exemplar exists (THR.0200) the README carries
  no example project. Separating the company projects from the engine
  without publishing would have been a fallback only if publication
  were long and complicated; it was not. Decided 2026-08-29 from
  `00-brief-public-engine.md`, executed 2026-08-30 (history 2.21,
  3.0; research `2026-08-29-split-migration-runbook.md`).
- **POS.0990** The public face. The engine lives at a public repository
  of the principal's, named `forge-of-thought` — the bare word "forge"
  is overloaded on every code host and says nothing in a search — under
  the licence **CC BY 4.0**: anyone may use and adapt the engine, and
  must credit the author and link to the repository. The README
  therefore names one person, the licence holder — the author with a
  contact address — as a fixed text of the readme recipe, and this is
  not an instance fact: it is who the work is by, whoever runs an
  instance. The `LICENSE` file carries the licence's verbatim legal
  code. Decided and executed 2026-08-30, with the first public commit.
- **POS.1000** Every project has a README and, if it is a thought
  project, release notes — both renders of the project's own recipes
  (`recipes/readme.md`, `recipes/release-notes.md`, `output:` in the
  project root), exactly as the engine has them (POS.0720, POS.0730;
  POS.0810 for the review of the regenerated output): the recipe is what
  is iterated, the render is never edited by hand, and every `/release`
  of the project regenerates both after its check (POS.1100). A library has a
  README only — a catalogue of what it holds and how to use it, from its
  ledger and indexes — since release notes are compiled from the
  Notes lines of an intent's history rows, which a library does not
  have; its history is git. The two recipes are genres of `/recipe` (skeletons
  `templates/recipe-readme.md`, `templates/recipe-release-notes.md`),
  scaffolded by `/new-project` and expected by `/check`; the ledger's
  Renders table carries them like any render. Every README closes with
  one fixed sentence, part of the readme genre: reading the repository
  needs nothing beyond a Markdown viewer, maintaining and evolving it
  needs Forge of Thought — the engine, linked
  (github.com/pche-broken-artist/forge-of-thought) — so that whoever
  finds the project knows what runs it (principal's decision
  2026-08-30). The engine's own README is the one exception: the
  sentence exists to point a visitor to the engine, and the engine's
  README is that destination (3.6).
- **POS.1010** A project may carry an icon: `logo.png` in the project
  root, supplied by the principal, picked up as the repository avatar by
  hosts that do so. Optional — a project without an icon is complete;
  `/check` does not report its absence. No `assets/` directory exists;
  one is introduced only when images beyond the logo appear.
- **POS.1020** A project registers what it relies on outside its own
  repository. The ledger carries a Dependencies table — path, library,
  used by, note — with one row per document of another repository the
  project cites: a deck template named in a recipe, a library document
  an index entry or a position refers to. Registration only, like
  sources: what the document is for lives where it is used. No version
  is recorded — a library document is maintained by its owner and cited
  as a moving target by design (POS.0970). `/check` verifies that every
  registered path exists on disk and reports a library that is not
  cloned alongside; an index entry or recipe pointing outside the
  project without a row is a finding. The `/forge` map says which
  libraries the project needs, and the project's README carries the same
  line. `/ingest` registers the row when the principal directs a project
  to a library document instead of copying it. Rationale: a
  cross-repository citation is a dependency taken knowingly (POS.0970) —
  knowingly means written down where state lives, not discovered when a
  render loses its template.

- **POS.1030** The forge's behaviour lives in the engine, never in the
  assistant's private memory. Claude Code keeps a per-directory memory
  outside the repository; whatever it learns there about how the forge
  should work — a working method, a rule of a command, a convention — is
  written into CLAUDE.md, the commands or the templates and removed from
  memory, so that every instance of the forge behaves the same and a new
  user meets the same forge as the principal. Memory is left with what
  is personal to one principal — his idiom, his private choices — and
  instance facts go to `CLAUDE.local.md` and `identities.local.md`
  (POS.0950). Decided 2026-08-30 at the audit before the first fresh
  deployment (history 3.0).
- **POS.1040** A source has one form. A file in `sources/` is either
  text or a functional binary, never both by default. At `/ingest`
  every binary file — isolated or inside a bundle — gets one question:
  convert to Markdown? Yes: `doc2md` writes `sources/<slug>.md`, and
  that extract is the source — tracked in git, registered in the
  ledger, catalogued in the index with Origin "extract of `<original>`
  (markitdown)", immutable from registration; the original is not
  copied into the project, and where it already lies in `sources/` it
  is added to `sources/.gitignore` and stays local. No: the binary is
  the source as a functional thing — a deck template, a graphic, a
  logo — copied, registered and catalogued as is, with no extract.
  Text files get no question. Keeping both is the exception, on the
  principal's explicit word. The ledger's Sources column reads Form
  (`text | extract of <original> | binary`); the `light` check treats
  a binary without an extract and an extract without its original as
  the normal case. Reason: the repository carries what the forge works
  with — text — and a binary nobody reads from git is weight without
  use; a binary that is used as a thing is kept because it is used.
  Transition: the convention applies from its date on; extracts made
  before keep their `.extract.md` names, and a binary already in git
  beside its extract leaves the index on the principal's word, never
  automatically. Decided 2026-08-30 (history 3.1).
- **POS.1050** First run is one command. After cloning the engine,
  `/setup` prepares the instance: it fills `CLAUDE.local.md` from
  `templates/CLAUDE.local.md` in an elicitation interview — who the
  principal is by role, the conversation language — and
  `identities.local.md` from its template with the git identities per
  host (POS.0950), and it creates `.claude/settings.local.json` with
  the session model set to **Fable**, without asking: the strongest
  available model is the forge's default (POS.0530), the whole forge
  including the blind reviewers runs on it (POS.0930), and a
  newcomer's first minute is no place for a model decision. The
  command says in one sentence that Fable was set and that `/model` or
  editing the file changes it at any time. `/setup` never overwrites:
  an existing instance file or `settings.local.json` is reported as it
  stands, not replaced. The git-identities interview closes with an
  offer: the global guard of POS.0950 — `user.useConfigOnly = true`
  appended to `~/.gitconfig`, read first, never overwriting existing
  content — written on the user's word; declined, printed for him to
  apply by hand. Where `~/.gitconfig` carries a global `user.name` or
  `user.email`, `/setup` says the guard only bites once that identity
  is removed and offers the removal, again only on his word. `/setup`
  runs no git operation — the user's git configuration file is the
  one thing it may edit outside the engine, on his word. Named
  `/setup`, not `/init`: Claude Code's built-in `/init` generates a
  CLAUDE.md, and the collision would send a newcomer to exactly the
  wrong action at the most sensitive moment. Decided 2026-09-01 after
  a newcomer's first run (history 3.7–3.8).
- **POS.1060** A project arrives through the scripts-only door.
  `/import-project <git-url>` brings an existing project into the
  forge: it calls `scripts/forge-clone.ps1` (POS.0550), which clones
  the repository into `projects/<repository name>` — no slug
  parameter: the directory falls out of the repository's name, and a
  nonconforming name is fixed by renaming the directory afterwards —
  refuses to overwrite an existing directory, and reports facts: the
  last commit, the origin, the commit identity git resolves for the
  fresh clone, and whether the project carries a ledger with a `kind:`
  header (its absence is a fact, not a defect). The script carries no
  identity (POS.0830): it accepts `-Name` and `-Email` and sets the
  repository's local commit identity only when given both. The
  command layer passes `-Name`/`-Email` by default: the identity is a
  property of the project (POS.0950), proposed from the roster in
  `identities.local.md` by the URL's host and confirmed or overridden
  on the principal's word. It runs the script bare only when the
  principal says his own git configuration resolves the identity, and
  the script reports which one the clone resolved; a clone left with
  no identity is caught by `forge-save`, which reports and commits
  nothing (POS.0950). Work then starts by selecting the project —
  `/forge <slug>` — because the engine does not track it and cannot
  guess it.

## Open threads

- **THR.0090** Multi-principal use. Current working assumption: a second
  principal receives Forge — including the `forge` project itself — via
  git and runs their own instance. How genuine multi-user operation
  would work is an open point for the future; deliberately not being
  worked on now. One case named 2026-09-06 (CHL.0140, POS.0700): an
  assignment handed to a colleague's instance as his brief — how it
  is seeded, how the IDs continue, where the essence lens finds a
  parent; this thread's, when it is taken up.
- **THR.0140** The delivery side. Whether the forge's output one day
  feeds a delivery chain as grown layers of the forge or hands over
  to a separate delivery framework is open and deliberately not
  worked on now; it is taken up when a subject project first needs
  the linkage — flow-ba is a natural candidate.
- **THR.0150** Replacing the PowerShell scripts with POSIX `sh`.
  Considered: a single `scripts/*.sh` set (POSIX, no bashisms — macOS
  ships bash 3.2), run on Windows in Git Bash, which comes with Git
  for Windows and is required by Claude Code anyway — so no platform
  gains a dependency, unlike the `pwsh` install POS.0830 asks of
  non-Windows users; from PowerShell the call is
  `sh ./scripts/<name>.sh …`, Claude calls them directly. The
  principal is undecided whether to do it at all; no priority while
  PowerShell 7 suffices. If taken up: the set is replaced whole, never
  run side by side. Already excluded: a dual `.ps1` + `.sh` set (two
  truths drift apart) and a rewrite in Python (a dependency without
  benefit; Python stays only for markitdown).
- **THR.0170** Branch documents. Considered on 2026-08-27 alongside
  POS.0920 and deferred as too heavy for now: a working document per
  large whole (`branches/<name>.md` — a verbatim seed followed by
  positions and threads worked like the intent, states `open | merged
  | dropped`, merged into the intent with provenance or dropped to a
  REJ). To be taken up only if a brief in draft turns out to need
  structured, position-level work before it can be locked and mined;
  until then a draft brief is the branch.

- **THR.0180** The output language. POS.0060 makes English the
  language of every artefact as a rule of the forge; the principal
  stated on 2026-08-29 that it is not — it is his own rule, enforced
  by him, for the company projects of this instance, and a project
  with Czech output is conceivable. The rule therefore belongs to the
  instance or the project, not to the engine that is to become public
  (00-brief-public-engine.md). Deliberately left as is: more than one
  output language is to be solved when a project needs it — where the
  choice lives (instance default, per-project override), what stays
  English as notation (ID prefixes, `shall`, status words), how the
  reviewers and `/render` read it. The first project with Czech output
  opens it — planned as the first project after the split.
- **THR.0190** A plugin as a later distribution layer. Claude Code
  plugins would give the only real upgrade channel and project =
  repository, but a plugin carries no `CLAUDE.md`, and commands are
  discovered only up to the repository root — so it forces changes
  nobody needs yet: shortening the core to a bootstrap skill injected by
  a SessionStart hook (as Superpowers does; its repository `CLAUDE.md`
  is for contributors only), rewriting the commands from
  `projects/<slug>/` to the repository root, solving multi-project
  operations. A `CLAUDE.md` split is not a cheap step: 435 lines, and
  moving half the rules from always-on to on-demand is a behaviour
  change ("200 lines" is a recommendation, not a limit). `@import` of
  the forge `CLAUDE.md` into a user's works but carries only
  `CLAUDE.md`, not commands and agents. No preparation now; taken up
  when `forge-pull` proves an insufficient upgrade channel. Research:
  `2026-08-29-claude-code-packaging.md`,
  `2026-08-29-framework-distribution-in-the-field.md`.
- **THR.0200** The public face: an exemplar project for the README — the
  forge itself, or one created later; the company projects cannot
  travel. Until one exists the README carries a one-sentence placeholder
  (readme recipe 0.24). Repository name and licence settled in POS.0990.
- **THR.0210** A guard rail for the public boundary. The rewrite before
  publication (POS.0980) found the leak surface where the challenge
  predicted it: the forge project's own artefacts quoting the substance
  of subject projects — a sentence of a company intent in a CTO
  challenge, a deck's name in a position. A grep before a push is a net,
  not a rule. Wanted: a standing rule that `projects/forge` never
  carries the *content* of a subject project — only process facts: that
  a project exists, its versions, dates and counts — and a home for it:
  CLAUDE.md, the challenger and critic prompts (they read the subject
  projects as evidence), a check as a sweep, or all three. Opened
  2026-08-30 at the principal's direction.
  **Parked 2026-09-03** by the principal: the risk is small while he
  knows of it, and a rule with its checks would add weight the forge
  does not need now; not closed, to be taken up when the boundary is
  next at stake (a publication of a further project, a reviewer run on
  `projects/forge` with subject projects in reach). Claude's proposed
  solution, recorded for that day: a check, not a critic lens, and
  not the check alone. Not a lens, because the critic reads the chain
  and the leak surface lies outside it — challenges, research notes,
  templates, recipes, README — and a lens runs on the principal's word
  while the boundary must hold before every push; the matter is a
  convention of the repository, which is the engine check's job at
  every `/release` of the engine. Not the check alone, because a check
  catches a leak after it is written, and challenges, reviews and
  research are immutable from creation and written by isolated agents
  that read subject projects as evidence — a leak there is repaired
  only by breaking immutability again. Hence two homes: a check of
  its own owning the rule (POS.1140) (the engine — core, operating
  layer, `projects/forge` with its immutable documents — carries no
  content of any subject project; a process fact is admissible:
  existence, slug, kind, versions, dates, states, counts, commands run;
  content is not: a position, a requirement, a quoted or paraphrased
  sentence, a deliverable's name, a person, an organisation, a host;
  verified by reading, never by a term list, POS.0980), and one
  sentence under Inputs in both contract skills (POS.1120) citing
  that item, reaching every agent.
  CLAUDE.md deliberately left out: the rule concerns one project, not
  every session, and THR.0240 argues against another sentence in the
  core. A position under the next free POS number records the
  decision when it falls.
- **THR.0230** A common engine beneath several frameworks. Opened
  2026-09-03 at the principal's direction; a large rebuild if taken up,
  to be worked out first and decided later — the principal is not sure
  it is a good idea. The idea: whatever every framework needs alike is
  lifted out of the forge into an engine they share — git through the
  scripts, the ledger and its upkeep, versioning and Version History,
  the ID scheme, isolated agents on the session model, recipes and
  renders, sources and research with their indexes, `/save` and
  `/check`, `/setup` and the instance facts — so that a new framework is
  written as content only. Forge of Thought becomes the first framework
  on that engine, not the engine itself; the picture is several small
  cooperating frameworks on one engine, not one large one that absorbs
  everything (much could be pushed into the forge, but CLAUDE.md is
  already large — THR.0240 — and the separation helps there). Two
  further frameworks named as the concrete cases: a product framework (a
  screen described functionally per module, one artefact per module,
  HTML prototypes rendered from them) and a project-management framework
  (inputs from the forge's assignments; later meeting inputs over which
  an agent runs unattended, sorting tasks and new requirements into
  artefacts — Markdown or otherwise — or handing them on through MCP;
  verification of an implementation against its assignment; a high-level
  idea). What they show about the boundary: the chain is the framework's
  (its artefacts, their number, order and templates); "everything is
  Markdown" is a forge rule — the engine carries recipe and render, the
  framework names the output form; a dependency between frameworks is
  the Dependencies mechanism across a framework boundary; the ledger's
  tables are partly the framework's (tasks); agent types beyond the two
  (a verifier) are the framework's.
  *Agents.* Critic and challenger alike: the mechanism — isolated
  subagent, ledger record, states, walkthrough — is the engine's, the
  prompt content the framework's. Challenger personas are the
  framework's (a UX challenger, a challenger of a work plan). For the
  critic a nested point: what is generic (consistency, formal
  correctness) and what is the framework's — in the forge the drift
  brief → intent → assignment, perhaps further down.
  *How the engine reaches a framework at every session* — no decision
  now, every path recorded: one engine repository with the frameworks as
  directories in it (simplest, one `forge-pull` upgrades everything, but
  one CLAUDE.md and one command tree for all); the engine as a Claude
  Code plugin with each framework a repository of its own (the cleanest
  boundary; the finding of THR.0190 applies — a plugin carries no
  CLAUDE.md, so a bootstrap skill by SessionStart hook — the largest
  rebuild); engine and framework as two repositories joined by `@import`
  and a clone alongside (CLAUDE.md travels, commands and agents do not —
  copied or linked). THR.0190 is from now read as part of this question
  and stays a thread of its own.
  *Order of work.* The second framework must exist in outline before the
  boundary can be drawn; the engine is not built ahead of it. Where the
  engine is thought: here as a thread for now — it may become the first
  thread turned into a project of its own; the principal undecided.
  THR.0220 was settled on today's forge at 3.33 (POS.1100) as an engine
  matter that carries over; THR.0210 stays open on the same
  recommendation. CHL.0150 (2026-09-06, parked until after 4.0): since
  3.0 every new position has been the engine's and the boundary is
  being drawn by accretion; taken up after 4.0 if the split proves
  useful.
- **THR.0240** The size of CLAUDE.md. 523 lines on 2026-09-03 and
  growing with every iteration; THR.0190 already records that a split
  moves rules from always-on to on-demand and is a behaviour change, not
  a cut. To be dealt with sooner or later whatever becomes of THR.0230,
  which would help. Opened 2026-09-03 at the principal's direction. To
  think through: what must be always-on, what can live in commands,
  skills and templates and be read when its situation arises, and how
  the effect is measured — by behaviour, never by line count. Measured
  2026-09-06 at the THR.0270 trial (POS.1120): every reviewer subagent
  receives, in its first user message before the task, the whole
  CLAUDE.md together with `CLAUDE.local.md`, the assistant's memory
  file and the git status — about 600 lines, the largest block of its
  context, several times its own agent body and contract together; the
  instance facts of `CLAUDE.local.md` (principal, language, git
  identities) thereby reach an isolated reviewer that needs none of
  them. The cost of CLAUDE.md is paid once per reviewer run, not once
  per session.
- **THR.0250** Two suggested functions: an expander and an essence
  manager. A tip the principal received on 2026-09-03 — where from not
  recorded. The essence manager got its detail the same day: at the end
  of the chain a blind agent, without context, distils the essence of
  the final document by itself, and that essence is checked against the
  brief to see how far the whole intent drifted. The `essence` lens of
  the critic (POS.0410) is that mechanism applied to every adjacent pair
  of the chain; whether an end-to-end distillation is a further thing or
  the same lens run brief-to-last-layer is open. The expander has a name
  only. Parked until more detail arrives.
- **THR.0290** Research on the reviewer mechanism. What `/research`
  gains from kinds — the principal's idea of 2026-09-04 alongside the
  checks, which became POS.1140 — deferred on 2026-09-06 by his word:
  one command with one output today; taken up when a second way of
  researching appears. Opened 2026-09-04; the check half closed at
  3.44.
- **THR.0300** A user's private layer. Whoever runs the forge may
  want reviewers, checks or other agents of their own, for themselves
  only, with no ambition of contributing them to the engine — the
  principal's idea of 2026-09-04, offered as possibly interesting, no
  priority. It would need a place the engine does not know and
  `forge-pull` never overwrites, on the pattern of `CLAUDE.local.md`
  and `settings.local.json` (gitignored), and the rosters of
  `/critique`, `/challenge` and `/check` would list what lies there
  beside the engine's own. Open: how a local agent takes the shared
  contract skill (POS.1120), what happens when the engine renames or
  reshapes it, and
  whether Claude Code's own user-level agents already serve. Opened
  2026-09-04.
- **THR.0320** A harness lens. The principal's direction of
  2026-09-05: the critic roster gets a lens `harness` that reviews
  the operating layer — CLAUDE.md and the skills, commands and agents
  of `.claude/` — against current Claude Code conventions, and the
  knowledge comes from the official plugins (`plugin-dev`, whose
  `skill-reviewer` and `skill-development` carry the conventions for
  skills, commands and agents; `claude-md-management`, whose
  `claude-md-improver` reads CLAUDE.md), while the output is the
  classic critic's: a dated immutable report in `reviews/`, FND in
  the ledger, settled by walkthrough like every lens (POS.0400,
  POS.0410). The trial of the same day is the evidence that the
  shape fits a foreign agent (`reviews/2026-09-05-critique-harness.md`,
  FND.0190–0280, filed under THR.0290). Open: the mechanism by which
  `/critique harness` reaches the plugin — a mapping in `.claude/skills/critique/SKILL.md`
  from the lens to the plugin agent with the skeleton's Output section
  carried in the prompt, or an own `critic-harness` agent naming the
  critic contract and the plugin's skills alike in its front-matter
  (`skills:`, the field verified 2026-09-06, POS.1120); the plugin as an
  engine dependency — named by `/setup` and CLAUDE.md, and what the
  lens does when the plugin is absent; whether
  `claude-md-improver`'s rubric, written for codebases (build
  commands, architecture map), serves a constitution like the forge's
  CLAUDE.md beyond its conciseness criterion; the regression step of
  every lens, which the trial skipped. Relation: the first concrete
  kind of THR.0290, and the shape of the operating layer it reviews
  is POS.1120's and THR.0240's question. Opened 2026-09-05.

Note: the ID THR.0120 was inadvertently used twice — first for the
readme-recipe thread (opened 1.14, closed 1.16), then for the
assignment-apparatus boundary (opened 1.24, closed 2.4). Citations of
THR.0120 from POS.0210 and version 2.4 refer to the latter. Recorded
as-is; IDs are never renumbered.

## Rejected directions

- **REJ.0010** `clarifications.md` as an append-only Q&A log. Rejected
  because it left the current state of intent scattered across brief, log
  and assignment, with no single place answering "what do I want now".
  Replaced by `10-intent.md`.
- **REJ.0020** Workstreams as first-class entities with their own IDs and
  lifecycle. Rejected as structure for its own sake; plain heading groups
  plus stable global IDs achieve the same at lower cost.
- **REJ.0030** Hard quality gates blocking approval. Rejected: these are
  assignments for people, and the principal decides what ships.
- **REJ.0040** A templated brief with chapters (goal, high-level idea,
  and so on). Rejected; see POS.0110.
- **REJ.0050** Priority tags on items (`critical`, `important`,
  `nice-to-have`). Originally wanted as an optional attribute, dropped in
  favour of the group BRD convention: everything is essential, exceptions
  are noted as *optional*.
- **REJ.0060** Separate templates per genre of assignment. Rejected in
  favour of one universal skeleton with optional sections, so that
  everything arriving from the principal has a consistent shape.
- **REJ.0070** A dedicated feedback channel for comments coming back from
  the recipients. Rejected; see POS.0170.
- **REJ.0080** Merging document review and substantive challenge into one
  reviewer. Rejected: an agent doing both does neither properly, and the
  formal audit benefits from a clean context while the substantive
  challenge benefits from a different register entirely.
- **REJ.0090** Composite naming such as `BA-FLOW` for the BA initiative.
  Rejected because it destroys the word; `FLOW:BA` keeps both the
  programme and the instance legible.
- **REJ.0100** Single-letter and hyphenated ID prefixes (`R-001`,
  `P-01`). Replaced by three-letter dotted `PREFIX.NNNN` aligned with the
  group BRD standard.
- **REJ.0110** MAJOR.MINOR versioning with MAJOR meaning a scope change.
  Replaced by the group convention where integers denote approval; a
  scope change is a reason for re-approval anyway.
- **REJ.0120** "Mandate" and "charter" as the name of the handover
  document. Mandate rejected outright by the principal; charter carries
  project-management ceremony and implies a project, which many
  assignments are not. "Assignment" retained.
- **REJ.0125** The founding framing "a CTO's tool for briefing his direct
  reports (heads)" as the system's identity. Dropped by the principal on
  2026-07-31: it describes the first instance, not the engine.
  Superseded by the general-engine framing (POS.0005).
- **REJ.0130** "Cascade" as the system name: literally names the
  waterfall. "Foundry" rejected for collisions (Azure AI Foundry,
  Palantir Foundry). "Continuum", "Strata", "Idea Forge" and Czech
  "Kovárna" considered; **Forge of Thought** chosen.
- **REJ.0140** `local/` as the home of user-local files (POS.0750,
  adopted 2.1). Dropped on 2026-08-29: it existed only to keep company
  material out of the repository, which the gitignored `projects/*` now
  does; deck templates live in a library project (POS.0970) and are
  named by path (POS.0740).
- **REJ.0150** Shapes of the engine/projects relation rejected on
  2026-08-29 (research `2026-08-29-git-engine-projects-separation.md`,
  `2026-08-29-framework-distribution-in-the-field.md`): git submodules,
  subtree and worktrees — they model a dependency, which this relation
  is not; the engine as a template repository and copying the engine
  into projects — every comparable project that does so ends in
  manifests, override layers and migrations; a plugin as the only shape
  now (THR.0190).
- **REJ.0160** Stale-only rendering at the save (option A of THR.0220):
  one command as today, `/save` regenerating only a render whose recipe
  or input moved in that save, a `stale (skipped <date>)` mark in the
  ledger for a render skipped on the principal's word. Rejected
  2026-09-05: it saves perhaps a third of the engine's saves and
  nothing on projects, whose README input — the ledger — moves at every
  operation, and it adds a staleness state that `/save`, `/forge` and
  `/check` must all read alike; the two-command shape of POS.1100 saves
  everything and adds nothing.
- **REJ.0170** A fixed working branch with a forge switch that merges
  (option C of THR.0220): a `work` branch per repository, one script
  creating and switching it, `/release` merging it into `main`.
  Rejected 2026-09-05 as the first step towards the wrapper of git the
  principal does not want — merge and conflict logic in the forge's
  hands, two branches a non-developer must understand — while forcing a
  branch on those who do not need one. The switching half survives as
  the voluntary `forge-branch` of POS.1110; the merging half stays
  git's.

## Candidate structure for assignment

Not applicable: this project's handover artefacts are the core itself
(`CLAUDE.md`, `templates/`, `.claude/`) and `README.md`. A
`20-assignment.md` would duplicate them for an audience that does not
exist; see the ledger.
