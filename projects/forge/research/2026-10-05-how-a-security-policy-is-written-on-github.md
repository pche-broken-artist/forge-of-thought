---
project: forge
kind: research
topic: how a security policy (SECURITY.md) is written on GitHub - what GitHub provides and recommends, and what comparable projects actually publish
date: 2026-10-05
author: Claude (research for the principal)
status: immutable
---

# How a security policy is written on GitHub

## Question

The forge's repository on GitHub has a README, a licence and, since
2026-10-04, a CONTRIBUTING file; the community profile of
2026-10-04 listed the security policy among the files still missing
(`research/2026-10-04-how-a-contributing-file-is-written-on-github.md`,
finding 7). The principal wants a `SECURITY.md`. What does GitHub
provide and recommend for it, what do the guidance and the evidence
say a good one holds, and what do projects comparable to the forge,
frameworks of instructions that an agent executes, actually publish?

Out of scope: the forge's security itself (what it does on a
machine is read from its own files, not from the web); bug bounties
and legal safe-harbour language, which presume an organisation.

## Marks

Practice: [C] consensus, [E] emerging, [X] contested. Evidence: (V)
read at source 2026-10-05 through a summarising fetch tool, so a
quotation is the summariser's relay unless it is marked raw; (S)
secondary; (O) this note's own synthesis. All product facts are of
2026-10-05 and of a platform that changes.

## Key findings

### 1. GitHub's mechanism: one file, three places, two surfaces [C] (V)

- A `SECURITY.md` may live in the repository root, in `docs/` or in
  `.github/`; where more than one exists, `.github/` wins, then the
  root, then `docs/`. An account's public `.github` repository can
  hold a default one for every repository that has none of its own.
- It is shown in the repository's Security tab under "Reporting:
  Security policy" and, when private vulnerability reporting is on,
  above the report form; GitHub also links it from the page where a
  new issue is opened (the docs imply it; the CONTRIBUTING research
  of 2026-10-04 saw the row).
- GitHub's "Start setup" wizard writes a two-section template:
  **Supported Versions**, a table of version against "Supported" with
  ticks and crosses, and **Reporting a Vulnerability** with the
  placeholder "Use this section to tell people how to report a
  vulnerability. Tell them where to go, how often they can expect to
  get an update on a reported vulnerability, what to expect if the
  vulnerability is accepted or declined, etc." Nothing else is
  prescribed.
- Private vulnerability reporting (PVR) is a repository setting
  (Settings, Advanced Security, "Private vulnerability reporting")
  that owners and administrators of a public repository switch on;
  it puts a "Report a vulnerability" button on the Advisories page,
  the report arrives as a draft advisory seen by administrators and
  security managers, the reporter becomes a collaborator on it and
  is credited when it is accepted. It is independent of
  `SECURITY.md`; the policy, if present, is displayed above the
  form. An optional `.github/VULNERABILITY_REPORT.yml` customises the
  form with the issue-form YAML syntax; a form that fails to parse
  falls back to the default one.
- The list of community health files GitHub recognises today:
  ACCESSIBILITY, CODE_OF_CONDUCT, CONTRIBUTING, SECURITY, SUPPORT,
  FUNDING.yml, issue and pull-request templates, discussion category
  forms, VULNERABILITY_REPORT.yml.

### 2. What a good policy holds: five questions, promised sustainably [C] (V, S)

