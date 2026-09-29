---
project: forge
type: research
topic: the file format of an append-only record of changes read by a human, a script and a model
date: 2026-09-29
derived_from: 10-intent.md v4.33 (THR.0470); the principal's questions of 2026-09-29
status: immutable
---

# The file format of a change record

## Question

In what file format is an append-only record of changes kept, so
that a human can read it, a search returns whole records, and a
script or a model parses it without guessing: Markdown, plain text
or a structured line format; and do logs have standards to follow?

The facts behind the question. The record in view is the history
companion of a forge document in the shape of a log: one record
per changed item, carrying the date, the version, the ID, the kind
of change, a reason in prose, and the previous wording word for
word. The previous wording is prose of one or more paragraphs with
quotation marks, backticks and vertical bars in it. Today the
companion is a Markdown table with one row per version, a row
being one line of up to several thousand characters. The readers
are the model, the checks (agents that read and search files, and
run no program), now and then a script, and rarely the principal.

What a record carries is a separate question, answered in
`2026-09-29-change-history-of-document-items.md`.

Surveyed on 2026-09-29: JSON Lines and the JSON grammar (RFC 8259),
logfmt, GNU recutils, git trailers, the changelog standards, the
tools that keep one file per change, plain text accounting, and
Org mode.

Epistemic tags: [V] wording returned as a quotation from the page
itself; [S] taken from a search summary, a secondary page or
inference. Pages were read through a fetch tool that condenses
them, so a [V] quotation is as that tool returned it. Status per
finding: consensus / emerging / contested.

## Answer in one paragraph

Logs have standards, and records of prose have conventions, and
the two do not meet. For records a machine reads there is one
plain answer, JSON Lines: one JSON value per line, UTF-8, every
character of a text written safely by the rules of JSON. For
records a human reads the field uses Markdown and, where a record
carries prose, one file per record with a small structured head.
No standard serves long prose, strict parsing and one record per
line at once: a paragraph inside JSON becomes one long line of
escapes, and a line format a human reads well (logfmt) has no
answer for long text. For the forge, whose readers search more
than they parse, the recommendation is a log of one record per
line inside a Markdown file, the structured fields in a fixed
order and every piece of quoted wording written as a JSON string;
JSON Lines is the alternative the day a script becomes the main
reader.

## Findings

### A. Line formats for machines

1. **JSON Lines is the standard of structured logs.** [V,
   jsonlines.org] Three rules: UTF-8; "Each Line is a Valid JSON
   Value"; the line terminator is `\n`. The extension is `.jsonl`.
   The format "is a convenient format for storing structured data
   that may be processed one record at a time. It works well with
   unix-style text processing tools and shell pipelines. It's a
   great format for log files." The page carries no version
   number. NDJSON is the same format under another name [S].
   Status: consensus.
2. **JSON writes any text on one line, at the price of escapes.**
   [V, RFC 8259, section 7] "All Unicode characters may be placed
   within the quotation marks, except for the characters that MUST
   be escaped: quotation mark, reverse solidus, and the control
   characters (U+0000 through U+001F)." A line break inside a text
   is written `\n`. Every character of a quoted wording therefore
   has one defined spelling; a text of several paragraphs is one
   long line. Status: consensus.
3. **logfmt is the line format a human reads, and has no answer
   for prose.** [V, Brandur Leach, 2013-10-28] "Each line consists
   of a single level of key/value pairs which are densely packed
   together"; it "achieves pretty good readability for both human
   and computer, even while not being optimal for either", and
   "it's still difficult to scan quickly for humans", for which
   the author adds a message field written for people. There is
   no formal specification [S]. Status: consensus among its
   users.

### B. Text formats for people that tools also read

4. **Recfiles are the plain-text database made for both.** [V, GNU
   recutils 1.9, 2024-09-19] Fields as `Name: value`, records
   separated by blank lines, a long value continued on lines
   opening with `+`; the stated aim is a format "human-readable,
   human-writable and still easy to parse and to manipulate
   automatically". The tools are a GNU package and are not part of
   PowerShell or of a usual Windows machine [S]. Status: niche.
5. **Git trailers put named fields under free prose.** [V, git
   2.56.0] A trailer is a key and a value separated by a colon;
   the block of trailers stands at the end of the message after a
   blank line. Conventional Commits writes its footers this way
   [S]. The shape is prose first, a structured tail after; the
   forge's `**Notes:**` block at the end of a history row is the
   same shape. Status: consensus.
6. **The changelog standards choose the human.** [V, Common
   Changelog] It "targets human readers and avoids encoded
   communication"; releases are headed `## VERSION - DATE`, the
   date in ISO 8601. Keep a Changelog is Markdown as well (finding
   8 of `2026-09-03-version-history-placement.md`). Status:
   consensus.
7. **Where a record carries prose, the field keeps one file per
   record.** Changesets: a Markdown file with a YAML head naming
   what is touched and how, the text below [V]. reno: one YAML
   file per change, its sections holding text [V]. towncrier: one
   file per change, the type in its name [S]. Decision records and
   OpenSpec: a file or a folder per decision or change (findings
   11 and 12 of `2026-09-29-change-history-of-document-items.md`).
   The reason the tools give for separate files is that many
   authors writing into one file collide (finding 11 of
   `2026-09-03-version-history-placement.md`), which is not the
   forge's case: it has one writer. Status: consensus.
8. **Plain text accounting keeps a journal in a line format of its
   own, with a checker.** [S, plaintextaccounting.org, Beancount]
   The data are kept as readable text so that they stay accessible
   "even without software", are version-controlled and searched
   with ordinary tools; Beancount reads the file as an ordered
   stream of directives and refuses what does not check. The
   entries run in the order of time, oldest first. Status:
   consensus in its community.
