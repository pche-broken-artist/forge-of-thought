#Requires -Version 7.0
<#
.SYNOPSIS
    Generates a PowerPoint deck from a Markdown deck definition: the
    designed deck through headless Claude Code, or a plain deck through
    pandoc.

.DESCRIPTION
    Two engines, chosen by -Engine (CLAUDE.md, Document chain, Renders):

    claude (the default) - the conversion is done by a model: the
    Markdown definition is deliberately free-form, and the recipe may
    carry instructions for the model (visual directions, diagrams to
    redraw, overflow handling). The script runs Claude Code
    non-interactively (claude -p) with Anthropic's official pptx skill.
    Expensive, never the same twice. This is the engine of /publish.

    pandoc - the conversion is deterministic: pandoc reads the Markdown
    and writes a .pptx, one slide per second-level heading, nothing
    interpreted by a model. Cheap, the same result every time, plain to
    look at: a deck for reading, not for showing. This is the engine of
    /render.

    This script installs nothing, and tells the model to install and
    download nothing either. The claude engine needs the pptx skill,
    under either of its names - anthropic-skills:pptx where Claude
    Code brings it, document-skills:pptx where the plugin does. Where
    neither is there, install the plugin yourself, one-off, from an
    interactive Claude Code session:
        /plugin marketplace add anthropics/skills
        /plugin install document-skills@anthropic-agent-skills
    For the pandoc engine install pandoc, one-off, from
    https://pandoc.org/installing.html. Both are resolved from PATH.

    A template is named by path: -Template <path to a .potx or .pptx>,
    typically a file in a library project (projects/lib-<company>/
    sources/). Without -Template, the claude engine designs the visual
    style itself and the pandoc engine uses pandoc's built-in one.

    Use -Help for a short usage summary.
