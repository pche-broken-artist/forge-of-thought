---
description: Compose or finish a brief — the principal's idea put together, found with Claude and locked when done
---

The definition of the brief's elicitation, in the seven blocks of
POS.1310 of the forge intent; what it is to achieve and why is
POS.1330. Shared mechanism is cited and never repeated here: the form
of the conversation and one write per round (CLAUDE.md, Working
methods and prime directive 9), versioning with history and ledger
(CLAUDE.md, Versioning & status), the language (CLAUDE.md, prime
directive 6).

**Target.** `00-brief.md` (bare) or `00-brief-<name>.md` (with a
name — a later whole of thinking born during the project's life).
Shape of the result: `templates/brief.md` — a YAML header, then
free form: any headings, tables or lists the principal finds
useful, no IDs, no conventions of the chain. Its lifecycle from
draft to the lock and its language: CLAUDE.md, Document chain 1 and
prime directive 6.

**Inputs.** The principal's thought, however it arrives. Around
it, gathered during the elicitation: research notes (`research/`),
sources (`sources/`) and Claude's own proposals. The existing
intent and ledger are read only to know what already stands, never
to shape the text.

**Aim.** The brief puts the idea together: what the principal
wants and why, with what he chose to take from the finding around
it, in whatever structure serves the thought. The finding is wide
(research, sources, his ideas and Claude's) and the brief is not
its record: what goes in and what stays out is the principal's
decision, made on what was found. What stays out lives in
`research/` and `sources/` where it is a finding or a source, and
otherwise nowhere. The brief is rough on purpose, neither perfect
nor detailed: the chiselling is the intent's, and a brief polished
until the intent has nothing left to do has gone too far. Its usual
shape is light: the topics of the whole, each with a few sentences
of what the principal wants of it, the research that verifies or
limits it cited beside it, and what is still open. It is composed in
a round or two and then mined. It is where thoughts are thrown in
before they are sifted: not all of them survive, and the sifting is
the intent's. Nothing
in it is yet a position: its thoughts are to be processed, not
decisions, and may be changed, reworked or dropped when mined. The
brief is complete when the principal
says so and locks it; the Map is walked before the lock is
offered.

**Partner.** The brief is the principal's: what is in it he
approved, whoever first said it. Claude's part changes on the way.
At the opening Claude is the active one: he
inspires, brings how the same thing is done elsewhere and how
original the idea is, verifies what can be verified, and proposes
research and ingest (Instruments); a proposal of his, however
large, serves the finding and is not the brief. Then the brief is
written. Claude moves the principal to say what he wants, why and
what he does not want, and he forms the record: on the principal's
word to write, he takes what the talk arrived at and writes it
down so that it is understood. He may translate, mend the grammar
and word an idea of his own that the principal has accepted; what
he has formulated he reflects back before it is written. What he
does not do is take the brief over: he does not decide what goes
in, and he does not chisel it into an intent.

Claude holds the form. A brief says what the idea is and why; it
may carry a mechanism where the mechanism is part of the idea.
Once the talk turns to taking it apart and agreeing it piece by
piece (definitions, blocks, wording), Claude says in one sentence
that this is the intent's work, does not develop it, and offers
once to lock the brief and go on in the intent: a recommendation,
never a gate. The
principal decides whether it stays in the brief as one open line
or is let go. No walkthrough runs over the text of a brief and no
IDs enter it.

What Claude thinks of it he says when asked (`??`, CLAUDE.md,
Working methods). What does not fit he says at once and unasked,
in one sentence: a wrong assumption, a contradiction, a risk
(CLAUDE.md, prime directive 1). What goes into the brief and what
stays out is the principal's to say.

Nothing in a brief marks authorship. `(source: <path>)` stands
where the identity of a source supports, limits or contradicts the
thought, and becomes a fact with provenance at mining; what merely
inspired the thought carries no mark and stays discoverable through
the research note. A short `(remark: …)` stands where a reservation
or an uncertainty must stay visible, named by what it is and not by
who made it; a suggestion or an alternative the principal did not
take is gone, unless he says it stays.

**Map.** The Map is of the finding, not of the brief: it names
what the finding looks at, and what of it enters the brief is the
principal's choice. The brief has no required content, and the Map
prescribes neither headings nor the order of the conversation. It
is walked once, at the closing, before the lock is offered: has
each area been consciously considered? An area may leave nothing
in the brief. The walk asks and does not mend: a tension, an
alternative left undecided or a boundary left vague may stay in
the brief as it is, since resolving them is the intent's work.
- the thought: what the principal wants, why, and what prompted
  it;
- the boundaries: what the principal does not want, and what is
  out of scope;
- the world around it: what exists that does the same or the
  opposite, and what of it is inspiration, counter-example or
  proof that the wheel exists;
- the material: the sources and research the thought rests on,
  gathered and registered, so that the intent can cite them;
- what is still open: what was not decided or verified during the
  finding.

**Instruments.** `/research <topic>`: durable findings into
`research/`, indexed. `/ingest [file]`: outside material into
`sources/`, registered and indexed. Both are steps of the
elicitation, proposed by Claude and run on the principal's word.
Claude proposes a research step against a named need: an
uncertainty, a comparison, an inspiration. After it he says what
it changed in the thought, what stays uncertain and whether more
research is likely to change anything; whether to go on is the
principal's to say. What the research did not find, or found not
to hold, is a finding like any other and stands in the research
note; it enters the brief where the principal takes it.

**Course.** Resolve the project and the file; create the brief
with its companion and ledger row if it does not exist; stop if it
is approved — a new whole is a new brief. However the text
arrives: pasted whole — store it verbatim and ask whether it is
finished, if so lock at once; begun outside — store what came,
then work from where it stops; born here — the principal opens
with a rough idea and Claude works from the first word as the
Partner says, verifies, confronts, proposes, draws out, and writes
down what the two of them arrived at, condensed where the talk was
long and in whatever wording says it best, reflected back before
it is written; a summary or a structured proposal he asks to
record is stored as shown, never re-narrated. Write once per round on his
confirmation; lock only on his explicit word; end by naming the
state and, if locked, proposing `/forge intent`.

Before the lock the principal may have Claude give the brief a
structure: the text gathered under headings in a logical order,
what repeats pointed out, the grammar mended. Claude adds nothing,
drops nothing and rewords no thought; he shows the structure
before it is written, and the headings are the principal's to
rename. The step is the principal's to ask for, never a condition
of the lock.

How the files are made: a new brief is created from
`templates/brief.md` (the minimal YAML header, nothing else) with
its companion `<file>.history.md` from `templates/history.md` and
its row in the ledger's Briefs table (Mined: pending). The lock is
CLAUDE.md's (Document chain 1); the ledger row is updated with it,
and the whole is then mined by `/forge intent`.
