---
description: Report project state from the ledger
argument-hint: [project-slug]
---

Read the ledger of project $1 (or all projects if none given) and report
in Czech, compactly:

1. Documents: file, version, status, date.
3. Sources and research: files present in `sources/` or `research/`
   but not registered in the ledger are reported as "waiting for
   /ingest" (or /research bookkeeping); registered files without an
   entry in the directory's `00-INDEX.md` are listed too.
4. Findings: open by severity; awaiting the principal's verdict.
5. Open questions owned by the principal (from 20-assignment.md and intent
   Open threads).
6. Recommended next step (one line — e.g. "intent stable, worth running
   /forge assignment" or "3 findings await verdicts").

If the ledger disagrees with reality (versions in front-matter, files on
disk), report the discrepancy and offer to fix the ledger. Read-only
otherwise.
