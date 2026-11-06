---
project: <slug>
purpose: user-stories-export
audience: the stakeholders who approve the stories as a whole, the delivery that builds from them and the testers who test from them
version: 0.1
---

# Recipe — user-stories-export

<!-- User-stories-export-genre recipe, iterated via /recipe
user-stories-export. The rules: CLAUDE.md, Document chain,
Renders; the stories' own: .claude/skills/forge/states/user-stories.md.
-->

## Inputs
- 35-user-stories.md

## Instructions
- Reproduce the Template exactly: the two headings, the purpose line
  in italics, then the stories one after another; no table.
- One story after another, in the order of the input; group headings
  of the input are not carried.
- Each story: the level-3 heading `### US.NNNN — <name>`, a blank
  line, the sentence on a line of its own, the acceptance criteria
  as `- ` items directly below it; then only the parts the story
  has, each after a blank line, its bold label on a line of its own
  (`**Edge cases:**`, `**Risks:**`, `**Note:**`, `**Questions:**`)
  with its items below it, and last `**Reference:**` with its IDs on
  the same line.
- No line is hard-wrapped: every sentence, item and label stands on
  one line, whatever its length — an exception to the wrapping of
  CLAUDE.md, Document kinds, since the export is pasted into a wiki
  or a tracker that may break a wrapped line where it stands.
- Reference: carry BR, NFR, UC and DEP IDs; leave out every POS,
  since the stakeholders never see the intent; a story whose
  Reference holds only POS has no Reference part in the export.
- Questions keep their numbering and `→ <owner>`; nothing of a story
  is reworded, shortened or added.
- No front-matter of the input, no history, no template comment.

## Template

# User stories

## <Section heading>

*<Purpose line>*

### US.NNNN — <name>

<sentence>
- <criterion>
- <criterion>

**Edge cases:**
- <situation> → <what happens>

**Risks:**
- <risk> → <mitigation | consequences>

**Note:**
- <what lies behind the link> – <link>

**Questions:**
1. <question> → <owner>

**Reference:** <BR.NNNN, NFR.NNNN, UC.NNNN, DEP.NNNN>
