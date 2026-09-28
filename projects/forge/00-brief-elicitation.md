---
project: forge
title: Elicitation — one mechanism and shape for composing every artefact, user-definable
date: 2026-09-28
author: PCHe
version: 0.5
status: draft
last_change: 0.5 (2026-09-28): the brief is mainly the principal's text and Claude may work on it; a mechanism may stand in a brief where it is part of the idea; a structure before the lock on the principal's word; the walk of the Map asks and does not mend; the intent's Map looks at the briefs as wholes.
---

<!-- Born in the forge on 2026-09-28. Everything below is the
principal's: what is in the brief he approved, whoever first said it.
A source is cited as (source: <path>); a remark the principal did
not adopt stands as (remark: …). -->

## A note on this brief itself

This is not a good brief, and no brief should look like it. It
grew to some 580 lines, with three definitions worded block by
block and two rounds of walkthrough over exact wording: we went
straight to the intent's work and did it in a brief. Decided
2026-09-28: it is finished as it stands and not cut down by force,
so that the work is not thrown away. It is the exception and must
not serve as an example. What it taught goes into the definition
of the brief's elicitation below.

What a brief is, in the principal's words: a brief is a free
structure for putting an idea together, which is then chiselled.
It is not perfect and should not be overly detailed: a brief
chiselled so far that no work is left for the intent is not good.
Nor is it a map of everything we went through: on the ground of
research, ingestion, my ideas and yours, decisions are made about
what goes into the brief and what does not. In my mind the brief
on elicitation is at most one A4 of free text where I write what I
want; on that we make the intent, where we write the maps, decide
on the seven blocks and describe the elicitor.

## Where the elicitation lives today

Where does the elicitation of an artefact live today — the way we
talk over a brief, an intent and so on? In CLAUDE.md, or in the
agents and skills?

Three layers, each with a different role. CLAUDE.md carries
principles only: prime directive 1, the working methods (elicitation
interview, walkthrough, in pieces, draft early, reflect back) and
Document chain 1–3. The walkthrough skill carries the shape of the
conversation shared by everything: one item per message, what an
item carries, the verdict line, how verdicts reach the write; its
section "The elicitation interview" says an interview runs the same
way. The `/forge` state files carry what differs per artefact:
`brief.md` (role clarifier and reality check; clarify, correlate with
reality; three ways a text arrives), `intent.md` (role elicitor; six
rules of the interview), `assignment.md` (role drafter; the one
elicitation question is the success criteria). The agents take no
part: critic, challenger and check are isolated reviewers that never
see the conversation.

The mechanism for a per-artefact elicitation already exists:
`/forge <state>` resolves `.claude/skills/forge/states/<state>.md`
(how we get there) and `templates/<artefact>.md` (what is to come
out); a new artefact is a new pair of files and the dispatcher never
changes. The pair is unbalanced: the template carries the structure
of the result well; the state file carries a role and rules of
conduct, but nowhere is there a statement of what a given artefact
needs to have found before it is complete. The precedent exists in
the forge: `/recipe <genre>`. A genre file
(`.claude/skills/recipe/genres/presentation.md`) carries a numbered
elicitation checklist and points at its skeleton
`templates/recipe-<genre>.md`.

The elicitation should be different for every artefact: we talk one
way over a brief, another over an intent, and a wholly different way
over a BRD. Every artefact has its template.

## What elicitation is

Elicitation is not any conversation of ours. Elicitation, in its
meaning, is not even a conversation. It is a process of finding. It
fits the making of an artefact best: together we find the artefact;
we form knowledge.

The conversation is only the medium; the interview is one
instrument, research and sources are others. "Elicitation interview"
is right as a name: elicitation is what we do, the interview is the
form. What has no place of its own yet is the process — what is
found for which artefact, and that it is found by research and
sources as well as by questions. The interview is the only form of
elicitation the forge names today, and the paragraph in CLAUDE.md
describes only that form.

