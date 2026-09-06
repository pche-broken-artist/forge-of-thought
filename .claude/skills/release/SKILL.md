---
description: Release one repository from main — full check with walkthrough, README and release notes, then /save with the release message and the tag at an approved major
argument-hint: '[project-slug] [-m "message"] [-Tag name]'
disable-model-invocation: true
---

Release one repository from `main` (POS.1100): the full conformance
check settled by walkthrough (POS.0570), the README and the release
notes regenerated from the settled sources under the principal's eyes
(POS.0810, POS.1000), and then `/save` (`.claude/skills/save/SKILL.md`)
with the release message and, at an approved major, the tag. The
repository is named by its slug, `forge` meaning the engine; without
a slug, ask which repository — a release is always one repository,
never a sweep.

1. Determine the state from `./scripts/forge-status.ps1` (the scripts
   are the only door to git — CLAUDE.md, Persistence). A release runs
   on `main` only: on any other
   branch, stop and report the branch the repository is on and how to
   get back (`./scripts/forge-branch.ps1 <slug> main`, after saving).
   Merging a branch into `main` is git's business, by hand or by
   merge request, never this command's (POS.1110).
2. Run the checks over the sources through the `/check` procedure
   (`.claude/skills/check/SKILL.md`) and report the result to the
   principal — always, even when clean. A project: `light` and
   `project`. The engine: `light`, `engine` and `project`, the two
   project checks on `projects/forge`. Launched at once, awaited
   together. Clean: state that the checks passed.
   Findings: settle them by walkthrough (CLAUDE.md, Working methods);
   a finding may be deferred, as the `/check` procedure says, and the
   release proceeds. Never fix silently; never proceed with an unsettled
   finding. The check runs before the renders so that a fix of the
   walkthrough — an intent bump, a changed convention — is already in
   the inputs the renders derive from (POS.0570).
3. Offer `/critique essence` once, in one sentence: the lens that
   guards what a release publishes, the drift of the chain
   (POS.0400). On the principal's word run it through its own
   definition (`.claude/skills/critique/SKILL.md`) and settle its
   findings by walkthrough before going on; on his no, or silence,
   run nothing — no reviewer ever runs at a release on Claude's own
   judgement.
4. Only once the findings are settled, regenerate the repository's
   README and release notes from their recipes — unconditionally, no
   staleness test, always through the `/render` procedure
   (`.claude/skills/render/SKILL.md`), never through an ad-hoc subagent
   prompt (POS.1070). The two renders are launched at once, each
   through the `/render` procedure, and awaited together. Report the
   steps, including a short summary of what materially changed in the
   regenerated files (POS.0810, POS.1000): the principal rules on the
   delta before the commit. A render made from the settled sources is
   current by construction; its verification is `/render` step 6 (the
   file, its provenance, the ledger), not a check. Which renders a
   repository has is CLAUDE.md, Document chain 7's. A project whose
   recipe is missing is reported (a `/check` finding)
   and released without the render. Other renders are never
   regenerated here; their staleness is the principal's business,
   shown by the `/forge` map (POS.0570).
5. Then run `/save` for this repository through its own definition
   (`.claude/skills/save/SKILL.md`), with two things decided here: the
   commit message is `release <intent version>: <one line>` — the
   line summarising the rounds since the last release, from the rows
   of the intent's `.history.md` companion, the primary record
   (CLAUDE.md, Versioning & status), unless `-m` was supplied; for a
   library, whose history is git, the version is omitted and the line
   describes what changed — and, when the intent's version is an
   integer (an approved major), the tag `v<major>`, proposed and
   taken on the principal's word (a rule of the procedure, not a gate
   in the script). Any other tag is his request, as `/save` has it.

The check is advisory (POS.0430): the principal may order the release
at any moment regardless of findings.
