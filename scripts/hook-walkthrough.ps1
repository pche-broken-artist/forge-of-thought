<#
.SYNOPSIS
UserPromptSubmit hook of the engine: repeats the one-item walkthrough
rule at every prompt (POS.1170).

.DESCRIPTION
Claude Code runs this script on every user prompt (configured in
.claude/settings.json) and adds its standard output to the context of
that turn. It prints two lines: the rule that must hold in a long
conversation, and the pointer to the skill that holds the full shape.
It reads nothing, writes nothing, takes no arguments. Cross-platform
PowerShell 7; the working directory is the engine root when it runs.
#>

Write-Output "Walkthrough rule: one item per reply - acknowledge the last verdict, put one item forward, stop. A question from the principal keeps the item open."
Write-Output "When a walkthrough or an interview is running, work by .claude/skills/walkthrough/SKILL.md."
