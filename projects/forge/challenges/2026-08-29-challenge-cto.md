---
date: 2026-08-29
project: forge
target: 00-brief-public-engine.md v0.4 (draft brief, pending)
reviewed: projects/forge/00-brief-public-engine.md v0.4; projects/forge/10-intent.md v2.19 (POS.0060, POS.0180, POS.0330, POS.0550, POS.0710, POS.0740, POS.0750, POS.0760, POS.0780, POS.0820, POS.0830, POS.0930, THR.0090, THR.0130, THR.0180); projects/forge/decisions.md (DEC.0010–0070); projects/forge/ledger.md; projects/forge/challenges/2026-08-17-challenge-cto.md (CHL.0010–0060); projects/forge/research/2026-08-29-framework-distribution-in-the-field.md; projects/forge/research/2026-08-29-claude-code-packaging.md; projects/forge/research/2026-08-29-git-engine-projects-separation.md; projects/forge/research/00-INDEX.md; projects/forge/recipes/readme.md v0.21 (inputs); CLAUDE.md (root, 435 lines); .gitignore; .claude/settings.json; scripts/forge-save.ps1; projects/agentic-platform/recipes/agentic-platform-it-deck.md (template reference only)
reviewer: challenger persona cto (peer CTO, isolated context)
---

# Peer review (cto) — 2026-08-29

## Overall read

As written, this brief is three things bundled as one: (a) publishing
the engine on a personal public GitHub with fresh history, (b) the
git shape for engine-beside-projects (gitignored `projects/*`, nested
repositories, scripts looping over `projects/*/.git`), and (c) a set
of new engine concepts that arrived in the same conversation — a
`library` project kind with relaxed immutability, `CLAUDE.local.md`
for instance facts, a commands→skills migration and a CLAUDE.md split
sold as free preparation for a plugin. Part (b) is well researched,
tested, and right; it settles THR.0130 and I have little to add there.
Parts (a) and (c) are where the thinking is thin. The brief says the
goal is publication and never says for whom or why, so nothing
downstream can be sized; it does not touch the one question that can
stop publication outright (who owns the engine); and it takes on a
real inter-repository dependency (libraries) one paragraph after the
research explained that the engine/project relation is clean
precisely because it is *not* a dependency.

## Challenges

### CHL.0070 — Nothing in the brief says the engine is yours to publish
- **Severity:** dealbreaker (conditional — see epistemic status)
- **Challenge:** The engine was designed and hardened over five weeks
  on two company initiatives as test material, lives on the employer's
  GitLab, and every commit carries the company identity
  (`forge-save.ps1` hard-codes the company address). The brief plans
  a personal public GitHub, a LICENSE of the principal's choosing, and
  the company GitLab demoted to a read-only archive. Nowhere does it
  ask whether the employer has a claim on work of this kind — an IP
  clause covering work related to the employer's business, a tools
  policy on publishing under a personal account, or a rule on using
  company infrastructure for a personal project. A CTO is the one
  employee whose contract most likely has the broad clause. "Mention
  of the company is not a no-go" is a statement about data, not about
  ownership.
- **Why it matters:** If the answer is unfavourable, every other item
  in the brief is moot, and finding out *after* a public push with a
  permissive licence is the worst order. If the answer is favourable,
  it costs one sentence in the brief and removes the only risk that is
  not reversible.
- **What would change my mind:** A line stating that the contract and
  policy have been checked and the engine is the principal's to
  publish — or that it is being published with the company's
  knowledge. Either settles it.
- **Epistemic status:** my judgement; the severity hinges on the
  contract, which I cannot see. Dealbreaker if the claim exists,
  cosmetic if it does not.

### CHL.0080 — Publication has no stated audience, and the brief sizes the work for a user it says will not come
- **Severity:** major
- **Challenge:** "Cíl je zveřejnění" is the whole rationale. The
  previous review asked (2026-08-17, unanswered) whether the public
  engine is for adoption inside the group or a portfolio/community
  artefact; the brief still does not say. Its own text implies the
  latter: the plugin comes "až přijde první cizí uživatel", i.e. no
  user is expected at publication. Yet three conditions (easy upgrade,
  a compatibility tool, all-platform scripts) and three preparatory
  steps (skills migration, CLAUDE.md split, plugin-readiness) are
  sized for a user population. Meanwhile the one thing an actual first
  user would need — an exemplar project showing the chain working —
  is "open". Compare the ecosystem you researched: the projects with
  adoption are the ones with a runnable example in the repository, not
  the ones with a tidy upgrade story.
- **Why it matters:** Without an audience the brief cannot be tested
  against anything, and the natural failure at twelve months is a
  public repository with a clean README, zero forks and a set of
  upgrade mechanics nobody has exercised — indistinguishable from the
  private state you have today, at the cost of a migration weekend.
  If the audience is the company ("company rollout", POS.0780), a
  personal public GitHub is an odd venue: colleagues would clone a
  public personal repo to do company work, with the exemplars on the
  company GitLab they cannot reference from a public README.
