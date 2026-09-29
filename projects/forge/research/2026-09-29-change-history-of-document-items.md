---
project: forge
type: research
topic: how the history of changes to the items of a document is recorded
date: 2026-09-29
derived_from: 10-intent.md v4.33 (THR.0470); the principal's questions of 2026-09-29
status: immutable
---

# How the history of a document's items is recorded

## Question

When a document made of identified items changes (positions,
requirements, provisions, decisions), what does the record of the
change look like elsewhere: one record per version or one per item;
is the previous wording kept word for word, and where; where does
the reason of a change live; how are a summary of a version and the
release notes derived from the records; and what does a reader need
in order to pull everything about one item?

The facts behind the question. The forge intent stands at 2 997
lines and cannot be read (THR.0470); the principal wants the
stories, the reasons told with them and the measurements out of the
positions and in the history, without losing anything. The history
companion today holds one table row per version, written as prose;
21 of the 110 positions of the intent are named in no row, and one
row cites its positions as a range, which a search for a single ID
does not find. In the conversation of 2026-09-29 a log was drafted:
one record per changed item with date, version, ID, kind of change,
the reason, and the previous wording under `Was`.

The file format of such a record is a separate question, answered
in `2026-09-29-change-record-file-format.md`. Where the history
lives (in the document, beside it, in git) was answered in
`2026-09-03-version-history-placement.md`, and the shape of release
notes in `2026-09-05-good-release-notes.md`; neither is repeated
here.

Surveyed on 2026-09-29: regulated audit trails (21 CFR Part 11, EU
GMP Annex 11), data systems (event sourcing, system-versioned
temporal tables, OpenStreetMap), requirements tools (Jama Connect,
DOORS Next, Doorstop, OpenSpec), decision records, legislation
(legislation.gov.uk, EUR-Lex), standards (ISO/IEC Directives,
Part 2), wikis (MediaWiki) and the tools that compile release notes
from records written with the change (Changesets, Kubernetes, reno,
towncrier).

Epistemic tags: [V] wording returned as a quotation from the page
itself; [S] taken from a search summary, a secondary page or
inference. Pages were read through a fetch tool that condenses
them, so a [V] quotation is as that tool returned it. Status per
finding: consensus / emerging / contested.

## Answer in one paragraph

Every field that records changes to identified items does it on two
levels at once: a record of the group of changes made together,
which carries the reason and the occasion (a changeset, a commit, a
change folder, an amending act, the foreword of an edition), and a
history per item, keyed by the item's stable identifier, that
points to the group. The previous wording is kept word for word
everywhere and paraphrased nowhere; it sits either in the record
itself (the old value of an audit trail, the previous value of an
event, the history row of a temporal table) or in a store of whole
earlier versions (point-in-time legislation, wiki revisions, git).
The unit kept is the whole field or the whole item, and the
difference is computed when someone looks. The reason lives at the
level of the group far more often than at the level of the item.
Notes for the reader of a release are written with the change, not
deduced at the release; even the school that generates everything
from records marks a breaking change by hand at the time it is
made. For the forge: a log on two levels, one record per round and
one per item, the previous wording word for word, the reason shared
by a round written once, and at the least the "action required"
written with the change.

## Findings

### A. Regulated records

1. **21 CFR 11.10(e) asks that a change never hides what stood
   before.** [V, Cornell LII] "Use of secure, computer-generated,
   time-stamped audit trails to independently record the date and
   time of operator entries and actions that create, modify, or
   delete electronic records. Record changes shall not obscure
   previously recorded information." Creation is recorded as much
   as modification. The rule names no reason for a change. Status:
   consensus (regulation in force).
