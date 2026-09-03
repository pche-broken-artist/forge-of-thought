---
project: forge
type: research
topic: where the version history of a versioned working document lives
date: 2026-09-03
derived_from: 10-intent.md v3.13 (principal's question of 2026-09-03; Versioning & status in CLAUDE.md)
status: immutable
---

# Where the version history of a versioned document lives

## Question

Where should the version history of a versioned working document
live — inside the document (a Version History table at its head, as
corporate document control and the house scheme prescribe), in a
companion file (`CHANGELOG.md` style), or only in git (commit messages
and the generated release notes) — so that the document stays readable
for humans and cheap for an LLM that loads the whole file every time it
works on it? The facts behind the question: measured today, the table
is 8,477 of 21,265 words (40 %, 72 rows) in the forge's own intent and
11 % in a brief; the intent is rewritten for coherence, so the rows are
the only prose record of *why* something changed; the same information
exists three times (the row, the commit message the save script
composes from it, the Unreleased head of the release notes rendered
from the rows); and one mechanism lives in one place (prime directive
10). Four areas surveyed on 2026-09-03: document-control practice
(ISO/IEC/IEEE 29148:2018 and 15289:2019, ISO 9001:2015 clause 7.5,
PMI/BABOK-style templates, university records-management guidance),
software practice (Keep a Changelog 1.1.0, Common Changelog,
Conventional Commits 1.0.0, semantic-release, towncrier 25.8.0, Nygard
and MADR ADRs, PEP 1 and PEP 12 as of 2026-08, RFC 7322 and
Internet-Draft practice, Google's docguide, Write the Docs),
Markdown/LLM-era practice (Spec Kit, BMAD v4 and v6, OpenSpec,
LeanSpec, Agent OS; Anthropic's context-engineering guidance of
2025-09-29; Liu et al. 2023 on position bias), and wiki/knowledge
tools (Confluence, Notion, Google Docs, MediaWiki, Obsidian Sync).
Epistemic tags: [V] verified on the page or in the extracted PDF, [S]
inferred from surrounding evidence or memory of a paywalled text.
Status per finding: consensus / emerging / contested.

## Answer in one paragraph

Every family that manages versioned text outside a word processor
keeps the history *beside* the document, not in it: git-native
communities (PEPs, RFCs, ADRs, Google's engineering docs) treat the
repository as the record and add at most a status line, a dated
header, or an optional newest-first summary at the *end* of the file;
changelog practice (Keep a Changelog, towncrier, semantic-release)
keeps a curated, human-written `CHANGELOG.md` as a separate file and
warns against both raw `git log` and full automation; every wiki and
document tool holds history as a separate view; and the AI
spec-driven frameworks carry no history in a spec at all — BMAD had a
Change Log table at the top of its PRD in v4 and dropped it in v6. The
in-document table is a convention of paper-era document control, and
even there the standards do not mandate it: ISO/IEC/IEEE 29148:2018
says revision information "may include" a list of changed clauses and
a list of previous versions, and lets a conforming information item be
"divided into separate documents or volumes"; ISO 9001:2015 asks for
version control and change identification without naming a format;
and the records-management guidance that recommends the table says in
the same breath that it "can be created as a separate document and
filed in the same folder". For the forge the recommendation is the
hybrid: the intent keeps version, date, status and a one-line `last
change` in its front-matter and moves the full table to a companion
`10-intent.history.md`, which becomes the single primary record from
which the save script's commit message and the release-notes render are
derived; the assignment, handed over as one self-contained file and
short-lived in versions, keeps its table where document control expects
it; a locked brief is never touched. This removes ~40 % of the tokens
from every read of the intent by every command and subagent, keeps the
"why" prose one file away, and leaves the three copies as one record
plus two derivations.

## Findings

### A. Document-control practice

1. **ISO/IEC/IEEE 29148:2018 puts revision information at the head,
   as a "may", and as lists, not prose.** Clause 9.2.1 Identification
   [V]: "Include the following identification matter: a) title; and
   b) revision notice. The title and a revision notice uniquely
   identify the document. Revision information may include the project
   name, version number of the document, date of release, approved
   signature, a list of sub-clauses that have been changed in the
   current version of the document and a list of version numbers and
   dates of release of all previous versions of the document." Clause
   9.2.2 Front matter is a table of contents and lists of figures and
   tables — the revision notice precedes them. Annex A.2.1 (OpsCon)
   repeats the wording. Nothing in the standard asks for a
   *description* of each change or its reason; the house table's
   "Modification" column is a house choice, not a standard's. Status:
   consensus (2018 text; the ReqView and well-architected-guide
   29148-derived SRS templates both omit any history section [V]).
2. **29148 itself allows the history to be a separate volume.**
   Clause 4.4 NOTE 2 [V]: "each information item is described as if it
   were published as a separate document. However, information items
   can be considered as conforming if they are unpublished but
   available in a repository for reference, divided into separate
   documents or volumes, or combined with other information items."
   A companion history file is therefore not a departure from the
   standard the house scheme aligns with. Status: consensus.
3. **29148 locates the *substantive* change history with the
   requirements, in the tool, not in the document.** Clause 6.4.3.3
   [V]: "The requirements shall be configuration controlled. The
   ancillary information recorded along with the requirements can
   include a summary rationale for each requirement, decisions,
   assumptions and a change history, along with the requirements
   categorization information described in 5.2.8." History is
   attribute data of items, and the standard expects a requirements
   management tool to carry it. Status: consensus.
4. **ISO/IEC/IEEE 15289:2019** defines generic content per document
   type (clauses 7.2–7.8 Description, Plan, Policy, Procedure, Report,
   Request, Specification; 9.2 Record) [V, contents page of the
   sample]. The generic content list that 29148 inherits — issue date
   and status, scope, issuing organisation, references, context,
   notation, body, summary, glossary, change history — is recalled
   from the paywalled text [S]. Even so read, 15289 names *what* an
   item carries, never *where* in the file. Status: consensus.
5. **ISO 9001:2015 clause 7.5 requires version control, not a
   table.** 7.5.2 asks for "identification and description (e.g., a
   title, date, author, or reference number)"; 7.5.3.2 for "control of
   changes (e.g., version control)" and "retention and disposition"
   [V, quoted via a 2019 commentary]. The commentary notes the
   standard "doesn't require you to write a procedure for how you
   control documented information"; the revision-history table is
   auditor custom, not clause text. Status: consensus.
6. **Records-management guidance recommends the table and, in the
   same paragraph, the separate file.** University of Edinburgh,
   *Version Control* v2 (examples dated 2005–2006) [V]: "The table can
   either be included at the start of the document, for example for
   very formal documents, or it can be created as a separate document
   and filed in the same folder as the document concerned, for example
   for guidance or procedure documents." University of Nottingham,
   *Guidance Document: Version Control* v1.0, approved 2015-05-01 [V]:
   "Version control tables are useful to have at the start of a
   document whilst the document is being developed. Alternatively,
   they can be created as a separate document to that document and
   filed in the same electronic folder for reference purposes only.
   Document Control Tables if used should be inserted on the front
   page of a document." Both distinguish the *document control* block
   (identity, status, approver, next review — front page) from the
   *version control* table (what changed, who, when — front or
   separate). Columns everywhere: version, changes/purpose, author,
   date — the house table exactly. Status: consensus.
7. **PMI/BABOK-style corporate templates** carry a "Document History"
   or "Revision History" block at the front (revision, date,
   description, author) [S — seen in search snippets and in general
   practice; no primary template fetched]. BABOK v3 prescribes
   requirements management and traceability, not a document layout
   [S]. Status: consensus that the block exists at the front of
   Word-era templates; the placement is a template habit, not a body
   of knowledge's requirement.

### B. Software practice

8. **Keep a Changelog 1.1.0** [V]: "A changelog is a file which
   contains a curated, chronologically ordered list of notable changes
   for each version of a project." Principles: for humans, not
   machines; every version has an entry; latest version first; each
   version dated; an `Unreleased` section at the top. The file is
   `CHANGELOG.md` at the repository root — a companion, never inside
   the artefacts it describes — and commit diffs are rejected as a
   changelog because they are "full of noise". Status: consensus.
9. **Common Changelog** [V]: "Using `git log` as a changelog is a bad
   idea: it's full of noise" and "Don't take the easy way out with
   full automation. This results in poor changelogs, defeating their
   purpose." — while "a clean changelog starts with a clean git
   history. Let them strengthen each other." Status: consensus.
10. **Conventional Commits 1.0.0** lists "Automatically generating
    CHANGELOGs" and "Automatically determining a semantic version
    bump" as purposes of structured commit messages [V];
    **semantic-release** "automates the whole package release workflow
    including: determining the next version number, generating the
    release notes, and publishing the package" from commit messages
    [V]. This is the "git only" school: the commit is the primary
    record, the changelog a render. Status: consensus for libraries
    and services; contested for documents (findings 8, 9, 11).
11. **towncrier 25.8.0** rejects both the single shared file and the
    git log [V]: fragments exist because one file "which developers
    all write to" produces merge conflicts, and commits are not read
    because they carry "complex information about the original issue,
    how it was fixed, who authored the fix, and who reviewed the fix"
    that readers of the news do not need — "towncrier delivers the
    news which is convenient to those that hear it, not those that
    write it." Status: consensus in the Python ecosystem.
12. **ADRs carry a status, never a history.** Nygard (2011-11-15) [V]
    names five components — Title, Context, Decision, Status,
    Consequences — and "If a decision is reversed, we will keep the
    old one around, but mark it as superseded." The MADR template [V]
    carries `status`, `date`, `decision-makers`, `consulted`,
    `informed` and no revision section; the status value set is
    `proposed | rejected | accepted | deprecated | … | superseded by
    ADR-0123`. History is git plus the chain of superseding records.
    Status: consensus.
13. **PEPs: git is the record, and the optional in-file summary sits
    at the end.** PEP 1 [V]: "Because the PEPs are maintained as text
    files in a versioned repository, their revision history is the
    historical record of the feature proposal. This historical record
    is available by the normal git commands for retrieving older
    revisions, and can also be browsed on GitHub." `Post-History`
    records discussion dates, not versions. On 2026-02-02 PEP 1 added
    an optional **Change History** section — "Think of this as a
    'changelog' or 'release notes' for the PEP … add a new bullet item
    in newest-first (i.e. reverse chronological) order … This isn't
    mandatory, so it's left to the PEP author's discretion" — placed
    after Footnotes and before Copyright, i.e. the last content
    section of the document; PEP 12 (2026-02-22) added it to the
    template and uses it itself. Status: emerging (seven months old),
    and the clearest precedent for "changelog at the end of the file".
14. **RFCs: no history in the published document; a removable
    appendix in drafts.** RFC 7322 (2014-09) defines the structure of
    an RFC without any history section [V]; Internet-Drafts carry an
    "Appendix A. Change Log (to be removed by RFC Editor before
    publication)" [V, iCalendar venue draft], and the datatracker
    holds each document's history as an external view. The working
    text carries its change log at the *back* and sheds it at
    publication. Status: consensus.
