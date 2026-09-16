---
name: check-<name>
description: Check "<name>" — <what this check verifies, in one line>. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.
tools: Read, Glob, Grep
model: inherit
skills:
  - check-contract
---

<!-- Skeleton of a check file (.claude/agents/check-<name>.md):
front-matter and Lens section, nothing else; shared behaviour is the
contract skill named above (CLAUDE.md, Isolated reviewers). The
description says what the check verifies and when it fits. Delete
this comment in the check file. -->

## Lens

<!-- The check's own section. Three parts:
1. What you read — a project, every project, or the engine; how the
   target narrows it; what a library reduces it to.
2. What you verify — the rules, each with its owner (CLAUDE.md
   section, template, position) cited and never restated; what is a
   fact rather than a finding.
3. Cost — the scope you read: named files, or the whole, honestly. -->
