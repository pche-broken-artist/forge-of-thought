---
date: 2026-10-02
project: forge
check: project
target: projects/forge (C:\pche\_dev\forge-of-thought\projects\forge)
reviewer: check project (isolated context)
---

# Check (project) — projects/forge — 2026-10-02

2 findings

## Findings

### FND.0740 — low — Four lines under Waiting on principal retell their thread instead of citing it
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:224-228 (THR.0400), :265-268 (THR.0420), :269-272 (THR.0430), :219-223 (THR.0470)
- **Rule:** CLAUDE.md, Ledger: a matter that has an ID gets one line — the ID, a few words, its state — and its substance stays in the thread or the record; the ledger cites and never copies. THR.0400 carries four dated events of the thread's history and the refused save of 2026-09-26; THR.0420 lists the thread's three cases; THR.0430 restates what the command would do and how; THR.0470 recounts what each round of the migration did, with versions.
- **Fix:** Cut each of the four lines to the ID, a few words and the present state (for example "THR.0400 — a gate in front of the tools; the hard half open, nothing scheduled"), leaving the dated events, the cases and the mechanism in C:\pche\_dev\forge-of-thought\projects\forge\10-intent.threads.md, where they already stand.

### FND.0750 — low — The Published line of the Format section is "not set" in two recipes, and one of them has a published file
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\recipes\cto-pitch.md:117-118; C:\pche\_dev\forge-of-thought\projects\forge\recipes\ceo-pitch.md:137-138
- **Rule:** `templates/recipe.md`, Format (lines 35-37): the Published line names `template <path | none>, model <name>`; recipes conform to the skeleton in their sections (CLAUDE.md, Document chain 7). Both recipes read "not set; `/publish` asks before its first run". For `cto-pitch` that first run has happened: C:\pche\_dev\forge-of-thought\projects\forge\published\cto-pitch.docx exists and the ledger's Published table (ledger.md:56) records its model, so the file in `published/` traces to a Format section that does not say what it is made with.
- **Fix:** At the next iteration of `recipes/cto-pitch.md`, write the Published line in the skeleton's shape with what the published file was made with (reference or none, the model the ledger row records); for `recipes/ceo-pitch.md`, which has no published file, either fill the line the same way or drop it until the principal first publishes.

## Facts
- projects/forge has no `.git` of its own — it is not a nested repository but is tracked by the engine's repository (CLAUDE.md, Persistence: every project is gitignored by the engine, `projects/forge` excepted); no way in is needed.
