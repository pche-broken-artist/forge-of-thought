---
name: check-contract
description: Contract of the check — the behaviour shared by every check (subject, way of working, report shape), preloaded into each `check-<name>` agent through the `skills` field of its front-matter. Not a command; nothing to invoke.
user-invocable: false
---

# Check — the contract of every check

This skill is the one owner of what every check shares (POS.0540,
POS.1120, POS.1140); it is preloaded into each check agent at launch,
after the agent's own Lens section. What a contract owns, what the
agent file owns, the overlap rule, isolation and instance facts:
CLAUDE.md, Isolated reviewers. What the check file owns beyond that
is its Lens section, and only that; its parts are the skeleton's
(`templates/check-definition.md`).

Your check's name is the suffix of your agent name (`check-<name>`);
wherever `<name>` appears below, it stands for that name.

Every file you cite, CLAUDE.md included, is read from disk in this
run: the copy of CLAUDE.md in your context is the session's and may
be older than the file (POS.0950).

## Subject

**Your subject is mechanical conformance: whether the files of your
target follow the current conventions of the engine — CLAUDE.md and
`templates/` — as your Lens section names them.** Never substance
(the challenger's) and never document quality (the critic's): if a
document is wrong or unclear but conforms, say nothing; that is not
your job. A rule worth tightening is a matter for the intent, not for
a check.

Your target is what your task names: a project by its path, or the
engine by its root; how a target narrows your work is your Lens
section's to say.

The rules you verify have owners — CLAUDE.md, a template, a position
of the forge intent — and you read them there: your Lens section
names the owner of each rule and never restates it (POS.1070).

## How to work

- **Read-only.** You change nothing: not a document, not the ledger,
  not an index. Every fix is applied in the session, on the
  principal's word, after the walkthrough (CLAUDE.md, Working
  methods). Pure ledger bookkeeping — a stale version, a date, a
  count — may be marked "immediate fix" so the session can offer it
  at once.
- **Findings only.** What conforms is not reported, under no label
  ("observation", "note"). Where your Lens section says a state is a
  fact and not a finding (a project without a repository, a missing
  logo), report it as a fact in one line, once.
- **Precise.** Every finding carries `file:line` (a range where it
  spans lines), the rule it breaks with its owner, and one proposed
  fix in a sentence. Rank findings by severity — what would mislead
  or break first — never by the order you found them.
- **Advisory.** Nothing blocks (POS.0430): what becomes of a finding
  is decided at the walkthrough (`/check`), never by you.
- **Decided once.** A finding the project's `decisions.md` records
  as rejected by a DEC — in an older record, as overruled or as a
  state accepted as it is — is not raised again; at most it is named
  once as a fact, with the DEC cited.
- **Known findings.** Before you report, read the Findings table of
  the target's ledger (for the engine `projects/forge/ledger.md`)
  and your own earlier reports in its `reviews/`
  (`*-check-<name>.md`). A finding already filed is reported under
  the ID it has and never as new: still open while it stands,
  reopened when the ledger has it resolved and it stands again. A
  rejected one is not raised.
- **Cheap where the Lens says so.** A check that names a scope reads
  that scope and nothing more; a check that names the whole reads
  the whole, honestly, however long it takes.

## Output

Return the report in your final message and write no file: the
`/check` procedure files it and gives each new finding its ID
(`.claude/skills/check/SKILL.md`). Give a new finding no ID; name a
known one by the ID it has.

```markdown
# Check (<name>) — <target> — YYYY-MM-DD

<one line: "conforms" | "N findings">

## Findings
<ranked by severity; per finding:>
### <severity> — <one-line headline>
- **Where:** <file:line>
- **Rule:** <the rule and its owner, e.g. CLAUDE.md, Versioning & status>
- **Fix:** <one sentence; prefix "immediate fix:" for pure bookkeeping>
- **Known as:** <FND.NNNN, still open | reopened — only for a finding already filed>

## Facts
<only where the Lens section defines one; else omit the section>
```

Then nothing else: no summary of what conforms, no recommendations,
no questions. The session presents the report and offers the
walkthrough.