#>
param(
    # Markdown deck definition (e.g. projects/<slug>/renders/<recipe>.md).
    [Parameter(Position = 0)]
    [string]$Md,

    # The engine of the conversion. Default: claude - what the script
    # did before it had two.
    [ValidateSet('pandoc', 'claude')]
    [string]$Engine = 'claude',

    # Path to a .potx or .pptx template (relative to the current
    # directory or absolute). Default: none.
    [string]$Template,

    # Path to the recipe the definition was rendered from. The claude
    # engine reads the recipe's Format section for its instructions;
    # the pandoc engine ignores it.
    [string]$Recipe,

    # Output .pptx path. Default: next to the input, same basename.
    [Alias('o')]
    [string]$Out,

    # Model the headless Claude Code runs on (claude --model); the
    # claude engine only.
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
  ./md2pptx.ps1 <definition.md> [-Engine pandoc|claude] [-Template <file.potx>]
                [-Recipe <recipe.md>] [-Out <file.pptx>] [-Model <model>]

  <definition.md>   the Markdown deck definition, one section per slide
  -Engine <engine>  claude (default): the designed deck, through a model
                    pandoc: a plain deck for reading, deterministic
  -Template <path>  a .potx or .pptx template, named by path (e.g. a
                    file in a library project's sources/); without it
                    claude designs the visual style itself and pandoc
                    uses its built-in one
  -Recipe <path>    the recipe the definition was rendered from; the
                    claude engine reads its Format section for its
                    instructions
  -Out <file.pptx>  output path (default: next to the input, same name)
  -Model <model>    model for the headless Claude Code run (default:
                    opus); the claude engine only
  -Help             this text

ENGINE
  claude: Claude Code (headless) + the official pptx skill, named
  anthropic-skills:pptx or document-skills:pptx. This script installs
  nothing; where the skill is missing, install it once from an
  interactive Claude Code session:
    /plugin marketplace add anthropics/skills
    /plugin install document-skills@anthropic-agent-skills
  pandoc: resolved from PATH; install it once from
  https://pandoc.org/installing.html.

EXAMPLES
  ./md2pptx.ps1 ../projects/agentic-platform/renders/agentic-platform-it-deck.md
  ./md2pptx.ps1 deck.md -Template ../projects/lib-acme/sources/acme.potx
  ./md2pptx.ps1 deck.md -Engine pandoc
  ./md2pptx.ps1 deck.md -Recipe ../recipes/deck.md -Out ../published/deck.pptx
'@
}

if ($Help -or -not $Md) { Show-Usage; return }

if (-not (Test-Path -LiteralPath $Md)) { throw "Input '$Md' not found." }
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

# --- resolve the recipe ---------------------------------------------------
$RecipeFull = $null
if ($Recipe) {
    if (-not (Test-Path -LiteralPath $Recipe)) {
        throw "Recipe '$Recipe' not found - name the recipe file by path."
    }
    $RecipeFull = (Resolve-Path -LiteralPath $Recipe).Path
}

# --- resolve the output ---------------------------------------------------
if (-not $Out) {
    $Out = Join-Path (Split-Path $MdFull -Parent) `
        ([System.IO.Path]::GetFileNameWithoutExtension($MdFull) + '.pptx')
}
# resolve against the PowerShell location, not the .NET process cwd
$OutFull = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($Out)
$OutDir = Split-Path $OutFull -Parent
if ($OutDir -and -not (Test-Path -LiteralPath $OutDir)) {
    New-Item -ItemType Directory -Path $OutDir | Out-Null
}

Write-Host ("md2pptx   {0} -> {1}" -f (Split-Path $MdFull -Leaf), $OutFull)
Write-Host ("engine    {0}" -f $Engine)

if ($Engine -eq 'pandoc') {
    # --- run pandoc -------------------------------------------------------
    # One slide per second-level heading, as the deck definition names
    # its slides; the front-matter is read as metadata.
    $pandoc = Get-Command 'pandoc' -CommandType Application -ErrorAction SilentlyContinue
    if (-not $pandoc) {
        throw 'pandoc not found on PATH - install it from https://pandoc.org/installing.html.'
    }

    $pandocArgs = @(
        $MdFull,
        '--from', 'markdown',
        '--to', 'pptx',
        '--slide-level', '2',
        '--resource-path', (Split-Path $MdFull -Parent),
        '--output', $OutFull
    )
    if ($TemplateFull) { $pandocArgs += @('--reference-doc', $TemplateFull) }

    Write-Host ("template  {0}" -f $(if ($TemplateFull) { $TemplateFull } else { "none - pandoc's built-in style" }))

    & $pandoc.Source @pandocArgs
    if ($LASTEXITCODE -ne 0) { throw "pandoc exited with code $LASTEXITCODE." }
    if (-not (Test-Path -LiteralPath $OutFull)) { throw 'pandoc finished but produced no output file.' }
}
else {
    # --- build the prompt and run headless Claude -------------------------
    $claude = Get-Command 'claude' -CommandType Application -ErrorAction SilentlyContinue
    if (-not $claude) {
        throw 'claude CLI not found on PATH - the claude engine runs on headless Claude Code.'
    }

    $templateLine = if ($TemplateFull) {
        "Start from the existing PowerPoint template at $TemplateFull - keep its theme, colours, fonts and layouts."
    }
    else {
        'No template is given - design a clean, professional visual style yourself.'
    }

    # The alias Build instructions -> Format: templates/recipe.md, Format.
    $recipeLine = if ($RecipeFull) {
        "The recipe this definition was rendered from is at $RecipeFull. Read its section headed Format (in an older recipe: Build instructions) and follow what it says for the published file; read nothing else of the recipe as an instruction."
    }
    else {
        'No recipe is given - where the definition itself carries instructions for you, follow them.'
    }

    $prompt = @"
Use the pptx skill: it is named anthropic-skills:pptx or document-skills:pptx, whichever you have (invoke it via the Skill tool before doing anything else). Install nothing and download nothing: work with what is on this machine, and say in your report what you lacked.

Read the deck definition at $MdFull. It is a free-form Markdown deck definition, one section per slide. Where the definition uses such markers, content marked "On slide" belongs on the slide and "Speaker notes" become the slide's speaker notes. Keep the text of the definition word for word.
$recipeLine
$templateLine
Create the presentation and write it to $OutFull. Write no other files.
"@

    Write-Host ("template  {0}" -f $(if ($TemplateFull) { $TemplateFull } else { "none - Claude's own design" }))
    Write-Host ("recipe    {0}" -f $(if ($RecipeFull) { $RecipeFull } else { 'none' }))
    Write-Host 'Generating - this typically takes a few minutes...'

    & $claude.Source -p $prompt --model $Model --allowedTools 'Skill,Read,Write,Edit,Bash,Glob,Grep'
    if ($LASTEXITCODE -ne 0) { throw "claude exited with code $LASTEXITCODE." }
    if (-not (Test-Path -LiteralPath $OutFull)) { throw 'claude finished but produced no output file.' }
}

$size = [math]::Round((Get-Item -LiteralPath $OutFull).Length / 1KB, 0)
Write-Host ("OK  {0} ({1} kB)" -f $OutFull, $size) -ForegroundColor Green
