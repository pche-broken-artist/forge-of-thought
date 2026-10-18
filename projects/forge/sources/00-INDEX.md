---
project: forge
directory: sources
updated: 2026-10-18
---

# Index — sources of Forge of Thought

<!-- Resource index: a light catalogue so that Claude and the principal
know what exists here and what it is for without re-reading the files.
Freely rewritten (like the ledger) while the files it catalogues stay
immutable. Tracks nothing — no processing state, no positions — and is
an automatic input of no command; a contradiction between the intent
and a resource is not a finding. Registration state lives in the ledger.
Written by /ingest; verified by /check. A bundle is ONE entry pointing
to its own 00-INDEX.md — two levels, never deeper. -->

### `forge-run-record-health.md`
- **What:** A structured record of one real run of the forge (10–13 September 2026) on a private project whose terminal artefact was a report for a third party, not an assignment: a timeline (E), the mechanisms used (D), eight failures (F), thirteen things that worked (W), thirteen engine gaps (G) and sixteen proposals (P), with stable item numbers for citation. Carries nothing of the subject project's content.
- **Origin:** Written by Claude on 13 September 2026 in a separate, isolated instance of the forge, from three conversation exports, the project's history companions, ledger and decisions, through six isolated read-only agents plus a quantitative pass; ingested here the same day.
- **Role:** External feedback from the field — the first record of the engine used on a real project by its own principal; evidence for the conduct rules and the growth of the chain below the assignment.
- **Use for:** Deciding the proposals P.01–P.16 one by one (walkthrough into the intent); evidence when a working method, a prime directive or a state file is revised (F.01–F.08, G.01–G.13); the case for a lower layer with an external audience (G.05, P.09); what to keep as it is (W.01–W.13).

### `word-default-a4.docx`
- **What:** A functional binary, not a text: a Word document whose only purpose is its styles and page setup — Word's default look with the heading styles written out (Title, Subtitle, Heading 1–4; body in Normal) on an A4 page with 2.54 cm margins. Its few lines of content are sample paragraphs that keep the styles in the file and are ignored by the conversion.
- **Origin:** Made on 20 September 2026 by Word itself, through automation, from the principal's `Normal.dotm` — a new document with each heading style applied once and the paper set to A4 — because `Normal.dotm` alone keeps the heading styles latent and a Word file built from it shows headings as body text. Stored here the same day on the principal's word; confirmed as its home on 21 September 2026. Not converted to Markdown: it is a functional thing.
- **Role:** —
- **Use for:** —

### `forge-elicitation-brief-review.md`
- **What:** A review of `00-brief-elicitation.md` 0.2 against `10-intent.md` 4.31, in twelve sections: what the extension gets right, seventeen material problems each with a recommended wording, thirteen decisions the brief should make explicitly, a proposed normative contract for the seven-block definition, complete candidate definitions of brief, intent and assignment, the boundaries between the three, seven risks with controls, a ten-step implementation sequence and a disposition of the brief (keep, modify, move to separate work). Its conclusion: the definition contract and the three definitions are mature enough to work, the engine split belongs to a separate brief.
- **Origin:** Author and date not stated in the file; its front-matter names the two reviewed documents and the text declares itself material for the forge to ingest and work through, not a replacement brief. Found in `sources/` and registered on the principal's command on 28 September 2026.
- **Role:** —
- **Use for:** A critique of `00-brief-elicitation.md`: to be analysed and used to improve `00-brief-elicitation.md`.

### `forge-elicitation-brief-review-v0.4.md`
- **What:** A second, incremental review of `00-brief-elicitation.md`, of its version 0.4, following `forge-elicitation-brief-review.md`: six points that 0.4 resolved, twelve remaining issues each with a recommended wording, one central decision it holds still open (whether Claude may formulate the text of a brief once the principal has accepted the substance), ten candidate amendments, and a disposition in three groups (ready to mine, decide during mining, keep out of this decision). Its conclusion: version 0.4 is ready to be used as input to the intent.
- **Origin:** Author and date not stated in the file; its front-matter names the reviewed document and the previous review. Found in `sources/` and registered on the principal's command on 28 September 2026.
- **Role:** A review, like the one before it: read and weighed, the principal deciding by his own judgement what of it is taken.
- **Use for:** To be looked at against `00-brief-elicitation.md` 0.4 and used as the principal sees fit.