9. **Org mode logs under the item, newest first.** [V, Org manual]
   A change of state is recorded as a list under the headline,
   "the newest first", a time stamp with an optional note, and may
   be put into a drawer. The history sits inside the document,
   which the forge has decided against (POS.0310). Status:
   consensus in its community.

### C. Order and dates

10. **Logs and journals append at the end; changelogs put the
    newest first.** Event logs, JSON Lines files and accounting
    journals grow at the end (findings 1, 8; finding 4 of
    `2026-09-29-change-history-of-document-items.md`); Keep a
    Changelog, Common Changelog and Org
    mode put the newest on top (findings 6, 9). The difference
    follows the reader: a file that is read from the top shows the
    newest first, a file that is searched grows at the end. [S,
    inference] Status: consensus within each family.
11. **Dates follow ISO 8601.** `YYYY-MM-DD` in every format
    surveyed that names one (finding 6). The forge already writes
    its dates so. Status: consensus.

## Options with trade-offs

**(a) The Markdown table, one row per version, as today.** Nothing
to build. A row is one line of several thousand characters; a
search for an ID returns the whole row of the version, not the
record of the item; a vertical bar in a quoted wording breaks the
table.

**(b) A log in a Markdown file, one record per line.** Each record
a list item with its fields in a fixed order; quoted wording
written as a JSON string, so that every character has a defined
spelling (finding 2) and nothing is invented. A search for an ID
returns whole records; a difference in git is one line per record;
the page renders as a list. The lines are long and are not wrapped,
as table rows are not. A text of several paragraphs is hard to read
in the raw file. A script splits the line and reads the strings
with a JSON parser.

**(c) A log in a Markdown file, one block per record.** A heading
line with the date, the version, the ID and the kind; the text
below it, wrapped like all prose; named fields at the end in the
manner of trailers (finding 5). The best to read, and quoted
wording needs no escapes at all. A search for an ID returns the
heading lines, and the record must then be read by its place; a
script needs a parser of blocks; the file is several times longer.

**(d) JSON Lines, `<file>.history.jsonl`.** The standard (finding
1); every parser reads it, PowerShell among them; a search returns
whole records. The raw file is the hardest to read and is shown as
plain text by a repository browser; a reader script becomes
necessary for the principal; it is the first file of the chain that
is not Markdown.

**(e) One file per version in a directory.** The field's way for
records of prose (finding 7). The forge intent alone has 142
versions; the directory would hold as many files and grow with
every round; the companion would stop being one file handed over
with its document.

**(f) A recfile or a YAML stream.** Reads well and holds long
text. Neither has a parser in PowerShell out of the box, and
recutils would be one more program to install [S].

## Relevance to this project

Recommendation: **(b)**, with (d) as the alternative.

- **The readers decide.** The model and the checks search and read;
  neither runs a parser. For them the unit that matters is what a
  search returns, and one record per line returns the record
  whole. The principal reads the companion rarely and mostly
  through the model.
- **Nothing invented for the hard part.** The one place where a
  home-made format breaks is quoted wording. Writing it as a JSON
  string borrows a rule that is standard and that every parser
  knows (finding 2). The field separators are the forge's own
  choice; no standard covers them. This combination has no outside
  model and is Claude's synthesis [S].
- **Hard-wrapped prose.** The wording of an item is wrapped at
  about 72 columns in its document. Copied into one line, the line
  breaks of the wrapping become spaces and only the breaks between
  paragraphs are kept, as `\n`. "Word for word" then means the
  words and the punctuation, not the wrapping; a check compares
  with the white space normalised.
- **Order.** Append at the end (finding 10): the file is searched,
  not read from the top, and a difference in git is then always at
  the end of the file. Today's companion runs newest first; the
  change of order is a decision of its own.
- **When (d) becomes right.** The day a script is the main reader,
  or the fields multiply: JSON Lines then costs only the raw
  readability that (b) has already largely given up.
- **What stays Markdown.** Under (b) the companion keeps its name,
  `<file>.history.md`, and its place among the document kinds; the
  rule that prose is wrapped gains one exception beside tables and
  code blocks, the log line.

Not researched and left to the forge: what becomes of the 142 rows
the companion holds today, and whether the companions of briefs and
recipes, which are short, take the new shape at all.

Nothing here is done by this note. The position it would touch is
POS.0310 (the history companion), through `/forge intent`;
`templates/history.md`, the write step and the checks follow from
it.

## Sources

- JSON Lines, https://jsonlines.org/ (fetched 2026-09-29)
- RFC 8259, *The JavaScript Object Notation (JSON) Data
  Interchange Format* (2017-12), section 7,
  https://www.rfc-editor.org/rfc/rfc8259.html
- Brandur Leach, *logfmt* (2013-10-28), https://brandur.org/logfmt
- GNU recutils manual, version 1.9 (2024-09-19),
  https://www.gnu.org/software/recutils/manual/recutils.html
- git, *git-interpret-trailers*, version 2.56.0,
  https://git-scm.com/docs/git-interpret-trailers
- Common Changelog, https://common-changelog.org/
- Changesets, *A detailed explanation*,
  https://github.com/changesets/changesets/blob/main/docs/detailed-explanation.md
- OpenStack reno, *Usage*,
  https://docs.openstack.org/reno/latest/user/usage.html
- towncrier 25.8.0, https://towncrier.readthedocs.io/en/stable/
  (through a search summary)
- Plain Text Accounting, *What is Plain Text Accounting?*,
  https://plaintextaccounting.org/What-is-Plain-Text-Accounting;
  Beancount documentation, https://beancount.github.io/docs/
  (both through a search summary)
- The Org Manual, *Tracking TODO state changes*,
  https://orgmode.org/manual/Tracking-TODO-state-changes.html
