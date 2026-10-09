---
date: 2026-10-09
project: forge
target: intent v4.64
reviewed: projects/forge/10-intent.md v4.64; projects/forge/threads.md (2026-10-09); projects/forge/00-brief.md (placeholder, DEC.0010); projects/forge/00-brief-next-gen.md v0.3; projects/forge/00-brief-documentation.md v0.1; projects/forge/00-brief-public-engine.md v1.0; projects/forge/00-brief-elicitation.md v1.0; projects/forge/40-solution-design.md v0.7; projects/forge/decisions.md (DEC.0010 to DEC.0180); projects/forge/ledger.md (2026-10-09); projects/forge/10-intent.history.md (head, the records of 4.42); projects/forge/10-intent.history.archive.md (row 4.0); projects/forge/sources/00-INDEX.md; projects/forge/research/2026-10-03-operating-claude-code-for-many-users-in-a-company.md; projects/forge/research/2026-10-03-the-threshold-of-entry-for-a-non-developer.md; projects/forge/research/2026-10-03-testing-the-behaviour-of-a-prompt-framework.md; projects/forge/challenges/2026-08-17-challenge-cto.md (CHL.0010 to 0060); projects/forge/challenges/2026-08-29-challenge-cto.md (CHL.0070 to 0130); projects/forge/challenges/2026-09-06-challenge-cto.md (CHL.0140 to 0190); .claude/skills/forge/states/intent.md; .claude/skills/release/SKILL.md; .claude/skills/challenger-contract (as delivered); docs/README.md (front-matter only, version 4.62); projects/agentic-platform/ledger.md, projects/flow-ba/ledger.md, projects/forge-rollout/ledger.md (header and Documents rows only: versions and dates, no content); CLAUDE.md as delivered in context, not re-read from disk; no challenge rests on its wording
reviewer: challenger persona cto (CTO register, isolated context)
---

# Peer review (cto) — 2026-10-09

## Overall read

As written at 4.64, this intent is the design record of a working
single-author engine. Since 4.0 (2026-09-06; sixty-four minors in
thirty-three days) it has gained an elicitation per artefact, a
solution design layer, a history log, Python scripts and generated
documentation, every one of them the engine's, and most of the
earlier challenges have been absorbed rather than waved away. Where I
disagree is what the major is for. The approval is being timed to a
presentation (THR.0570), not to a closed set of features; the
audience that presentation serves is the one the intent names first
(the company rollout, POS.0980) and the one the project's own
research of 2026-10-03 says the fixed shape may not reach; and the
brief that carries that evidence (`next-gen` 0.3) is pending and
unmined. 5.0 as queued would sign, as "approved", a document that by
its own thread still carries solution in twenty-two positions, over a
solution design the principal has not read whole, tested by checks
that verify the paper against the paper.

## Challenges

### CHL.0200 — The major is for a date, and nothing named closes
- **Severity:** major
- **Challenge:** POS.0300 says a major "closes a set of features the
  principal names". No set is named: THR.0570 holds "whether a major
  is made before the presentation and what it closes" open, and the
  one argument on record for making it is Claude's, a fixed point for
  the audience to pull to. Three matters stand open that an approval
  would sign over. (1) THR.0520's second pass: the intent still
  carries solution in twenty-two listed positions and three stale
  places (POS.0600 and POS.0620 still speak of the assignment as where
  version 1 ends), six days after POS.1390 made solution in the
  intent a defect. (2) The solution design at 0.7 says in its own
  head that it is a proposal "not yet judged by the principal" and
  that the forge "cannot yet be built from its artefacts alone", which
  is what POS.1400 asks of a chain. (3) The brief `next-gen`,
  pending, asks in its first section whether "we are not heading
  somewhere that cannot be managed": a question the principal raised
  about the whole and has not answered. 4.0 closed a named set, "the
  engine's operating layer" (archive row 4.0). 5.0 would close a
  presentation date.