15. **Docs-as-code.** Google's internal Markdown style guide
    (docguide/style.md) [V], under Document layout: "`author`:
    Optional. If you'd like to claim ownership of the document … add
    yourself under the title. However, revision history generally
    suffices." — revision history meaning the VCS log, and the guide
    lists no in-file history section. Write the Docs' docs-as-code
    guide names version control (git) as the history mechanism and
    says nothing of revision tables in documents [V]. Status:
    consensus.

### C. Markdown/LLM-era practice

16. **No AI spec-driven framework keeps an in-file history.** Spec
    Kit's `spec-template.md` carries only `Feature Branch`, `Created`,
    `Status: Draft` and no version or changelog [V]; its constitution
    template ends with a one-line footer — "**Version**: … |
    **Ratified**: … | **Last Amended**: …" — as the *last* line of the
    file, and the `/constitution` command "prepend[s] as an HTML
    comment at top of the constitution file" a *Sync Impact Report*
    (version change old → new, modified principles, added and removed
    sections, deferred TODOs) — a machine-written, last-change-only
    summary that is invisible in the render and overwritten each time
    [V]. OpenSpec records change as `openspec/changes/<name>/`
    proposals with ADDED/MODIFIED/REMOVED deltas, archived on
    completion to `changes/archive/YYYY-MM-DD-<name>/`; the spec file
    itself carries no history [V]. LeanSpec front-matter is `status`,
    `created`, `priority`, `tags`; specs are held under "<2,000
    tokens" because "context rot is real"; a `backfill` command
    derives front-matter dates from git [V]. Agent OS's shape-spec
    produces a folder with no version field at all [V]. Status:
    consensus among the frameworks surveyed.
