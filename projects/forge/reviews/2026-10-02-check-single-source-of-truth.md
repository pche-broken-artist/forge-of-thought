---
date: 2026-10-02
project: forge
check: single-source-of-truth
target: the engine (C:\pche\_dev\forge-of-thought)
reviewer: check single-source-of-truth (isolated context)
---

# Check (single-source-of-truth) — engine (C:\pche\_dev\forge-of-thought) — 2026-10-02

19 findings; 64 files of the operating layer read whole (CLAUDE.md, 28 skill files with states and genres, 8 agents, 17 templates, the help headers of 9 scripts, .claude/settings.json), plus the Findings table of C:\pche\_dev\forge-of-thought\projects\forge\ledger.md and decisions.md for known findings. No earlier report of this check is filed and no DEC rejects any of the findings below; eight of them (marked) stand from the unfiled run of 2026-09-20 that THR.0240 records as deferred.

## Findings

### FND.0540 — high — What a brief is and who writes it is stated in six places, and the copies no longer agree
- **Where:** C:\pche\_dev\forge-of-thought\CLAUDE.md:61-63, 163, 193-195, 204-221, 669; C:\pche\_dev\forge-of-thought\.claude\skills\forge\states\brief.md:15-17, 34-36, 41-42, 109-113, 133-136; C:\pche\_dev\forge-of-thought\.claude\skills\spinoff\SKILL.md:19-20
- **Rule:** One owner per rule (CLAUDE.md, prime directive 10; POS.1070). brief.md:17-19 names CLAUDE.md, Document chain 1 as the owner of what a brief is and of its lifecycle, and CLAUDE.md:220-221 names the state file as the owner of how it is found, yet each restates the other. The drift is already there: CLAUDE.md:193-195 and 204 say "as the principal wrote it", "verbatim", "written by the principal", line 61-63 says "stored verbatim in whatever language they were written", line 669 "captured verbatim", while line 163 and brief.md:48-53 say Claude forms the record and may translate. (The brief's rules restated: deferred 2026-09-20, THR.0240, never filed.)
- **Fix:** Keep what a brief is once, in Document chain 1, cut the kinds-table cell, the code-block line, the clause of prime directive 6 and the Commands row to a bare label or pointer, and delete from brief.md the shape sentence, "rough on purpose", "the principal's by approval", the three origins and the lock lifecycle in favour of the citation it already carries at lines 17-19.

### FND.0550 — medium — /spinoff cites numbered steps of two state files that have no numbered steps
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\spinoff\SKILL.md:21-25
- **Rule:** A procedure another file owns is cited by path and the citation must reach it (POS.1070). "the `/forge brief` procedure (its step 4)" and "the `/forge intent` procedure (its step 2)" point at C:\pche\_dev\forge-of-thought\.claude\skills\forge\states\brief.md and intent.md, which are written in blocks (Target, Inputs, Aim, Partner, Map, Instruments, Course) and carry no step 4 or step 2.
- **Fix:** Cite the block that owns the act, as C:\pche\_dev\forge-of-thought\.claude\skills\new-project\SKILL.md:62-63 does ("its Course"), for the lock and for the first mining.

### FND.0560 — medium — What reject, park and obsolete write is stated three times, and one copy has drifted
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\critique\SKILL.md:42-48; C:\pche\_dev\forge-of-thought\.claude\skills\challenge\SKILL.md:48-55; C:\pche\_dev\forge-of-thought\.claude\skills\check\SKILL.md:57-63
- **Rule:** POS.1070. The three commands repeat the same rule set (reject: a DEC in the shape of templates/decisions.md, state `rejected`; park: `parked`; obsolete: `obsolete` with what made it moot; states change, never delete); only `accept` differs per command. The state words are owned by C:\pche\_dev\forge-of-thought\templates\ledger.md:75-85. Drift: challenge says "his one-line reason", the other two "the principal's reason".
- **Fix:** State the three shared verdicts and "states change only, never delete" once, in C:\pche\_dev\forge-of-thought\.claude\skills\walkthrough\SKILL.md (From verdicts to the write), and leave in each command only what `accept` writes there.

### FND.0570 — medium — The rules of how a render and a published file are made stand in CLAUDE.md and again in their definitions
- **Where:** C:\pche\_dev\forge-of-thought\CLAUDE.md:302-307, 321-325; against C:\pche\_dev\forge-of-thought\.claude\skills\render\SKILL.md:25-27, 35-37, 38-49 and C:\pche\_dev\forge-of-thought\.claude\skills\publish\SKILL.md:8-12
- **Rule:** POS.1070: "the rules of a mechanism - isolation, wrapping, provenance, what may be read - are written once, in its own definition"; CLAUDE.md:325-328 itself says how each step runs is its own definition's. The output path, "overwriting freely, history in git", the isolation of the subagent, the provenance front-matter and "makes a file and sends nothing anywhere" each stand in both.
- **Fix:** In Document chain 7 keep what a render, a recipe and a published file are, and cut the sentences on where the output lands, isolation, provenance and who may start `/publish` to the citation of the two skills that already follows.

### FND.0580 — medium — The joint pass of the assignment is described three times inside one state file
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\forge\states\assignment.md:29-42 (Partner), 63-67 (Instruments), 78-80 (Course), 82-103 (the three phases)
- **Rule:** A procedure stated in two places is a defect (CLAUDE.md, prime directive 10). The questions up front, the recast with the provenance map and the walkthrough by group are told in Partner and again in the phases; "a tool of the pass, not part of the assignment" stands at 63-64 and 94, "one item of the walkthrough is one group" at 65-66 and 95-96, the offer of `/critique essence` at 66-67, 78-80 and 101-103.
- **Fix:** Keep the procedure in the three phases and let Partner, Instruments and Course name the phases without retelling them.

### FND.0590 — low — The purpose of the intent's "Candidate structure for assignment" section is told in the state file, twice, and differently in the template that owns it
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\forge\states\intent.md:58-59, 87-98; C:\pche\_dev\forge-of-thought\templates\intent.md:38-40
- **Rule:** POS.1070; intent.md:44-45 says "where it lands is the template's". The state file says the section carries the recipients, the objective and the success criteria as positions; the template says only "Optional staging area before distillation. Delete once the assignment exists and leads."
- **Fix:** Move the sentence on what the section carries into the template's comment and leave in the state file the Map bullet with a pointer to the template.

### FND.0600 — low — /ingest implies a git operation that no script offers
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\ingest\SKILL.md:67-68
- **Rule:** No direct operation where a mechanism exists; the scripts are the only door to git (CLAUDE.md, Persistence, lines 454-456). "a binary already in git beside its extract leaves the index only on the principal's word" is an untracking, which no script in scripts/ performs (the header of forge-save.ps1: it stages everything and never cleans).
- **Fix:** Say that the untracking is the principal's own act in git by hand, as CLAUDE.md, Persistence says of the way in, or name the script once one exists.

### FND.0610 — low — The Commands table and three summaries in CLAUDE.md restate the procedures of the commands
- **Where:** C:\pche\_dev\forge-of-thought\CLAUDE.md:668, 669, 670, 672, 673, 677, 681, 682, 683; 483-489; 345-350; 591-593
- **Rule:** POS.1070; CLAUDE.md:487-488 says which checks each door runs "is its own definition's", yet row 682 names the `light` check, row 683 the release sequence and tag, row 668 the whole of `/setup` (near word for word its skill `description`), row 677 how a target narrows each lens (the lens files', by C:\pche\_dev\forge-of-thought\.claude\skills\critique\SKILL.md:25-26). The sequence of `/save` and `/release` is summarised three times in CLAUDE.md. (Commands table: deferred 2026-09-20, THR.0240, never filed.)
- **Fix:** Cut every Commands row to its purpose in one clause, naming no check, lens, step or tag, since `/man` prints the skill's own `description` beside it, and keep the save and release summary in Persistence alone.

### FND.0620 — low — Rules echoed inside CLAUDE.md, section to section
- **Where:** C:\pche\_dev\forge-of-thought\CLAUDE.md:28-30 against 118-119 (verbatim); 33 against 131-133; 76-91 against 145-147; the history companion at 167, 177-179, 198-199, 235, 309-311, 395-398 against its owner 504-507; "a recipe carries no status" at 172, 179, 307-309 against 503; the ledger as source of truth and registration only at 170, 201, 294 against 650-655; the reviewers' outputs at 587-589 against 623-624, 630, 636-639 and 422-424; CLAUDE.local.md at 18-22 against 359-361
- **Rule:** One owner per rule, inside a file as across files (POS.1070). (Deferred 2026-09-20, THR.0240, never filed; the check filing rule added since is a new instance.)
- **Fix:** Leave each rule in the section that owns it and cut the other places to the bare label or a section reference, as line 255-256 already does for Iteration default.

### FND.0630 — low — Rosters written out by name where the roster is a scan
- **Where:** C:\pche\_dev\forge-of-thought\CLAUDE.md:340-341, 351-352, 620-621, 627, 676, 677, 678, 681; C:\pche\_dev\forge-of-thought\.claude\skills\critique\SKILL.md:18-20; C:\pche\_dev\forge-of-thought\.claude\skills\man\SKILL.md:34-38 (the five scan paths of the dispatchers)
- **Rule:** POS.1070; each dispatcher says its roster is the scan of its files and that adding a member changes nothing else (check/SKILL.md:6-10, critique/SKILL.md:6-10, challenge/SKILL.md:6-11, recipe/SKILL.md:9-12), yet a new check, lens, persona or genre must also be written into CLAUDE.md in up to three places. (Deferred 2026-09-20, THR.0240, never filed.)
- **Fix:** Name no member of a roster outside its own file and its dispatcher's composition, and let `/man` read each roster's location from the dispatcher's skill.

### FND.0640 — low — /ingest and /research restate the index fields and the ledger columns
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\ingest\SKILL.md:50-51, 69-73, 82-84, 91-93; C:\pche\_dev\forge-of-thought\.claude\skills\research\SKILL.md:22-26
- **Rule:** The fields are owned by C:\pche\_dev\forge-of-thought\templates\index.md:15-25 and the columns and their vocabularies by C:\pche\_dev\forge-of-thought\templates\ledger.md:49-72 (CLAUDE.md, Document chain 5: "the fixed free-text fields the skeleton shows"). (Deferred 2026-09-20, THR.0240, never filed.)
- **Fix:** Have both skills say "an entry in the shape of templates/index.md" and "a row as templates/ledger.md has the table", keeping only what the command decides (who gives the Role, what is asked).

### FND.0650 — low — Genre checklists repeat the rules their skeletons carry
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\recipe\genres\presentation.md:22-25, 32-34, 39-45 against C:\pche\_dev\forge-of-thought\templates\recipe-presentation.md:20-22, 40-44, 55-64 (and CLAUDE.md:341-342); C:\pche\_dev\forge-of-thought\.claude\skills\recipe\genres\readme.md:22-26 against C:\pche\_dev\forge-of-thought\templates\recipe-readme.md:18-21 and C:\pche\_dev\forge-of-thought\.claude\skills\new-project\SKILL.md:31-32; C:\pche\_dev\forge-of-thought\.claude\skills\recipe\genres\release-notes.md:7-8 against CLAUDE.md:347-350
- **Rule:** POS.1070; the genre file "carries the elicitation checklist and points at the canonical skeleton" (recipe/SKILL.md:7-9). The Mermaid constraint, the picture-from-a-render rule and the input sets per kind stand word for word in both. (Deferred 2026-09-20, THR.0240, never filed.)
- **Fix:** Let each checklist item ask its question and leave the rule to the skeleton it points at.

### FND.0660 — low — The bundle index entry is a declared copy that is no longer a copy
- **Where:** C:\pche\_dev\forge-of-thought\templates\index-bundle.md:12-14, 20-24 against C:\pche\_dev\forge-of-thought\templates\index.md:15-19
- **Rule:** POS.1070; the comment says the entry "is carried verbatim from templates/index.md", and the Role line already differs between the two. (Deferred 2026-09-20, THR.0240, never filed.)
- **Fix:** Replace the entry block of the bundle skeleton by one line referring to the sources entry of templates/index.md.

### FND.0670 — low — Mining states enumerated outside their owner
- **Where:** C:\pche\_dev\forge-of-thought\CLAUDE.md:227-229; C:\pche\_dev\forge-of-thought\.claude\skills\forge\states\intent.md:106-107
- **Rule:** The state vocabularies are the ledger skeleton's (POS.1070; C:\pche\_dev\forge-of-thought\templates\ledger.md:22-25 for the Briefs table), as CLAUDE.md:624-625 already has it for finding states. (State vocabularies in three places: deferred 2026-09-20, THR.0240, never filed; settled since for findings and challenges only.)
- **Fix:** Have both places say "mining state as templates/ledger.md, Briefs, has it".

### FND.0680 — low — The critic contract restates prime directive 8
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\critic-contract\SKILL.md:61-65; also C:\pche\_dev\forge-of-thought\CLAUDE.md:575-576 stating the critic's conduct that the contract owns at 69-71
- **Rule:** POS.1070; "Completeness is the test, not brevity: length is never a defect; excess of the wrong kind (solving instead of assigning) is" is CLAUDE.md, prime directive 8 (lines 66-75), uncited, while the same bullet cites its two other owners. (Deferred 2026-09-20, THR.0240, never filed.)
- **Fix:** Replace the sentence by the citation of prime directive 8 and drop the critic's sentence from Requirement style.

### FND.0690 — low — Lens sections restate rules they verify
- **Where:** C:\pche\_dev\forge-of-thought\.claude\agents\check-engine.md:38-42; C:\pche\_dev\forge-of-thought\.claude\agents\check-history.md:18-21; C:\pche\_dev\forge-of-thought\.claude\agents\critic-clarity.md:52-53, 61
- **Rule:** A Lens "names the owner of each rule and never restates it" (C:\pche\_dev\forge-of-thought\.claude\skills\check-contract\SKILL.md:35-37; POS.1120). check-engine lists two rules of Versioning & status with no owner named; check-history repeats the parenthesis of CLAUDE.md:512-513 word for word beside its citation; critic-clarity's checklist paraphrases Requirement style, which its own line 32-33 says is "stated there and not here".
- **Fix:** Name the owning section in each place and delete the repeated rule text.

### FND.0700 — low — One-line rules echoed without naming their owner
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\challenge\SKILL.md:49-50 (CLAUDE.md:631-632); C:\pche\_dev\forge-of-thought\.claude\skills\walkthrough\SKILL.md:38-39 (CLAUDE.md:151-152); C:\pche\_dev\forge-of-thought\CLAUDE.md:269-270 (templates/index.md:18) and 302 (templates/recipe.md:18-19); C:\pche\_dev\forge-of-thought\.claude\skills\ingest\SKILL.md:47-51, C:\pche\_dev\forge-of-thought\templates\ledger.md:50-51 and C:\pche\_dev\forge-of-thought\templates\index-bundle.md:14-15 (CLAUDE.md:259-260); C:\pche\_dev\forge-of-thought\scripts\forge-branch.ps1:20-23 (release/SKILL.md:17-22)
- **Rule:** POS.1070: a one-line reminder at the point of action is not a restatement only where it names its owner.
- **Fix:** Add the owner in parentheses to each reminder that is read at the point of action and delete the rest.

### FND.0710 — low — The sweep of /ingest reports changed sources, a detection the project check exists for
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\ingest\SKILL.md:16-25
- **Rule:** No check outside the check agents; the immutability of registered sources is verified by C:\pche\_dev\forge-of-thought\.claude\agents\check-project.md:61-65 (Immutables), by other signs than the modification time the sweep uses, so one concern has two detectors.
- **Fix:** Keep in the sweep what `/ingest` does with a changed file per kind and name the `project` check as the one place that finds a breach, or move the modification-time test into that check's Lens.

### FND.0720 — low — What a Lens section holds is listed in each contract and again in each skeleton, and the YAML quoting caveat stands three times
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\check-contract\SKILL.md:13-16 against C:\pche\_dev\forge-of-thought\templates\check.md:20-26; C:\pche\_dev\forge-of-thought\.claude\skills\critic-contract\SKILL.md:13-16 against C:\pche\_dev\forge-of-thought\templates\critic.md:19-26; C:\pche\_dev\forge-of-thought\.claude\skills\challenger-contract\SKILL.md:13-16 against C:\pche\_dev\forge-of-thought\templates\challenger.md:20-26; the caveat at templates\check.md:13-16, templates\critic.md:12-15, templates\challenger.md:13-15
- **Rule:** POS.1120 gives one owner, CLAUDE.md, Isolated reviewers, for what a lens file owns, and CLAUDE.md:601-602 says only "only the Lens section its own"; the list then lives in two files per kind, and the quoting rule has no owner at all.
- **Fix:** Let each skeleton own the parts of its Lens section with the contract's opener citing it, and state the quoting caveat once in CLAUDE.md, Isolated reviewers, cited from the three skeletons.
