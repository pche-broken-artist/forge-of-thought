---
project: forge
document: 40-solution-design.md
---

# History — 40-solution-design.md

<!-- The history of a versioned document: CLAUDE.md, Versioning &
status. One record per change, one line each, appended at the end,
never rewritten:
- <date> | <version> | <author> | <subject> | <kind> | <reason> | Action: <what the user must do> | Was: <wording that ceased to hold>
Kinds: created | changed | closed | removed | approved. The subject
is an ID, several IDs where the whole line holds for each, or a
place without an ID: a section, the file, or in the forge's own
project the operating layer. Reason is left out on
`created`; `Action` and `Was` only where the record has them, `Was`
always last, paragraphs in it divided by `<br>`. At the birth of a
document, one record of the file and one naming every item born
with it. Lines are not wrapped. -->

- 2026-10-04 | 0.1 | PCHe | 40-solution-design.md | created
- 2026-10-04 | 0.1 | PCHe | SOL.0010, SOL.0020, SOL.0030, SOL.0040, SOL.0100, SOL.0110, SOL.0120, SOL.0130, SOL.0140, SOL.0150, SOL.0160, SOL.0200, SOL.0210, SOL.0220, SOL.0230, SOL.0300, SOL.0330, SOL.0400, SOL.0410, SOL.0420, SOL.0430, SOL.0440, SOL.0500, SOL.0510, SOL.0520, SOL.0530, SOL.0550, SOL.0600, SOL.0610, SOL.0620, TBC.0010, TBC.0020, TBC.0030 | created
- 2026-10-04 | 0.2 | PCHe | SOL.0170 | created
- 2026-10-04 | 0.2 | PCHe | SOL.0300 | changed | The skeletons of the reviewers renamed to the pattern `<type>-definition.md`, the principal's word of 2026-10-04 (THR.0520, step 5). | Was: `templates/critic.md`, `templates/challenger.md` and `templates/check.md` are the skeletons of a lens file.
- 2026-10-04 | 0.2 | PCHe | SOL.0330 | changed | The skeleton of a check renamed to `templates/check-definition.md` (THR.0520, step 5). | Was: One contract skill `check-contract`; one agent per check, `check-<name>`, front-matter and Lens only, from `templates/check.md`; a new check is one file.
- 2026-10-04 | 0.3 | PCHe | SOL.0450 | created
- 2026-10-09 | 0.4 | PCHe | SOL.0460 | created
- 2026-10-09 | 0.5 | PCHe | SOL.0620 | changed | The scripts are Python, rewritten 2026-10-09 and tested against a fixture; the shared modules; the hook; the option spelling (POS.0830, THR.0150 closed). | Was: The scripts are PowerShell 7, which is itself cross-platform (`pwsh`, one install on a non-Windows machine), and they use nothing Windows-only: paths composed with `Join-Path` or forward slashes, no `cmd`, registry or Windows-only cmdlets, `$IsWindows` only where the platform genuinely differs, external tools (`git`, `markitdown`, `pandoc`, `claude`) resolved from PATH, and usage examples in the scripts' help free of Windows-specific paths and invocations. The rewrite of the PowerShell scripts in Python is open, THR.0150. Realises: POS.0830. Choice: PowerShell 7 at the start, the reason not recorded in the intent. Portability is not verified: the set has not been run on Linux. Where: `scripts/`.
- 2026-10-09 | 0.5 | PCHe | SOL.0020, SOL.0150, SOL.0160, SOL.0220, SOL.0430, SOL.0440, SOL.0500, SOL.0510, SOL.0540, SOL.0550, SOL.0600 | changed | The Python scripts named in place of the PowerShell ones, the hook started by `python`, the options in their Python spelling (`--engine`, `--recipe`, `--template`, `--reference`, `--model`); how the scripts recognise a project is `forge_repos.py`'s. | Was: `scripts/<name>.ps1`, `pwsh`, `-Engine`, `-Recipe`, `-Template`, `-Reference`, `-Model`; the help headers of `forge-status.ps1`, `forge-save.ps1` and `forge-pull.ps1`
- 2026-10-09 | 0.6 | PCHe | SOL.0460 | changed | Built whole and run once on 2026-10-09; three scripts, the writer's task handed as a file; the Where names every file. | Was: runs two agents and one script; Built 2026-10-09 as far as the two agents, the index script and the first run; not yet built: the skill, the state by hashes, the scan as one script (the first run was checked by a trial script in the engine's `tmp/`)
- 2026-10-09 | 0.6 | PCHe | SOL.0500 | changed | The engine's public address, the one owner the documentation reads it from (the planner of 2026-10-09 found none). | Was: `forge-of-thought`, full name Forge of Thought in documents: the universal core
- 2026-10-09 | 0.7 | PCHe | SOL.0460 | changed | The contract skill `docs-contract` and the skeleton `templates/docs-map.md`, born from the single-source-of-truth check of 2026-10-09 (FND.1060, FND.1090). | Was: Where: `.claude/skills/document/SKILL.md`, `.claude/agents/docs-planner.md`,
- 2026-10-10 | 0.8 | PCHe | head | changed | The provenance said of the whole what holds of the items of 0.1; the later items and the one judged item named (FND.1340, essence 2026-10-09). | Was: A proposal, handed over to Claude and not yet judged by the principal. It is a one-off move (THR.0520, step 4): the solution stands here as it stood in the intent at 4.55, and no choice in it is new. Every choice below is one the intent recorded, save where an item says the judgement is Claude's. Where the intent and its history give no reason for a choice, the item says the reason is not recorded, and none is invented. What an item says of a file, a research note or an open thread beyond the intent was read from that file by Claude on 2026-10-04. Where a `Choice` names no cost, the intent records none.
- 2026-10-10 | 0.8 | PCHe | SOL.0010 | changed | The three working methods of 4.63 realised by CLAUDE.md, Working methods (FND.1310). | Was: POS.0860, POS.0880, POS.0890, POS.0900, POS.0910, POS.1080, POS.1030, POS.1160, POS.1210, POS.1370, POS.1410. Choice: no real
- 2026-10-10 | 0.8 | PCHe | SOL.0150 | changed | What `/setup` asks and what it does when declined, from POS.1050 (FND.1230). | Was: session model. It closes with the git identity: it offers to write the `includeIf` stanzas
- 2026-10-10 | 0.8 | PCHe | SOL.0150 | changed | As before.
- 2026-10-10 | 0.8 | PCHe | SOL.0160 | changed | Where the clone lands and how a name is fixed, from POS.1060 (FND.1230). | Was: which creates `00-brief.md`. `/import-project` calls `scripts/forge-clone.py`. `/spinoff` creates files only.
- 2026-10-10 | 0.8 | PCHe | SOL.0230 | changed | What `/ingest` does with a bundle's index and the split of a file, from POS.0180 (FND.1230). | Was: - **SOL.0230 The resource indexes.** `/ingest` and `/research` write the entries of `00-INDEX.md`, `/new-project` scaffolds the indexes and the check `light` verifies index against directory.
- 2026-10-10 | 0.8 | PCHe | SOL.0500 | changed | One owner of the public address: the pinned facts of the readme recipe, as POS.1450 wants; this item cites (FND.1320, essence 2026-10-09). | Was: `forge-of-thought`, full name Forge of Thought in documents; its public home is `https://github.com/pche-broken-artist/forge-of-thought`, the address a clone and a project's README point to. The
- 2026-10-10 | 0.8 | PCHe | SOL.0530 | changed | What the release does with the documentation, from POS.1450 (FND.1330). | Was: with the release message and tag: not a second procedure.