2. **EU GMP Annex 11, clause 9, asks for the reason.** [S, search
   summary of the Commission's text of 2011] "For change or
   deletion of GMP-relevant data the reason should be documented";
   the audit trail is to be available in a generally intelligible
   form. The clause speaks of changes and deletions; the creation
   of data is not named. A revision of the annex is in
   consultation and was not read. Status: consensus.
3. **What an entry carries in practice.** [V, ISPE, 2026-06-24] The
   usual fields are the user, the time, the action, the old value
   and the new value. Status: consensus.

### B. Data systems

4. **Event sourcing keeps the changes and derives the state.** [V,
   Fowler, 2005-12-12] "Capture all changes to an application
   state as a sequence of events"; "we can discard the application
   state completely and rebuild it by re-running the events from
   the event log on an empty application"; and for reversal "the
   event should ensure it stores everything needed for reversal
   during processing. You can do this by storing the previous
   values on any value that is changed." Status: consensus as a
   pattern.
5. **A temporal table keeps the whole previous row.** [V, Microsoft
   Learn, 2026-08-18] "The system uses the history table to
   automatically store the previous version of the row each time a
   row in the temporal table gets updated or deleted." The current
   table holds what holds now, the history table everything that
   ceased to hold, each with the period in which it was valid. The
   named uses: "Auditing all data changes", "Reconstructing the
   state of the data as of any time in the past". No reason is
   stored. Status: consensus.
6. **OpenStreetMap separates the group from the item.** [V, page
   edited 2026-08-13] A changeset is "a collection of elements
   edited by a mapper in a single editing session" and carries a
   comment "describing why a mapper made that group of changes, or
   what was changed"; "the history of changes to tags is not
   stored on changesets themselves: this can be inferred from the
   history as a whole." Each version of an element points to the
   changeset that made it. Status: consensus.

### C. Requirements tools

7. **Jama Connect versions the item.** [S, search summary of the
   help pages] A new version of an item arises with every change
   of a field; the list of versions shows the change details
   generated by the tool, the comment of the person who made the
   change, the date, the person, and the baselines and reviews
   that contain the version. Two versions are compared on request,
   deleted text in red and added text in green. Status: consensus
   among the commercial tools.
8. **DOORS Next shows history per artefact.** [V, Softacus,
   undated] Two views, revisions and an audit history "with an
   explanation of actions performed on it and changes which were
   created with information on date and time and author of it"; a
   baseline is "a snapshot which includes certain revisions of
   artifacts". Status: consensus.
9. **The standard puts the history with the requirement.**
   ISO/IEC/IEEE 29148:2018, clause 6.4.3.3, lists a change history
   among the information recorded along with each requirement
   (finding 3 of `2026-09-03-version-history-placement.md`).
   Status: consensus.
10. **Doorstop leaves the history to version control.** [V] One
    file per item; the history of an item lives in the version
    control system; a fingerprint stored at review lets the tool
    "detect unreviewed changes to an item by comparing the current
    item fingerprint to the last reviewed fingerprint". Status:
    consensus among the tools that keep requirements as text.
11. **OpenSpec records a change as a folder of its own.** [V] A
    proposal carries the intent and the reason; delta files list
    the requirements under ADDED, MODIFIED and REMOVED; a modified
    requirement carries its new text, not the old one; on archive
    the deltas are applied to the specification and the folder
    moves to a dated archive, which keeps "the full context of
    every change". The old wording is in git. Status: emerging.

### D. Decision records

12. **An accepted decision is never edited; a new one supersedes
    it.** [V, AWS Prescriptive Guidance] "When the team accepts an
    ADR, it becomes immutable. If new insights require a different
    decision, the team proposes a new ADR. When the team accepts
    the new ADR, it supersedes the previous ADR." A rejected record
    carries "a reason for the rejection to prevent future
    discussions on the same topic". The earlier decision stays
    whole, as its own file, and the reason lives in the record
    itself. Status: consensus.

### E. Law and standards

13. **Revised legislation shows the change in the text and cites
    the authority beside it.** [S, legislation.gov.uk, read through
    a summary; the editorial conventions themselves could not be
    reached] Amendments are worked into the text, inserted words in
    square brackets and removed words as dots; an annotation of
    the textual kind names the amending legislation and the date;
    earlier versions of a provision are reached through the
    point-in-time view. Whether an annotation ever carries the
    words that were replaced was not verified. Status: consensus.
14. **A consolidated EU text labels each part with its origin.**
    [S, EUR-Lex] A consolidated text combines the basic act with
    its amendments and corrigenda as of one date, is a
    documentation tool without legal effect, and marks each
    passage with the act it comes from (B the basic act, M1, M2
    the amending acts, C a corrigendum). The reason of an
    amendment lives in the amending act. Status: consensus.
15. **A new edition of a standard lists its changes by clause
    number.** [S, ISO/IEC Directives, Part 2, ninth edition 2021]
    The foreword carries a statement that the document replaces
    the previous edition and a statement of the significant
    changes against it, written as a list keyed by clause: "7.4
    clarification in Table 5 that negative permissions are no
    longer permitted". A summary per version, made of lines per
    item. Status: consensus.

### F. Wikis

16. **MediaWiki keeps every revision whole and one line of reason
    with it.** [V] The edit summary holds up to 500 characters,
    cannot be changed once saved, and "If you remove text, a
    summary is especially important to clarify your reasons";
    when a section is edited its title is put in front of the
    summary by the software. The history is per page, never per
    section. Status: consensus.

### G. Release notes compiled from records

17. **The note is written when the change is made.** [V,
    Changesets] "the best time to capture this information is when
    submitting a PR (when it is fresh in your mind), not when you
    eventually go to batch and release these changes." Status:
    consensus.
18. **Kubernetes asks the author and marks what the reader must
    do.** [V] The author of a change writes the note in a block of
    the pull request; a change that needs the user to act carries
    the phrase "action required"; the release team collects and
    reviews the notes. The guidance for the wording: "consider
    what they need to know". Status: consensus.
19. **reno keeps one note per change, in sections.** [V, OpenStack]
    Sections `prelude`, `features`, `issues`, `upgrade`,
    `deprecations`, `critical`, `security`, `fixes`, `other`; the
    notes of a release are compiled by reading the history and the
    tags. towncrier works the same way with typed fragments [S].
    Status: consensus.
20. **Full derivation exists, and still asks for a mark.**
    Conventional Commits with semantic-release derives the notes
    and the version from typed records alone (finding 10 of
    `2026-09-03-version-history-placement.md`); a breaking change
    is nevertheless marked by the author in the record [S]. Common
    Changelog [V] warns: "Don't take the easy way out with full
    automation. This results in poor changelogs, defeating their
    purpose." Status: contested.

## What the findings say to the five questions

**Per item or per version.** Both, on two levels (findings 6, 7,
11, 14, 15). The group carries what its changes share; the item's
history is a view keyed by the identifier. No system surveyed
writes one prose record per version and leaves the items to be
found in it. Status: consensus.

**The previous wording.** Always word for word, never summarised.
Two homes: the record itself (findings 1, 3, 4, 5) or a store of
whole earlier versions (findings 10, 11, 13, 16). Where the record
must stand on its own, it carries the old value; where a store of
versions is at hand, the record points into it. The unit is the
whole field or the whole item (findings 5, 7, 16); no system stores
"the part that changed" of a text, the difference is computed for
the reader. Status: consensus.

**The reason.** At the level of the group in most systems
(findings 6, 11, 14, 16); per item in the regulated trail (finding
2) and as an optional comment in the requirements tools (finding
7); inside the record in decision records (finding 12). Status:
consensus that it is written, contested where.

**Summary and release notes.** The practice with the longest record
writes the reader's note with the change (findings 17 to 19). The
generating school depends on typed records and a hand-made mark for
what breaks (finding 20). Status: contested.

**Everything about one item.** A stable identifier in every record
that touches the item; the view per item is then computed. No
system surveyed cites items as a range. Status: consensus; the
statement about ranges is an inference [S].

## Options with trade-offs

**(a) One prose row per version, as today.** Nothing to build. The
items are found only where the prose happens to name them; the
previous wording is in git alone; a story taken out of a position
has no place of its own.

**(b) One record per item, nothing per round.** A search for an ID
returns whole records. A reason shared by several items is written
with each of them, and what has no ID (the occasion of the round,
changes outside the document) has no home.

**(c) Two levels: one record per round, one per item.** The shape
of the field. The round carries the occasion, the author and what
the items share; the item carries its kind of change, its own
reason and the previous wording. A search for an ID returns the
item's records, each naming the version whose round record holds
the rest; the reader makes one step more.

**(d) No record per item; the history derived from git.** The
previous wording is already there word for word. The forge reaches
git only through its scripts, so a script would have to produce the
history of one item from the versions of the file; the reason would
still need a home; and a companion handed over with its document
would carry nothing.

## Relevance to this project

Recommendation: **(c)**, with the previous wording in the record.

- **Two levels.** One record per round and one per changed item,
  the ID written in full in every record, never a range. This
  differs from what was said in the conversation of 2026-09-29,
  where a shared reason was to be repeated with every item: the
  field writes it once, with the group (findings 6, 11, 14).
- **`Was` word for word.** Supported without exception. The forge
  has a store of versions in git, which would allow a pointer
  instead of a copy (finding 11); the copy is justified because
  git is behind the scripts and the companion travels with its
  document. The field keeps the whole item rather than its changed
  part; the changed part alone is the forge's own choice and is
  checkable only as "this text stood in the previous version of
  the item".
- **A record of creation without text.** Consistent with the
  field: the creation is an event, the wording is in the document
  (findings 1, 2).
- **The reader's note.** Deriving the release notes from the log
  at the release goes against the practice of findings 17 to 19
  and against the forge's own finding of 2026-09-05. What makes it
  defensible is that the item records are themselves written with
  the change, typed by kind and carrying the reason; what would be
  derived is the wording for the reader only. The least that is
  written with the change is what the reader must do (finding 18).
- **The check.** A fingerprint per item (finding 10) would let a
  check say mechanically that an item changed and no record names
  it. Offered as an idea, not proposed.

Nothing here is done by this note. The positions it would touch are
POS.0120 (what a position carries), POS.0310 (the history
companion) and POS.0730 (the release notes), through `/forge
intent`; the operating layer follows from them.

## Sources

- 21 CFR 11.10, Legal Information Institute,
  https://www.law.cornell.edu/cfr/text/21/11.10 (fetched
  2026-09-29; the eCFR page itself refused the fetch)
