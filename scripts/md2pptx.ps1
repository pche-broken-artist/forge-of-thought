#Requires -Version 7.0
<#
.SYNOPSIS
    Generates a PowerPoint deck from a Markdown deck definition using
    headless Claude Code.

.DESCRIPTION
    The conversion is done by an LLM, never by a deterministic
    converter: the Markdown definition is deliberately free-form and
    may itself contain instructions for the model (slide-by-slide
    content, speaker notes, diagrams, visual directions). The script
    runs Claude Code non-interactively (claude -p) with Anthropic's
    official pptx skill.

    This script installs nothing. Install the engine yourself, one-off,
    from an interactive Claude Code session:
        /plugin marketplace add anthropics/skills
        /plugin install document-skills@anthropic-agent-skills

    A template is named by path: -Template <path to a .potx or .pptx>,
    typically a file in a library project (projects/lib-<company>/
    sources/). Without -Template, Claude designs the visual style
    itself.

    Use -Help for a short usage summary.
#>
param(
    # Markdown deck definition (e.g. projects/<slug>/renders/<recipe>.md).
    [Parameter(Position = 0)]
    [string]$Md,

    # Path to a .potx or .pptx template (relative to the current
    # directory or absolute). Default: none - Claude designs the visuals.
    [string]$Template,

    # Output .pptx path. Default: next to the input, same basename.
    [Alias('o')]
    [string]$Out,

    # Model the headless Claude Code runs on (claude --model).
    [string]$Model = 'opus',

    # Print usage summary and exit.
    [Alias('h', '?')]
    [switch]$Help
)

Set-StrictMode -Version 3.0
$ErrorActionPreference = 'Stop'

function Show-Usage {
    @'
md2pptx.ps1 - generate a PowerPoint deck from a Markdown deck definition

USAGE
  ./md2pptx.ps1 <definition.md> [-Template <file.potx>] [-Out <file.pptx>]

  <definition.md>   free-form Markdown deck definition; may contain
                    instructions for the LLM - it is read by Claude,
                    not parsed mechanically
  -Template <path>  a .potx or .pptx template, named by path (e.g. a
                    file in a library project's sources/); without it
                    Claude designs the visual style itself
  -Out <file.pptx>  output path (default: next to the input, same name)
  -Model <model>    model for the headless Claude Code run (default: opus)
  -Help             this text

ENGINE
  Claude Code (headless) + the official pptx skill. This script installs
  nothing; install the skill once from an interactive Claude Code session:
    /plugin marketplace add anthropics/skills
    /plugin install document-skills@anthropic-agent-skills

EXAMPLES
  ./md2pptx.ps1 ../projects/agentic-platform/renders/agentic-platform-it-deck.md
  ./md2pptx.ps1 deck.md -Template ../projects/lib-acme/sources/acme.potx
  ./md2pptx.ps1 deck.md -Out out/deck.pptx
'@
}

if ($Help -or -not $Md) { Show-Usage; return }

$claude = Get-Command 'claude' -CommandType Application -ErrorAction SilentlyContinue
if (-not $claude) {
    throw 'claude CLI not found on PATH - md2pptx runs on headless Claude Code.'
}

$MdFull = (Resolve-Path -LiteralPath $Md).Path

# --- resolve the template -------------------------------------------------
$TemplateFull = $null
if ($Template) {
    if (-not (Test-Path -LiteralPath $Template)) {
        throw "Template '$Template' not found - name a .potx or .pptx file by path."
    }
    if ([System.IO.Path]::GetExtension($Template) -notin '.potx', '.pptx') {
        throw "Template '$Template' is not a .potx or .pptx file."
    }
    $TemplateFull = (Resolve-Path -LiteralPath $Template).Path
}

# --- resolve the output ---------------------------------------------------
if (-not $Out) {
    $Out = Join-Path (Split-Path $MdFull -Parent) `
        ([System.IO.Path]::GetFileNameWithoutExtension($MdFull) + '.pptx')
}
# resolve against the PowerShell location, not the .NET process cwd
$OutFull = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($Out)

# --- build the prompt and run headless Claude -----------------------------
$templateLine = if ($TemplateFull) {
    "Start from the existing PowerPoint template at $TemplateFull - keep its theme, colours, fonts and layouts."
}
else {
    'No template is given - design a clean, professional visual style yourself.'
}

$prompt = @"
Use the document-skills:pptx skill (invoke it via the Skill tool before doing anything else).

Read the deck definition at $MdFull. It is a free-form Markdown deck definition that contains both the slide content and instructions for you - follow them. Where the definition uses such markers, content marked "On slide" belongs on the slide and "Speaker notes" become the slide's speaker notes.
$templateLine
Create the presentation and write it to $OutFull. Write no other files.
"@

Write-Host ("md2pptx   {0} -> {1}" -f (Split-Path $MdFull -Leaf), $OutFull)
Write-Host ("template  {0}" -f $(if ($TemplateFull) { $TemplateFull } else { "none - Claude's own design" }))
Write-Host 'Generating - this typically takes a few minutes...'

& $claude.Source -p $prompt --model $Model --allowedTools 'Skill,Read,Write,Edit,Bash,Glob,Grep'
if ($LASTEXITCODE -ne 0) { throw "claude exited with code $LASTEXITCODE." }
if (-not (Test-Path -LiteralPath $OutFull)) { throw 'claude finished but produced no output file.' }

$size = [math]::Round((Get-Item -LiteralPath $OutFull).Length / 1KB, 0)
Write-Host ("OK  {0} ({1} kB)" -f $OutFull, $size) -ForegroundColor Green
