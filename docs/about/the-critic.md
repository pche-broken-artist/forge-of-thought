---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 5985ec3000a8b4b2
inputs:
  - .claude/skills/critic-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0400
  - projects/forge/10-intent.md#POS.0410
  - projects/forge/10-intent.md#POS.0270
  - projects/forge/10-intent.md#POS.1140
  - CLAUDE.md#Isolated reviewers
---

# The critic

The critic is the reviewer that judges how well the documents of a
project are written, and never what they say. This page explains what
a critic lens judges, why there are two lenses, how a lens works and
what it returns. It is for whoever runs a critique, adds a lens or
weighs the forge as a method.

## What it is

The critic judges the quality of a project's
[artefacts](../reference/glossary.md) as documents. An artefact is a
document of the chain: a brief, the intent or a layer below the
intent. The critic reads through a
[lens](../reference/critic-lenses.md), that is one angle of reading
with its own categories of finding. It never judges the substance of
the thinking of the principal (the person whose thinking is being
forged).

The forge has three kinds of reviewer, and their jobs are strictly
separate:

- The critic reads the quality of the documents, never the substance.
- The [challengers](../reference/glossary.md) read the substance of
  the thinking, never the quality of a document. A question such as
  whether the objective is the real problem belongs to them.
- The [checks](../reference/glossary.md) read mechanical conformance
  with the conventions, never either.

Where a document is sound and the thinking is wrong, the critic says
nothing.

A lens runs as an isolated subagent (a separate run of Claude that
never sees the working conversation). It reads every input from disk
in its own run. It took no part in the drafting, and it is not told
what the drafter intended. It judges only what the documents say.

A finding (one result of a reviewer) is advisory. The principal
decides, and "rejected" is a legitimate outcome, not a failure.

The critic has two lenses:

- `clarity` reads each artefact on its own.
- `essence` reads the chain. For every adjacent pair of artefacts it
  first distils, blind, the essence of the downstream artefact in a
  few sentences. It then distils the essence of the upstream artefact
  the same way and compares the two. A finding of `essence` is a
  difference of essences, not of texts.

```
clarity   each artefact on its own

          brief       intent       assignment       later layer

essence   each adjacent pair, both distilled blind, then compared

          brief -> intent     intent -> assignment     ... -> later layer
```

What each lens goes after is listed in
[Critic lenses](../reference/critic-lenses.md).

## How it works

### When a lens runs

A lens runs on the principal's word alone, typed as
`/critique <lens>`. Claude never starts a lens on its own judgement.
No lens runs at a save. A release offers `critique essence` once and
runs no reviewer on its own. How a lens is run is described in
[Critique the documents](../use/critique-the-documents.md).

A lens runs on the same model as the conversation that starts it.

### The target

A run may name a target. The target is one of two things:

- an artefact, named as `/forge` names it: `brief`, `brief-<name>`,
  `intent`, `assignment` or a later layer;
- any file of the project, named by its path:
  `/critique <lens> <path>`.

A file is read with the chain around it. A
[work product](../reference/glossary.md) (an output that Claude
composes and the principal judges) is read with its specification.
The report names the file. Where the file gives the lens nothing to
work on, the report says so and carries nothing else.

A target narrows each lens in its own way:

- `clarity` reads that artefact alone.
- `essence` reads that artefact against its parent.

A transition between two artefacts is addressed by its downstream
artefact. No arrow is ever typed.

Without a target, a lens works on everything it reads.

### What a lens reads

A lens reads the whole chain and the earlier reports. It modifies
none of them:

- the briefs;
- the intent;
- the [threads](../reference/glossary.md) of the project;
- every layer below the intent that exists;
- the decisions (`decisions.md`);
- the [ledger](../reference/glossary.md) (the file that shows the
  state of the project);
- every file in `reviews/`, where the reports of the reviewers are
  filed.

### The way a lens works

- **Regression first.** A lens re-tests every finding of its own that
  was marked resolved since its last run. It reports each as verified
  or reopened. A filed finding is always reported under the ID it
  has, as still open, reopened or verified resolved.
- **Rejected findings stay rejected.** A finding the principal
  rejected is settled by a decision and is not raised again.
- **New findings.** Each new finding carries a severity (high, medium
  or low) and one of the categories of the lens.
- **Each artefact against its own definition.** An artefact is judged
  against its own [definition](../reference/glossary.md)
  (`.claude/skills/forge/states/<artefact>.md`), never against the
  definition of another. For an assignment, completeness is the
  test, not brevity.
- **Deliberate omissions are never defects.** The two lists below
  name them.
- **Testability is a recommendation, not a rule.** Wording that
  cannot be tested goes into the recommendations of the report,
  never into a finding.
- **Sharp and few beats thorough and long.** Five sharp findings beat
  twenty trivial ones. A lens never invents a finding to appear
  thorough. It never softens a finding whose fix is inconvenient.
- **The document, not the substance.** A lens never edits an artefact
  of the chain. It never proposes substance. It proposes the fix of
  the document.

A lens never reports these as defects in any artefact:

- a missing stakeholder list;
- a missing RACI;
- a missing impact analysis;
- a missing MECE decomposition;
- a missing table of contents;
- absent priorities;
- a missing section that may be a delegation.

A lens never reports these as defects in a solution design:

- a part whose detail is left to the file it names;
- a choice said to have had no real alternative;
- a section deleted for being empty.

Which filed findings a lens re-tests depends on the report that
holds them:

- A report without a lens in its name belongs to the retired single
  critic. Its findings belong to a lens where they fall under the
  categories of that lens.