- **Why it matters:** A major is the one promise the forge makes to a
  reader outside the conversation (POS.1100: an integer is a released
  major, anything else a snapshot). If what it attests is that the
  principal felt done in the week of the talk, the signal CHL.0190
  asked for and POS.0300 gave is spent at its second use. The cheaper
  thing exists: a snapshot release carries the fixed point the
  presentation needs, and the major waits for the named set.
- **What would change my mind:** A named set 5.0 closes, written into
  the approval record, with the twenty-two-position pass done or
  deferred with its reason; and either the principal's reading of
  the solution design or a statement that the major approves the
  intent alone and the design stays 0.x, unjudged.
- **Epistemic status:** my judgement; the facts read from THR.0520,
  THR.0570, the head of `40-solution-design.md` 0.7 and the archive
  row of 4.0.

### CHL.0210 — The first audience cannot, as far as the project's own research knows, run the shape 5.0 fixes
- **Severity:** major; a dealbreaker for the rollout ambition if the
  company's Claude Code deployment locks customisation to plugins,
  which I cannot see from here
- **Challenge:** POS.0980 puts the rollout in the company first. The
  research of 2026-10-03 on operating Claude Code in a company found,
  at the vendor's pages, three managed settings that switch off,
  silently and without an error the forge would see, the three things
  the forge is made of: `strictPluginOnlyCustomization` drops
  project-level skills and agents, `allowManagedHooksOnly` drops the
  per-prompt hook, `allowManagedPermissionRulesOnly` drops the deny
  rules that make the scripts the only door to git. Its own sentence:
  "A company that locks customisation to plugins can run the forge
  only as a plugin from a marketplace it has allowed." The plugin is
  the shape the intent has deferred three times (REJ.0150, THR.0190,
  and `engine-split` after `brd` in POS.1380). Three further findings
  of the same day stack on it. The threshold-of-entry note counts
  eleven steps to the first useful question, nine of them before any
  thinking, every prerequisite the forge's own, and reports "nothing
  in this field ... built for analysts". POS.1110 declares the forge
  "a single-user tool per instance" while the brief `next-gen`
  reports the first two-person company project as "very unpleasant"
  and its collisions silent. POS.0930 forbids the one cost lever the
  vendor names first, and nothing measures what a forge operation
  costs in tokens (THR.0410 measures minutes), for an audience on
  per-seat allowances. None of this stands in the intent as a
  position, a fact or a rejection; it stands in a pending brief. The
  rollout project itself (`forge-rollout`, a process fact: brief 0.1,
  intent not started, last touched 2026-10-03) has no intent.
- **Why it matters:** The presentation would show a v5 whose "next
  generation" brief lists, as still to be found, the properties the
  people in the room need in order to use it: who the user is,
  several people on one project, upgrade and compatibility, operation
  in a company, the threshold of entry. The rational response of a
  colleague behind managed settings is to clone v5, see nothing load
  and conclude the forge does not work; of a colleague without them,
  to count the eleven steps and wait. Either way the forge learns
  nothing, because POS.0780 keeps adoption outside its sight and
  POS.0170 gives feedback no channel.
- **What would change my mind:** One fact, recorded as a FCT with its
  source: the managed settings of the company deployment as they
  stand, the three locks off and project customisation allowed. Or
  the first audience moved: a major that names the principal's own
  use and the public project as what it serves, and the company
  rollout as what `next-gen` is for.
- **Epistemic status:** the lock mechanism: verified at the project's
  research of 2026-10-03, which read the vendor's pages; the
  existence of the three settings confirmed today from secondary
  sources, their effect list not re-read at the vendor's page. The
  field finding on analysts: the research's own, taken as it stands.
  The weight: my judgement.