### `docs-audit-2026-10-11.md`
- **What:** A structured record of one audit of the generated documentation in `docs/` against the forge's own intent (POS.1450, POS.1470, POS.0950) at commit `04e332a`: a verdict with a judgement by section, eighteen measurements (M.01–M.18) of the tree, forty-six findings (F.01–F.46) by severity with evidence, where each is to be mended and what was not re-checked, seven contradictions inside the owner files (C.01–C.07), eight things that work (W.01–W.08) and what was not verified. Decides nothing and changes nothing.
- **Origin:** Written by Claude on 11 October 2026 in a session outside the forge, from a read-only clone, through six isolated read-only agents, one per part of `docs/`, plus a mechanical measuring pass; registered here the same day.
- **Role:** An audit of the documentation by a separate agent that went through the whole of `docs/` without the context of this forge: the basis for deciding how the documentation is to be improved.
- **Use for:** Deciding, finding by finding, what of the documentation and of its generator is changed (F.01–F.46, by walkthrough into the intent and the documentation's definitions); settling the contradictions inside the owner files before a regeneration (C.01–C.07); the measurements as the baseline a later audit is compared with (M.01–M.18).

### `ledger-merge-review.md`
- **What:** a second look at why the ledger merges badly when two branches or two people write it, from the shape of the file rather than from the field: five causes (the `updated` counter, long one-line notes, appends at the tail, free rewriting, the shared next ID), what git offers (`merge=union`, a table-aware custom driver, `rerere`), four format changes for the ledger itself, an event-sourced ledger rendered from an append-only log, and lazy ID allocation finalised at the release. Proposes, decides nothing.
- **Origin:** written in Czech by a model in a session outside the forge, from a read-only look at the repository at v5.9; pasted into the conversation by the principal on 2026-10-17 and stored in English on his word.
- **Role:** the same question as the research of 2026-10-17 on mergeable shared records, asked from another angle; to be compared and synthesised with it before anything enters the intent (the principal's word of 2026-10-17).
- **Use for:** the synthesis of the two views on the ledger's merge problem; the list of format defects of today's ledger; the event-log alternative and lazy IDs as candidates when the counters are taken up.

### `merge-design-review.md`
- **What:** a review in three parts of Claude's complete proposal for the merge mechanism of the forge's files (the four ways of merging, the generated ledger, the record driver, threads as files, the version as a boundary, ID blocks per branch): what git does not do as the proposal assumed (`ours` not built in and reversed in a rebase), the ledger out of git, the counters before the test, deletion in an immutable file as a conflict, the version as a boundary record, decisions as unmutated blocks, a closed thread immutable. Proposes, decides nothing.
- **Origin:** written in Czech by a model in a session outside the forge, the second and third parts answering Claude's replies; pasted into the conversation by the principal on 2026-10-17 and stored in English on his word.
- **Role:** the outside review of the proposal that the brief `collaboration` stores; its accepted points are in the brief, the brief cites it where a point came from it (the principal's word of 2026-10-17).
- **Use for:** checking, when the brief is mined, which part of the mechanism rests on the review's correction and why; the arguments for the ledger out of git and for the version as a boundary.

### `merge-brief-critique.md`
- **What:** a critique of the brief `collaboration` 0.1 against the repository, in seven sections: factual errors (docs-map.md is authored, not derived; the research index is derivable only after the note carries Answer and Consult when; `kind` and `language` lose their home with the ledger; the ID block from a branch name collides by the birthday paradox; the order of forge-save; the verification as written cannot pass), what in B has no home (Work, the brief's Note, Dependencies, parked and obsolete, Waiting), F1 sharpened (`<base>+`, a `landed` record per document, forge-land, no reordering of a history, two clones on main), the details of C and D (rebase.backend, renormalize, /document on main, the driver's name), A2's traps and check, what is missing (git worktree for two windows, git rm --cached at the migration, the wording of the principle), and a revised order. Proposes, decides nothing.
- **Origin:** written in Czech by a model in a session outside the forge, from the brief and the repository; pasted into the conversation by the principal on 2026-10-17 and stored in English on his word.
- **Role:** the critique the brief `collaboration` 0.2 works in; the brief cites it where a point came from it (the principal's word of 2026-10-17).
- **Use for:** checking, when the brief is mined, which part rests on this critique's correction; the arithmetic of the ID space; the list of what the ledger alone knows today.

### `merge-brief-critique-2.md`
- **What:** a critique of the brief `collaboration` 0.2 in ten sections: `<base>+` in the header conflicts in the very case F1 solves (a branch must never touch the header); F2 inconsistent (per branch or per author) and without a mechanism of writing the reservation to main (plumbing without a checkout, branch protection as a limit, one hundred across prefixes, allocation on main reading the reservations); immutable indexes make every correction a conflict; a round on main before the landing breaks the attribution (land first); the driver's gaps (keys, regions outside records, record kinds, the merged-unseen report, a closed thread changed after closing, the driver's version); M (the archive read, --undo by a manifest, the shape as markers, the engine's prefixes); the state as a release render instead of README tables; two facts on worktrees; the order (C1 with B, D split); minor points. Proposes, decides nothing.
- **Origin:** written in Czech by a model in a session outside the forge, from the brief 0.2 and the repository; pasted into the conversation by the principal on 2026-10-17 and stored in English on his word.
- **Role:** the critique the brief `collaboration` 0.3 works in; the brief cites it where a point came from it (the principal's word of 2026-10-17).
- **Use for:** checking, when the brief is mined, which part rests on this critique's correction; the plumbing of the reservation; the keys of the driver's units.

### `merge-brief-critique-3.md`
- **What:** a critique of the brief `collaboration` 0.3 in eight sections: a merge of main into a branch breaks the attribution of versions (an ordering rule in the driver: the side whose new records hold a landed goes first); `mined:` and `state:` in headers contradict the untouched header (records instead, threads the named exception); a hundred per branch across prefixes burns the ID space by branches, not by use (per prefix on demand; five digits to be decided now, with the numbers); provenance on a branch cites a version that does not exist (`v5.12+N`); the A2 render check must compare the AST or normalised whitespace; the closed-thread check must compare with the closing commit; C before F1 in the order; minor points (land first per document, "until F2" dropped for history lines, a finding settled by no version, the Work state and the Sources Form in M, `forge-branch --reserve`). Proposes, decides nothing.
- **Origin:** written in Czech by a model in a session outside the forge, from the brief 0.3 and the repository; pasted into the conversation by the principal on 2026-10-17 and stored in English on his word.
- **Role:** the critique the brief `collaboration` 0.4 works in; the brief cites it where a point came from it (the principal's word of 2026-10-17).
- **Use for:** checking, when the brief is mined, which part rests on this critique's correction; the ordering rule of the driver; the arithmetic of the four-digit space.

### `merge-brief-critique-4.md`
- **What:** a critique of the brief `collaboration` 0.4 in six sections: the record of a mining belongs in the intent's history with the brief as subject (its version column says which intent mined it); state records and the version (a state-only round on main raises nothing, a landing always raises); the reservation of IDs at the reflection and not inside the write, into the nearest free hundred, blocks never released and the consequence for groups, the file `ids.md`; the scope of five digits (27 places in 15 files); the Waiting rule against today's practice (the parked under a heading of their own); minor points (the header wording, more Markdown traps, the double `landed`, a state-only round in the test). Proposes, decides nothing.
- **Origin:** written in Czech by a model in a session outside the forge, from the brief 0.4 and the repository; pasted into the conversation by the principal on 2026-10-17 and stored in English on his word.
- **Role:** the critique the brief `collaboration` 0.5 works in; the brief cites it where a point came from it (the principal's word of 2026-10-17).
- **Use for:** checking, when the brief is mined, which part rests on this critique's correction; the rule of state records and versions; the Waiting rule.

### `merge-brief-critique-5.md`
- **What:** a critique of the brief `collaboration` 0.5 in four points: `updated` leaves the recipes' headers too, not only the indexes; the key of a reservation line is the prefix with the start of the block, not the start alone; a missing `ids.md` reads as no reservations and `/new-project` creates it from the template, so the migration need not; the `closed` record of an engine finding keeps the finding as its subject, the fixed layer named in the reason. Proposes, decides nothing.
- **Origin:** written in Czech by a model in a session outside the forge, from the brief 0.5 and CLAUDE.md; pasted into the conversation by the principal on 2026-10-17 and stored in English on his word.
- **Role:** the critique the brief `collaboration` 0.6 works in; the brief cites it where a point came from it (the principal's word of 2026-10-17).
- **Use for:** checking, when the brief is mined, which part rests on this critique's correction; the key of `ids.md`; the shape of a `closed` record.

### `merge-brief-critique-6.md`
- **What:** a critique of the brief `collaboration` 0.7 in six points: `<slug>@<branch>` as the slug of a worktree for the commands, forge-save without a slug visiting both trees; the write step never fetching, the state read at the reflection and a stale state never blocking; the steps of finishing a rebase by hand corrected (add, then continue; the manual path starting with the person's own pull --rebase); new IDs four-digit until 9999 with no padding, and a numeric sort by (prefix, number); the order of releases against the order of the steps of one migration run; the engine's second root carrying only `projects/forge`. Proposes, decides nothing.
- **Origin:** written in Czech by a model in a session outside the forge, from the brief 0.7; pasted into the conversation by the principal on 2026-10-17 and stored in English on his word.
- **Role:** the critique the brief `collaboration` 0.8 works in; the brief cites it where a point came from it (the principal's word of 2026-10-17).
- **Use for:** checking, when the brief is mined, which part rests on this critique's correction; the addressing of a worktree; the shape of IDs past 9999.

### `mining-critique.md`
- **What:** a critique of Claude's proposal of 2026-10-17 for mining the brief `collaboration` 0.8 into the intent, in six points: positions too large and carrying realisation and history (split POS.1600 and POS.1650, realisation to the solution design); a bare `/save` contradicting itself between two projects and two trees; four existing positions left untouched (the header fields, the language rule, the library born as the ledger, the Waiting rule); double ownership of the driver's ordering rule and of the free-number rule; the four releases a plan, not a stance; small points (more REJ, groups, `v<base>+N`). Proposes, decides nothing.
- **Origin:** written in Czech by a model in a session outside the forge, from the proposal; pasted into the conversation by the principal on 2026-10-17 and stored in English on his word.
- **Role:** the critique the mining of the brief `collaboration` works in before the write of intent 5.13 (the principal's word of 2026-10-17).
- **Use for:** checking, after the write, which cut of the positions rests on this critique; the size of a position as a model (POS.1660).

### `design-critique.md`
- **What:** a critique of Claude's proposal of 2026-10-17 for the solution design pass over the brief `collaboration` (0.17 to 0.18), in five points: the first report of a day on two branches collides, so every report carries the time-and-hash suffix (a change of POS.1720); the ledger script reads the threads and the project file too; CLAUDE.md and the documentation missing from the Where of several parts; the fixed shape of a verdict in a DEC for the script; smaller points (the instance files in a worktree, the owners of the 72-column rule, the registration's choice, `/end`, the provenance of research and critiques, the README recipe's input, the turning over of "Not built" at a release). Approves the shape of the pass. Proposes, decides nothing.
- **Origin:** written in Czech by a model in a session outside the forge, from the proposal; pasted into the conversation by the principal on 2026-10-17 and stored in English on his word.
- **Role:** the critique the solution design pass works in before the write of 0.18 (the principal's word of 2026-10-17).
- **Use for:** checking, after the write, which part of the design rests on this critique; the shape of a DEC verdict the ledger script parses.

### `design-critique-2.md`
- **What:** a second critique of the corrected solution design pass over the brief `collaboration`, three points: POS.1720 must say what SOL.0810 says (verified, it does); whether the renders are written one sentence per line too, and the render skill's line 37; several Verdict lines in one decision and a partial verdict as the verdict on the whole ID. Proposes, decides nothing.
- **Origin:** written in Czech by a model in a session outside the forge, from the corrected proposal; pasted into the conversation by the principal on 2026-10-17 and stored in English on his word.
- **Role:** the second critique the solution design pass works in before the write of 0.18 (the principal's word of 2026-10-17).
- **Use for:** checking, after the write, why POS.1580 reaches the renders and why a decision carries several Verdict lines.

### `architect-challenge-review.md`
- **What:** a review of the architect's challenge of the solution design 0.18 (`challenges/2026-10-17-challenge-architect.md`), a verdict and a way of mending for each of CHL.0250 to CHL.0300, all six accepted: a `/merge <branch>` command with a walkthrough of the conflicts; the model of one integrator and N contributors on a host that protects main, with ID blocks per author assigned by hand and no plumbing; the migration refusing while branches are in flight, `--undo` restoring from the index, the tests of the driver and of `ours` under rebase before the releases; the ledger script dropping a row aloud instead of crashing, a dry run over today's projects; a release, the documentation and a publish refusing a repository behind or diverged; POS.0820 narrowed to the old shape for reading. Proposes; the principal adopted it whole on 2026-10-17.
- **Origin:** written in Czech by a model in a session outside the forge, from the challenge report and the design; pasted into the conversation by the principal on 2026-10-17 and stored in English on his word.
- **Role:** the review by which the six challenges of the architect were settled, intent 5.16 and design 0.19 (the principal's word of 2026-10-17).
- **Use for:** the reasons behind the integrator model, the blocks per author and the `/merge` command; the preliminary tests before the first and the second release.

### `architect-challenge-review-2.md`
- **What:** a second review, of the proposal that mends the architect's six challenges: the rebase of the next `/save` drops the merge commit of `/merge` and brings its conflicts back, so `/merge` refuses a repository behind or diverged and `/setup` sets `rerere.enabled`, not offers it; `/merge` fetches and merges `origin/<branch>`, a fast-forward allowed; ID blocks assigned above the highest used number, the overlap check reporting a block over a used number; a question on the numbering of the TBCs (TBC.0040 is taken, closed at 0.17, so no mix-up). Proposes, decides nothing.
- **Origin:** written in Czech by a model in a session outside the forge, from the proposal; pasted into the conversation by the principal on 2026-10-17 and stored in English on his word.
- **Role:** the second review the mending of the challenges works in before the write of intent 5.16 and design 0.19 (the principal's word of 2026-10-17).
- **Use for:** why rerere is set and not offered; why `/merge` refuses a repository behind.

### `architect-challenge-review-3.md`
- **What:** a review of the architect's second challenge, of the solution design 0.19 (`challenges/2026-10-17-challenge-architect-2.md`), a verdict and a way of mending for each of CHL.0310 to CHL.0360, all six accepted: `/merge` in both directions with the source chosen by where the branch lives and `forge-branch --done`; the order of the releases reversed, the driver first and the reflow last as a release of its own with a blame ignore-revs file, a DEC reversing "A2 first"; the verdict of a merge conflict as a `changed` record and the driver's conflict output as standard markers; rerere a convenience, `/merge` ending with the push and forge-save pulling a merge commit by merge; the engine's own attribute list; "join the landing" instead of "land first". Answers the challenger's five questions, the author's handle as an exact key among them. Proposes; the principal adopted it whole on 2026-10-17.
- **Origin:** written in Czech by a model in a session outside the forge, from the challenge report and the design; pasted into the conversation by the principal on 2026-10-17 and stored in English on his word.
- **Role:** the review by which the six challenges of the architect's second run were settled, intent 5.17 and design 0.20 (the principal's word of 2026-10-17).
- **Use for:** the reasons behind the order of the releases, the two directions of `/merge`, the landing as the first act of the save and the handle as the key of an ID block.

### `cutover-plan-critique.md`
- **What:** a critique of the work product `work/collaboration-cutover.md` as made 2026-10-17: missing steps (the fixture, a tag before every migration, the map's entries, `/release` calling forge-land and the release-notes tolerance, `blame.ignoreRevsFile` in `/setup`, the screenplays under the conversion) and weak closings and order (the ledger script tested over migrated throwaway clones and so after the migration script, `--apply` and `--undo` on a clone, the records before the skills stop writing the ledger, the version token of a merge verdict before the third release, test 2 red until the third release). Proposes, decides nothing.
- **Origin:** written in Czech by a model in a session outside the forge, from the plan file; pasted into the conversation by the principal on 2026-10-17 and stored in English on his word.
- **Role:** the critique the plan was worked by hand against on 2026-10-17 (the principal's word).
- **Use for:** the reasons behind the fixture step, the tags before a migration and the order of the ledger and migration scripts.

### `cutover-challenge-review.md`
- **What:** a review of the architect's challenge of the cutover plan (`challenges/2026-10-17-challenge-architect-3.md`), a verdict and a way of mending for each of CHL.0370 to CHL.0430, all seven accepted: the first release built on a branch of the engine in a second tree made by hand, six to eight sittings; the fixture as two projects cloned from a bare remote by a script of the engine, skipped by a bare save through a flag of the project file; the engine's project migrated right after the two scripts; the driver, `/merge`, the worktree and the version as a boundary one release, four releases in all, the ID blocks on the trigger of a second author; the pass of three closings defined; the way back by tag said truthfully, the tag per project before its migration; the dependencies between releases marked. Answers the challenger's four questions. Proposes; the principal adopted it whole on 2026-10-17.
- **Origin:** written in Czech by a model in a session outside the forge, from the challenge report and the plan; pasted into the conversation by the principal on 2026-10-17 and stored in English on his word.
- **Role:** the review by which the seven challenges of the cutover plan were settled, intent 5.19, design 0.21, DEC.0220 and the plan reworked (the principal's word of 2026-10-17).
- **Use for:** the reasons behind the branch of the engine, the fixture script, the four releases and the trigger of the ID blocks.

### `cutover-challenge-review-2.md`
- **What:** a review of the architect's second challenge of the cutover plan (`challenges/2026-10-18-challenge-architect.md`), a verdict and a way of mending for each of CHL.0500 to CHL.0550, all six accepted: the next free number on a branch read over every local branch of the clone, the blocks per handle only between clones and authors, the trigger of the fourth release widened to a second clone of the same author, the one exception to "never renumbered" at a clash; the tests on the fixture alone, `forge-clone` with a target name, the guard of the fixture by name; the fixture carrying the old shape itself with a tag per shape; the conversion committing through forge-save, a sixth mark, the blame file; the Action for every other machine; a walkthrough over the origins of the engine's threads. Answers the challenger's four questions. In two pieces, the second three corrections of the first (the new number allocated over the branches, the thread file renamed at a clash, the test over the three kinds of records). Proposes; the principal adopted it whole on 2026-10-18.
- **Origin:** written in the conversation's language by a model in a session outside the forge, from the challenge report and the plan; pasted into the conversation by the principal on 2026-10-18 and stored in English on his word.
- **Role:** the review by which the six challenges of 2026-10-18 were settled, intent 5.22, design 0.23, DEC.0240, the specification 0.4 and the plan reworked (the principal's word of 2026-10-18).
- **Use for:** the reasons behind the allocation over local branches, the renumbering at a clash, the fixture with its own old shape and the path of a second machine.

### `cutover-challenge-review-3.md`
- **What:** the third piece of the review of the architect's second challenge of the cutover plan, four corrections after the write of the second piece: the trigger in the plan's introduction, R1.26 the engine's tag alone, a concrete shape number with its closing in the release rows, and the limit of the allocation over the local branches, which reads the committed state only, two windows before a save may clash, the remedy POS.0220.
- **Origin:** written in the conversation's language by a model in a session outside the forge; pasted into the conversation by the principal on 2026-10-18 and stored in English on his word.
- **Role:** the piece by which POS.1730 got its sentence on the committed state and the plan its corrections of 2026-10-18; the shape tag it corrects was dropped the same day by CHL.0610.
- **Use for:** the reason the allocation over branches is a rule with a known limit and not a guarantee.

### `projects/lib-allwyn/sources/fork-brd/` (library document, cited, not copied)
- **What:** the BRD layer built in a colleague's fork of the engine (intent 2.8, August 2026): the fork's rules, templates, skills and critic, three BRDs with three critique rounds, and the group's BRD standard and tutorial; the bundle's own index catalogues the fourteen files.
- **Origin:** the company library, registered there on 2026-10-13; kept out of this public project because it carries names, company content and the group's internal standard.
- **Role:** the material of the engine's own BRD artefact (`/new-artefact brd`, THR.0360, POS.0700): read for the research of the BRD layer and cited by path; nothing of it is copied into the engine.
- **Use for:** what the fork's BRD layer is and how it held; the group standard's rules; worked BRDs to judge a template by.
