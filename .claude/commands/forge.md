---
description: Work the document chain — bare = state map, with a target = iterate that artefact
argument-hint: [target-state] [project-slug]
---

Role: dispatcher for work on the document chain. The chain is a star,
not a fixed line: each target state declares its own inputs in its
definition file. Definitions live in `.claude/commands/forge/<state>.md`
— one file per target state, named after the artefact it produces.
Adding a layer means adding a file; this dispatcher never changes.

**Bare `/forge` — report the map.**
1. Infer the current project from context ($1 may be a slug; if
   ambiguous, ask).
2. Read the project's ledger and list `.claude/commands/forge/` for the
   available target states.
3. Report in Czech, compactly:
   - the project's kind (ledger header, POS.0960) and whether it is
     under git — `projects/<slug>/.git` present or "not under git",
     stated as a fact, never as a defect;
   - a `library` is material, not a project waiting for a brief:
     report its sources and research (from the ledger and the
     indexes) and stop after the git line — no chain, no target
     states, no next step beyond `/ingest`;
   - which chain artefacts exist, at what version and status —
     briefs with their mining state, a draft brief or a `pending` /
     `partial` one named as work waiting;
   - which target states can be worked on from here (inputs exist) and
     which cannot yet (say what is missing);
   - which renders are stale — compare each render's front-matter
     provenance (recipe and input versions) against the current files;
   - what is waiting on the principal (from the ledger).
4. Recommend the natural next step — a recommendation, never a gate.

**`/forge <state>` — work on that artefact.**
1. Resolve `.claude/commands/forge/$1.md`. If it does not exist, list
   the states that do and stop.
2. Read the file and follow it. It declares the target artefact, its
   inputs and its working rules; everything else (write-once-per-round,
   versioning, ledger upkeep) follows the core conventions.