- A report of a check shares the sequence of finding IDs with the
  critic. Its findings never belong to a lens.

### What it produces

A lens returns its report in its final message and writes no file.
The `/critique` command files the report in `reviews/`, and
`scripts/forge-report.py` completes the name of the file. The command
gives each new finding its ID. The lens gives a new finding no ID and
names a known finding by the ID it has. No ID is therefore given
twice.

The report is dated, immutable and written in English. It names the
lens, the target and every file that was read, with the version
where a file has one. Its matter has four parts:

- The delta summary: the count of new findings, and the known
  findings by their state.
- The findings: each with its severity, its category, a headline of
  one line, the location, the issue, why it matters and a suggested
  fix.
- The recommendations: wording that is hard to test, groups that
  overlap, items that could be split. They are not findings and not
  gates. The principal may ignore them without recording anything.
- The sections of the lens itself, as the lens defines them.

After the filing, the command offers a
[walkthrough](../reference/glossary.md) (the conversation in which
the principal gives a verdict on each finding). The states of the
findings are kept as records, and the ledger is made from them.

### One contract, one Lens section each

Each lens is one agent file, `critic-<lens>`. What every lens shares
is written once, in the contract of the critic
(`.claude/skills/critic-contract/SKILL.md`), and loaded into each
lens. The contract holds four things:

- conduct and isolation;
- the subject and its boundary;
- the way of working;
- the shape of the output.

Only the Lens section of an agent file belongs to the lens. A Lens
section is a specialisation of the contract, never a replacement. It
may narrow what is read or make a shared rule stricter. It never
renames, drops or duplicates a shared rule or field. The protocol
changes in the contract alone.

A new lens is added only by the principal's decision, and only where
what it finds genuinely differs. The way is described in
[Add a critic lens](../extend/add-a-critic-lens.md).

## Why

- **Why a lens is isolated.** A lens never sees the working
  conversation. That blindness is the source of its value.
- **Why two lenses.** One critic hunted formalities and never guarded
  the chain. `essence` is the lens that guards the chain against
  drift. That is also the reason a release offers `essence` and no
  other lens: it guards what a release publishes.
- **Why a target.** One file or one transition can be reviewed alone.
- **Why any file may be the target.** What Claude composes and the
  principal judges, a work product above all, deserves the isolated
  look as much as the chain. The cost is a report that sometimes
  says there was nothing to find.
- **Why no arrow is typed.** Every layer has exactly one parent. The
  downstream artefact is enough to name the transition.
- **Why a lens runs on the principal's word alone.** A run costs
  tokens, and what is spent is the principal's to decide. There is
  no other reason.
- **Why the same model.** Speed is bought with context, never with a
  weaker reviewer.
- **Why testability is a recommendation.** Testability is
  recommended, never required. Assignments are deliberately
  high-level. Delegating the concretisation through a `DEL` item is
  a legitimate outcome.
- **Why deliberate omissions are not defects.** The principal sets
  direction. The assignment deliberately stays high-level, and its
  recipients are assumed competent and senior. A missing section may
  be a delegation. A solution design holds what cannot be read off
  the thing itself.
- **Why a rejected finding is not raised again.** Findings are
  advisory and the principal decides. The ID of a finding gives its
  verdict a place. A finding without an ID has no place for its
  verdict, and a rejected one would return at the next run.
- **Why the command gives the IDs and never the lens.** The rule
  holds for every kind of reviewer alike, and three reasons are
  given:
  - The IDs of a project's findings and challenges are given in one
    place.
  - Two reviewers run at once would otherwise take one ID.
  - A check that every save runs would otherwise write into the
    project at every save.

  The lens therefore returns its findings unnumbered, and reviewers
  of any kind may run in parallel.
- **Why the critic and the checks share one sequence of IDs.** There
  is one mechanism for every reviewer. With two, nobody could tell
  why the findings of one reviewer are kept and those of another are
  not.

For three rules the reason is not recorded:

- regression first;
- sharp and few beats thorough and long;
- each artefact judged against its own definition.

## A worked example

The principal runs `/critique clarity intent` on a project. The lens
reads the intent on its own and finds one word used for two things.
Its report carries this finding:

```markdown
### [medium] [<category of the lens>] — One term carries two meanings
- **Location:** `10-intent.md`, two items of one group
- **Issue:** The first item uses "platform" for the shared runtime.
  The second uses it for the team that operates the runtime.
- **Why it matters:** A recipient who reads the second item with the
  first meaning reads a different requirement.
- **Suggested fix:** Keep "platform" for the runtime and name the
  team by a word of its own in the second item.
```

What the example shows:

- The finding is about the document. The lens does not say what the
  platform should be or whether the requirement is right. It proposes
  a fix of the wording.
- The category is one of the categories of `clarity`, which
  [Critic lenses](../reference/critic-lenses.md) lists.
- The finding leaves the lens without an ID. The command files the
  report in `reviews/` and gives the finding an ID of the project's
  one sequence of findings, with the prefix `FND`.
- In the walkthrough the principal gives a verdict. A rejected
  finding is not raised again. A finding marked resolved is re-tested
  at the next run of `clarity` and reported as verified or reopened.
- Had the lens found only that an item is hard to test, the remark
  would stand among the recommendations and not among the findings.

## See also

- [Critique the documents](../use/critique-the-documents.md): running
  a lens.
- [Critic lenses](../reference/critic-lenses.md): the lenses and
  their angles.
- [Add a critic lens](../extend/add-a-critic-lens.md): adding a lens
  of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
