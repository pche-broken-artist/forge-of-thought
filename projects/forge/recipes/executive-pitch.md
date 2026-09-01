---
project: forge
purpose: Slide-by-slide source material for a five-slide executive pitch of Forge of Thought
audience: C-level executives whose experience of AI is chatting with it
version: 0.1
updated: 2026-08-30
---

# Recipe — Executive pitch

## Inputs
- 10-intent.md
- ../../CLAUDE.md

## Instructions
- The render is **source material for building a presentation**, not
  the presentation itself: one section per slide, carrying the exact
  on-slide text and the speaker notes. Slide count exactly 5; follow
  the Template's slide list — no agenda slide, no section dividers,
  no appendix.
- Audience: C-level executives who know AI as a chat window — they
  have asked it questions and received good answers, and that is the
  whole of their mental model. Register: short and hard-hitting;
  plain language; one idea per slide; no process description, no
  tooling, no method names. Language: English.
- The one message: **a chat gives you an answer; the forge gives you a
  decision you can stand behind.** Centre of gravity: slide 3 — an AI
  that argues back, in isolation, and whose every objection ends in a
  recorded verdict. That is the one experience this audience has not
  had; the deck dwells there.
- Content comes from the Inputs only — no invention, no softening.
  The single worked example on S03 is drawn from the intent's
  evidence about a real project but is **anonymised**: "one enterprise
  platform project", never a project name, never a company name.
- Speaker notes: what the presenter says, three to six sentences per
  slide, conversational; no IDs, no citations — the audience and the
  presenter need neither.
- On-slide density: at most 4 lines per slide, at most 12 words per
  line; a title of at most 8 words. Everything beyond that belongs to
  the notes. Each slide may carry one closing line in bold.
- Vocabulary discipline: "chat" always means the question-and-answer
  use of AI the audience knows; "the forge" is the system; "the idea"
  is what enters and "the output" is what leaves — never "brief",
  "intent", "assignment", "ledger", "recipe", "render", "critic",
  "challenger", never any ID or prefix. The two reviewers are "two
  opponents that never saw you". The regenerated outputs are
  "outputs" or named by their audience ("a pitch for the group", "a
  deck for the delivery team"), never "renders".
- Must not appear: any project name, company name, person, vendor or
  model name; internal figures other than the anonymised challenge
  counts on S03; nothing from the intent's open threads or rejected
  directions; no repository paths, commands or file names.
- Diagrams sit on the slides the Template assigns them to, as inline
  Mermaid blocks — valid standalone, simple enough to survive
  conversion into native slide shapes, at most seven nodes.
- Copy the Build instructions section verbatim into the render,
  immediately after the front-matter.
- Per-slide format:
  ```
  ## SNN — <slide title>
  **On slide:** <title line and lines exactly as they should appear>
  **Diagram:** <mermaid block — only where the Template assigns one>
  **Speaker notes:** <what the presenter says>
  ```

## Build instructions
- Template: none for now — design freely, dark background, one
  accent colour, generous whitespace; a `.potx` will be named by path
  once the principal has ingested it.
- Model: opus.
- Never let text overflow: if a slide's lines do not fit at the
  template's body size, shorten nothing — move the last line to the
  notes and say so in the build log. Redraw Mermaid diagrams as
  native shapes with the same node labels; no rendered images of
  Mermaid. The bold closing line of each slide is set apart visually
  (larger, accent colour, bottom of the slide). No slide numbers, no
  footer, no logo.

## Template
Front-matter provenance per the render convention, then the Build
instructions, then one section per slide:

| # | Slide | Content | Diagram |
|---|---|---|---|
| S01 | The chat answers. Nobody checks the question. | Today: idea → chat → good answer → e-mail → assignment. The answer takes a minute; what was in the head was never examined. The error is not in the answer, it is in the question — and nobody reads the question. Closing line: **The mistake is upstream of the answer.** | Flow: idea → chat → assignment, with a question mark over the first arrow |
| S02 | A forge, not a whisperer. | The idea enters as written and never changes. From it a working shape is hammered until it holds: what I want, why, what is open, what I dropped and why. Only then is an output cast — and the output can be anything: an assignment for a team, a strategy paper, a board proposal, an argument for the supervisory board, input to someone else's document. Form comes last; substance is forged once. The AI does not compose — it asks, argues back, keeps order. The human decides. Closing line: **Substance forged once, form cast at the end.** | Three stations: idea (locked) → working shape (rewritten) → outputs (many) |
| S03 | Two opponents that never saw you. | One reads only the document and hunts for what is unclear or self-contradictory. The other reads only the document and attacks the substance: is this even the right problem? what happens in a year? Both work in isolation — they do not know the conversation and cannot nod along. Every objection ends in a recorded verdict: accepted, rejected with a reason, left open. Example: one enterprise platform project — thirty-four objections, thirty-one accepted, three rejected with a written reason, before a single team member saw it. Closing line: **An AI that argues back, and a verdict that is written down.** | — |
| S04 | One idea, every audience in its own language. | From the same forged substance the outputs are generated for each audience: a five-minute pitch for group leadership, a technical deck for a supplier, a one-page mail for a colleague, an executive summary, an architecture picture for someone outside IT. Each output has its own recipe — for whom, what, how long — and that is what gets tuned, never the text. The idea changes → everything regenerates at once, every output at the current version. No "which version of the deck is the right one", no rewriting five documents after one change. Closing line: **Change the idea once; every output follows.** | Hub: the forged substance in the centre, six outputs around it, each labelled with its audience |
| S05 | What it means for you. | Three lines, not a feature list: an assignment that survives the team's first question; every decision carries a date and a reason — a year later too; an idea from anyone, the same discipline for everyone, from the CEO to the analyst. Closing line: **A chat gives you an answer. The forge gives you a decision you can stand behind.** | — |
