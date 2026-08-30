---
description: Compose or iterate a project's readme recipe — the render is the project's README.md, regenerated on every save
argument-hint: [project-slug]
---

Genre: readme. Skeleton: `templates/recipe-readme.md`. Output:
`README.md` in the project root (POS.1000 of the forge intent).

Every project carries this recipe: `/new-project` scaffolds it from
the skeleton, and every `/save` that touches the project regenerates
the render before the check. Iterating it is how the README is
changed — the render is never edited by hand.

Role: interviewer. Elicit the answers below from the principal —
options and trade-offs offered, decisions his — then compose or
iterate the recipe from the skeleton. Answers are carried in the
conversation and written once per round, on confirmation. When the
principal asks for a first version without an interview, draft it
from the inputs (the ledger, the brief, the intent's essence) and
present it as a draft to iterate.

Elicitation checklist:
1. **Primary reader.** The recipients of the assignment, colleagues
   browsing the repository, or the principal returning — the README
   is written for the first of them.
2. **Inputs.** A thought project: ledger, brief, intent, and the
   assignment once it exists. A library: ledger and the two
   `00-INDEX.md` catalogues — its README is a catalogue of what the
   library holds, with Role / Use for per document, and how to use
   it (e.g. the path a deck template is named by).
3. **What the essence must say** and how much of it — the problem,
   the direction, the recipients; one screen, not the intent.
4. **State.** Which ledger facts appear: chain versions and statuses,
   briefs and mining state, renders, what is waiting on the
   principal.
5. **What must not appear.** Confidentiality toward whoever can reach
   the repository; internal figures; nothing from other projects.
6. **Language.** Artefacts default to English; the principal may
   decide otherwise for this project's readers — ask, never assume.

Compose the recipe from the skeleton, delete unused placeholders and
all template comments, and offer `/render readme` as the next step.