### CHL.0220 — The test of a major tests the paper against the paper; what the user pulls is behaviour
- **Severity:** major
- **Challenge:** POS.0300's test for a major is every check, both
  critic lenses and one challenge. Every item of it reads documents:
  the checks verify files against conventions, the critic reads
  document quality, I read the thinking. Nothing in it runs the
  engine. The project's own research on testing (2026-10-03) says it
  plainly: static checks prove "the files agree, not that the model
  obeys them", "would not have caught a change of conduct", and the
  forge has only those. It names a cheap option, a handful of
  scripted scenarios with file-level assertions, three trials each,
  run before a release, and the intent has neither a position nor a
  thread on it. Below the intent the gap is stacked: TBC.0020 says no
  check keeps the solution design true to the files that realise it,
  and SOL.0620 records that the Python scripts "have not been run on
  Linux" while POS.0830 says itself that portability "is a writing
  rule, not a claim" until they are. Of the test that does exist, one
  part has now been declined at both majors: `essence` at 4.0 by the
  principal's word (archive row 4.0) and at 5.0 in advance
  (THR.0550). The rule says both lenses; the practice is one.
- **Why it matters:** v4 was offered to the user as "the point to
  pull to". What he pulls is a set of instruction files whose
  behaviour was verified by the author's own sessions and by nothing
  else, and a model or harness update between majors changes that
  behaviour unverified; the research quotes the vendor's own reason
  for evals, that a skill which worked last month may behave
  differently today. The forge's recorded failures are all failures
  of conduct, not of files: the thirteen walkthrough breaks behind
  POS.1170, the six edits behind POS.1460, the two raw git reads
  behind THR.0400. The test of a major catches none of that class.
- **What would change my mind:** Either a stated reading of POS.0300,
  written where the user reads it (the head of the release notes),
  that a major attests document conformance and nothing of behaviour;
  or the smallest behavioural suite the research describes, run once
  before 5.0 on the three recorded failures, with its result in the
  approval record.
- **Epistemic status:** consensus on the method (the research's
  sources, Anthropic, OpenAI and Google, agree on scripted scenarios
  drawn from real failures, several trials, outcome over path); my
  judgement that a major without any of it is a date with an integer.

### CHL.0230 — The rules are written as walls and held as preferences, and a second user cannot tell which is which
- **Severity:** major
- **Challenge:** The intent states its mechanisms as absolutes, and
  the record shows each bending at the first price, honestly recorded
  every time. One model for the whole forge (POS.0930): the README
  rendered on another model on the principal's word at the release of
  2026-10-02 "against the rule of `/render`" (THR.0410), then the
  documentation writer put on a faster model a week later, the
  exception written into the position. The scripts as the only door
  to git, "no exceptions" (POS.0550, POS.1200): DEC.0120's force-push,
  "knowingly, once". Immutability (POS.0320): the pre-publication
  rewrite (POS.0980) and DEC.0110's two edits of locked files. Step by
  step (POS.1460): six edits of the core file on 2026-10-03. Both
  lenses at a major (POS.0300): one lens, twice. Each exception was
  defensible in its moment; the pattern says the absolute is the
  wrong grain for the rule. The research on company operation asks of
  a framework exactly what an absolute cannot give: "behaviour that
  degrades visibly, not silently, when a company has restricted the
  model, the permission mode or project-level customisation". A rule
  written "one model, no pins" has no degraded form; a rule written
  "the session model unless X, and then say so" has one.
- **Why it matters:** The documentation command generated eighty-odd
  pages that mirror these positions for three readers, the user
  first. He reads the walls; the author knows the exceptions. The
  user either complies literally, every check and render on the
  strongest model, five to eight minutes a README (THR.0410), on a
  seat allowance, or learns from the record that the author bends
  them and stops trusting any of them. The second is the rational
  choice, and it is the behaviour THR.0400 and POS.1170 exist to
  prevent in Claude, now transplanted to the user.
- **What would change my mind:** A position, or a rule for positions,
  that says which mechanisms are walls (held by the harness, no
  exception on record) and which are defaults with a stated degraded
  form, and the record shown to match it for the five above.
