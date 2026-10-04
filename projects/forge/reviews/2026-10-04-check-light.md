---
date: 2026-10-04
project: forge
check: light
target: projects/forge
reviewer: check light (isolated context)
---

# Check (light) — projects/forge — 2026-10-04

4 findings

## Findings

### FND.0900 — medium — Two brief companions still carry a Version History table; neither was moved to an archive
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\00-brief-public-engine.history.md:6-18` (heading "Version History", the older header comment, a table of one row); `C:\pche\_dev\forge-of-thought\projects\forge\00-brief-elicitation.history.md:16-24` (a table, same shape). No `00-brief-public-engine.history.archive.md` or `00-brief-elicitation.history.archive.md` exists on disk. The intent and all five recipes have made the move; these two have not.
- **Rule:** CLAUDE.md, Versioning & status: a companion written before the log moves as it stands to `<file>.history.archive.md`, and a Version History table in a companion is a `/check` finding settled by that move, on the principal's word; the shape of the log is `templates/history.md`'s. No DEC in `decisions.md` rejects this (DEC.0150 and DEC.0160 concern other findings of the history check).
- **Fix:** On the principal's word, move each of the two files untouched to `<file>.history.archive.md`; the new `<file>.history.md` in the shape of `templates/history.md` begins with the brief's next version.

### FND.0910 — low — The Documents table carries two rows the template does not have
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:35` (`20-assignment.md | — | not planned: ...`) and `:36` (`decisions.md | — | 18 records ...`)
- **Rule:** `templates/ledger.md:30-36`, Documents: the intent, then one row per layer below the intent, added when the layer is born; "a layer the project does not have gets no row" (CLAUDE.md, Ledger: a layer a project does not have is not missing). `20-assignment.md` does not exist on disk; `decisions.md` is a record, not a layer. The template's comment under the table (lines 34-36) is also absent from the ledger.
- **Fix:** immediate fix: delete the `20-assignment.md` row and add the template's comment under the table; whether the `decisions.md` row goes with it is one question for the walkthrough (its count and date are correct today: 18 records, DEC.0010 to DEC.0180, newest 2026-10-02).

### FND.0920 — low — Four table comments in the ledger are behind the template
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:20-23` (Briefs: "approved (locked at 1.0, immutable)"; the template has "approved (1.0 and on, changed after that as any artefact is)"); `:39-40` (Renders: "CLAUDE.md, Document chain 7"); `:50-52` (Published: "Document chain 7"); `:59-63` (Sources: "Document chain 5")
- **Rule:** the ledger is shaped as `templates/ledger.md` says for its kind (`templates/ledger.md:21-25`, `:39-40`, `:45-47`, `:52-56`): the template cites "Document chain, Renders" and "Document chain, External inputs"; the numbers 7 and 5 name no item of CLAUDE.md, Document chain, which is numbered 1 to 4.
- **Fix:** immediate fix: replace the four comments with the template's current wording.

### FND.0930 — low — Three matters under Waiting on principal still have no ID, five writes after they were raised
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:321-327` (how `shall` stands in an assignment in another language, raised 2026-10-02; `essence` not run on this project, 2026-10-02; three weakly founded places in the README of 2026-10-02)
- **Rule:** CLAUDE.md, Ledger: free text only for a matter with no ID yet, which gets one at the next write. The intent has been written at 4.50, 4.51, 4.52, 4.53 and 4.54 since (`C:\pche\_dev\forge-of-thought\projects\forge\10-intent.history.md:146-181`).
- **Fix:** At the next write, give each of the three an ID (a thread in `C:\pche\_dev\forge-of-thought\projects\forge\threads.md`) and cut its ledger line to the ID, a few words and its state, or drop the line if the principal says the matter is no longer open.
