---
date: 2026-10-02
project: forge
check: history
target: projects/forge
reviewer: check history (isolated context)
---

# Check (history) — projects/forge — 2026-10-02

10 findings (none known: the ledger's Findings table and `reviews/` hold no earlier `history` report, so a finding rejected at the unfiled first run cannot be recognised here)

Files read: `C:\pche\_dev\forge-of-thought\projects\forge\10-intent.md` with `10-intent.threads.md`, `10-intent.history.md` and (searched) `10-intent.history.archive.md`; the five recipes under `C:\pche\_dev\forge-of-thought\projects\forge\recipes\` with their histories and (searched) archives; the three briefs with their companions. In the proposed records `<date>`, `<version>` and `<author>` are the write step's.

## Findings

### FND.0440 — medium — POS.1040 no longer says what "one form" means for a binary; the words stand only in its record of 4.42
- **Where:** projects/forge/10-intent.md:1919-1925 (the text that left: projects/forge/10-intent.history.md:81)
- **Rule:** CLAUDE.md, Document chain 2: where the output is only part of a file, a section of CLAUDE.md among them, the item keeps the full information. The one-form rule is carried by CLAUDE.md, Document chain 5, as well as by the skill. The item now reads "either text or a functional binary, never both by default" and never names the extract, so "both" and the reason that follows ("a binary nobody reads from git is weight without use") cannot be understood from the item.
- **Fix:** return to the item, word for word from the `Was` of its 4.42 record, the sentences that state the rule, and leave the procedure with the skill.
  - Returns: "At `/ingest` every binary file — isolated or inside a bundle — gets one question: convert to Markdown? Yes: `doc2md` writes `sources/<slug>.md`, and that extract is the source [...] the original is not copied into the project [...] No: the binary is the source as a functional thing — a deck template, a graphic, a logo [...] Keeping both is the exception, on the principal's explicit word."
  - Record: `- <date> | <version> | <author> | POS.1040 | changed | What "one form" means for a binary returned to the item from its record of 4.42: a section of CLAUDE.md carries the rule beside the skill, and without it "never both" is not understood; the procedure stays the skill's.`

### FND.0450 — medium — POS.0950 carries the story of its reversal: what stood before, why that was dropped, what the field showed
- **Where:** projects/forge/10-intent.md:1603-1611
- **Rule:** CLAUDE.md, Versioning & status: the way to an item (why it changed, what was said, trials) goes into its record, never into the item.
- **Fix:** move the two sentences into a record; the sentence after them ("The two-roles case is accepted as a risk …") then names a case the item no longer introduces and the item loses its only date, both to be settled in the same step.
  - Leaves: "Reversed 2026-09-16, written 2026-09-18: the identity was a property of the project, set locally in every repository and proposed by the command layer from a roster in `identities.local.md`, and the per-host include was rejected because a host is only a correlate of the identity and fails where one host serves two roles. In the field the roster duplicated what the user's includes already resolved, every repository carried the same identity twice, and the forge had gained a file, a template and three identity steps for a case that had not occurred."
  - Record: `- <date> | <version> | <author> | POS.0950 | changed | The way to the position moved to its history, stance unchanged: what stood before the reversal and what the field showed. | Was: Reversed 2026-09-16, written 2026-09-18: the identity was a property of the project, set locally in every repository and proposed by the command layer from a roster in `identities.local.md`, and the per-host include was rejected because a host is only a correlate of the identity and fails where one host serves two roles. In the field the roster duplicated what the user's includes already resolved, every repository carried the same identity twice, and the forge had gained a file, a template and three identity steps for a case that had not occurred.`

### FND.0460 — medium — POS.1330 closes with what the definition replaced and how the brief was mined
- **Where:** projects/forge/10-intent.md:391-398
- **Rule:** CLAUDE.md, Versioning & status: the way to an item goes into its record, never into the item. The closing paragraph is outside the seven blocks the item holds word for word, and neither fact stands in the history (the archive's row 4.32 searched, the log has no record of POS.1330), so the record is where they must go.
- **Fix:** keep "Decided 2026-09-28 from `00-brief-elicitation.md`." and move the rest of the paragraph into a record; the pointer to THR.0440 (a) to (c) is kept by the thread itself, which names the definitions it would change.
  - Leaves: "With the translation, the mending of grammar and the structure before the lock, the definition replaces the earlier rule never to translate, restructure or tidy the text of a brief. Two sentences of the brief's text are not carried here, since they speak of the mining and not of the definition: the one that leaves that rule to the mining, settled by this position, and the one naming three matters left open for the intent, which are THR.0440 (a) to (c)."
  - Record: `- <date> | <version> | <author> | POS.1330 | changed | The way to the position moved to its history, stance unchanged: what the definition replaced and what of the brief's text was not carried at the mining. | Was: With the translation, the mending of grammar and the structure before the lock, the definition replaces the earlier rule never to translate, restructure or tidy the text of a brief. Two sentences of the brief's text are not carried here, since they speak of the mining and not of the definition: the one that leaves that rule to the mining, settled by this position, and the one naming three matters left open for the intent, which are THR.0440 (a) to (c).`

### FND.0470 — low — POS.0160, POS.0230 and POS.1090 cite numbered items of a source that the item no longer names
- **Where:** projects/forge/10-intent.md:784-785 ("(P.15, P.09, G.10)"), :1020-1022 ("(P.08, F.04)"), :1692-1696 ("(P.05, F.06)"); the words that tied them to the run record left at 4.42: projects/forge/10-intent.history.md:34, :41, :68
- **Rule:** CLAUDE.md, Versioning & status and Document chain 2, the other way: an item is not understood where what resolves it stands only in the history. In POS.0160 the reason of the rule left with it.
- **Fix:** name the source by path before the numbers in each of the three items, as POS.1160 does (`sources/forge-run-record-health.md`), one record per item and no `Was`; POS.1050, REJ.0190 and REJ.0200 carry the same bare numbers from before the cleaning and take the same mend.
  - Record, per item: `- <date> | <version> | <author> | POS.0160 | changed | The source of the cited numbers named by path; its naming had left with the way at 4.42.` (the same for POS.0230 and POS.1090)

### FND.0480 — low — POS.0020 keeps what was rejected on the way to it
- **Where:** projects/forge/10-intent.md:63-65
- **Rule:** CLAUDE.md, Versioning & status: what was said on the way goes into the record. The stance itself stands earlier in the item ("raised at once, as one question"); the archive does not carry the rejection (searched).
- **Fix:** move the clause into a record, the sentence then ending at "(P.03, F.04: Claude's constructions presented as facts)."
  - Leaves: "; the record's "no warnings unless asked" rejected by the principal — he wants to be told of problems, holes and contradictions, as a question"
  - Record: `- <date> | <version> | <author> | POS.0020 | changed | The way to the position moved to its history, stance unchanged: the part of the source's proposal that was not taken. | Was: ; the record's "no warnings unless asked" rejected by the principal — he wants to be told of problems, holes and contradictions, as a question`

### FND.0490 — low — POS.0740 and POS.1150 carry where the output lands and the model default, which the scripts' headers carry
- **Where:** projects/forge/10-intent.md:1491-1496 (POS.0740), :1517-1519 (POS.1150); the carriers: scripts/md2pptx.ps1:61-67 and :95-96, scripts/md2docx.ps1:91-93
- **Rule:** CLAUDE.md, Document chain 2: where an item's output is a file of its own, the realisation is the file's; and Document chain 7: where the output lands is the script's header's.
- **Fix:** move the parameter detail into records, the items keeping what the headers do not say ("tracked in git like any render output", "a presentation recipe may recommend one in its Format section"); the `-Template` passage of POS.0740 is left untouched, waiting as disagreement (12) of THR.0470.
  - Leaves, POS.0740: "The output defaults to the input's directory and basename with a `.pptx` extension, so a deck generated from `renders/<recipe>.md` lands as `renders/<recipe>.pptx` [...] ; `-Out` overrides. The headless run's model is chosen by `-Model`, default opus"
  - Leaves, POS.1150: "The output defaults to the input's directory and basename with a `.docx` extension [...] ; `-Out` overrides."
  - Records: `- <date> | <version> | <author> | POS.0740 | changed | Detail moved; the help of `scripts/md2pptx.ps1` carries it. | Was: The output defaults to the input's directory and basename with a `.pptx` extension, so a deck generated from `renders/<recipe>.md` lands as `renders/<recipe>.pptx` [...] ; `-Out` overrides. The headless run's model is chosen by `-Model`, default opus` and `- <date> | <version> | <author> | POS.1150 | changed | Detail moved; the help of `scripts/md2docx.ps1` carries it. | Was: The output defaults to the input's directory and basename with a `.docx` extension [...] ; `-Out` overrides.`

### FND.0500 — low — The note closing the threads file points at a citation that left POS.0210 at 4.42
- **Where:** projects/forge/10-intent.threads.md:963-964 ("Citations of THR.0120 from POS.0210 and version 2.4 refer to the latter."); the citation now stands at projects/forge/10-intent.history.md:40
- **Rule:** CLAUDE.md, Document chain 2: the threads file is part of the intent; a sentence of it that can be followed only through the history does not hold in the document.
- **Fix:** reword the sentence so that it names where the citations now stand, the 4.42 record of POS.0210 in the log and the row of 2.4 in the archive; no record, the threads file having no history of its own.

### FND.0510 — low — Two clauses in POS.0590 and POS.1040 say how the item came about
- **Where:** projects/forge/10-intent.md:1468-1469 (POS.0590), :1929-1930 (POS.1040)
- **Rule:** CLAUDE.md, Versioning & status: why an item changed and what was said goes into its record.
- **Fix:** move both clauses into records; POS.0590 then reads "… the recipe's `## Format` section, which is never copied into the render".
  - Leaves, POS.0590: "replaces the Build instructions of the presentation genre and"
  - Leaves, POS.1040: ", simplified by the principal"
  - Records: `- <date> | <version> | <author> | POS.0590 | changed | What the Format section replaced moved to the history, stance unchanged. | Was: replaces the Build instructions of the presentation genre and` and `- <date> | <version> | <author> | POS.1040 | changed | The way to the position moved to its history, stance unchanged. | Was: , simplified by the principal`

### FND.0520 — low — The release-notes recipe keeps the migration an instruction came from and how the minors stood before 4.0
- **Where:** projects/forge/recipes/release-notes.md:46 and :77-79
- **Rule:** CLAUDE.md, Versioning & status: the rule holds for every versioned document, recipes included; the way goes into the record in `recipes/release-notes.history.md`.
- **Fix:** move the parenthesis and the sentence into one record of the recipe's next version.
  - Leaves: "(the migration of 2026-09-05, POS.0730)" and "The sections of 3.1–3.x in the current edition are therefore carried over verbatim until 4.0 and folded then."
  - Record: `- <date> | <recipe version> | <author> | Instructions | changed | The way to two instructions moved to the history: the migration one came from, and how the minors stood before 4.0. | Was: (the migration of 2026-09-05, POS.0730) [...] The sections of 3.1–3.x in the current edition are therefore carried over verbatim until 4.0 and folded then.`

### FND.0530 — low — The executive-pitch recipe says who decided its template and when
- **Where:** projects/forge/recipes/executive-pitch.md:73-74
- **Rule:** CLAUDE.md, Versioning & status: what was said and decided on the way goes into the record; the archive's row 0.3 already carries the decision (projects/forge/recipes/executive-pitch.history.archive.md:21).
- **Fix:** move the parenthesis into a record of the recipe's next version in `recipes/executive-pitch.history.md`.
  - Leaves: "(principal's decision of 2026-09-10; no `.potx`)"
  - Record: `- <date> | <recipe version> | <author> | Format | changed | The way to the instruction moved to the history; the decision stands in the archive's row 0.3. | Was: (principal's decision of 2026-09-10; no `.potx`)`
