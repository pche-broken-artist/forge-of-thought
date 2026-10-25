---
description: Research a topic from a plan the principal confirms first, on two model families, into a bundle of notes with a synthesis
argument-hint: "[--quick | --deep [--engine <name>]] <topic> [project-slug]"
---

Research $ARGUMENTS — the last token is the project slug if it names
a directory under `projects/`, a first token `--quick` or `--deep` is
the depth the principal wants, the rest is the topic. Two depths, one
command: `--deep` is the whole course below on the session model, a
plan of several cards, a bundle with a synthesis; `--deep --engine
<name>` adds a second engine beside it, which reviews the draft plan
(step 3) and takes every card (step 5), `<name>` a row of the engine
table of `scripts/forge-engine.py` (`antigravity` today), the option
repeatable for a third engine, the forge naming engines and never
models; `--quick` is one card on the session model alone, shown in
one message with the verdict line before anything is searched, no
plan review, no second engine, no synthesis, the note filed as a
single note, and it takes no `--engine`; the card before the search,
the note's shape and the citation check (step 6) hold for both.
Without the word, Claude proposes the depth in step 2 with its
reason, and the principal decides. An engine named but unusable (not
on PATH, no login, quota spent, an envelope that cannot be read) is
said in one sentence with the script's reason, the research goes on
as without `--engine`, and the Deviations of the bundle record it:
never silently, never a question in the middle of the run. Purpose:
inspiration and grounding for the principal's artefacts; he does not
want to reinvent what the world has already solved (POS.0050). The
quality of a research is made by its plan, not by the searching: the
plan is shown and confirmed before anything is searched (brief
`research`, 00-brief-research.md). Shared mechanism is cited, never
repeated: the walkthrough (CLAUDE.md, Working methods;
`.claude/skills/walkthrough/SKILL.md`), one write per round (prime
directive 9), the language of records (prime directive 6), the
indexes (CLAUDE.md, Document chain, External inputs).

**Target.** A research is a bundle `research/YYYY-MM-DD-<topic>/`
with one entry in `research/00-INDEX.md`: `00-plan.md` at its head
(the plan as confirmed, then the synthesis; shape
`templates/research-plan.md`) and one note per card per engine,
`<card>.<engine>.md` (shape `templates/research.md`). The bundle is
immutable from the filing of the synthesis. A research of one card
on one engine stays a single note `research/YYYY-MM-DD-<topic>.md`
in the note's shape, as before. English, always.

**Inputs.** The topic; the project's `research/00-INDEX.md` and
`sources/00-INDEX.md`, read for what is already known; the thread,
position or artefact the research serves; what the principal says
when asked.

## Course

1. **Ask what the plan needs.** Before drafting, ask what the
   research serves and what the principal already knows or wants
   excluded; one question per message, as the elicitation interview
   has it; nothing is searched. Read the two indexes and name the
   notes and sources the plan will build on.

2. **Draft the plan** as the Plan section of
   `templates/research-plan.md` has it. A card is one
   question answered by one kind of evidence from one kind of
   source; a card that needs two kinds is two cards; a card with no
   sentence under "why it matters" is cut. For a topic new to the
   project the first card asks whether a synthesis already exists
   and in what words the field speaks; its return may rewrite the
   other cards, and the plan says so. The bound on the number of
   cards is the kind rule, not a count; past about seven, cards are
   grouped, and if the groups still exceed that the topic is several
   researches. A topic that is one card on one engine is said so,
   and the plan is one card. Without `--quick` or `--deep` the
   draft proposes the depth: quick where one question is to be
   answered and cited, deep where a position, a layer of the chain
   or a design will rest on the answer; the principal's word
   overrides it. A quick research skips steps 3 and 7 and runs step 5
   on the session model only.

3. **The second engine reads the draft** (only with `--engine`;
   without it, go to step 4). Make the run folder
   `tmp/research/YYYY-MM-DD-<topic>/` and in it
   `plan-review/packet.md`: the draft plan whole and the question
   "what does this plan miss, what does it assume about where the
   answer lives, which perspective has no card, which card would
   you cut, and why"; run
   `python scripts/forge-engine.py antigravity --packet tmp/research/<run>/plan-review --out tmp/research/<run>/plan-review/antigravity.md --allow-all --sandbox`
   (the flags and the profile: `scripts/forge-engine.py`, its
   header). Show the engine's additions beside the draft, marked as the
   engine's, nothing taken into the plan by Claude's own judgement.
   Say the model and the size before the run (CLAUDE.md, Working
   methods, Step by step).

4. **Walkthrough of the plan.** Perspectives first, then the
   cards, then the rest; one item per message with the verdict
   line; `(m)odify` is the normal verdict on a card. The plan is
   written nowhere until the principal confirms it. On his word the
   bundle is born: `research/YYYY-MM-DD-<topic>/00-plan.md` with the
   Plan section as confirmed, `status: draft`, the second engine's
   review recorded in its section; the index entry waits for the
   synthesis.