- **Epistemic status:** the five exceptions read from the intent, its
  history, `decisions.md` and the threads; reading them as one
  pattern is my judgement.

### CHL.0240 — The intent's own Map is not walked for the forge: no recipient, no objective, no measure, and the layer below declared for an audience that does not exist
- **Severity:** minor
- **Challenge:** The intent's definition
  (`.claude/skills/forge/states/intent.md`, Map) asks, before the
  approval, for "what the layer below will need: the recipients, the
  objective and the success criteria" and for "reality: what of it is
  feasible". The intent's own closing section says the layer below is
  "not applicable ... for an audience that does not exist". That
  sentence predates the solution design, which is that layer at 0.7,
  and the rollout project, which exists. The brief `next-gen` opens
  with "by what one tells that it works" and "who the target user is"
  as open in the aim itself. The forge at 4.64 has no success
  criterion for itself anywhere, and POS.0780 keeps outcomes outside
  its sight by position, which was the right answer to CHL.0010 for a
  subject project and is no answer for a rollout the principal is
  about to stand in front of. On the chain side, the process facts of
  the other ledgers: no assignment of any subject project has moved
  since 2026-09-04, sixty-four versions of the forge intent since.
  The question of 2026-09-06, whether the chain positions are stable
  because they are right or because they are unused, has nothing
  since to answer it.
- **Why it matters:** The Aim approves an intent only after "a final
  reality check before a lower layer is derived". The Map's reality
  area has no entry for the forge beyond Claude's observations of
  Claude Code (the Facts section says so); the feasibility question
  the `next-gen` brief raises about the whole is that reality check,
  and it is pending.
- **What would change my mind:** The Map walked aloud for the forge
  intent before 5.0, as the definition prescribes, with the
  recipients of the engine named (the principal, the public project,
  the company user) and one sentence per audience on what "it works"
  would mean; and the closing section brought to the existence of the
  solution design.
- **Epistemic status:** my judgement; the Map read from the state
  file, the rest from the files.

## What is strong
- POS.1390 and POS.1400: the cut between intent and solution is the
  right one, the one the earlier reviews circled without naming, and
  the test of a sentence ("would it still hold if the thing were
  realised in a wholly different way") is usable by anyone.
- The record keeps its own exceptions (DEC.0110, DEC.0120, the
  cleaning at 4.42 verified three ways and mechanically). That honesty
  is what makes CHL.0230 arguable at all; most projects could not
  show the pattern because they would not have written it down.
- POS.1410 (handing over, with the list of what was assumed and
  chosen) and the eighteen researches of 2026-10-03 with their
  epistemic marks: the forge reads its own evidence better than it
  yet acts on it.
- POS.1450 and the first run of `/document`: a documentation that
  cannot drift from its owners is the right mechanism for a tool whose
  owner changes it daily.

## Questions I cannot answer from the documents
- What are the managed settings of the company's Claude Code
  deployment: are project skills, agents, hooks and permission rules
  allowed, and on which plan? CHL.0210 is a dealbreaker or a footnote
  on this alone.
- What is the audience to hold after the presentation, a clone, a
  plugin, a pitch, and is anyone in the room expected to run the
  engine before `next-gen` is worked? THR.0570 records the question
  as Claude's, unanswered.
- Has any person other than the principal started a session on the
  engine at 4.x and reached `/forge intent`? The run record of
  `health` was the author's own.
- What does a release of the forge cost in tokens on the session
  model, the three checks and the two renders, per run? THR.0410 has
  minutes; the `next-gen` brief lists cost and nothing measures it.
- Is 5.0 meant to approve the solution design as well, or the intent
  alone with the design at 0.x? The ledger's Documents table will say
  "approved" for one file and "draft" for the other, and the user who
  pulls the tag cannot tell which it covers.
