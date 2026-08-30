---
description: Save the forge to git with the pre-save conformance check and render refresh
argument-hint: [project-slug] [-m "message"]
---

Save the forge to git with the pre-save conformance check
(POS.0570). The engine and every project are repositories of their
own (POS.0940): bare, `scripts/forge-save.ps1` gives each repository
with changes its own commit and pushes where an origin exists; a
project slug limits the save to that repository (`forge` = the
engine); `-m "message"` sets the commit message. A project without
a repository is skipped with a note — say so in the report, it is a
property, not a defect. Arguments are passed through to the script.

1. Determine scope from `./scripts/forge-status.ps1` — never from
   direct git commands; the scripts are the only door to git, for
   reading state too. It reports the engine and each project
   separately. Engine files touched → run the `/check-forge`
   procedure; project files touched → run `/check` for each affected
   project; both → both. A project "not under git" with changes is
   named in the report and otherwise left alone.
2. If the scope includes the core or `projects/forge/`, first
   regenerate `README.md` by the `/render readme` procedure and
   `RELEASE-NOTES.md` by the `/render release-notes` procedure
   (released sections carried over verbatim, only the Unreleased
   head recomposed) — unconditionally, no staleness test — and
   report the steps, including a short summary of what materially
   changed in the regenerated files (POS.0810): the principal rules
   on the delta as part of the pre-save report. Other renders are
   never regenerated here; they surface as ordinary check findings.
3. Report the result to the principal — always, even when clean.
4. Clean check: state that the check passed and run the script.
5. Findings: go through them with the principal iteratively — each
   finding is either resolved together (fix agreed, then applied) or
   explicitly accepted by the principal; acceptance may be a
   deferral, recorded in the affected project's ledger under
   "Waiting on principal". Never fix silently; never proceed with an
   unsettled finding.
6. Unless `-m` was supplied, draft a one-line English commit message
   summarising the round and propose it to the principal; commit
   with the confirmed or adjusted wording. When more than one
   repository has changes, one message per repository is drafted, or
   the save is run per slug. The script's auto-generated file list is
   used only if the principal says so.
7. Only then run `./scripts/forge-save.ps1 [slug] [-m "message"]`
   and report the outcome — the script itself prints the commit's
   file summary; no direct git verification afterwards.

The check is advisory (POS.0430): the principal may order the save
at any moment regardless of findings.
