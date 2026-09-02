---
date: YYYY-MM-DD
project: <slug>
reviewed: 20-assignment.md vX.Y, 10-intent.md vX.Y
reviewer: critic subagent (isolated context)
---

# Critique — YYYY-MM-DD

<!-- Immutable once written. One file per run. The critic sees artefacts
only, never the drafting conversation. All findings are advisory; the
principal decides. Update ledger.md in the same run. -->

## Delta summary
- **New:** FND.00xx, …
- **Verified resolved:** FND.00xx, …          <!-- regression-checked -->
- **Still open:** FND.00xx, …
- **Newly obsolete:** FND.00xx, …

## Findings
<!-- Severity and category as the critic agent defines them
(.claude/agents/critic.md) — not restated here (POS.1070). -->

### FND.00xx [severity] [category]
- **Location:** <section / item ID>
- **Issue:** …
- **Why it matters:** …
- **Suggested fix:** …

## Recommendations
<!-- Not findings, not gates: wording that is hard to test, groups that
overlap, items that could be split. The principal may ignore these
without recording anything. -->
- …

## Advisory checklist
<!-- Answer yes / no / delegated / n-a with one line each. -->
- Objective outcome-phrased and unambiguous?
- Scope boundaries stated, with out-of-scope items where the topic invites
  creep?
- Requirements written as shall / shall not, one idea each, no duplicates?
- Constraints separated from requirements (no leaked solutioning)?
- Deliverables actionable, with owners and timing where relevant?
- Open questions each have an owner?
- Success criteria present, or explicitly delegated, or deliberately
  absent?
- Assignment carries the full in-scope substance of the intent — no
  silent omissions (explicit DEL/TBC delegation is fine); detail is of
  the assigning kind, not the solving kind?
- Assignment consistent with the current intent (no divergence)?
- Terms section present and matching what the document actually uses?
- Any item that cannot be understood without an external link?