The elicitation interview defines the aim and the partner who helps
me reach it.

What is not elicitation: composing a recipe (configuration from known
options, not the finding of knowledge), `/setup`, and the walkthrough
of a reviewer's findings after `/critique`, `/challenge` or `/check`
(it has its shape already and nothing per artefact in it).

The map of what is to be found stands before the template; the
template is the shape of the result. Three things, then: the map
(what to find), the process (how the map is walked), the template
(where it lands). A map is not a questionnaire but a map of what
must be found for the artefact to be complete; how it is found is
the situation's.

## The shape of a definition

For every artefact type we set what the elicitation is to achieve.
The first element of a definition is not a piece of knowledge nor a
question but the aim of the elicitation of that artefact and
Claude's role in it. A definition of the elicitation of one artefact
is composed of seven blocks, in reading order:

1. **Target** — the artefact's file and its template (the shape of
   the result). Exists today.
2. **Inputs** — what the finding starts from. Exists today; widened
   for the brief.
3. **Aim** — what the elicitation achieves and when the artefact is
   complete; the one place where completion is stated. A short
   paragraph. New.
4. **Partner** — Claude's stance: what he does, what he does not do,
   who steers the finding and who the decisions. Replaces today's
   "Role".
5. **Map** — what must be found, in the artefact's own vocabulary;
   not questions, not criteria. New; the equivalent of the genre
   files' elicitation checklist.
6. **Instruments** — only the mechanisms of the forge this artefact
   uses in a way of its own (`/research` and `/ingest` as steps of
   the brief), cited, never described; the working methods that
   apply unchanged are not listed. New; scattered through the text
   today.
7. **Course** — how it runs: the ways in, the order, and what is
   offered when the Aim's completion is reached (the brief's lock;
   the next state). It states no completion of its own. Exists today
   as steps 1–5; narrows to what is specific.

Every definition carries all seven blocks, so that the shape can be
checked. A block may be empty on purpose and then says so with the
reason ("Shared methods only" for Instruments); it is never
silently left out.

Outside the definition, as shared mechanism cited and never
repeated: the form of the conversation (the walkthrough skill),
write once per round, versioning with history and ledger, creation
from the template, the language question, "end by naming the
state". A definition cites, never restates: Target one line, Inputs
two, Course only what is specific to the artefact.

Aim and Partner do not repeat each other: Aim says what is true of
the artefact at the end (a state); Partner says only what Claude
does beyond that (conduct), and cites the Aim.

A definition is not long: the state file is loaded only when
`/forge <state>` runs and adds nothing to the always-on context;
what it must not do is restate CLAUDE.md. The rules of particular
artefacts that CLAUDE.md carries today (Document chain 1–3,
Requirement style, prime directive 8) are what moves into the
definitions; until the move, citation.

The genre files map onto this shape without loss: Genre/Skeleton to
Target, Role to Partner, Elicitation checklist to Map.

All three definitions now have their blocks here: the brief's in
full, the intent's and the assignment's with Aim, Partner, Map,
Instruments and Course, their Target and Inputs standing in
today's state files. A review of this brief carries candidates of
its own (source: sources/forge-elicitation-brief-review.md,
sections 6 and 7); they were read as material and not taken as
wording, since they restate shared rules that a definition only
cites.

## Brief

Two ways in stay equally valid: when I have it thought through, the
input is a document. More and more I also want to work from a rough
idea: let us explore it together, find inspiration, do research,
ingest input files, and think over it what to do next. Not a new
way: it is today's "born here" with a different partner. Today Claude
clarifies and only offers research; in this version the partner
takes part in the finding, research and ingest are steps of the
brief's elicitation, expected and no longer an extra on the side,
each proposed by Claude and run on the principal's word, and a
concrete proposal is the tool by which the reaction is drawn out.