- European Commission, EudraLex Volume 4, *Annex 11: Computerised
  Systems* (2011),
  https://health.ec.europa.eu/system/files/2016-11/annex11_01-2011_en_0.pdf
  (through a search summary)
- Gabriel Buta, *What 21 CFR Part 11 §11.10(e) Actually Requires
  of an Audit Trail*, ISPE (2026-06-24),
  https://ispe.org/pharmaceutical-engineering/ispeak/what-21-cfr-part-11-ss1110e-actually-requires-audit-trail-and-why
- Martin Fowler, *Event Sourcing* (2005-12-12),
  https://martinfowler.com/eaaDev/EventSourcing.html
- Microsoft Learn, *Temporal tables* (2026-08-18),
  https://learn.microsoft.com/en-us/sql/relational-databases/tables/temporal-tables
- OpenStreetMap Wiki, *Changeset* (edited 2026-08-13),
  https://wiki.openstreetmap.org/wiki/Changeset
- Jama Connect Help, *Item versions* and *Compare versions of an
  item*,
  https://help.jamasoftware.com/ah/en/manage-content/item-versions.html
  (through a search summary)
- Softacus, *History in DOORS Next* (undated),
  https://softacus.com/blog/articles/dng/history-in-doors-next
- Doorstop, *Item reference*,
  https://doorstop.readthedocs.io/en/latest/reference/item.html
