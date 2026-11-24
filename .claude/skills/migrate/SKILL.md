---
description: Bring a project to the shape of a release that changed the shape of files — a dry run first, the migration on the principal's word, the threads' origins judged, then /save
argument-hint: "[project-slug] [--comments | --blocker]"
---

The door to `scripts/forge-migrate.py` (SOL.0800, POS.1740): the
script does every deterministic step and is described in full by its
help header; this command adds what needs judgement and runs
nothing without the principal's word. A migration runs once per
project, on one clone, on `main`; everyone else pulls (the
refusals and the way back are the script's).

1. Infer the project from context (`$0` may be a slug; `forge` is the
   forge's own project, a repository of its own beside the engine,
   POS.1980; if ambiguous, ask). Run the dry run,
   `python scripts/forge-migrate.py <slug>`, and show its print as
   it came: the marks of the shape, the steps that would run and
   what each would change. A project already in shape ends here.
2. On the principal's word, and only then, run
   `python scripts/forge-migrate.py <slug> --apply`. The script
   commits nothing.
3. Judge what the script printed for the principal: the origins it
   guessed for the threads it cut (`threads/THR.NNNN.md`, the field
   `origin`), the text after the last thread that was not a thread,
   the Waiting lines without an ID. The origins are a walkthrough
   (CLAUDE.md, Working methods): one table of Claude's judgement from
   the texts, the principal correcting what is wrong, written into
   the thread files at the round's end; what is not a thread goes
   where it belongs, usually a record of the intent's history.
4. Make the ledger, `python scripts/forge-ledger.py <slug>`, and
   propose `/save <slug>`; the migrated shape reaches the remote by
   that save. Should anything be wrong, the way back is the
   script's, as its header says; the tag before the migration is
   POS.1740's, taken through `/save <slug> --tag <name>` before
   `--apply`.

**`/migrate <slug> --comments` — the comments of the skeletons.** A
step of its own, on the owner's word and never a condition of a
write (POS.2030, SOL.0970): the script's `--comments` replaces, in
every file made from a template that is not immutable, the skeleton's
comment by the line that names the skeleton. The course is the same:
the dry run shown as it came, `--comments --apply` on the principal's
word, what the script printed for him judged, a recipe whose genre
the file does not tell and a comment of a file's own above all, then
the ledger and `/save <slug>`.

**`/migrate <slug> --blocker` — the mark of blocking.** A step of its
own of the same kind, on the owner's word and never a condition of a
write (POS.2040, SOL.0980): the script's `--blocker` brings a TBC
that says whether it blocks in the wording before to the one mark in
its brackets. The course is the same: the dry run shown as it came,
`--blocker --apply` on the principal's word, then the items the
script printed and left, each put to the principal with the wording
Claude would give it and written on his word, then the ledger and
`/save <slug>`.
