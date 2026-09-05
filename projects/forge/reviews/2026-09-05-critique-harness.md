---
date: 2026-09-05
project: forge
lens: harness
target: the operating layer `.claude/` (commands and agents) — the
  handover artefact of this project (ledger, Documents)
reviewed: .claude/commands/*.md (15), .claude/commands/forge/*.md (3),
  .claude/commands/recipe/*.md (3), .claude/agents/*.md (3),
  templates/critic.md, templates/challenger.md, .claude/settings.json,
  .claude/settings.local.json; for context: CLAUDE.md
reviewer: agent `skill-reviewer` of the plugin `plugin-dev`
  (marketplace `claude-plugins-official`, Anthropic), run in an
  isolated context on an ad-hoc prompt — not a lens of the roster.
  First trial of an external agent as a lens (THR.0290); the report
  was recast into the critic's shape by Claude in the session, the
  substance of every finding unchanged. The lens name `harness` is
  the principal's choice of 2026-09-05.
---

# Critique (harness) — 2026-09-05

## Delta summary
- **New:** FND.0190, FND.0200, FND.0210, FND.0220, FND.0230, FND.0240,
  FND.0250, FND.0260, FND.0270, FND.0280
- **Verified resolved:** — (no earlier run of this lens; regression
  not tested)
- **Still open:** —
- **Newly obsolete:** —

## Scope note
The reviewer read the operating layer against current Claude Code
practice for skills, commands and agents: front-matter completeness,
description quality and triggering, progressive disclosure, writing
style, duplication, argument handling, the choice of
`.claude/commands/` against `.claude/skills/<name>/SKILL.md`, and the
shared reviewer text. It was told the layer is not a plugin and that
CLAUDE.md is its constitution. Overall verdict: no hard conformance
issue against the documented format — every front-matter field used
(`description`, `argument-hint`, `name`, `tools`, `model`) is valid
for its file type, agent names match filenames, no required field is
missing. The problems are structural, not textual. Where the reviewer
relies on a front-matter field it could not verify against the
installed version (`skills:` on agents, `context: fork` with
`agent:`, `user-invocable`), the finding says so.

## Findings

### FND.0190 [high] [inconsistency]
- **Location:** `.claude/commands/forge/brief.md`, `forge/intent.md`,
  `forge/assignment.md`, `.claude/commands/recipe/presentation.md`,
  `recipe/readme.md`, `recipe/release-notes.md`; dispatchers
  `.claude/commands/forge.md`, `recipe.md`
- **Issue:** Claude Code registers every `.md` under
  `.claude/commands/`, subdirectories included, as a command with the
  directory as namespace. The layer therefore exposes 21 commands,
  not 15: `/forge:brief`, `/forge:intent`, `/forge:assignment`,
  `/recipe:presentation`, `/recipe:readme`, `/recipe:release-notes`
  appear in the `/` menu and in the model's skill list. Argument
  numbering differs between the two entry paths: `forge/brief.md`
  says `$1` = name, `$2` = slug, correct for a direct
  `/forge:brief <name> <slug>`; through the dispatcher
  (`/forge brief <name> <slug>`) the arguments are `$1` = brief,
  `$2` = name, `$3` = slug and no substitution happens at all —
  `forge.md` step 2 says "read the file and follow it", so the model
  sees the literal `$1` in a file opened with Read. CLAUDE.md and
  `/check-forge` step 1 (commands table against files) do not know
  these six commands exist.
- **Why it matters:** The model may dispatch to a state file directly
  from its description, bypassing the dispatcher and its input
  declaration; and the argument a state file names is not the one it
  receives.
- **Suggested fix:** Within the current layout: replace `$1`/`$2` in
  the six nested files with named prose ("the name argument", "the
  slug argument, else the current project from context"), state in
  `forge.md` and `recipe.md` step 1 that a state file's arguments
  are those following the state name, and set
  `disable-model-invocation: true` on the six nested files. The
  structural fix is the skills layout of FND.0260.

### FND.0200 [high] [gap]
- **Location:** `.claude/agents/critic-clarity.md:4`,
  `critic-essence.md:4`, `challenger-cto.md:4`;
  `templates/critic.md:4`, `templates/challenger.md:4`
- **Issue:** `tools: Read, Write, Glob, Grep` (plus web tools for the
  challenger). The Output section instructs each agent to update
  `ledger.md` (new FND/CHL rows, verified or reopened states,
  document states). Without `Edit` the only way is to read the whole
  ledger and re-`Write` it in full.
- **Why it matters:** A truncated or re-flowed rewrite silently loses
  rows of the single source of truth for state, inside an isolated
  agent nobody watches until `/check` runs.
- **Suggested fix:** `tools: Read, Edit, Write, Glob, Grep` in both
  skeletons and all three agents; `Write` stays for the new review or
  challenge file. The one change the reviewer would make before the
  next reviewer run.

### FND.0210 [high] [gap]
- **Location:** `.claude/commands/save.md`, `spinoff.md`, `setup.md`,
  `new-project.md`, `import-project.md`, `ingest.md`, `render.md`
- **Issue:** Since commands and skills were unified, Claude may
  invoke any command on its own judgement from its description unless
  the file sets `disable-model-invocation: true`. None does. The
  forge's Step by step method and prime directive 2 say a write,
  commit, push or scaffold happens only on the principal's word;
  `render.md` even states "Claude never regenerates on its own
  judgement" — in prose, not in the mechanism.
- **Why it matters:** The guarantee rests on the model's obedience to
  CLAUDE.md, not on the harness. Side benefit of the fix: the
  descriptions of disabled commands are no longer loaded into the
  model's context, trimming the always-on cost of the layer.
- **Suggested fix:** `disable-model-invocation: true` on the seven
  commands named and on the six nested files of FND.0190. Leave
  `forge`, `ledger`, `check`, `check-forge`, `critique`, `challenge`,
  `research`, `recipe` model-invocable: maps, reports and rosters are
  read-only, and CLAUDE.md wants Claude to propose them.

### FND.0220 [medium] [gap]
- **Location:** `.claude/commands/render.md`, steps 3 and 5
- **Issue:** Step 3 says the subagent prompt names the project, the
  recipe path, the output path and the render date, and that the
  subagent must not read the previous render except to learn the
  front-matter format. The front-matter shape is defined in step 5,
  which the subagent never sees. A first render has no source for
  the provenance block; a later one copies the previous render and
  propagates any drift. `check.md` by contrast tells its subagent to
  read the command file.
- **Why it matters:** The provenance block is what `/forge` and
  `/check` read to decide staleness (POS.1070); an agent that has to
  guess its shape undermines the one definition.
- **Suggested fix:** In step 3, instruct the subagent to read
  `.claude/commands/render.md` step 5 for the front-matter shape, or
  carry the block from step 5 verbatim in the prompt. Alternatively a
  `renderer` agent in `.claude/agents/` with `tools: Read, Write,
  Glob` and the shape in its body — consistent with the reviewers,
  tighter than `general-purpose` (which has Bash and Edit the renderer
  has no business using), and it removes the second hand-rolled
  "spawn one subagent" paragraph that `check.md` and `render.md` both
  carry.

### FND.0230 [medium] [ambiguity]
- **Location:** `.claude/commands/research.md:6` (`Research "$1"`),
  `.claude/commands/ingest.md` (paths with spaces),
  `.claude/commands/save.md` step 7
- **Issue:** `$1` is the first whitespace-delimited token.
  `/research zero trust architecture flow-ba` gives `$1` = `zero`;
  the quotes in `"$1"` do nothing at substitution time, and the
  argument hint `<topic> [project-slug]` invites exactly this.
  `save.md` step 7 writes the literal `[slug] [-m "message"]` where it
  means to pass the arguments through.
- **Why it matters:** A multi-word topic or a path with a space is
  silently truncated.
- **Suggested fix:** `research.md`: use `$ARGUMENTS` and say "the
  last token is the project slug if it matches a directory under
  `projects/`; the rest is the topic", or change the hint to
  `"<topic>" [project-slug]` and require quotes. `save.md`:
  `./scripts/forge-save.ps1 $ARGUMENTS`.

### FND.0240 [medium] [ambiguity]
- **Location:** `.claude/commands/check.md`, step 0 (lines 14–19)
- **Issue:** "instructs it to read this file and execute its checks" —
  by the time the model composes the subagent prompt, "this file" is
  an expanded prompt, not a path. `check-forge.md` gets it right by
  citing `.claude/commands/check.md` explicitly.
- **Why it matters:** The subagent may receive no path and improvise
  the checks.
- **Suggested fix:** "instructs it to read `.claude/commands/check.md`
  and execute the checks under *Checks per project* as written".

### FND.0250 [medium] [contradiction]
- **Location:** `.claude/agents/challenger-cto.md:15`
- **Issue:** "(for the current principal, a fellow CTO in a large
  multinational group)" is a fact about one instance. CLAUDE.md says
  who the principal is lives in `CLAUDE.local.md`, never in the
  engine; subagents do not receive `CLAUDE.local.md`, so the persona
  cannot read it either.
- **Why it matters:** The engine is public; an instance fact in a
  committed persona is the leak class of THR.0210, and a second
  principal inherits a wrong register.
- **Suggested fix:** Make the Lens generic ("a senior leader of the
  principal's own standing and register") and have `challenge.md`
  pass the principal's role from `CLAUDE.local.md` in the task prompt
  beside project path and target — not conversation content, so
  isolation holds.

### FND.0260 [medium] [divergence]
- **Location:** `.claude/commands/` as a whole against
  `.claude/skills/<name>/SKILL.md`
- **Issue:** Both layouts register `/name` and support the same
  front-matter fields and `$ARGUMENTS`/`$1`. The skill directory
  shape was designed for exactly this layer's pattern — a dispatcher
  with supporting files read on demand — and the commands layout
  registers those supporting files as commands (FND.0190).
  Gained by migrating: supporting files without registration
  (`.claude/skills/forge/SKILL.md` with `states/brief.md` beside it —
  FND.0190 disappears structurally); `user-invocable: false` for
  helper skills only other mechanisms read (FND.0270); `context:
  fork` with `agent: <type>`, which runs a skill in a forked subagent
  with the skill's body as its instructions — what `check.md` and
  `check-forge.md` step 0 hand-roll today, so the isolation of
  POS.0930 becomes a declared property (both fields to be verified
  against the installed version); a recognised `references/` and
  `scripts/` convention, so `templates/critic.md` could sit beside
  the reviewer skill. Paid: 15 directories instead of 15 files; the
  unused `/forge:brief` namespace shortcuts; documentation churn in
  CLAUDE.md (Commands table, Repository layout, the `/forge <state>`
  row), `forge.md` and `recipe.md` step 1, `check-forge.md` steps 1
  and 3, the intent's positions naming `.claude/commands/...`, the
  README render — under POS.1070 all in one round. A mixed layout
  works technically but is two loading mechanisms for one command
  set.
- **Why it matters:** The layer's shape is the subject of THR.0270
  and THR.0240; this is the concrete trade-off they need.
- **Suggested fix:** Migrate all fifteen in one round, or none; if
  none, FND.0190 and FND.0210 are the cheap substitute. The
  principal's decision, into the intent.

### FND.0270 [medium] [duplication]
- **Location:** `.claude/agents/critic-clarity.md:71–172`,
  `critic-essence.md:73–174`, `challenger-cto.md:43–131` against
  `templates/critic.md:30–131`, `templates/challenger.md:27–115`
- **Issue:** The Subject, How to work and Output sections are
  byte-for-byte identical to the skeletons with only `<lens>`,
  `<persona>` and `<register>` filled — the verbatim mechanism is
  honoured today. It remains a maintained duplication of about 100
  lines times three, plus a `/check-forge` step 3 bullet whose only
  job is to police it: the defect class POS.1070 names.
- **Why it matters:** Three copies of the reviewers' core rules drift
  the day the check is skipped.
- **Suggested fix:** Ranked. A: `skills:` preload in the agent
  front-matter — the shared text as
  `.claude/skills/critic-shared/SKILL.md` (`user-invocable: false`,
  `disable-model-invocation: true`), likewise `challenger-shared`;
  each agent file becomes front-matter, Lens and
  `skills: [critic-shared]`; one owner, no check needed,
  `templates/critic.md` shrinks to the Lens skeleton; same runtime
  token cost, a single-sourcing gain, not a context gain; field to be
  verified against the installed version. B: runtime Read of the
  skeleton as the agent's first step — not recommended, the agent's
  core rules would depend on a Read it might skip or paraphrase. C:
  status quo, drift managed by `/check-forge` — acceptable if A is
  unavailable. This is THR.0270's proposed solution, confirmed from
  outside.

### FND.0280 [low] [duplication]
- **Location:** fourteen command files (every command except
  `spinoff.md`, `recipe.md` and the three genre files)
- **Issue:** "conversation language (`CLAUDE.local.md`)" or
  "principal's language" is restated per command — the single most
  common line in the layer — while CLAUDE.md, always in context,
  states prime directive 6 once.
- **Why it matters:** POS.1070: a rule stated in two places is a
  defect; fourteen places is fourteen chances to drift.
- **Suggested fix:** Delete the clause everywhere except `setup.md`
  (lines 10–11), where the exception — language not yet
  configured — is genuinely local.

## Recommendations
<!-- Not findings, not gates: wording that is hard to test, groups that
overlap, items that could be split. The principal may ignore these
without recording anything. -->
- **POS citations in operating files.** 59 `POS.xxxx` citations
  inside the commands (`check.md` alone carries 13) serve
  `/check-forge` traceability and the principal, not the model
  executing the command; to the model they are inert tokens. If
  kept, one HTML comment per file listing the positions it
  implements would give the same traceability with the body reading
  as pure instruction. The principal's call.
- **`critique.md` and `challenge.md` are near-mirrors.** About 60 %
  of their text is structurally identical (roster, invocation,
  isolation sentence, "when it returns", walkthrough offer) —
  deliberate ("the critic is the mirror of the challenger"). A single
  `review.md` dispatcher taking `critic|challenger` as `$1` would
  halve the text; the two-command surface is arguably clearer for
  the user. Taste.
- **Maintainer comments inside agent system prompts.** The HTML
  comment "Lens file: the Lens section is this lens's own …" at the
  top of each agent is addressed to the maintainer but delivered to
  the subagent as part of its system prompt. Harmless, slightly
  noisy; goes away under FND.0270 option A.
- **Agent descriptions describe what, not when.** For hand-invoked
  reviewers the current form is right. One sentence "Invoked only
  through `/critique`; never delegate to it proactively" would make
  that explicit to the session model, which otherwise sees three
  tempting reviewer agents in its roster.
- **`argument-hint` values beginning with `[`.** Exactly the form the
  official docs use, accepted by Claude Code's parser; a strict YAML
  parser would read `[target-state]` as a flow sequence. Quoting the
  value costs nothing and survives a parser change. Purely defensive.

## What is done well
- Every file has a description; none is truncated, misleading or
  mid-sentence. Descriptions consistently state the bare/with-argument
  split, which is what a dispatcher needs for correct triggering.
- Writing style is uniformly imperative and addressed to Claude; role
  statements open the files and set the register before the steps.
- Progressive disclosure is real even without `references/`:
  `templates/` holds the skeletons, commands cite them by path, and
  the agent files carry only what the agent must have in its prompt.
- `model: inherit` on the agents is the correct value and a recorded
  decision. The challenger's `WebSearch`/`WebFetch` and the critics'
  absence of them match their remits exactly.
- `settings.json` denies `~/.ssh` and `~/.aws` reads;
  `settings.local.json` carries only the model and is gitignored.
- The verbatim-copy discipline is honoured to the byte in all three
  agents.

## Priority order for action (the reviewer's)
1. FND.0200 — `Edit` for the reviewer agents and skeletons.
2. FND.0190, FND.0210 — `disable-model-invocation` and the `$1`
   numbering.
3. FND.0220, FND.0230, FND.0240 — the three prompt and argument gaps.
4. FND.0260 with FND.0270 — the layout and the shared-text mechanism
   decided in one round; they touch the same files and the same
   CLAUDE.md passages.
5. FND.0280 — the language-clause sweep, in whichever round next
   touches the commands.