- **What would change my mind:** One sentence naming the audience
  (the company; the community; nobody — a portfolio) and, if it is
  anyone at all, the exemplar decided before the push rather than
  after. If the honest answer is "portfolio", say so and drop the
  plugin preparation from the brief.
- **Epistemic status:** my judgement

### CHL.0090 — The brief is the first file to fail its own pre-push grep, and the leak surface is `projects/forge`, not the code
- **Severity:** major
- **Challenge:** Migration step 4 greps the company name, the host and the
  commit identity before
  the push. That grep hits `00-brief-public-engine.md` nine times —
  the company GitLab, `lib-<company>`, `<company>.potx`, the commit
  identity — and
  the brief is destined to be locked, immutable, and shipped inside
  `projects/forge` on the public repository. So the plan as written
  either violates immutability (edit the locked brief), violates the
  grep (push anyway), or drops the founding record of this very change
  from the public copy. The same applies to the forge intent, whose
  Version History and open threads will carry `lib-<company>`,
  Microsoft AI Foundry and the company project slugs forever. The
  brief frames the sensitivity problem as a scripts-and-templates
  problem (remove `$RemoteUrl`, remove `user.email`); the actual
  surface is the forge's own chain, which by design records everything
  verbatim and never edits it.
- **Why it matters:** "Nothing sensitive, no instance facts" is a
  condition (5) that the immutability convention structurally cannot
  keep for `projects/forge` — the project is the engine's diary. You
  need a stated rule for what a public diary may say (company names
  yes, remotes and personal emails no, and what about a private
  project whose subject is personal?), and the rule must
  apply to the brief before it is locked, since afterwards it cannot.
  Also note `.claude/settings.json` pins `"model": "fable"` — an
  instance preference that POS.0930 already says moves to user-local
  settings on going public, absent from the brief's file table.
- **What would change my mind:** A stated boundary for the public
  forge project (what kinds of mention are acceptable in immutable
  artefacts) applied to this brief before its lock, and either the
  grep list reconciled with that boundary or an explicit decision that
  the grep is advisory.
- **Epistemic status:** consensus on the mechanism (immutable files
  cannot be scrubbed later); my judgement on the boundary.

### CHL.0100 — Libraries are a real dependency between repositories, and the brief adds one with no mechanism the day after the research showed why that fails
- **Severity:** major
- **Challenge:** The git research's central argument is that the
  engine/project relation is clean because it is *not* a dependency —
  nothing pins anything, so "no mechanism" works. The brief then
  introduces `kind: library`: a project other projects cite by path
  (`projects/lib-<company>/sources/<company>.potx` from a presentation
  recipe; provenance paths from an intent). That *is* a dependency —
  content one repository needs from another, at a version — and it
  carries exactly the problems the research listed for submodules:
  a private URL implied by a path in a possibly less-private project,
  an empty directory on any machine where the library is not cloned,
  no pin (the brief explicitly loosens immutability in libraries, so
  "cites by path" cites a moving target). A recipe rendered on a
  machine without `lib-<company>` silently loses its template; an
  intent
  citing a library source is unverifiable from the project's own
  repository. The brief says "nic se neredefinuje" and in the same
  paragraph redefines source immutability (POS.0180) for one project
  kind and adds a cross-repository reference type that nothing in the
  forge tracks or checks.
- **Why it matters:** This is scope creep inside a publication brief,
  and the kind that is cheap now and expensive later: once three
  projects reference two libraries, "which version of the BRQ
  convention did this assignment follow" has no answer, and `/check`
  cannot see across repositories. The honest alternative — a library
  is a project's own `sources/` copy, duplicated on purpose — was not
  weighed. Nor was the version question: a library file replaced in
  place changes what every citing artefact meant.
- **What would change my mind:** Either the library concept leaves
  this brief for its own (it is a whole of thinking by the forge's own
  definition, POS.0920), or the brief states how a cross-repository
  citation is resolved and checked when the library is absent or has
  moved on, and why in-project copying is worse.
- **Epistemic status:** consensus on the mechanism (a path into
  another repository is a dependency); my judgement on the remedy.

