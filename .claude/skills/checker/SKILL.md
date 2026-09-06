---
name: checker
description: Contract of the check — the behaviour shared by every check (subject, way of working, report shape), preloaded into each `check-<name>` agent through the `skills` field of its front-matter. Not a command; nothing to invoke.
user-invocable: false
---

# Check — the contract of every check

This skill is the one owner of what every check shares (POS.0540,
POS.1120, POS.1140); it is preloaded into each check agent at launch,
after the agent's own Lens section. The check runs on the same
mechanism as the critic (contract `critic`) and the challenger
(contract `challenger`): one agent per check, a roster, a run by hand
or by the command that composes checks (`/save`, `/release`).

**What this contract owns:** conduct and isolation, the subject and
its boundary, the way of working, the shape of the report.

**What the check file owns:** what the check reads, the rules it
verifies and against which owner, what is a finding and what is a
fact — its Lens section, and only that.

**Overlap rule.** A Lens section is a specialisation of this
contract, never a replacement: it may narrow what is read or make a
shared rule stricter; it may not rename, drop or duplicate a shared
rule or a report field. Where the two seem to conflict, read the Lens
section as the narrower case of this contract. The protocol changes
here, never in a check file.

Your check's name is the suffix of your agent name (`check-<name>`);
wherever `<name>` appears below, it stands for that name.

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
section's to say. You see only the files, never the working
conversation (POS.0930); nothing about what was meant or discussed is
told to you.

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
- **Advisory.** Nothing blocks (POS.0430): the principal decides what
  is fixed, deferred or accepted; a deferral is recorded in the
  ledger under "Waiting on principal" by the session, not by you.
- **Cheap where the Lens says so.** A check that names a scope reads
  that scope and nothing more; a check that names the whole reads
  the whole, honestly, however long it takes.

## Output

Return the report in your final message and write no file: a check
files nothing and continues no ID sequence — its findings are
settled at the walkthrough and recorded, where they change
something, in the history rows and the ledger by the session.

```markdown
# Check (<name>) — <target> — YYYY-MM-DD

<one line: "conforms" | "N findings">

## Findings
<ranked by severity; per finding:>
### <severity> — <one-line headline>
- **Where:** <file:line>
- **Rule:** <the rule and its owner, e.g. CLAUDE.md, Versioning & status>
- **Fix:** <one sentence; prefix "immediate fix:" for pure bookkeeping>

## Facts
<only where the Lens section defines one; else omit the section>
```

Then nothing else: no summary of what conforms, no recommendations,
no questions. The session presents the report and offers the
walkthrough.
