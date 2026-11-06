---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 38cb02703f746349
inputs:
  - .claude/skills/check-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0540
  - projects/forge/10-intent.md#POS.0570
  - projects/forge/10-intent.md#POS.1140
---

# The check

A check is a reviewer that verifies whether the files of a project,
or of the engine itself, follow the current conventions of the forge.
This page explains what a check verifies and what it leaves alone,
why it changes nothing and only reports, and who gives its findings
their IDs and files its report. It is written for anyone who runs a
check, who adds one, or who wants to judge what a check's report is
worth. How a check is run is the matter of
[Check conformance](../use/check-conformance.md); which checks exist
is listed in [Checks](../reference/checks.md).

## What it is

A check is one of the three kinds of isolated reviewer in the forge.
The other two are the critic, which judges the quality of a document,
and the challenger, which attacks the substance of the thinking. The
check's subject is mechanical conformance: whether the files of its
target follow the current conventions of the engine, which are
`CLAUDE.md` and the templates in `templates/`. It never judges
substance. It never judges document quality. A document that is
wrong or unclear but conforms gets no remark from a check. A rule
that seems worth tightening is a matter for the intent of the forge,
not for a check.

Every check owns one concern and none of another check's. The first
checks are:

- `project`: structure, IDs, language, immutable documents, recipes
  and renders.
- `light`: the front-matter against the history companion and the
  form of its log, what the ledger script reports, dependencies,
  resource indexes; the check that fits a save.
- `engine`: the core of the engine against itself and against the
  forge intent, with the sweep for renamed things.
- `single-source-of-truth`: the whole operating layer searched for
  restatements of a rule and for operations done directly instead
  of through their mechanism; the honest sweep, expensive by design.
- `history`: a document read together with its history companion,
  reporting where the division between the two does not hold.

The word for all of these is "check": the light check, the project
check. The name of the mechanism serves for its members. The roster
is open; a new check is added by the principal's decision, and the
way to add one is the matter of
[Add a check](../extend/add-a-check.md).

A check is an isolated subagent, that is, a run of Claude that sees
nothing of the working conversation and reads every input from disk.
What every check shares (its subject, its way of working, the shape
of its report) is owned by one contract. What one check owns beyond
that is its own definition file, the agent file `check-<name>`, and
there only its Lens section: what it reads, what it goes after, and
how its target narrows its work.

## How it works

**The target.** A check takes a project, named by its slug, or the
engine. How a target narrows the work is said by the check's Lens
section.

**The rules at their owners.** The rules a check verifies have
owners: `CLAUDE.md`, a template, a position of the forge intent. The
check reads each rule where its owner states it. Its Lens section
names the owner of each rule and never restates the rule.

**Read-only.** A check changes nothing: not a document, not the
ledger (the state report of a project, made at read time from its
documents), not an index. Every fix is applied afterwards by Claude
in the conversation, on the principal's word, after the walkthrough.
The principal is the person whose thinking is forged and the final
authority on all content; a walkthrough is the way a list of items
is worked with the principal, one item per message, each closed with
a verdict. A fix that is pure bookkeeping, such as a comment behind
its template or a missing field of an index entry, may be marked
"immediate fix". Claude can then offer it at once.

**Findings only.** A check reports what does not conform. What
conforms is not reported, under no label such as "observation" or
"note". Where a check's Lens section says that a state is a fact and
not a finding (a project without a repository, a missing logo), the
check reports it as a fact in one line, once.

**Precise and ranked.** Every finding carries the file and the line
where it stands (a range where it spans lines), the rule it breaks
together with the owner of that rule, and one proposed fix in one
sentence. Findings are ranked by severity: what would mislead or
break first comes first, never what was found first.

**Advisory.** Nothing blocks. What becomes of a finding is decided
at the walkthrough that follows the run, never by the check.

**Decided once.** A finding that the project's decisions file
records as rejected is not raised again. This holds whether the
decision is in an older record, overrules the finding or accepts a
state as it is. At most the check names it once as a fact, with the
decision cited.

**Known findings.** Before it reports, a check reads the Findings
table of the target's ledger and its own earlier reports in the
project's `reviews/` directory. A finding that is already filed is
reported under the ID it has and never as new. It is "still open"
while it stands. It is "reopened" when the ledger has it resolved
and it stands again. A rejected one is not raised.

**Cheap where the Lens says so.** A check whose Lens section names a
scope reads that scope and nothing more. A check that names the
whole reads the whole, honestly, however long it takes.