### CHL.0110 — The "three free steps" are not free: the CLAUDE.md split changes how the forge behaves, on a claim the documentation does not make
- **Severity:** major
- **Challenge:** The brief presents skills migration, a CLAUDE.md
  split into a short core plus skill-loaded reference, and no absolute
  paths as costless and sensible without a plugin. Two corrections
  first. The 200-line claim is overstated: the documentation gives a
  target under 200 lines and warns that bloated files get instructions
  ignored — guidance, not a threshold above which instructions are
  dropped. And CLAUDE.md is 435 lines today, so the split is not
  trimming; it is moving more than half of the engine's rules from
  always-on to on-demand. That is a behaviour change, not packaging.
  The forge's prime directives are precisely the rules the model tends
  to violate under load — the principal's own memory notes exist
  because "write once per round", "propose, never decide" and "pre-save
  check visible" slipped *while always-on*. The plan relies on Claude
  reaching for the right reference skill at the right moment; the
  OpenSpec maintainers you cite killed a passive context file for
  exactly this reason ("agents might read it, might not, might forget
  what they read"). Likewise `context: fork` replacing the reviewer
  and render isolation is a rewrite of a mechanism that works today,
  justified by a phase 2 whose trigger ("first foreign user") the brief
  itself does not expect.
- **Why it matters:** The forge's value is the discipline it imposes
  on the model; the split trades that discipline for plugin-readiness
  nobody has asked for. If the plugin never comes, you have paid in
  reliability for nothing. If it does come, the research says the
  core arrives by an `@import` line or a SessionStart hook anyway —
  neither requires the core to be short, only to be a file.
- **What would change my mind:** A measurement: run the same three
  routine sessions with the current CLAUDE.md and with the split, and
  count directive violations. Or a decision that the split is a phase
  2 item taken up with the plugin, not before.
- **Epistemic status:** emerging practice on CLAUDE.md sizing (the
  guidance exists, the mechanism is not published); my judgement on
  the reliability risk.

### CHL.0120 — Fresh history throws away the record the design says lives in git, and parks the only copy on the employer's server
- **Severity:** major
- **Challenge:** POS.0710 says a recipe's change history lives in git;
  renders are "overwritten freely, history in git"; DEC.0040 refused
  to back-fill decisions because git and the intent already held the
  history. The brief starts the public repository with fresh history
  and keeps the real one as a read-only archive on the company GitLab.
  Two
  consequences. The public engine's recipes and renders arrive with
  no history at all — the readme recipe at 0.21 with nothing before
  it — so a convention the intent relies on is void for the public
  copy from day one. And the only full history sits on infrastructure
  the principal does not control and loses access to the day he
  changes employer; the personal, public, "canonical" repository is
  the one without the record. The obvious middle — rewrite history
  once with `git filter-repo` removing `projects/agentic-platform`,
  `projects/flow-ba` and `local/`, keeping the engine's commits — is
  not considered; commit messages naming company projects fall under
  the brief's own "mention is not a no-go".
- **Why it matters:** The forge's provenance story is its main claim
  to being more than a folder of Markdown. Publishing the engine
  without its provenance undercuts the claim in the very artefact
  meant to show it.
- **What would change my mind:** A stated reason fresh history is
  preferred over a filtered one (e.g. commit bodies contain material
  that must not appear), or a decision to filter instead.
- **Epistemic status:** consensus on the mechanism (history rewrite
  by path is routine); my judgement on the weight.

### CHL.0130 — "Upgrade" is a fast-forward of an untagged branch, so the compatibility tool has nothing to compare against
- **Severity:** minor
- **Challenge:** Condition 3 asks for an easy upgrade and a tool that
  checks a project against "the new version". The mechanism proposed
  is `forge-pull` = `git pull` on linear `main` with no tags and no
  releases; "version" of the engine exists only as the forge intent's
  front-matter number. A user cannot pin, roll back or name the engine
  version his project was last conformed to, no project records it,
  and `/check` reports against whatever `main` is now (POS.0820 makes
  that a fact, not a defect — fine, but it is not a compatibility
  check). The forge already has integer approvals; a tag per approved
  major and an engine-version line in each project ledger would make
  condition 3 true at almost no cost. Separately: a new project is
  "not under git" until the user remembers `git init` — a sensitive
  corpus may start its life unbacked by default.
- **Why it matters:** Small, but condition 3 is one of six the brief
  claims phase 1 satisfies "without any mechanism"; as written it is
  satisfied in name.
- **What would change my mind:** Tags at approvals and a recorded
  engine version per project; or the brief dropping the word
  "compatibility" and saying what `/check` actually does.
- **Epistemic status:** my judgement

## What is strong

- The git shape is right and, unusually, *tested*: gitignored
  `projects/*` with nested repositories, the `projects/*` vs
  `projects/` pitfall caught, submodules/subtree/template rejected on
  mechanism rather than taste. THR.0130 is effectively answered.
- "Engine clone as working directory, launch from the root" matches
  a documented Claude Code route; not inventing a discovery hack is
  the correct restraint.
- `/new-project` not touching git and letting `.git/config` be the
  only configuration is the right kind of "no mechanism".
- Two phases with one engine shape, plugin as a later distribution
  layer, is the correct sequencing — provided the phase-2 preparation
  is not pulled into phase 1 (CHL.0110).

## Questions I cannot answer from the documents

- Does your employment contract or the group's IP/tools policy give
  the employer a claim on the engine or restrict publishing under a
  personal account? (CHL.0070 stands or falls on this.)
- Who is the publication for — the company, the wider community, or a
  portfolio with no user expected? (CHL.0080.)
- Is the archive on the company GitLab something you would still have
  in three years, and is that acceptable? (CHL.0120.)
- Why fresh history rather than a path-filtered one — is there content
  in commit bodies that must not appear?
- For libraries: is a citing project ever expected to be read on a
  machine that lacks the library? If never, CHL.0100 shrinks to the
  versioning point.
- Have you observed any difference in directive adherence between
  sessions with the full CLAUDE.md and sessions where rules were moved
  into commands? Any data at all would sharpen or dissolve CHL.0110.
