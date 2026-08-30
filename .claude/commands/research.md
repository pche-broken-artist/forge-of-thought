---
description: Research current best practices on a topic; store durable notes
argument-hint: <topic> [project-slug]
---

Research "$1" with current web sources. Purpose: inspiration and
grounding for the principal's intent or assignment — he does not want to
reinvent what the world has already solved. One research, one
question: a topic that turns out to be several questions becomes
several notes, each answering one — never one combined document.

1. Search for current best practices, established frameworks, and notable
   recent developments. Prefer primary and high-quality sources; note
   publication dates. Mark epistemic status: consensus vs. emerging vs.
   contested.
2. Write `research/YYYY-MM-DD-<topic-slug>.md` in the project (English,
   immutable): question, key findings with sources, options with
   trade-offs, and a short "relevance to this project" section with a
   concrete recommendation.
3. Index and register. Add an entry to `research/00-INDEX.md`
   (skeleton `templates/index.md`; create the index if missing):
   **Question**, **Answer in short** (two or three lines), **Consult
   when**. Add a registration row to the Research table in `ledger.md`
   (file, date, derived from). The index tracks nothing and is no
   automatic input of any command.
4. Summarise for the principal in Czech, leading with the recommendation
   and the trade-offs, not a literature review.
5. If findings suggest changes to intent or assignment, propose them
   explicitly — via `/forge intent` or `/forge assignment`, never silently.