17. **BMAD dropped its Change Log between v4 and v6.** v4.44.0
    `prd-tmpl.yaml` [V] holds, inside the first section "Goals and
    Background Context", a `Change Log` table with columns `[Date,
    Version, Description, Author]` and the instruction "Track document
    versions and changes" — the corporate pattern imported verbatim,
    at the top. v6.11.0 `prd-template.md` [V] has no Change Log,
    history or version field in any of its sections (0 Document
    Purpose … 9 Assumptions Index). No rationale is published; the
    move coincides with the v6 rewrite towards leaner skills [S].
    Status: emerging — the one framework that had the table removed
    it.
18. **Context cost is a first-order design constraint.** Anthropic,
    *Effective context engineering for AI agents* (2025-09-29) [V]:
    "Context, therefore, must be treated as a finite resource with
    diminishing marginal returns"; "LLMs have an 'attention budget'
    that they draw on when parsing large volumes of context"; "Good
    context engineering means finding the smallest possible set of
    high-signal tokens that maximize the likelihood of some desired
    outcome"; and the recommended shape is progressive disclosure —
    identifiers kept in context, files loaded just-in-time. A history
    table read at every turn but consulted at almost none is the
    textbook low-signal block. Status: consensus.
19. **Position matters, not only size.** Liu et al., *Lost in the
    Middle* (TACL 2023) [V]: "performance is often highest when
    relevant information occurs at the beginning or end of the input
    context, and significantly degrades when models must access
    relevant information in the middle of long contexts." Inference
    [S]: a 40 % history block at the head of a document occupies the
    high-attention position and pushes Purpose, Objective and the
    positions towards the middle; moving the table to the end
    changes nothing in token cost and merely swaps which block sits in
    the other privileged position. Status: consensus on the effect,
    inference on its application to one file.
20. **Measured locally** (2026-09-03, project fact): 8,477 of 21,265
    words of the forge intent are history rows — roughly 11k tokens
    per read, and the intent is read by `/forge intent`, `/critique`,
    every `/challenge`, `/check-forge`, `/render readme`,
    `/render release-notes` and their isolated subagents, each of
    which loads the file afresh [V]. The history's share grows with
    every round while the substance is rewritten for coherence and
    does not grow.

### D. Wiki and knowledge-tool practice

21. **Confluence** keeps page history as a separate view (More
    options › Page History: version number, contributors, date, an
    optional change comment; "All page history is retained") [V].
    K15t, the vendor of controlled-document versioning for Confluence
    (2026-05-06) [V]: "Gone is the process of tracking changes in
    revision history tables within the document – though if you want a
    revision history table included, you could easily maintain one in
    another Confluence page." The same vendor's 2014 argument [V] is
    the contested half: per-edit page history is not per-*release*
    version history, which is why controlled-document teams still
    maintain a curated version table somewhere. Status: consensus that
    history is a view, contested whether a curated table is still
    needed — resolved by keeping it as a *separate page*.
22. **Notion** — `•••` › Version history, retained 7 / 30 / 90 days /
    unlimited by plan; never in the page body [V]. **Google Docs** —
    the "Last edit" link opens version history; up to 40 named
    versions per document; a separate panel [V]. **MediaWiki** — the
    View history tab lists timestamp, contributor, edit summary and
    minor-edit flag; "does not appear within the page content" [V].
    **Obsidian Sync** — server-side version history, 1 month
    (Standard) or 12 months (Plus); nothing stored in the note [V].
    Status: consensus, without exception across tools.

## Options with trade-offs

Costs are stated for the intent (72 rows, 40 %); the assignment is
shorter-lived in versions and every cost scales down accordingly.

**(a) Table at the head, as today.** Humans: the state of the document
is announced before its content, which corporate readers expect and
casual readers scroll past; at 72 rows the scroll is two screens.
LLM: full cost on every read, in the most-attended position (findings
18–20). Lost: nothing. Document control: exact conformance with the
paper-era template, more than 29148 asks (finding 1). Duplication:
unchanged — row primary, commit and release notes derived.

**(b) Table at the end.** Humans: content first, history as an
appendix — the PEP 1 (2026) and Internet-Draft shape (findings 13,
14). LLM: identical token cost; the position swap gains nothing
measurable (finding 19). Lost: nothing. Document control: still in the
document, at the place 29148 reserves for appendices rather than
identification matter — a mild deviation. Duplication: unchanged. A
cosmetic half-measure: it answers the human complaint and not the
question.

**(c) Companion file per document (`10-intent.history.md`) or one
`CHANGELOG.md` per project.** Humans: the document reads as its
current state; the history is one click away and, as a list of
versions with prose, reads *better* alone than as a preamble. LLM:
~40 % of the intent's tokens leave every read; the companion is loaded
only when a "why" question arises — progressive disclosure (finding
18). Lost: the document alone no longer carries its audit trail; a
file mailed out of its folder arrives without its history (the
records-management guidance accepts exactly this for "guidance or
procedure documents", finding 6). Document control: conformant by
29148 4.4 NOTE 2 (finding 2) and by the two guidance texts (finding
6); an auditor used to Word templates will ask where the table is.
Duplication: unchanged in count, but the primary moves to the
companion — the save script and the release-notes recipe must read it
there. Per document beats per project: the front-matter version and
its rows stay 1:1, the assignment can keep a different regime, and no
"document" column is needed.

**(d) Git only — the commit message is the history, plus the
generated release notes.** Humans: `git log --follow 10-intent.md`
shows every round, but only to someone at a shell; the handed-over
assignment carries nothing. LLM: same saving as (c), but the "why" is
reachable only through git, and the forge's four scripts are the only
door to git, reading included — Claude cannot run `git log` by its own
judgement without a fifth script or a widening of `forge-status`.
Lost: the prose record becomes commit-shaped (one commit may carry
several files and several documents' bumps) and the release notes
are a render, "not a record of thinking" — regenerated, never
authoritative. Document control: the weakest conformance (finding 5
asks for identifiable revision status; a commit hash is not a version
number the document knows). Duplication: reduced to two copies, at
the price of making the derived copy the primary — the changelog
community's explicit warning (findings 8, 9, 11).

**(e) Hybrid — front-matter carries version, date, status and a
one-line `last change`; the full table lives in the companion.**
Humans: everything of (c), plus the head of the document still says
what the latest round did — the Spec Kit constitution footer and Sync
Impact Report in one line (finding 16). LLM: the saving of (c); the
freshest "why" — the one most often needed in the next round —
travels with the document at the cost of one line. Lost: as (c), less
the last row. Document control: as (c), and the "revision notice" of
29148 9.2.1 (version, date, the change of the current version) is in
fact fully present in the front-matter — only the list of *previous*
versions moves out. Duplication: the row in the companion is the one
primary; the `last change` line is that row's summary, the commit
message the script's copy of it, the release notes a render of the
companion since the last major. One record, three derivations.

## Relevance to this project

Recommendation: **(e) for the intent, (a) unchanged for the assignment
and the briefs**, stated as one rule in *Versioning & status*: a
continuously rewritten chain document keeps its Version History in a
companion `<document>.history.md` beside it and carries version, date,
status and a one-line `last change` in its front-matter; a document
that is handed over or locked carries its Version History in its
head. Reasons, in order of weight:

- **The intent is internal and read by machines far more often than
  by the principal.** Every command and every isolated subagent loads
  it whole; 40 % of that load is a preamble consulted in perhaps one
  round in twenty. Anthropic's guidance (finding 18) and every
  LLM-era framework (findings 16, 17) say the same thing: keep the
  working file lean, load history on demand. The saving compounds:
  the rows grow every round, the substance does not.
- **The assignment is the one file handed over, self-contained, to
  recipients who compare versions.** Its history must travel with it;
  its versions are few because it is frozen direction, so the table is
  short; and it is the document that the corporate BRD alignment is
  for. Keeping its table where document control expects it (finding
  6: "very formal documents … at the start") costs little and spares
  the recipients a second file. Moving it to the end (b) would save no
  tokens and only unsettle a corporate reader.
- **A locked brief is immutable**; its table froze with it. Nothing
  to do, and nothing that the rule needs to say beyond "locked".
- **The primary source is, and stays, the Version History row.** The
  save script already composes the commit message from it and the
  release-notes recipe already renders from the rows; both are
  derivations by mechanism, which the house rule permits — a
  procedure stated twice is the defect, not a record rendered twice.
  Making git the primary (d) would invert that and collide with the
  four-scripts rule. What changes under (e) is only *where* the script
  and the recipe read the row: the companion.
- **Conformance is kept, not traded.** 29148 permits separate volumes
  (finding 2) and asks only for a revision notice at the head, which
  the front-matter with `last change` satisfies (finding 1); ISO 9001
  asks for version control and identification of changes, both intact
  (finding 5); the records-management guidance names the separate file
  as the normal option for working documents (finding 6).

What the change would touch, for the principal's decision and in the
order the forge works — none of it is done by this note: the rule in
CLAUDE.md *Versioning & status* and the document chain description;
`templates/` (the intent skeleton gains `last_change:` and loses the
table; a new `templates/history.md` skeleton for the companion);
`.claude/commands/forge/intent.md` (the write step appends the round's
row to the companion and rewrites `last_change:`); `scripts/
forge-save.ps1` (the commit message read from the companion's newest
row); `projects/forge/recipes/release-notes.md` (input
`10-intent.history.md` instead of the intent's table); the ledger's
Documents table (whether the companion is listed — recommendation: no,
it is part of the document like its front-matter); `/check` (companion
present and its newest row equal to the front-matter version); and a
one-off migration of the 72 rows out of `10-intent.md`, on the
principal's word. A challenger-persona or critic reading the intent
would then see the current state only; a reviewer who needs the
document's trajectory reads the companion — which is exactly the
division of the chain: consolidated current state in the intent,
record elsewhere.

Two cautions. First, the `last change` line must be written by the
same mechanism that appends the row, never by hand, or the two drift —
the Spec Kit Sync Impact Report shows the shape (machine-written,
overwritten each time). Second, the companion is a *record*, so it is
append-only like `decisions.md`, not freely rewritten like the ledger;
its rows are the provenance of the intent's changelog and a critic's
regression check reads them there.

## Sources

- ISO/IEC/IEEE 29148:2018, *Systems and software engineering — Life
  cycle processes — Requirements engineering*, clauses 4.4, 6.4.3.3,
  9.2.1–9.2.2, A.2.1 — full text as circulated at
  https://drkasbokar.com/wp-content/uploads/2024/09/29148-2018-ISOIECIEEE.pdf
  (IEEE 2018; fetched 2026-09-03); preview at
  https://cdn.standards.iteh.ai/samples/72089/62bb2ea1ef8b4f33a80d984f826267c1/ISO-IEC-IEEE-29148-2018.pdf
- ISO/IEC/IEEE 15289:2019, *Content of life-cycle information items
  (documentation)*, contents page of the preview,
  https://cdn.standards.iteh.ai/samples/74909/24359dd8f7184f7dbec19eed52a9e9ad/ISO-IEC-IEEE-15289-2019.pdf
  (2019; fetched 2026-09-03)
- ReqView, *ISO/IEC/IEEE 29148 Requirements Specification Templates*,
  https://www.reqview.com/doc/iso-iec-ieee-29148-templates/ (updated
  for 2.22.3); Well-Architected Guide, *ISO/IEC/IEEE 29148 SRS
  Template*,
  https://www.well-architected-guide.com/documents/iso-iec-ieee-29148-template/
- Pretesh Biswas, *ISO 9001:2015 Clause 7.5 Documented Information*
  (2019-05-11),
  https://preteshbiswas.com/2019/05/11/iso-90012015-clause-7-5-documented-information/
- University of Edinburgh, *Version Control*, Version 2 (undated,
  examples 2005–2006),
  https://edwebcontent.ed.ac.uk/sites/default/files/imports/fileManager/VersionControlV02.pdf
- University of Nottingham, *Guidance Document: Version Control*,
  v1.0, approved 2015-05-01,
  https://www.nottingham.ac.uk/governance/records-and-information-management/documents/guidance-documents/version-control---copy.pdf
- Keep a Changelog 1.1.0, https://keepachangelog.com/en/1.1.0/
- Common Changelog, https://common-changelog.org/
- Conventional Commits 1.0.0,
  https://www.conventionalcommits.org/en/v1.0.0/
- semantic-release documentation (archived GitBook),
  https://semantic-release.gitbook.io/semantic-release
- towncrier 25.8.0, *Philosophy*,
  https://towncrier.readthedocs.io/en/stable/
- Michael Nygard, *Documenting Architecture Decisions* (2011-11-15),
  https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- MADR template (develop branch),
  https://raw.githubusercontent.com/adr/madr/develop/template/adr-template.md;
  Olaf Zimmermann, *The Markdown ADR (MADR) Template Explained and
  Distilled* (2022-11-22),
  https://ozimmer.ch/practices/2022/11/22/MADRTemplatePrimer.html
- PEP 1 (last modified 2026-08-07) and PEP 12, sources at
  https://github.com/python/peps (`peps/pep-0001.rst`,
  `peps/pep-0012.rst`); rendered at https://peps.python.org/pep-0001/
- RFC 7322, *RFC Style Guide* (2014-09),
  https://www.rfc-editor.org/rfc/rfc7322.html; Internet-Draft
  change-log appendix example,
  https://icalendar.org/iCalendar-Venue-Draft/appendix-a-change-log-to-be-removed-by-rfc-editor-before-publication.html
- Google, *Markdown style guide* (docguide/style.md, Document layout),
  https://github.com/google/styleguide/blob/gh-pages/docguide/style.md
- Write the Docs, *Docs as Code*,
  https://www.writethedocs.org/guide/docs-as-code/
- GitHub Spec Kit, `templates/spec-template.md`,
  `templates/constitution-template.md`,
  `templates/commands/constitution.md` (main, fetched 2026-09-03),
  https://github.com/github/spec-kit
- BMAD-METHOD v4.44.0 `bmad-core/templates/prd-tmpl.yaml` and v6.11.0
  `src/bmm-skills/plan/bmad-prd/assets/prd-template.md`,
  https://github.com/bmad-code-org/BMAD-METHOD
- OpenSpec, https://github.com/Fission-AI/OpenSpec
- LeanSpec, *What is LeanSpec?*, https://www.lean-spec.dev/docs/guide/
- Agent OS, `commands/agent-os/shape-spec.md`,
  https://github.com/buildermethods/agent-os
- Anthropic, *Effective context engineering for AI agents*
  (2025-09-29),
  https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Nelson F. Liu et al., *Lost in the Middle: How Language Models Use
  Long Contexts*, TACL 2023, https://arxiv.org/abs/2307.03172
- Atlassian, *Page History and Page Comparison Views*,
  https://confluence.atlassian.com/doc/page-history-and-page-comparison-views-139379.html;
  K15t, *Why Confluence's Page History Feature Doesn't Help When
  Managing Versioned Documentation* (2014-10),
  https://www.k15t.com/blog/2014/10/why-confluence-s-page-history-feature-doesn-t-help-when-managing-versioned-documentation;
  K15t, *Controlled Documents Versioning in Confluence with Scroll
  Versions* (2026-05-06),
  https://www.k15t.com/blog/2016/03/controlled-documents-versioning-in-confluence-with-scroll-versions
- Notion, *Delete & restore content in Notion* (version history),
  https://www.notion.com/help/duplicate-delete-and-restore-content
- Google Docs Editors Help, *See what's changed in a file*,
  https://support.google.com/docs/answer/190843
- MediaWiki, *Help:Page history*,
  https://www.mediawiki.org/wiki/Help:Page_history
- Obsidian, *Version history* (Sync),
  https://obsidian.md/help/sync/version-history
