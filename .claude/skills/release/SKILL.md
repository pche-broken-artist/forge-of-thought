---
description: Release one repository from main — its checks with walkthrough, the documentation, README and release notes, then /save with the release message and the tag at an approved major; --auto runs through and stops only at a serious thing
argument-hint: '[project-slug] [-m "message"] [--tag name] [--auto]'
disable-model-invocation: true
---

Release one repository from `main` (POS.1100): the checks POS.1140
composes, settled by walkthrough (POS.0570), the documentation, the
README and the release notes regenerated from the settled sources
under the principal's eyes (POS.0810, POS.1000), and then `/save`
(`.claude/skills/save/SKILL.md`) with the release message and, at an
approved major, the tag. The repository is named by its slug, `forge`
meaning the engine; without a slug, ask which repository — a release
is always one repository, never a sweep. The order is the position's:
checks, documentation, README and release notes, state render, save;
the README reads the documentation's index, so the documentation
comes first.

`--auto` runs the whole release through (POS.1100): the checks and
their agents, the documentation, the renders and the save with the
drafted message, no step put to the principal but the one question of
the documentation (step 4), the model and the size of every run of
agents said as information. It stops only where a
thing is serious, as each step below says, and always at the tag of
a major. Nothing is parked on the principal's behalf: what `--auto`
cannot settle stays open, and the release waits for his word.

1. Determine the state from `python scripts/forge-status.py --remote`
   (the forge reads state by its script — CLAUDE.md, Persistence). A
   release runs on `main` only: on any other branch, stop and report the
   branch the repository is on and how to get back
   (`python scripts/forge-branch.py <slug> main`, after saving). A
   repository behind or diverged from its origin is refused with the
   offer of `/pull` (CLAUDE.md, Persistence): the renders a release
   makes are taken as `ours` at a merge, and that turns round in the
   rebase of the save (POS.1710, SOL.0530). Merging a branch into `main`
   is git's business, by hand or by merge request, never this command's
   (POS.1110). `--auto` stops here as any release does.
2. Run the checks over the sources through the `/check` procedure
   (`.claude/skills/check/SKILL.md`) and report the result to the
   principal — always, even when clean. A project: `light` and
   `project` on it. The engine: `engine` on the engine root, and
   `light` and `project` on `projects/forge`, the forge's own
   project. Launched at once, awaited together. Clean: state that
   the checks passed.
   Findings: settle them by walkthrough (CLAUDE.md, Working methods);
   a finding may be parked, as the `/check` procedure says, and the
   release proceeds. Never fix silently; a finding the principal has
   not settled when he orders the release to go on is parked by that
   word, said aloud, since the check is advisory (POS.0430). The check
   runs before the renders so that a fix of the
   walkthrough — an intent bump, a changed convention — is already in
   the inputs the renders derive from (POS.0570).
   With `--auto`, a finding whose fix lies in the operating layer or
   in bookkeeping and changes no position and no rule's meaning is
   fixed and recorded by Claude without a walkthrough, as an
   immediate fix is today; a finding of severity high, one whose fix
   would change a position or a rule's meaning, or one the report
   calls a decision, stops the release and is put to the principal.
   Nothing is parked on his behalf.
3. Offer `/critique essence` once, in one sentence: the lens that
   guards what a release publishes, the drift of the chain
   (POS.0400). On the principal's word run it through its own
   definition (`.claude/skills/critique/SKILL.md`) and settle its
   findings by walkthrough before going on; on his no, or silence,
   run nothing — no reviewer ever runs at a release on Claude's own
   judgement. With `--auto` the lens is neither offered nor run.
4. Report the age of the documentation: the `version` in the
   front-matter of the repository's `docs/README.md` against the
   intent's version (a repository without `docs/` has none, and that
   is no finding), and offer `/document` in one sentence. On the
   principal's word run it through its own definition
   (`.claude/skills/document/SKILL.md`) before the renders, so that
   the release carries current pages and the README reads the
   current index; on his no, or silence, run nothing. A release by
   hand never regenerates the documentation on its own (POS.1450);
   with `--auto` the release asks once, before anything runs, whether
   the documentation runs, the default yes, and on yes runs it as a
   part of the release, the models and the number of pages said
   before the writers are launched.
5. Only once the findings are settled and the documentation stands,
   regenerate the repository's README and release notes from their
   recipes — unconditionally, no staleness test, always through the
   `/render` procedure (`.claude/skills/render/SKILL.md`), never
   through an ad-hoc subagent prompt (POS.1070). The two renders are
   launched at once, each through the `/render` procedure, and
   awaited together. Report the steps, including a short summary of
   what materially changed in the regenerated files (POS.0810,
   POS.1000): the principal rules on the delta before the commit. A
   render made from the settled sources is current by construction;
   its verification is `/render` step 6 (the file, its provenance),
   not a check. Which renders a repository has is CLAUDE.md, Document
   chain, Renders's. A project whose recipe is missing is reported (a
   `/check` finding) and released without the render. Other renders
   are never regenerated here; their staleness is the principal's
   business, shown by the `/forge` map (POS.0570). Then the state
   render: `python scripts/forge-ledger.py <slug> --out
   renders/state.md` (for the engine `projects/forge/renders/state.md`),
   the ledger as a tracked render, made only on main, so that the
   state is on the remote where it is wanted (POS.1650); the Renders
   table does not list it, it being the ledger itself.
   With `--auto` the regenerated files are taken as they came, no
   delta put to the principal; the one stop is a hit of the scan
   (`/render` step 6) that the released version did not already
   carry. A hit the released version carried stands as before.
6. Then run `/save --quick` for this repository through its own
   definition (`.claude/skills/save/SKILL.md`): without the `light`
   check, which step 2 ran already and which nothing made since
   reads, with two things decided here: the commit message is
   `release <intent version>: <one line>` — the line summarising the
   rounds since the last release, from the records of the intent's
   history since the last release, and the rows of its archive where
   the span reaches before the log, the primary record (CLAUDE.md,
   Versioning & status), unless `-m` was supplied; for a library,
   whose history is git, the version is omitted and the line
   describes what changed — and, when the intent's version is an
   integer (an approved major), the tag `v<major>`, proposed and
   taken on the principal's word (a rule of the procedure, not a gate
   in the script). Before proposing the tag of a major of the forge
   intent, name what POS.0300 of that intent asks a major to pass —
   a reminder on the principal's word, never a gate. Any other tag is
   his request, as `/save` has it. With `--auto` the drafted message
   is used without confirmation, as a message given with `-m` is, and
   said aloud in the report; the tag of a major is never taken by
   `--auto`: the release stops before it and asks.

The check is advisory (POS.0430): the principal may order the release
at any moment regardless of findings, and the findings he has not
settled are parked by that word (step 2).