**Who files the report.** The check returns its report in its final
message and writes no file. Its new findings carry no ID; a known
finding is named by the ID it has. Claude, running the `/check`
command in the conversation, gives each new finding its ID, files
the report as a dated, immutable file in the project's `reviews/`
directory, presents it and offers the walkthrough. A check's
findings are filed like a critic's: as findings of the project's one
sequence of IDs, and a finding's state is settled by the walkthrough.
A rejected finding gets a decision and is then not raised again. A
run that finds nothing files nothing.

**Composition is the caller's.** Checks never call each other.
Which checks a command runs is decided by that command. The
bookkeeping check, `light`, belongs to the save: `/save` runs it
before it commits. The project's full conformance, the `project`
check, belongs to the release: `/release` runs its checks and
settles their findings with the principal before the release commit.
The `single-source-of-truth` check runs on the principal's word,
before a major release or after a round of work on the operating
layer, never by `/release` on its own; for a project it runs on
request. The `history` check likewise runs on the principal's word.

**What is never a finding.** The staleness of a render is never a
check finding, the README and the release notes included. The state
map of a project, which `/forge` shows, says what is stale, and a
render is regenerated only on the principal's word.

The documentation run uses the same channel for what it cannot
place: it files that as a check's report, which is explained in
[The documentation](the-documentation.md).

## Why

**One mechanism for every reviewer.** The check runs on the same
mechanism as the critic and the challenger: its own contract, one
agent per kind of check, a roster, a run by hand. The recorded
reason is that one mechanism should serve every reviewer, so that
the mechanism takes further kinds as they come. Whether a check is
called a review is not decided and does not matter to the mechanism.

**Conformance only, because the rest has an owner.** Substance stays
the challenger's territory and document quality stays the critic's.
A check therefore says nothing about a document that conforms, even
one that is wrong or unclear.

**Read-only and advisory, because the principal decides.** A check
reports and proposes. The principal decides what is fixed. Beyond
that division of roles the reason is not recorded.

**IDs from the command, not from the check.** A finding without an
ID has no place for its verdict. A rejected finding would then
return at the next run. A user could not tell why one reviewer's
findings are kept and another's are not. So the IDs of a project's
findings are given in one place, by the command, for every kind of
reviewer alike. Two further reasons are recorded. A check that every
save runs would otherwise write into the project at every save. Two
reviewers run at once would otherwise take the same ID. Because the
agent only returns its report, reviewers of any kind may run in
parallel.

**Why the full check left the save.** The full conformance check
cost minutes and a walkthrough at every save. So it moved to the
release, and the save kept the cheap bookkeeping check.

**Why a stale render is no finding.** The release regenerates the
README and the release notes anyway. So the finding was void at
every release and noise everywhere else. The state map already shows
staleness.

**Why each check owns one concern and none another's.** A rule an
older position attributed to one check procedure belongs to the
check that owns its concern, never to two. Beyond this the reason is
not recorded.

**Why a run that finds nothing files nothing.** The reason is not
recorded.

**Why the rules are read at their owners and never restated.** The
reason is not recorded in the inputs of this page.

## A worked example

The principal runs the light check on a project with the slug
`my-project` before a save. Claude launches the check as an isolated
subagent. The check reads the current conventions where their owners
state them: `CLAUDE.md` and the templates. It reads the Findings
table of the project's ledger and its own earlier reports in
`projects/my-project/reviews/`. Then it reads the files its Lens
section names and nothing more.

It returns, in its final message, a report with two findings and no
file written. Ranked first: the front-matter of the intent carries
`version: 1.2` while the last record of its history companion says
`1.3`, found at `10-intent.md:3`, breaking the rule of `CLAUDE.md`,
Versioning & status; the proposed fix is one sentence, to set the
header to the version the history records. Ranked second: an entry
of `sources/00-INDEX.md:14` lacks its Role field, breaking the shape
the index template owns; the fix is marked "immediate fix", since it
is pure bookkeeping. The second finding was filed in an earlier run
and is still open, so the report names it by the ID it already has.
The first is new and carries no ID.

Claude gives the new finding the next ID of the project's one
sequence, files the report as a dated file in
`projects/my-project/reviews/`, and presents both findings as a
walkthrough. The principal accepts the first, and Claude corrects
the header on his word. He rejects the second with a decision, since
the source's role is deliberately left open for now. From then on no
light check raises that entry again; at most it is named once as a
fact, with the decision cited. The report itself is never edited.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Checks](../reference/checks.md): the checks and what each
  verifies.
- [Add a check](../extend/add-a-check.md): adding a check of one's
  own.
- [The documentation](the-documentation.md): the documentation run,
  which files what it cannot place as a check's report.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
