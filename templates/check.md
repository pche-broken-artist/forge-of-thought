---
name: check-<name>
description: Check "<name>" — <what this check verifies, in one line>. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.
tools: Read, Glob, Grep
model: inherit
skills:
  - check-contract
---

<!-- Skeleton of a check file (.claude/agents/check-<name>.md). A
check file carries its front-matter and its Lens section, nothing
else: the behaviour shared by every check — subject, way of working,
report shape — is the contract skill .claude/skills/check-contract/SKILL.md,
preloaded through the skills field above and never restated here
(POS.0540, POS.1140). /check engine verifies that the named skill
exists. A new check is created only by the principal's decision, and
only where what it verifies genuinely differs from the existing
checks; a rule verified by two checks is a defect. Delete this comment
in the check file. -->

## Lens

<!-- The check's own section. Three parts:
1. What you read — a project, every project, or the engine; how the
   target narrows it; what a library reduces it to.
2. What you verify — the rules, each with its owner (CLAUDE.md
   section, template, position) cited and never restated; what is a
   fact rather than a finding.
3. Cost — the scope you read: named files, or the whole, honestly. -->