- OpenSpec, *Concepts*,
  https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md
- AWS Prescriptive Guidance, *Architectural decision record
  process*,
  https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html
- legislation.gov.uk, *Understanding legislation*,
  https://www.legislation.gov.uk/understanding-legislation; *Guide
  to Revised Legislation* (October 2013),
  https://www.legislation.gov.uk/pdfs/GuideToRevisedLegislation_Oct_2013.pdf
  (downloaded, not readable by the tools at hand)
- EUR-Lex, *Consolidated texts*,
  https://eur-lex.europa.eu/collection/eu-law/consleg.html
  (through a search summary)
- ISO/IEC Directives, Part 2, ninth edition (2021),
  https://www.iso.org/sites/directives/current/part2/index.xhtml
  (through a search summary)
- MediaWiki, *Help:Edit summary*,
  https://www.mediawiki.org/wiki/Help:Edit_summary
- Changesets, *A detailed explanation*,
  https://github.com/changesets/changesets/blob/main/docs/detailed-explanation.md
- Kubernetes, *Adding release notes*,
  https://github.com/kubernetes/community/blob/master/contributors/guide/release-notes.md
- OpenStack reno, *Usage*,
  https://docs.openstack.org/reno/latest/user/usage.html
- towncrier 25.8.0, https://towncrier.readthedocs.io/en/stable/
  (through a search summary)
- Common Changelog, https://common-changelog.org/