In the finding that leads to a brief we form the thought together:
creative, ideas, a lot of research, a lot of inspiration from public
sources. The finding gathers as many ideas as possible; the brief
takes from them what the principal chooses, so that together it
makes sense. Claude's part is above all to inspire, to offer how it
works elsewhere, to say how original the thoughts are. "Are we
reinventing the wheel?" belongs to the brief and, above all, to the
intent.

The brief is only the brief. A synthesis of Claude's — an
architecture, a comparison — does not turn the brief into an intent:
what is a finding (how X works, a verified fact, literature) becomes
a research note in `research/` and is cited; what is a proposal
enters the brief where the principal takes it, and what he does not
take is gone with the conversation; the chiselling is the intent's.
No IDs in a brief: that is well solved in the intent.

This turns a decision of 2026-09-14. The forge intent holds that a
brief born by elicitation carries the whole pile as it emerged
(POS.0110) and that what Claude brings needs no second home, the
brief being its home (REJ.0180); CLAUDE.md (Document kinds,
Document chain 1) and the brief's state file say the same. What
changes is what a brief holds: the principal's choice from the
finding, not its record. What stands is that there is no second
home: a new artefact for the ideas was weighed and not taken,
since findings and sources have `research/` and `sources/` and
what fell by in the conversation is gone. What stands as well is
the reason of that day: Claude never reports as written what
lives only in the conversation (CLAUDE.md, prime directive 9). To
be decided at mining.

### The definition of the brief's elicitation

