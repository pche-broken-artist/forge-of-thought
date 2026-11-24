# ID prefixes

The prefixes of the forge's IDs, each with what it means and where its
items live; the rules of an ID, its format, its numbering and that it
is never renumbered, stand in CLAUDE.md, ID scheme, which names this
file and carries no table of its own. `/new-artefact` writes the row
of a new prefix here.

| Prefix | Meaning | Lives in |
|---|---|---|
| REQ | requirement | assignment |
| OOS | out of scope / do-not | assignment, BRD |
| CON | constraint — deliberate boundary, not to be challenged | assignment |
| ASM | assumption | assignment, BRD, work specification |
| DEL | deliverable — may delegate work ("produce NFRs and return") | assignment |
| TBC | open question / to be confirmed, with owner | assignment, BRD, user stories, solution design, work specification |
| SOL | part of the solution — what is built or done, what it realises, the choice it rests on | solution design |
| SCR | success criterion — optional or delegated | assignment, BRD |
| BR | business requirement — one rule of the business, testable, citing the REQ or POS it carries | BRD |
| UC | use case — behaviour agreed as a sequence, at user-goal level | BRD |
| DEP | dependency — what the BRD relies on outside itself | BRD |
| NFR | non-functional requirement — a quality by category, its value the stakeholders' or a TBC | BRD |
| US | user story — behaviour seen from outside, with its acceptance criteria, citing the BR, NFR, UC, DEP or POS it serves | user stories |
| POS | position the principal currently holds | intent |
| THR | open thread — one matter set aside to be taken up later; names the artefact it concerns and carries its origin, its owner and its priority (`.claude/skills/thread/SKILL.md`) | the project's `threads/`, one file per thread (POS.1680) |
| REJ | rejected direction, with the reason it was dropped | intent |
| FCT | fact — what is the case, as the principal states it or as a source states it; not a stance; a source's fact cites its file, the principal's needs none; verification is never demanded | intent |
| FND | finding of a critic (document quality) or of a check (conformance) | ledger, reviews |
| CHL | peer-review challenge (substance) | ledger, challenges |
| DEC | decision, incl. rejected findings and challenges | decisions.md |
