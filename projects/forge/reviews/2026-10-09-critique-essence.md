---
date: 2026-10-09
project: forge
lens: essence
target: intent v4.64 (against the briefs above it and 40-solution-design v0.7 below it)
reviewed: 00-brief.md (placeholder, DEC.0010), 00-brief-public-engine.md v1.0, 00-brief-elicitation.md v1.0, 00-brief-next-gen.md v0.3, 00-brief-documentation.md v0.1, 10-intent.md v4.64, threads.md, 40-solution-design.md v0.7, 40-solution-design.history.md, decisions.md (to DEC.0180), ledger.md (2026-10-09), reviews/2026-08-27-critique.md (FND.0070 regression), CLAUDE.md on disk (Working methods), .claude/skills/forge/states/intent.md, .claude/skills/forge/states/solution-design.md, templates/ledger.md, .claude/skills/render/SKILL.md (searched for the instance-fact rule)
reviewer: critic lens essence (isolated context)
---

# Critique (essence) — 2026-10-09

## Delta summary
- **New:** FND.1310, FND.1320, FND.1330, FND.1340, FND.1350
- **Verified resolved:** FND.0070
- **Still open:** —
- **Newly obsolete:** —

No earlier run of this lens exists. Of the retired single critic's
findings only FND.0070 (`divergence`, 2026-08-27) falls under this
lens: it named a README three rounds behind the intent. The README
has been re-rendered by every release since (last 2026-10-09 from
intent 4.59, ledger Renders), and the staleness of a render is no
finding by POS.0570; verified resolved.

THR.0550 records that the principal declines this lens on the
project `forge` for now. This run was ordered by the session that
launched it; the report stands as any other and is the principal's
to settle or reject.

## Findings

### FND.1310 [medium] [lost]
- **Location:** 40-solution-design.md, SOL.0010 (Realises) and the
  head's list "No part answers …"; against 10-intent.md POS.1460,
  POS.1470, POS.1480
- **Issue:** The intent at 4.63 gave three working methods a
  position of their own: Step by step (POS.1460), Plain speech
  (POS.1470), A rule says the kind, never the count (POS.1480). The
  solution design, bumped to 0.7 the same day, realises none of them:
  SOL.0010's Realises list carries the methods up to POS.1210 and
  POS.1410 and stops there, and the head's list of positions no part
  answers does not name them either. The parts exist on disk
  (CLAUDE.md, Working methods, carries all three), so the realisation
  is not missing; the design's account of it is.
- **Why it matters:** The design's own completion test (its
  definition, Aim) is that every in-scope item of the layer above is
  realised by a part, knowingly left unanswered, or a TBC. Three
  positions are in none of the three states, so the design is behind
  its intent without saying so, which is exactly what POS.1420 says
  it must not be.
- **Suggested fix:** Add POS.1460, POS.1470 and POS.1480 to SOL.0010's
  Realises, or, if the principal holds that conduct rules need no
  part, name them in the head's list of positions no part answers,
  with the reason that list gives.

### FND.1320 [medium] [shifted]
- **Location:** 40-solution-design.md, SOL.0500 and SOL.0460; against
  10-intent.md POS.1450
- **Issue:** POS.1450 wants the facts no file owns, the public
  address of the repository among them, to have "one place in the
  project that both the README and the documentation read". The
  design names two. SOL.0500 carries the public address itself and,
  by its record of 0.6 in the history, is "the one owner the
  documentation reads it from"; SOL.0460 says the pinned facts the
  planner reads as an owner are the section "Pinned facts (not
  rendered)" of the readme recipe. The intent's one place has become
  two in the layer below, with no DEC and no thread saying which is
  the owner and why the other stays.
- **Why it matters:** The documentation and the README are generated
  from whatever file the planner and the recipe name; two owners of
  one fact is the drift POS.1450 was written to prevent, and the
  design is where whoever realises the forge looks to learn which
  file to change.
- **Suggested fix:** Name one owner in the design and have the other
  item cite it: either SOL.0500 drops the address and points to the
  recipe's pinned facts as SOL.0460 has them, or SOL.0460 says the
  planner reads the address from where SOL.0500 keeps it. The
  history's record of 0.6 then reads as what it is.