**Target.** `00-brief.md` (bare) or `00-brief-<name>.md` (with a
name — a later whole of thinking born during the project's life).
Shape of the result: `templates/brief.md` — a YAML header, then free
form: any headings, tables or lists the principal finds useful, no
IDs, no conventions of the chain. What a brief is, its language and
its lifecycle from draft to the lock: CLAUDE.md, Document chain 1.

**Inputs.** The principal's thought, however it arrives. Around it,
gathered during the elicitation: research notes (`research/`),
sources (`sources/`) and Claude's own proposals. The existing intent
and ledger are read only to know what already stands, never to shape
the text.

**Aim.** The brief puts the idea together: what the principal wants
and why, with what he chose to take from the finding around it, in
whatever structure serves the thought. The finding is wide
(research, sources, his ideas and Claude's) and the brief is not
its record: what goes in and what stays out is the principal's
decision, made on what was found. What stays out lives in
`research/` and `sources/` where it is a finding or a source, and
otherwise nowhere. The brief is rough on purpose, neither perfect
nor detailed: the chiselling is the intent's, and a brief polished
until the intent has nothing left to do has gone too far. Nothing
in it is yet a position. The brief is complete when the principal
says so and locks it; the Map is walked before the lock is
offered.

**Partner.** The brief is the principal's text, and Claude's part
changes on the way. At the opening Claude is the active one: he
inspires, brings how the same thing is done elsewhere and how
original the idea is, verifies what can be verified, and proposes
research and ingest (Instruments); a proposal of his, however
large, serves the finding and is not the brief. Then the brief is
written, and it is mainly the principal's text. Claude moves him to
describe what he wants, why and what he does not want, and writes
it down whole by whole as they have talked it over. Claude may
work on the text: translate it, mend its grammar, and put an idea
of his own into it in his own wording where the principal has
accepted it; what he has formulated he reflects back before it is
written. What he does not do is take the text over: he does not
decide what goes in, and he does not chisel it into an intent.

Claude holds the form. A brief says what the idea is and why; it
may carry a mechanism where the mechanism is part of the idea.
Once the talk turns to taking it apart and agreeing it piece by
piece (definitions, blocks, wording), Claude says in one sentence
that this is the intent's work and does not develop it. The
principal decides whether it stays in the
brief as one open line or is let go. No walkthrough runs over the
text of a brief and no IDs enter it.

What Claude thinks of it he says when asked (`??`, CLAUDE.md,
Working methods). What does not fit he says at once and unasked,
in one sentence: a wrong assumption, a contradiction, a risk
(CLAUDE.md, prime directive 1). What goes into the brief and what
stays out is the principal's to say.

**Map.** The Map is of the finding, not of the brief: it names what
the finding looks at, and what of it enters the brief is the
principal's choice. The brief has no required content, and the Map
prescribes neither headings nor the order of the conversation. It
is walked once, at the closing, before the lock is offered: has
each area been consciously considered? An area may leave nothing
in the brief. The walk asks and does not mend: a tension, an
alternative left undecided or a boundary left vague may stay in
the brief as it is, since resolving them is the intent's work.
- the thought in the principal's words: what he wants, why, and
  what prompted it;
- the world around it: what exists that does the same or the
  opposite, and what of it is inspiration, counter-example or proof
  that the wheel exists;
- the material: the sources and research the thought rests on,
  gathered and registered, so that the intent can cite them;
- what is still open: what was not decided or verified during the
  finding.

**Instruments.** `/research <topic>`: durable findings into
`research/`, indexed. `/ingest [file]`: outside material into
`sources/`, registered and indexed. Both are steps of the
elicitation, proposed by Claude and run on the principal's word.
Claude proposes a research step against a named need: an
uncertainty, a comparison, an inspiration. After it he says what it
changed in the thought, what stays uncertain and whether more
research is likely to change anything; whether to go on is the
principal's to say. What the research did not find, or found not to
hold, is a finding like any other and stands in the research note;
it enters the brief where the principal takes it.

**Course.** Resolve the project and the file; create the brief with
its companion and ledger row if it does not exist; stop if it is
approved — a new whole is a new brief. However the text arrives:
pasted whole — store it verbatim and ask whether it is finished, if
so lock at once; begun outside — store what came, then work from
where it stops; born here — the principal opens with a rough idea
and Claude works from the first word as the Partner says, verifies,
confronts, proposes, draws out, and accumulates the principal's
answers as his text, not as a summary of them; a summary or a
structured proposal he asks to record is stored as shown, never
re-narrated. Write once per round on his confirmation; lock only on
his explicit word; end by naming the state and, if locked, proposing
`/forge intent`.

Before the lock the principal may have Claude give the brief a
structure: the text gathered under headings in a logical order,
what repeats pointed out, the grammar mended. Claude adds nothing,
drops nothing and rewords no thought; he shows the structure
before it is written, and the headings are the principal's to
rename. The step is the principal's to ask for, never a condition
of the lock. With translation and grammar it turns the rule of
today's state file never to translate, restructure or tidy the
text; to be decided at mining.

Left open for the intent: whether the brief's Map names the
boundaries (what is not wanted, what is out of scope), whether the
Course offers the lock as soon as the talk turns to the intent's
work, and whether a brief born here carries marks and citations at
all.

### Inspiration: a preparation done outside the forge

Yesterday, instead of working straight in the forge, I began the
preparation of a new project in Claude Desktop, because a brief does
not work that way here yet, meaning to hand the result over as the
base of a brief. I would want to do even that in the brief. The
export lies in `tmp/rohlik-conversation-export.md` (not ingested: it
will be a project of its own). What that conversation did that
today's brief state does not:

1. Research as step zero, not an offer: on the first paragraph
   Claude verified reality (the API's documentation, the actual
   data, the literature) and corrected a wrong assumption at once.
2. Draft early to the extreme: the first answer was a whole
   architecture; the principal's reactions were four sentences,
   each of which redrew the proposal.
3. Few sharp questions at the end of every round — the two Claude
   could not decide, never a questionnaire.
4. Epistemic status on everything: verified on data, unverified,
   hypothesis; sources under every answer.
5. Confrontation with the outside on the principal's word: a second
   opinion's report and the projects it cites, each verified in its
   own repository, sorted into "take / leave" with the reason, and
   the principal walked through it.
6. A closing summary in categories Claude proposed himself.

What of it collides with today's brief state: "Claude does not take
the helm" (there, both held the finding; the principal held the
decisions); "never introduce IDs" (the resulting document had them —
and that is right: the brief is only the brief, the rest is the
intent's); "the words that stay are his" (there, largely Claude's
words with the principal's assent).

## Intent

In the intent we formalise: sort what matters and what does not,
which ideas yes and which no; give it sense and form; everything must
fit together. Claude's role is to help the principal extract that.
Beyond that: we must sort the thoughts — what is good and what bad,
what is feasible and what is not; make the final reality check; and
look at it by versions (this is a proof of concept, this the first
version, this is good but far in the future), perhaps already
helping to compose it into blocks.

**Aim.** The intent chisels the briefs into what the principal holds:
from the briefs, the sources and the conversation it keeps what
matters as positions, what is the case as facts, what is undecided
as threads and what was dropped as rejections with the reason. Every
idea is weighed twice — good or bad, feasible or not — and placed on
a horizon where the principal sees one: a proof of concept, the
first version, a later one, or good but far away. Everything
coherent, nothing twice, every position with its provenance, and the
whole passed through a final reality check before a lower layer is
derived. It is complete for now when no thread blocks the next
layer; it is never finished.

**Partner.** Claude helps the principal reach the Aim: mines the
briefs with him whole by whole, probes contradictions, gaps and
unstated assumptions, reflects a brain-dump back as structure before
it is written, offers options with trade-offs, proposes research
where a thread needs outside grounding, and runs the final reality
check with him. He composes the wording, the principal the
substance; a thread closes only on his word.

**Map.** What the intent finds, whatever the order; where it lands
is the template's. Walked at the round's end, before a lower layer
is proposed or the intent is approved; an area may stay empty when
it was considered and found not to apply.
- the essence: what the principal wants and why, as of today;
- the weight of every idea: what he holds and why, what he dropped
  and why, what he deferred, which is not dropped;
- the ground: what is the case, and on whose word or which source;
- the horizon: where he sees one, what is a proof of concept, the
  first version, later, or good but far away;
- what is open: what is undecided, what it would take to decide it,
  and which of it blocks the layer below;
- the briefs as wholes: whether the substance of each is in the
  intent, was dropped, or was knowingly left behind;
- what the layer below will need: the recipients, the objective and
  the success criteria, as soon as he sees them;
- reality: what of it is feasible, and where the wheel already
  exists.

**Instruments.** `/research <topic>`: proposed where a thread needs
outside grounding, run on the principal's word. A source enters
only as the principal directs (CLAUDE.md, Document chain 5).
`/challenge <persona> intent`: the independent reality check,
offered once the joint one is done, never run on Claude's own
judgement. The walkthrough of every position, where the intent was
consolidated by Claude (CLAUDE.md, Document chain 2).

**Course.** Resolve the project and read the inputs and the intent
as it stands. The ways in: no intent yet, and the locked briefs are
consolidated into the first one, which waits for its walkthrough
(CLAUDE.md, Document chain 2); a brief pending or partial, and it
is mined whole by whole, one brief at a time; an open thread, a
new word of the principal's or what the recipients sent back, and
the round starts there. Briefs are offered before threads. Within
a round one theme at a time; the reality check comes last, before
a lower layer is proposed. On the write, resolved threads move
into positions or rejections and the Mined column of every brief
touched is kept (write once per round, versioning and ledger:
CLAUDE.md). End by naming what changed and what stays open; when
the Aim's completion is reached, propose the next state, or the
approval where the chain ends at the intent: a recommendation,
never a gate.

Where the recipients, the objective and the success criteria live:
today only in the assignment (Objective, Purpose & Context, Success
Criteria with SCR — optional, delegated or absent). The intent has
no place for them but one that is easily forgotten: the section
"Candidate structure for assignment", an optional staging area
before distillation. They are substance, so intent-first says they
are found above: that section is where the intent carries the
recipients, the objective and the success criteria as soon as the
principal sees them — positions with IDs like everything in the
intent, no new section, no new prefix; the intent's Map names it and
its Aim includes it. The assignment then distils them too, instead
of finding them first.

## Assignment

Similar to the intent, but for whom it is intended: a bit like a
project. Claude guards completeness — the assignment covers
everything from the intent — and drift; here he can be quite
autonomous. The way I imagine it: at the start the questions Claude
needs answered, then he recasts the whole, then we go through it
together in some form.

**Aim.** The assignment carries the in-scope substance of the intent
to the recipients, complete and precise, so that they can act on it
without the principal in the room: who they are, what must be true
at the end, what is theirs to decide and bring back, what they shall
not do, and what the principal has left open on purpose. It is
complete when nothing the recipients would need is left to
assumption — delegated or open on purpose is complete, silent is
not.

**Partner.** Claude first reads the intent against what the
assignment needs — recipients, objective, delegation, success
criteria, horizon — and asks up front only what the intent lacks:
who the recipients are, what is delegated and what specified,
whether success criteria are present, delegated or deliberately
absent, what is later. Then he drafts the whole from the intent with
a provenance map (group → items → positions; positions that landed
nowhere, items that came from nowhere), guards completeness and
drift by it, and raises what the intent is silent on as a TBC rather
than filling it. The two then walk the draft through group by group,
the map in view, a question on one item opening it and closing it in
place; a substance change is proposed to the intent first. The
wording is Claude's, in the Requirement style; the substance the
principal's.

**Map.** What the assignment finds, most of it in the intent and
the rest by asking; where it lands is the template's. Walked
twice: before the recast, to see what the intent leaves unanswered,
and at the end of the joint pass; an area may stay empty when it
was considered and found not to apply.
- the recipients: who they are, what they already know and what
  they will do with the assignment;
- the objective: what must be true at the end;
- the cut: what of the intent is theirs now, what is expressly
  later and what is out of scope;
- the line between assigning and solving: what is specified, what
  is theirs to decide and bring back, what is left open on purpose
  and whose it is;
- the boundaries: what they shall not do, what is not to be
  challenged, and what the whole rests on;
- success: criteria present, delegated or deliberately absent;
- the words: what must be defined so that the assignment is read
  without the principal in the room.

**Instruments.** The provenance map (phase 2 below): a tool of the
pass, no part of the assignment. The walkthrough by group (phase 3
below): one item of the walkthrough is one group of the
assignment. `/critique essence`: the independent test of drift,
offered after the joint pass, never run on Claude's own judgement.

**Course.** Resolve the project and read the intent and the
assignment as it stands; say whether the intent is ready to be
derived from (CLAUDE.md, Document chain 2), never as a gate. The
ways in: no assignment yet, and the joint pass runs whole, in its
three phases below; an assignment that stands and an intent that
moved, and the pass runs on what changed, the provenance map
showing what the change touched; a wording fix, made in the
assignment directly. A substance change asked for in the
assignment goes to the intent first (CLAUDE.md, Working methods).
End by naming what changed; when the Aim's completion is reached,
offer `/critique essence`, then the approval: a recommendation,
never a gate.

The joint pass, in three phases and no new kind of interview:

1. Questions up front — one per message, only what is the
   principal's and the intent does not answer. None where the
   intent answers everything; rarely more than six, and where more
   are needed the intent is not ready and the work returns to it.
2. The recast — Claude writes the whole draft from the intent, and
   with it the provenance map: group → items → the positions they
   came from, plus the in-scope positions that landed nowhere (to be
   none) and the items with no position (drift, to be none). The map
   is a tool of the pass, not part of the assignment.
3. The walkthrough by group — one item of the walkthrough is one
   group (`### <Group>`): what it covers, from which positions, what
   in it is DEL or TBC, what is optional or later. A verdict per
   group; a question on a single item opens a sub-item and closes it
   before moving on. Dozens of items pass in a handful of messages
   and nothing is skipped, the provenance visible at each. After the
   pass, `/critique essence` offered as the independent test of
   drift; its findings, an ordinary walkthrough.

Why not item by item: most items are craft derived from the intent
and a verdict on each is ceremony. Why not "read the whole": without
the map one sees what is there, not what is missing.

## Horizon

The horizon lives in all three layers, each carrying its own kind,
nothing twice: the intent the judgement (why this is a proof of
concept, this the first version, this later — and what was deferred,
which is not what was rejected); the assignment the boundary (what
is assigned now and what is expressly later, so that the recipients
neither build it nor design it away; no reasons, those stay in the
intent); the BRD the phasing (what each version delivers, in what
order, with what dependencies — the first layer where the horizon
gets time and order). "Later" in an assignment is not out of scope:
out of scope is never done, later is done, only not now.

The principal's stance for now, to be confirmed when the BRD gets
its definition in the brief `brd`: the horizon is mandatory in the
BRD, even if only as the statement that everything is in the first
version; in the intent it is found and carried in free form (a word
in a position is enough); in the assignment an optional note, only
where the recipients would otherwise build something that is
later. The shape for the intent
and the assignment is not solved now; it returns in the brief `brd`.

## Marks in a brief

I do not care who came up with a thought. If it is in the brief, I
approved it; I see no gain in marking authorship. What stays,
because it carries something other than authorship: `(source:
<path>)` — not who said it but where it is from, becoming a fact
with provenance at mining; and a short `(remark: …)` only where a
reservation, an uncertainty or a suggestion was raised that the
principal did not adopt: a remark on the principal's thought, named
by what it is and not by who made it, so that it reads the same
whatever model the forge runs on. This changes CLAUDE.md, Document
chain 1 (the origin marks of a brief born by elicitation); to be
decided at mining.

What the marks do not carry and the brief must: how sure a claim
is. Whatever Claude brings as knowledge says in plain words whether
it is verified and on what, unverified, or a hypothesis (the
inspiration above, point 4); a claim never gains certainty by being
written into an artefact. Words, not marks: no mark of authorship
and no mark of acceptance returns, since what is in the brief the
principal approved. Whether the rule is the brief's alone or shared
by the whole chain is the intent's to sort.

## One mechanism, user-definable, and where to stop

What this brief is about is the elicitation: the shape of a
definition and the definitions of the brief, the intent and the
assignment. Everything from here on (the extension point for a
user's own definitions, the split of the engine, the installation,
the unifying of `/recipe` with `/forge`) is carried as a consequence
and as material for the briefs `brd` and `engine-split`; nothing of
it is decided here. Self-contained definitions are the prerequisite
of a later split, never the other way round.

I want the elicitation framed. And it should be user-definable: just
as I want a user-defined check, I may want a user-defined
elicitation. But that leads on to user-defined templates and
user-defined artefacts, and I am not sure where to stop.

The boundary already exists and only needs naming: mechanism versus
instance. The engine owns the mechanism — the `/forge` dispatcher,
the shape of a state file, the contract of a template, the shape of
the conversation (walkthrough), the numbering of layers. An instance
is one pair of files: state file plus template. A user-defined check
is an instance of the check contract; a user-defined artefact is an
instance of the same kind. The dispatcher does not change and the
chain is a star, so the engine never needs to know the artefact's
name. The stop is that line: the engine never defines an instance,
the user never changes the mechanism. The test: does CLAUDE.md have
to change for it? If not, it is THR.0300; if yes, it is a derivation
(THR.0420), a framework of its own, not a local addition. The risk
is blurring with THR.0420: the product framework is a set of
artefacts with a logic of its own, a single local pair of files is an
addition; without the line, THR.0300 grows into THR.0420 and the
"one tool that does everything" that is explicitly not wanted comes
in through the door for user artefacts. Order: shape first, then the
extension point — how a user supplies an elicitation cannot be
defined until the elicitation has a fixed shape in the engine's own
states.

Where the definitions live after the split is open: genre and state
files sit in `.claude/skills/…`, in the engine; a user's definition
(THR.0300) should sit where `forge-pull` never overwrites. (remark:
if the mechanism is one, the dispatcher reads both roots, the
engine's and the local one; for `engine-split`.)

The recipe: not elicitation — it is composed, not found; the seven
blocks are for the artefacts of the chain. Whether `/recipe` becomes
`/forge recipe <genre> [name]` is a question of mechanism (one
dispatcher or two), left open as a small matter. (remark: one
mechanism would unify the language question and "composed from the
skeleton"; against it stands that `/forge` is the door of the
chain.)

## The split, and the order of the work

Today `/forge` states and `/recipe` genres are the same mechanism
written twice in different shapes. My proposal: let us tune the
elicitations so that they share one mechanism and one shape, and we
will have to cut into the engine split.

I do not know how to split it. One idea is to have a real engine: a
separate git, a light shell that handles things like ingest, the
ledger and so on. Or we make Forge of Thought the big engine, into
which I install, from separate gits — official and unofficial —
something like plugins: brief, BRD, test analyst and so on.

The two ideas are one thing seen from two ends: a thin shell means
nothing without a place for "the rest", and plugins mean nothing
without a shell to install into. The question they open is what the
unit of installation is. The research of 2026-08-29
(source: research/2026-08-29-claude-code-packaging.md) names exactly
one thing a Claude Code plugin cannot carry: CLAUDE.md as always-on
context; skills, agents, templates and scripts it carries with a
version and an update channel. That divides by itself: the engine is
the repository with CLAUDE.md and the mechanisms — git scripts,
ledger, versioning and history, ID scheme, the reviewers' contracts,
ingest, research and indexes, save, release and check, setup, the
walkthrough shape, the `/forge` dispatcher; a framework is a package
of instances — definition pairs, lenses, personas, checks, genres.
The cost is the one CHL.0110 named: today's CLAUDE.md carries the
rules of particular artefacts, which must move into the definitions
of brief, intent and assignment, or there is nothing to package; the
elicitation per artefact is that move. The installation mechanism —
a Claude Code plugin marketplace or a `forge-install` from git into a
local root — is a research question, not a decision for now; the
objections of THR.0190 largely fall once CLAUDE.md stays in the
engine.

Order: the elicitation first. It can be solved in today's engine
without deciding the split — a checklist in every definition,
definition and template as a pair, the rules of particular artefacts
out of CLAUDE.md into their definitions — and once the definitions
are self-contained, the split becomes a decision about roots and
installation, a move of files instead of the "large rebuild"
THR.0230 fears. Then `brd` as the first instance of the new shape,
then `engine-split`.

Estimated effect on CLAUDE.md (663 lines on 2026-09-28) if the rules
move and are not copied: Document chain 1 from 26 lines to 4,
Document chain 2 from 8 to 2, Document chain 3 from 3 to 1,
Requirement style from 17 to 2, the Elicitation interview paragraph
from 10 to 3, prime directive 8 from 12 to 2 (disputable: it is also
a rule for reading), the `/recipe` row gone, one new paragraph of
about 10 lines on the shape of a definition — about 43 to 53 lines
fewer. The state files grow by about as much; the context loaded by
one `/forge <state>` stays roughly the same, only the always-on part
shrinks. ID scheme, Document kinds and Versioning are mechanism and
untouched.

The line count is an effect, not the proof. The proof is conduct:
the three definitions are written whole first, swept for
restatement (`/check single-source-of-truth`), and tried on real
work, one run from a brief through the intent to an assignment,
before any rule leaves CLAUDE.md; a rule leaves only once its
definition has been seen to hold. The situations to try are listed
in a review of this brief
(source: sources/forge-elicitation-brief-review.md, section 2.17):
a finished brief locked without an interview, a raw idea, a brief
that needs no research, a brief locked with a tension left
unresolved, an assignment drafted with no question asked, a drift
the provenance map catches. Locked artefacts are untouched by the
change: they are immutable already.
