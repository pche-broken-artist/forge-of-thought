---
description: Work the document chain — bare = state map, with a target = iterate that artefact
argument-hint: "[target-state] [project-slug]"
---

Role: dispatcher for work on the document chain. The chain is a star,
not a fixed line: each target state declares its own inputs in its
definition file; where the definitions live and how the chain grows
is CLAUDE.md, Document chain's. This dispatcher never changes.

**Bare `/forge` — report the map.**
1. Infer the current project from context ($0 may be a slug; if
   ambiguous, ask).
2. Read the project's ledger and list `.claude/skills/forge/states/` for the
   available target states.
3. Report compactly:
   - the project's kind (ledger header, POS.0960) and whether it is
     under git — `projects/<slug>/.git` present or "not under git",
     stated as a fact, never as a defect (CLAUDE.md, Persistence);
   - a `library` is material, not a project waiting for a brief:
     report its sources and research (from the ledger and the
     indexes) and stop after the git line — no chain, no target
     states, no next step beyond `/ingest`;
   - which chain artefacts exist, at what version and status —
     briefs with their mining state, a draft brief or a `pending` /
     `partial` one named as work waiting; a layer the project does
     not have is not reported as missing (CLAUDE.md, Ledger);
   - which target states can be worked on from here (inputs exist) and
     which cannot yet (say what is missing);
   - which renders are stale (as `/render` step 5 defines it) and
     which published files are (state `stale` in the ledger's
     Published table);
   - which libraries the project needs (the ledger's Dependencies
     table, POS.1020) and whether each is cloned alongside;
   - what is waiting on the principal (from the ledger): the few live
     matters named in words, the ID in brackets as an address, the
     rest as a count (CLAUDE.md, Working methods, Plain speech).
4. Recommend the natural next step in words — a recommendation, never a
   gate — and, where the map lists more than one matter waiting on
   the principal, offer a walkthrough of them (CLAUDE.md, Working
   methods).

**`/forge <state>` — work on that artefact.**
1. Resolve `.claude/skills/forge/states/$0.md`. If it does not exist, list
   the states that do and stop.
2. Read the file and follow it. It declares the target artefact, its
   inputs and its working rules; everything else (write-once-per-round,
   versioning, ledger upkeep) follows the core conventions. A state
   file's arguments are those following the state name: for `brief`
   the name, then the slug; for the other states the slug.