### FND.1330 [low] [lost]
- **Location:** 40-solution-design.md, SOL.0530 and SOL.0460; against
  10-intent.md POS.1450
- **Issue:** POS.1450 says a release never regenerates the
  documentation: it reports the age of the index against the intent's
  version and offers `/document`. SOL.0530 enumerates what `/release`
  does (checks, findings, README, release notes, save with tag) and
  carries no word of the documentation; SOL.0460, the part that
  realises POS.1450, says nothing of a release. The behaviour the
  intent wants of the release is realised nowhere the design can
  show.
- **Why it matters:** A reader of the design would build a release
  that either ignores the documentation or, following the older
  pattern of the README, regenerates it, which is what the intent
  and the brief `documentation` both rule out.
- **Suggested fix:** One sentence in SOL.0530 (or SOL.0460) saying
  that the release reports the index's age and offers `/document`,
  the detail being the release skill's, as the ledger's FND.1080
  already settled for the operating layer.

### FND.1340 [low] [provenance]
- **Location:** 40-solution-design.md, the head (first paragraph);
  SOL.0170, SOL.0450, SOL.0460, SOL.0620
- **Issue:** The head states the design's provenance as a whole: the
  solution stands "as it stood in the intent at 4.55", "no choice in
  it is new", what was read from files was read "on 2026-10-04", and
  the whole is "not yet judged by the principal". Four items postdate
  that: SOL.0170 (intent 4.57), SOL.0450 (4.58), SOL.0460 (4.60),
  SOL.0620 as rewritten (4.61), each with choices and dates of its
  own; and THR.0520 records SOL.0170 as handed over and judged by the
  principal at step 5. The definition (The shape of an item) wants
  the unjudged mark at the item, until he has judged it; the head's
  blanket mark no longer tells which items are the one-off move of
  step 4 and which came later, nor which have been judged.
- **Why it matters:** The principal reads the design to judge it
  (THR.0520 says he has not read it whole); a provenance claim that
  is true of some items and not of others makes the judged and the
  unjudged indistinguishable.