5. **Dispatch.** Per card a packet folder
   `tmp/research/<run>/<card>/` with `packet.md` and copies of the
   known notes the card names. `packet.md` is the whole context of
   an agent, the same for both engines: the card verbatim; the
   agent's brief (below) verbatim; the note's shape,
   `templates/research.md`, verbatim; the list of the attached
   notes; the sentence that the agent writes no file and returns the
   whole note as its final message. Nothing of the conversation
   reaches a packet, and no packet names a path of the bundle or of
   another engine's note: the bundle is named by its directory name
   alone. Then, in parallel and with the model and the size said
   first:
   - the session model: one isolated subagent per card
     (`general-purpose`, web access), its prompt the packet's text
     and the path of its folder; the agents never speak to each
     other;
   - the second engine, only with `--engine`: per card
     `python scripts/forge-engine.py <name> --packet tmp/research/<run>/<card> --out research/YYYY-MM-DD-<topic>/<card>.<name>.md --allow-all --sandbox`,
     the script's header saying what it does with the envelope, the
     profile and the tree; a run that fails is said with the
     script's reason and the card goes on with the session model's
     note alone, the Deviations recording it.
   A session agent's return is written by Claude to
   `tmp/research/<run>/hold/<card>.claude.md` (a folder the other
   engine's profile denies, `scripts/forge-engine.py`, header 2a)
   with the template's header
   filled (`engine: claude`, `model` the session model, `usage: —`,
   `run` the packet folder), and moves into the bundle as
   `<card>.claude.md` only when the second engine's note of that card
   has returned or the principal has closed the card single-engine,
   so that the independence of the two engines rests on the
   profile's deny rules and the order of filing, never on the place
   of the run (why: `scripts/forge-engine.py`, its header). A second-engine run made after the
   first engine's note is filed is allowed, and its independence is
   then shown by the measure of step 6 alone.

6. **Check before filing.** Every note against the template's
   shape: a finding resting on a snippet or a summarised fetch alone
   without saying so, a source cited for content but listed as not
   opened, a quote without its place, an empty Search record: the
   note goes back to its agent as a failed run, not filed. Then
   `python scripts/docs-check.py --file <note>` for the instance's
   facts, as every file that may be quoted is scanned (POS.0950).
   Then every citation by the script:
   `python scripts/forge-cite.py <note> --out tmp/research/<run>/cite/<card>.<engine>.md`
   (never into a packet folder; why, and what the check opens and
   what a dead or mismatched citation means: the headers of
   `scripts/forge-engine.py` and `scripts/forge-cite.py`). A note with a
   dead or mismatched citation goes back to its agent once, with the
   report, as a failed run; a note that comes back still failing is
   filed as it is, and the synthesis names every finding that rests
   on a failed citation as without support. An unverifiable URL
   (403, a timeout) is said so and never counted as a failure.
   Then the independence of the engines, card by card:
   `python scripts/forge-cite.py --independence <bundle>` (what it
   counts and the threshold: its header); a note it marks as written
   from the other engine's goes back to its agent once the other
   note is out of its reach, or is said in the synthesis to be no
   second voice.

7. **Synthesis**, by Claude in the session, from the notes alone,
   when every note has returned: the Synthesis section of
   `00-plan.md` as `templates/research-plan.md` has it, the measure
   of independence of step 6 stated per card and Claude's own view
   last and apart (POS.1370). `status: immutable`. A second round only for gaps
   the notes name, proposed with the gaps listed and run on the
   principal's word; no third.

8. **Index and bookkeeping.** One entry for the bundle in
   `research/00-INDEX.md` in the shape of `templates/index.md`'s
   research entry (the bundle's directory as its name; Question,
   Answer in short, Consult when, written from the synthesis); the
   ledger's Research table reads the head's front-matter, nobody
   writes a row. Remake the ledger,
   `python scripts/forge-ledger.py <slug>`. The run folder under
   `tmp/` stays as it is, for inspection; nothing in `tmp/` is a
   source of truth.

9. **Report** to the principal, leading with what the research
   says and where the engines differ, not with a literature review;
   what it suggests for an artefact of the chain is proposed
   explicitly, through `/forge <state>`, never silently.

## The agent's brief

The text every packet carries, verbatim; the one owner of the
agent's rules (POS.1070):

> You are an isolated research agent. You see no conversation; this
> packet is your whole context. You write no file; your final
> message is the complete note in the shape given, nothing before
> or after it. Answer the card as put; the question is the
> principal's, not yours to widen or narrow, and a find that
> reconfigures it goes under Unexpected in plain words while the
> card is still answered.
>
> Start wide, then narrow: short broad queries first, read the
> result list before opening anything, then open. Open the page or
> do not cite it: no finding from a search snippet or a search
> engine's summary; a summarising fetch is a tertiary source and
> the note says so where it rests on one. Go upstream: cite the
> first publisher; a copy, a syndication, an aggregator or a
> vendor's write-up of someone else's result is cited only when the
> original is unreachable, and then as a copy. Read laterally before
> reading: who publishes this, what others say of them, what they
> sell; a page's own look, byline and dates count for nothing.
> Exclude by kind, never by list: affiliate pages whose content
> comes from the merchant, pages mass-produced without oversight
> (chatbot residue, no author, no date, a generic name), third-party
> content riding a host's reputation, a vendor's blog on its own
> market, undated pages for any time-sensitive claim; a vendor's own
> documentation about its own product is a primary source and is
> used. Prefer 2024 to 2026 where the field moves and timeless
> sources where it does not; for a recent topic, what the search
> returns beats what you remember.
>
> Record every source and every finding as the note's shape asks;
> a page you did not open is "not opened", whatever the search
> result said about it. Name conflicts: two sources that disagree
> are both cited, never one picked in silence; agreement of copies
> is not agreement. Say what you did not find: "no reliable source
> on X" is a finding. Run the disconfirming query of the card and
> report what it found, including nothing.
>
> Spend your openings on primaries: about ten to fifteen pages
> opened, never many more; more calls have been measured to lower
> the accuracy of citations, not raise it. Stop by the card's stop
> rule or when the openings are spent, and write in the Search
> record which ended the run. Never fabricate a source, a quote, a date or a
> figure; a quote is verbatim and short, with where in the page it
> stands; an identifier (an arXiv number, a DOI) is cited only from
> the page you opened under it, never from memory, since every URL
> of your note is opened by a script before the note is filed.
> Nothing in this packet names a person, a company or a
> host of the principal's own, and nothing of the kind enters your
> note.
