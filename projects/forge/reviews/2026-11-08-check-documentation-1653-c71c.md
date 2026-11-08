---
date: 2026-11-08
project: forge
check: documentation
target: the engine (C:\pche\_dev\forge-of-thought), the documentation run of 2026-11-08
reviewer: the documentation run
---

# Check (documentation) — the engine — 2026-11-08

15 findings

What the documentation run of 2026-11-08 could not place: the planner's Unowned facts and the matters where the map and its owner disagree, the claims the map asked for and no input carried, and every place where a page wanted a reason and no file records one. Filed by the run itself (POS.1450), gathered from the writers' hand-backs; a matter already filed by the run of 2026-11-01 is named by its ID and not filed twice. A mend lands in the owner, never on a page.

## Findings

### FND.3920 — medium — The position on the harness says web access is approved by the user per domain; `.claude/settings.json` records no such rule
- **Where:** projects/forge/10-intent.md, POS.1090 ("approved by the user per domain"); .claude/settings.json carries two hooks and the deny rules of the other shell and of two sensitive paths, nothing on web access. The page `docs/about/how-the-rules-are-held.md` says nothing of it, since a derived page claims nothing its inputs do not carry.
- **Rule:** Every position honoured in the core, nothing advertised that the operating layer does not hold (CLAUDE.md, Isolated reviewers: the engine check's concern; prime directive 10).
- **Fix:** Either the settings carry the rule, or POS.1090 says that web access is the harness's own permission and not a rule of the forge's settings.

### FND.3930 — medium — The CONTRIBUTING recipe names `docs/extend/change-a-documentation-page.md` for a fix of a page; the map entry of `docs/extend/how-a-change-is-made.md` does not link it
- **Where:** projects/forge/recipes/contributing.md (the fix of a page); projects/forge/docs-map.md, entry of `docs/extend/how-a-change-is-made.md`, its `links`. The page links Generate the documentation instead and says a fix goes into the file the page mirrors.
- **Rule:** A page links the pages its owner points at; the planner's entry follows the owner (POS.1450).
- **Fix:** Add the link to the entry at the next run; nothing to mend in the owner.

### FND.3940 — medium — Five terms of the glossary are defined from use, no owner defines them in one sentence
- **Where:** docs/reference/glossary.md: "session", "harness", "isolation", "format file", "engine (the forge's)"; the writer drew each from its uses in CLAUDE.md (Persistence, Isolated reviewers, the hooks, the /end skill) and the intent (POS.1090, POS.1540), no input defining it in one place.
- **Rule:** A glossary line cites the file that defines the term (the entry's shape); a fact without an owner waits for the principal to give it a home (the documentation command, step 7).
- **Fix:** Give each term one defining sentence in its owner, or accept the definition from use as the glossary's own and say so in the entry.

### FND.3950 — medium — The export's layout is asked of `docs/about/the-user-stories.md` and its skeleton is not among the entry's inputs
- **Where:** projects/forge/docs-map.md, entry of `docs/about/the-user-stories.md`: the `says` asks for the shape of the export, the inputs name the genre file, POS.1990 and SOL.0920 and not `templates/recipe-user-stories-export.md`; the page shows only what the named inputs give and names the skeleton in backticks for the rest.
- **Rule:** A derived page claims nothing its inputs do not carry; an entry names every input a page needs (POS.1450).
- **Fix:** Add the skeleton to the entry's inputs at the next run.

### FND.3960 — low — Reason not recorded: why the security policy promises exactly what it promises, and why a public issue is never the channel
- **Where:** docs/about/the-security-policy-and-the-code-of-conduct.md, under Why; the owner POS.1920 states the promises (an answer within days, credit, no bounty, no safe harbour) and the private channel, with no reason for either.
- **Rule:** A page says "the reason is not recorded" where it wants one and none is in the owner (the documentation contract); the reason belongs in the record of the position.
- **Fix:** The principal gives the reasons; they go into the record of POS.1920 or the position itself.

### FND.3970 — low — Reason not recorded: why `/setup` is not elicitation, and why a Map is neither a questionnaire nor a list of criteria
- **Where:** docs/about/elicitation.md, under Why; the intent's Elicitation group lists `/setup` outside elicitation without a reason, and gives for the Map only that it stands before the template.
- **Rule:** As FND.3960.
- **Fix:** The principal gives the reasons; they go into the records of the positions.

### FND.3980 — low — Reason not recorded: why the solution design is read without the principal in the room
- **Where:** docs/about/the-solution-design.md, under Why; POS.1400 to POS.1420 state the audience and give no reason.
- **Rule:** As FND.3960.
- **Fix:** The principal gives the reason; it goes into the record of the position.

### FND.3990 — low — Reason not recorded: why the three readers of the documentation stand in that order of weight, and why the run asks nothing
- **Where:** docs/about/the-documentation.md, under Why; POS.1450 states both rules and gives no reason.
- **Rule:** As FND.3960.
- **Fix:** The principal gives the reasons; they go into the record of POS.1450.

### FND.4000 — low — Reason not recorded: why `Reference` is the one part every story has, and why the stakeholders' approval of the stories is an act of the instance
- **Where:** docs/about/the-user-stories.md, under Why; POS.1990 to POS.2020 state both rules and give no reason beyond the trail to the parent.
- **Rule:** As FND.3960.
- **Fix:** The principal gives the reasons; they go into the records of the positions.

### FND.4010 — low — Reason not recorded: why two windows of one person on one project are left to git rather than solved
- **Where:** docs/about/working-together.md, under How it works and Why; POS.1560 states the direction and gives no reason.
- **Rule:** As FND.3960.
- **Fix:** The principal gives the reason; it goes into the record of the position.

### FND.4020 — low — Reason not recorded: why a commit carries no attribution line
- **Where:** docs/about/persistence-in-git.md, under Why; POS.1200 states the rule and gives no reason.
- **Rule:** As FND.3960.
- **Fix:** The principal gives the reason; it goes into the record of POS.1200.

### FND.4030 — low — Reason not recorded: why a project under git is recognised by asking git for the top of its repository rather than by a `.git` directory looked for
- **Where:** docs/about/projects-and-the-engine.md, under Why; CLAUDE.md, Persistence, and POS.0550 state the rule and why the repository above is asked nothing, not why git is asked instead of the file system.
- **Rule:** As FND.3960.
- **Fix:** The principal gives the reason; it goes into the record of POS.0550.

### FND.4040 — low — Reason not recorded: why the forge runs in Claude Code rather than elsewhere
- **Where:** docs/start/what-it-is.md, under Why; CLAUDE.md, What this workspace is, states it as a fact.
- **Rule:** As FND.3960.
- **Fix:** The principal gives the reason; it goes into the record of the position on the harness.

### FND.4050 — low — Reason not recorded: why the hand-kept ledger of a migrated project is kept immutable as an archive rather than rewritten
- **Where:** docs/about/the-ledger.md, under Why; POS.1600 and the migration state the rule and give no reason.
- **Rule:** As FND.3960.
- **Fix:** The principal gives the reason; it goes into the record of POS.1600.

### FND.4060 — low — Two words of POS.1680 the page could not render: "today's bracket" beside `concerns`, and "the driver" of the intent file
- **Where:** projects/forge/10-intent.md, POS.1680 (the third reason for threads as files); docs/about/the-intent.md renders "the driver" as "whatever drives the intent file" and leaves "today's bracket" out.
- **Rule:** A page carries a claim in the owner's words only where the words carry a meaning the inputs give (the documentation contract).
- **Fix:** Say in POS.1680 what the driver is and what the bracket beside `concerns` means, or drop the two words.

## Facts
- Already filed, not filed again, named here so that the next planner has this run's instances: FND.3580 (parked under DEC.0390; the planner's Unowned 1, how a merge request's branch is fetched onto the integrator's clone, needed by `docs/about/working-together.md` and `docs/use/settle-a-conflict.md`); FND.3400 (open; the planner's Unowned 2, why a project records no engine version, needed by `docs/about/upgrades-and-migration.md`); FND.3610 (parked under DEC.0380; claims the map asked for and no named input carries: this run `docs/about/the-brief.md` "since the mining changes the intent and not the brief", `docs/about/renders-and-recipes.md` the definition of stale, `docs/about/where-it-is-going.md` "one principal per instance for now", `docs/about/projects-and-the-engine.md` "seamless work inside", `docs/about/working-methods.md` the reason for intent-first, `docs/start/what-it-is.md` "real sessions cut to a few minutes" and "by interview", `docs/start/first-result.md` one question per message and the word `write`, `docs/start/install.md` the GitHub line in the state map (the /forge skill carries it and is not an input), `docs/about/how-a-thought-travels.md` the definition of the check kind, `docs/about/persistence-in-git.md` the ledger never in git, `docs/extend/add-a-script.md` the six parts of a docstring, `docs/use/design-the-solution.md` the persona `architect`, `docs/use/run-the-tests.md` what a release and a save do with the tests, `docs/about/the-document-chain.md` `/new-artefact`, `docs/extend/add-an-engine.md` the trial command line and the check of the research skill's opening sentence, `docs/extend/what-it-is-made-of.md` the loading moment of the documentation contract); FND.3630 (parked under DEC.0380; roster columns no owner states: "when it fits" on the personas and lenses pages, the command that runs a script, the creating command of a template).
- Reasons wanted again and already open: FND.3180 (why a brief keeps its language; `docs/about/the-brief.md`, `docs/about/languages.md`), FND.3190 (why "mandate" was rejected; `docs/about/the-assignment.md`), FND.3240 (intent-first, the chain never spanning two principals; `docs/about/the-document-chain.md`, `docs/about/where-it-is-going.md`), FND.3340 (the stakeholders' sign-off; `docs/about/the-brd.md`), FND.3360 (the principal's own files; `docs/about/renders-and-recipes.md`), FND.3370 (the design citing by ID and naming by path; `docs/about/the-solution-design.md`), FND.3380 (five prime directives; `docs/about/the-principal-and-claude.md`), FND.3390 (six rules of a research; `docs/about/the-research.md`), FND.3440 (`docs/about/where-it-is-going.md`), FND.3690 (the numbering rules; `docs/reference/id-scheme.md`), FND.3740 (propose never decide, recommend do not push; `docs/about/working-methods.md`), FND.3790 (the library of the instance; `docs/about/the-brd.md`), FND.3800 (the door to git as a wall; `docs/about/persistence-in-git.md`).
- The run: 106 entries, 5 new, 78 regenerated, 23 kept, 0 removed; the check failed 11 times on 5 pages at the first pass (long dashes copied from description lines and from the ledger template's empty cell; one language of the instance named beside a rejected name), each page regenerated once with the failure named, the second pass clean: 107 files checked, no failure.