- **Suggested fix:** Keep the head's claim for the items of 0.1 by
  saying so ("the items of 0.1 stand as the intent had them at 4.55;
  later items name their own date"), and move the unjudged mark to
  the items that carry it, as the definition asks.

### FND.1350 [low] [lost]
- **Location:** 00-brief-documentation.md, "What I do not want" and
  "The outline" (last sentence); against 10-intent.md POS.1450,
  threads.md, ledger.md Briefs (row of the brief)
- **Issue:** The brief defers two pages by name: a tutorial with a
  worked example, after a public exemplar exists, and troubleshooting,
  when there is material. The intent's Map asks for "what he
  deferred, which is not dropped" to be carried; POS.1450 carries
  neither, no thread does (THR.0200 holds the exemplar and says
  nothing of a tutorial; THR.0590 is the other projects' reading),
  no REJ drops them, and the ledger's Briefs row says the brief is
  mined without a note of what was left behind.
- **Why it matters:** A deferral that survives only in the brief is
  found again only by rereading the brief, which is what the intent
  exists to make unnecessary (POS.0120).
- **Suggested fix:** A clause of POS.1450 or of THR.0200 naming the
  two deferred pages and their condition, or the Briefs row's note
  saying they were knowingly left in the brief.

## Recommendations
- 00-brief-next-gen.md (pending) carries in "Automation" the thought
  that a task can be handed over whole and comes back as a proposal;
  the intent already holds it as POS.1410, decided 2026-10-03 from
  THR.0520 and citing no brief. When the brief is mined, the row's
  note or POS.1410's provenance could say that this half of the
  section already stands, so the mining does not find it twice.
- 40-solution-design.md: the head says no part answers POS.0700,
  while SOL.0170 lists POS.0700 under Realises. One of the two should
  give; wording, the `clarity` lens's.
- 00-brief-public-engine.md defined a library as "a project with only
  `sources/`"; the intent widened it to `research/` and a README
  (POS.0970, POS.1000, with the reason in POS.1000). Nothing to
  record; noted so the widening is seen as deliberate.

## Distillations

### 40-solution-design.md v0.7 — essence
Read first, before the intent. A proposal handed over to Claude and
declared unjudged, made as a one-off move that lifted the solution
out of the intent as it stood at 4.55. It wants to tell whoever
rebuilds the forge what cannot be read off the files: that the forge
is instructions Claude Code reads, held by four ideas (one always-on
core and files read when their situation arises; state in the
project's Markdown; isolation bought with subagents on one model;
git, conversion and the hook as scripts), what each part is, which
positions it answers for, the choice behind it with its cost where a
real choice existed, and where it lives. It rules out designing the
wording of any file, how an artefact is found, and anything beyond
the files the forge makes, and names six positions no part answers.
It admits it is not enough to build from alone. It leaves open the
Mermaid dependency, the check that keeps it true, and the
independent challengers. Several items carry dates later than the
move it claims to be.

### 10-intent.md v4.64 — essence
Read second, before the briefs. A general-purpose engine in Claude
Code where anyone's thought travels a chain of versioned documents
from a brief through an intent to whatever layers the project needs,
Claude the cognitive extension that owns structure and proposes but
never decides, isolated reviewers blind to the conversation as the
adversarial pressure. It wants: a way of working (ask, elicit, one
write per round, walkthrough, step by step, plain speech, kind not
count); elicitation defined per artefact in seven blocks; a brief
that is the principal's choice from a wide finding, mined into one
intent that says what holds while its threads say what is worked; an
assignment complete and precise; a solution design that says how,
kept current, derived from the lowest layer above it; history as a
log beside every versioned document; one reviewer mechanism with
contracts, lenses, personas and checks; git only through scripts,
the harness enforcing the principal's word where it can; two speeds
of persistence; one model; one mechanism in one place; a public
engine split from private projects, open to contributors, documented
by generated pages; the chain extended by one command; independent
challengers planned. It rules out gates, priorities, a feedback
channel, a wrapper of git, a plugin now, recipes per page, a site,
a hand-kept philosophy. It leaves open the engine split, user
extensions, derivations, the gate before the tools, the session's
end, the stale clone, the second pass that moves the remaining
solution out. It knows it still carries solution (THR.0520).

### 00-brief.md — essence
A placeholder: the brief stage was skipped and the intent is the
earliest record (DEC.0010). No pair to review.

### 00-brief-public-engine.md v1.0 — essence
The forge as a project of its own that can go on git without worry,
nothing sensitive in it, anyone able to use it with projects in
repositories of their own, still driven by the forge's scripts. The
goal is publication: company rollout first, a public project a
community might form around, a showcase. The engine is the author's
to publish. Six conditions: separate the engine's upkeep from the
projects; everyone's own git and visibility; easy upgrade with a
conformance check and no engine version in the project; seamless
work as now; no sensitive content and no instance facts; scripts on
every platform. Promising: the engine as a clone with nested
repositories; a plugin later with no preparation now. Agreed in
outline: no policing of git, the forge project stays inside, a
library as a kind of project, `local/` dropped, instance facts in a
two-line local file, a kind marker in the ledger, output language
opened, a public boundary with one knowing rewrite of immutables, a
fresh history, a tag at every approved major.

### 00-brief-elicitation.md v1.0 — essence
One mechanism and shape for composing every artefact, user-definable
in time. Elicitation is finding, not conversation; the map of what
must be found stands before the template; every artefact type gets a
definition of seven blocks, and the brief's, the intent's and the
assignment's are worded here. A brief holds the principal's choice
from a wide finding and no mark of authorship; certainty is said in
words; the horizon lives in all three layers, each its own kind. The
boundary for a user's own additions is mechanism versus instance.
Order: the elicitation first, then `brd`, then `engine-split`; the
proof is conduct, the definitions to be tried on real work before a
rule leaves CLAUDE.md. Opens the recipients, objective and success
criteria as a staging area of the intent, and `/critique essence` as
the assignment's test of drift. Admits it is not a model of a brief.

### 00-brief-next-gen.md v0.3 — essence
Requirements for a forge that can be rolled out into real operation,
thrown in to be sifted later, thought as a whole rather than task by
task: the shape of the whole, user modifications, work without a
known artefact, further outputs and files, automation and handing a
task over whole, several people on one project, connection to the
systems around, upgrade and compatibility, testing the engine's
behaviour, operation in a company, a technical clean-up, news, the
threshold of entry; each with its research. Names the threads it
carries whole, in part and to be sifted. Opened THR.0520 from the
talk over it. Open in the aim itself: what rolled out means and who
the user is.

### 00-brief-documentation.md v0.1 — essence
The documentation as generated pages of one topic each in `docs/`,
readable on GitHub and in a clone, with an index; three readers in
order; the same outline of five sections for every project, filled
only where material exists; the README cut to orientation. Generated
by a command of its own in two phases, a mapper on the session model
and page makers on a faster one, the state by content hashes, the
map beside the ledger, the index derived by script; philosophy
derived from the brief and the intent; facts no file owns in one
place both README and documentation read; no instance facts. Not
wanted: a recipe per page, a site now, pages by hand, regeneration
at every release, a hand-kept philosophy, waiting for the split, the
news (stays in `next-gen`), a tutorial before an exemplar. Later: a
tutorial, troubleshooting, the news. Open: the outline against the
research, other projects' reading, the map's name and shape, the
pinned facts' place, where the agents live, the faster model, the
instance-fact scan, a link check, what a release does, stale owners.

### 00-brief-public-engine.md → 10-intent.md — comparison
Every want of the brief has its position and the positions cite the
brief: the split (POS.0760), the engine not knowing the projects and
the migration path (POS.0940), instance facts out (POS.0950), the
kind and the library (POS.0960, POS.0970), publication with its
audience, boundary and fresh history (POS.0980), the public face
(POS.0990), the scripts as the only door on every platform
(POS.0550, POS.0830), the tag at a major (POS.1100), the output
language (POS.0060); the shapes rejected are REJ.0140 and REJ.0150;
the plugin and the exemplar are THR.0190 and THR.0200. The library
grew a `research/` and a README on the way (POS.1000 gives the
reason). The one-off migration and the company's first library stay
out of the intent by the ledger's note. Nothing lost, nothing added
without provenance.

### 00-brief-elicitation.md → 10-intent.md — comparison
The brief's substance is POS.1300 to POS.1380 and POS.0110, every
position citing the brief and its date. Three turns against the
brief are each traced: the walkthrough of every consolidated
position was dropped with REJ.0230; the lock of a brief was withdrawn
in POS.0110 and recorded in THR.0520; the brief's "tried on real
work before any rule leaves CLAUDE.md" became POS.1380's "used on
real work at once and mended there", with the reason given and the
principal's word named. The three questions the brief left for the
intent went into threads, two closed at 4.46 by the ledger's note.
The split material went to THR.0230 and THR.0300. Nothing lost
without a trace.

### 00-brief-next-gen.md → 10-intent.md — comparison
Pending by the ledger, so nothing of it is expected in the intent
yet beyond THR.0520, which the brief and the thread both record. One
thought of the brief already stands as a position without citing it
(POS.1410, the handing over of a whole task); a recommendation, not
a finding, since the mining is still to come.

### 00-brief-documentation.md → 10-intent.md — comparison
The brief asked for one position and one part and got them: POS.1450
and SOL.0460, with the kinds `map` and `page` in POS.1080, the faster
model for a mirrored page in POS.0930, the instance-fact scan in
POS.0950, the three things not wanted as REJ.0240 to REJ.0260, the
other projects' reading as THR.0590. Every open question of the
brief is answered in the intent or in the design except the fate of
stale owners, which the first run overtook. Lost without a trace:
the two pages the brief deferred, a tutorial after an exemplar and
troubleshooting when there is material (FND.1350).

### 10-intent.md → 40-solution-design.md — comparison
The design realises the intent position by position, and the six it
answers nothing for it names with a reason; what the intent wants
and the design cannot yet give (buildable from the artefacts alone,
a check that keeps it true, the independent challengers) is a TBC or
named in the head and in THR.0520. Three positions of 4.63 have no
part and no reason for having none (FND.1310). The intent's one
place for the public address is two places in the design
(FND.1320). What the intent wants of a release towards the
documentation is in no part (FND.1330). The head's provenance claim
holds for the items of 0.1 and not for the four added since
(FND.1340). The solution the intent still carries, by THR.0520's
list for a second pass, is traced there and is not re-raised.