A guide of 2026-04-21 (Johnson, Hypertext Dispatches) condenses the
practice into five questions a policy must answer: which versions
receive fixes; how to report privately; what to include in a
report; what response to expect; which channels are wrong (public
issues and pull requests). Its rules: one primary reporting path,
PVR where enabled, a role address rather than a personal inbox as
the fallback, and no second channel unless both are watched; a
response window the maintainer can keep ("three business days met
every time beats an aggressive promise missed"); a short paragraph
on what happens after validation (advisory, coordinated timing, fix
before disclosure) without a formal incident process; honest scope,
nothing that implies a bounty, a 24/7 desk or legal review unless
they exist; safe-harbour text only with counsel and only for a
formal programme. What to avoid: unmonitored addresses, vague
process that needs clarification, and formalism that puts a
reporter off.

The OpenSSF Best Practices criteria say the same at the minimum:
the project must publish how to report a vulnerability; where
private reports are supported, how to send one privately; and the
initial response to any report of the last six months must be
within fourteen days.

### 3. The evidence: adoption is early, the asks are plain [E] (V, S)

- An empirical study of 3,323 SECURITY.md-related issues on GitHub
  (May 2019 to June 2025, 711 classified by hand; arXiv 2510.05604)
  finds 79.5 % of them are requests to add the file, 11.7 % to
  revise it (a dead address, a broken link), and that nearly half
  the addition requests came from one bounty platform. Recurring
  confusion: whether to use the policy's channel or GitHub's own
  "Report a vulnerability" button. The file is "in early diffusion".
- A study of 679 PyPI libraries on GitHub (Springer, EMSE 2025;
  read from its abstract only, the article sits behind a login)
  reports that projects with a security policy show stronger
  security practices overall and recommends a clear, complete one.
  Correlation, not cause, by the abstract's own wording.

### 4. What comparable projects publish (V, O)

| Project | Shape | Channel | Versions | Threat model |
|---|---|---|---|---|
| github/spec-kit | GitHub's corporate policy, 31 lines | e-mail to GitHub's open-source security address; open source "outside the bug bounty"; safe-harbour link | — | — |
| anthropics/claude-code | 12 lines | HackerOne submission form and bounty page | — | — |
| bmad-code-org/BMAD-METHOD | project's own, root | PVR preferred, a security e-mail, Discord DM | latest only | yes: "designed to execute instructions from markdown files"; the boundary is untrusted content (web pages, API responses, issue or PR bodies) altering agent behaviour, and file access beyond the configured scope; installing a module "is equivalent to running its code"; small team, best effort, acknowledgement "within days" |
| Fission-AI/OpenSpec | project's own, root, about 50 lines | GitHub Security Advisories only; "don't open a public issue" | latest npm version only; upgrade to get a fix | yes: a local CLI, no server, no listener; what it reads and writes and with whose permissions; in-scope and out-of-scope lists; "what the CLI does on your machine" (install scripts, shell calls, self-update on confirmation, telemetry and how to switch it off, network use); automated checks named; acknowledgement in 3 business days, fix or decision in 30 |
| obra/superpowers | not found at `main` (404) | — | — | — |
| buildermethods/agent-os | not found at `main` (404) | — | — | — |

Reading: the two corporate neighbours delegate to an organisation's
programme; the two small frameworks closest to the forge write the
file themselves and spend most of it on a **threat model** that
says what the tool is, what it does on the machine, what is in
scope and what is not, and what the user must vet himself. That
section is where a reader of a prompt framework actually learns
something, and it is absent from GitHub's template. [E] as a
practice among small agent frameworks, two examples.

## Options and trade-offs

**A. GitHub's template, filled in.** Supported versions and a
reporting paragraph. *For:* ten minutes, the checklist row turns
green, every reader recognises the shape. *Against:* says nothing a
visitor of a prompt framework wants to know; the studies' revision
requests are about exactly such files going stale.

**B. A short policy of the OpenSpec and BMAD shape.** Reporting
(PVR first, a fallback), supported versions (the latest release on
`main`; the `v<major>` tags), a threat model in the forge's own
terms, what the engine does on the machine, what is in and out of
scope, a sustainable response window, credit. *For:* answers the
five questions and the reader's real one, "what does this thing do
on my computer"; the forge already holds the facts in its solution
design (the wall, the scripts, the hook, the isolated subagents).
*Against:* about sixty lines to keep true as the engine changes;
the threat model is a claim the principal signs.

**C. A corporate policy** with bounty and safe harbour. *Against:*
the forge is one person's engine; the guide and both studies say
not to imply what is not there.

**D. How the file is made: a render of a recipe, or written by
hand.** The forge decided this for CONTRIBUTING on 2026-10-04
(POS.1440, SOL.0450): a render, so that what the file tells cannot
drift from the intent and the design; current only after a render.
A security policy has the same property, and a stronger reason: its
threat-model sentences are read off the solution design, which
changes. *Against:* one more recipe; a file that is only a few
fixed sentences gains little from a recipe beyond consistency.

## Relevance to this project

What the forge is, for the threat model, read from its own files
and not from the web (`40-solution-design.md` SOL.0510, SOL.0520,
SOL.0030, SOL.0300, SOL.0600; CLAUDE.md Persistence): a set of
instruction files Claude Code reads; no server, no listener, no
telemetry of its own; it reads and writes Markdown under
`projects/` with the user's permissions; its scripts call `git`,
`pandoc`, `markitdown` and headless `claude` from PATH and install
nothing; the hook runs `pwsh` at every prompt; the deny rules keep
raw `git` and the `~/.ssh` and `~/.aws` paths from Claude; the
reviewers run as subagents that see the project's files; the engine
sends nothing anywhere but what `forge-save` pushes to the user's
own remote and what `/publish` hands to headless Claude Code. What
leaves the machine through Claude Code itself is Anthropic's
policy, not the forge's. The matters of substance a policy of the
forge should name as its own: ingested sources are data and may
carry instructions, as BMAD names for markdown and OpenSpec for
spec files, and the reviewers read them; `projects/*` is gitignored
and what a project contains is its owner's (POS.0760); the instance
facts of `CLAUDE.local.md` reach every subagent (POS.0950) and so
must stay harmless; a `/publish` run executes a model with `Bash`
among its tools (`scripts/md2pptx.ps1`, `md2docx.ps1`); the
permission system is a guard, not a sandbox (SOL.0520).

**Recommendation** (this note's own, for the principal to decide
through `/forge intent`; each point a proposal):

1. **Option B, in the repository root, as a render of a recipe
   `security`** on the CONTRIBUTING precedent (D), about sixty
   lines, in the shape: how to report (PVR first; the author's
   GitHub profile as the fallback, as CONTRIBUTING already names
   it; no public issue); what to include; what to expect (an
   acknowledgement within a week, a fix or a decision as the
   principal's pace allows, credit in the advisory unless declined;
   no bounty); supported versions (the latest release on `main`,
   the `v<major>` tags, no older line patched); what the engine is
   and does on the machine, in the terms above; in scope and out of
   scope, the way OpenSpec lists them; a line that the sources a
   user ingests are his and may carry instructions the reviewers
   read.
2. **Switch on private vulnerability reporting** in the repository's
   settings before the file points at it, the way Discussions were
   switched on for CONTRIBUTING; a policy that names a button that
   is not there is the revision request of finding 3.
3. **One position in the intent** for the stance, as POS.1440 holds
   the contributing stance: what the forge promises a reporter and
   what it does not, so that the recipe has an owner to cite and
   the render cannot drift.
4. **Not now:** the custom report form, a code of conduct, a
   security tab beyond the policy; none of the neighbours of the
   forge's size has them, and the profile checklist is not tied to
   anything (CONTRIBUTING research, finding 6).

Trade-off stated once: B costs a threat model the principal must
stand behind and keep true, where A costs nothing and says nothing;
for a tool whose whole surface is "it executes instructions on your
machine", the sentences of B are the ones a careful reader opens
the file for.

**What stays uncertain.** Whether PVR is enabled on the forge's
repository was not checked (a setting, not a file). Superpowers and
Agent OS returned 404 at `main`; a file on another branch or under
`.github/` was not looked for. The Springer study was read from its
abstract. GitHub's own docs page was read through the summariser
and its source could not be fetched raw, so the exact wording of
the issue-page link rests on the CONTRIBUTING research of
2026-10-04. Whether a threat model in a policy measurably changes
what reporters send has no evidence either way.

## Sources

All fetched 2026-10-05 through a summarising fetch tool unless
marked raw.

- GitHub Docs, Adding a security policy to your repository -
  https://docs.github.com/code-security/getting-started/adding-a-security-policy-to-your-repository
  (undated) [V]
- GitHub Docs, Privately reporting a security vulnerability -
  https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability
  (undated) [V]
- GitHub Docs, Configuring private vulnerability reporting for a
  repository -
  https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/configuring-private-vulnerability-reporting-for-a-repository
  (undated) [V]
- GitHub Docs, Creating a default community health file -
  https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file
  (undated) [V]
- GitHub's default SECURITY.md template, as mirrored in
  mezgoodle/Templates - https://github.com/mezgoodle/Templates/blob/master/SECURITY.md
  [V, mirror]
- R. Johnson, How to Write an Effective Security Policy for GitHub
  Repositories, Hypertext Dispatches, 2026-04-21 -
  https://tenthirtyam.org/dispatches/2026/04/21/how-to-write-an-effective-security-policy-for-github-repositories/
  [V]
- OpenSSF Best Practices Badge, criteria (passing) -
  https://www.bestpractices.dev/en/criteria/0 [V]
- An Empirical Study of Security-Policy Related Issues in Open
  Source Projects, arXiv 2510.05604 (2025) -
  https://arxiv.org/html/2510.05604 [V]
- Security by documentation? characterizing GitHub SECURITY.md
  policy and their adoption in Python libraries, Empirical Software
  Engineering (2025) - https://link.springer.com/article/10.1007/s10664-025-10794-z
  [S, abstract only]
- github/spec-kit, SECURITY.md -
  https://github.com/github/spec-kit/blob/main/SECURITY.md [V]
- anthropics/claude-code, SECURITY.md -
  https://github.com/anthropics/claude-code/blob/main/SECURITY.md
  [V, raw]
- bmad-code-org/BMAD-METHOD, SECURITY.md -
  https://github.com/bmad-code-org/BMAD-METHOD/blob/main/SECURITY.md
  [V]
- Fission-AI/OpenSpec, SECURITY.md -
  https://github.com/Fission-AI/OpenSpec/blob/main/SECURITY.md [V]
- obra/superpowers and buildermethods/agent-os, `SECURITY.md` at
  `main` - not found (HTTP 404) on 2026-10-05.
