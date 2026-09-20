<#
.SYNOPSIS
UserPromptSubmit hook of the engine: repeats the one-item walkthrough
rule at every prompt (POS.1170).

.DESCRIPTION
Claude Code runs this script on every user prompt (configured in
.claude/settings.json) and adds its standard output to the context of
that turn. It prints two lines on the walkthrough: the rule that must
hold in a long conversation, and the pointer to the skill that holds
the full shape. Since 2026-09-20 it also prints three lines of conduct:
use the forge's scripts, explain and ask before running a command of
one's own, and change nothing that was not agreed and approved
(THR.0400 of the forge intent; a gate that enforces them is the
thread's open matter).
It reads nothing, writes nothing, takes no arguments. Cross-platform
PowerShell 7; the working directory is the engine root when it runs.
#>

Write-Output "Walkthrough rule: one item per reply - acknowledge the last verdict, put one item forward, stop. A question from the principal keeps the item open."
Write-Output "When a walkthrough or an interview is running, work by .claude/skills/walkthrough/SKILL.md."
Write-Output "Tools: where the forge has a script (scripts/*.ps1), use the script, never the raw tool. git only through scripts/forge-*.ps1, reading state included."
Write-Output "Own commands: before running anything of your own that is not plain reading, say what it does and why, and wait for the principal's yes."
Write-Output "Consent: write, run and change nothing that was not agreed and approved. A yes covers exactly what was asked, never its consequences."
