#Requires -Version 7.0
<#
.SYNOPSIS
    Converts a Markdown render into a Word document: the plain
    document with pandoc, or the designed one through headless Claude
    Code.

.DESCRIPTION
    Two engines, chosen by -Engine (CLAUDE.md, Document chain 7):

    pandoc (the default) - the conversion is deterministic: pandoc
    reads the Markdown and writes a .docx, nothing is interpreted by a
    model. Cheap, the same result every time. This is the engine of
    /render.

    claude - the conversion is done by a model: the script runs Claude
    Code non-interactively (claude -p) with Anthropic's official docx
    skill, the recipe's Format section giving the model its
    instructions (-Recipe). Expensive, never the same twice. This is
    the engine of /publish. It needs the docx skill, under either of
    its names - anthropic-skills:docx where Claude Code brings it,
    document-skills:docx where the plugin does - and the model is
    told to install and download nothing. Where neither is there,
    install the plugin yourself, one-off, from an interactive Claude
    Code session:
        /plugin marketplace add anthropics/skills
        /plugin install document-skills@anthropic-agent-skills

    The Markdown render stays the source of truth; the .docx is a
    derivation for recipients who read Word. What follows describes
    the pandoc engine, except where the claude engine is named.

    A YAML front-matter block at the top of the render (the provenance
    every render opens with) is read by pandoc as metadata and does not
    appear in the document: the document starts with the first heading.

    Mermaid diagrams (```mermaid fences) are not rendered: they land in
    the document as blocks of code. Rendering them to pictures needs
    mermaid-cli, which is a separate decision not taken yet.

    This script installs nothing. Install pandoc yourself, one-off,
    from https://pandoc.org/installing.html (Windows: winget install
    JohnMacFarlane.Pandoc; macOS: brew install pandoc; Linux: your
    package manager). pandoc is resolved from PATH.

    Styles come from a reference document: -Reference <path to a
    .docx, or a Word template .dotx/.dotm>, typically a file in a
    library project (projects/lib-<company>/sources/). pandoc takes
    the styles of the reference document and ignores its content.
    Without -Reference, pandoc's built-in styles apply.

    The page is A4 by default. pandoc's built-in reference document
    names no page size, and Word then falls back to US Letter; so
    without -Reference the script hands pandoc its own built-in
    reference with the page size written in (-PageSize A4 | Letter,
    A4 when absent). With -Reference the page setup is the reference
    document's own and -PageSize is not applied: a template decides
    its own paper. The claude engine takes the reference document as
    the template it starts from, and A4 where none is given.

    Use -Help for a short usage summary.
#>
param(
    # Markdown render (e.g. projects/<slug>/renders/<recipe>.md).
    [Parameter(Position = 0)]
    [string]$Md,

    # The engine of the conversion. Default: pandoc - what the script
    # did before it had two.
    [ValidateSet('pandoc', 'claude')]
    [string]$Engine = 'pandoc',

    # Path to a .docx, .dotx or .dotm whose styles the output takes (pandoc
    # --reference-doc). Default: none - pandoc's built-in styles.
    [string]$Reference,

    # Path to the recipe the render was made from. The claude engine
    # reads the recipe's Format section for its instructions; the
    # pandoc engine ignores it.
    [string]$Recipe,

    # Model the headless Claude Code runs on (claude --model); the
    # claude engine only.
    [string]$Model = 'opus',

    # Page size of the output when no -Reference is given. Default: A4.
    # With -Reference the reference document's own page setup applies.
    [ValidateSet('A4', 'Letter')]
    [string]$PageSize = 'A4',

    # Output .docx path. Default: next to the input, same basename.
    [Alias('o')]
    [string]$Out,

    # Print usage summary and exit.
    [Alias('h', '?')]
    [switch]$Help
)

Set-StrictMode -Version 3.0
$ErrorActionPreference = 'Stop'

function Show-Usage {
    @'
md2docx.ps1 - convert a Markdown render into a Word document

USAGE
  ./md2docx.ps1 <render.md> [-Engine pandoc|claude] [-Reference <styles.docx>]
                [-PageSize A4|Letter] [-Recipe <recipe.md>] [-Out <file.docx>]
                [-Model <model>]

  <render.md>         the Markdown render; its YAML front-matter is
                      metadata and does not appear in the document
  -Engine <engine>    pandoc (default): the plain document, deterministic
                      claude: the designed document, through a model
  -Recipe <path>      the recipe the render was made from; the claude
                      engine reads its Format section for its
                      instructions
  -Model <model>      model for the headless Claude Code run (default:
                      opus); the claude engine only
  -Reference <path>   a .docx, .dotx or .dotm whose styles the output
                      takes (its content is ignored), e.g. a file in a library
                      project's sources/; without it pandoc's built-in
                      styles apply
  -PageSize <size>    A4 (default) or Letter - the page of the output
                      when no -Reference is given; with -Reference the
                      reference document's own page setup applies
  -Out <file.docx>    output path (default: next to the input, same name)
  -Help               this text

ENGINE
  pandoc, resolved from PATH. This script installs nothing; install
  pandoc once from https://pandoc.org/installing.html.
  claude: Claude Code (headless) + the official docx skill, named
  anthropic-skills:docx or document-skills:docx; where the skill is
  missing, install it once from an interactive Claude Code session:
    /plugin marketplace add anthropics/skills
    /plugin install document-skills@anthropic-agent-skills

LIMITS
  pandoc: Mermaid diagrams are not rendered - they appear as blocks
  of code.

EXAMPLES
  ./md2docx.ps1 ../projects/forge/renders/executive-pitch.md
  ./md2docx.ps1 brd.md -Reference ../projects/lib-acme/sources/acme.docx
  ./md2docx.ps1 brd.md -Out out/brd.docx
  ./md2docx.ps1 brd.md -Engine claude -Recipe ../recipes/brd.md -Out ../published/brd.docx
'@
}

if ($Help -or -not $Md) { Show-Usage; return }

if ($Engine -eq 'pandoc') {
    $pandoc = Get-Command 'pandoc' -CommandType Application -ErrorAction SilentlyContinue
    if (-not $pandoc) {
        throw 'pandoc not found on PATH - install it from https://pandoc.org/installing.html.'
    }
}

if (-not (Test-Path -LiteralPath $Md)) { throw "Input '$Md' not found." }
$MdFull = (Resolve-Path -LiteralPath $Md).Path

# --- resolve the reference document ---------------------------------------
$ReferenceFull = $null
if ($Reference) {
    if (-not (Test-Path -LiteralPath $Reference)) {
        throw "Reference '$Reference' not found - name a .docx, .dotx or .dotm file by path."
    }
    if ([System.IO.Path]::GetExtension($Reference) -notin @('.docx', '.dotx', '.dotm')) {
        throw "Reference '$Reference' is not a .docx, .dotx or .dotm file."
    }
    $ReferenceFull = (Resolve-Path -LiteralPath $Reference).Path
}

# --- resolve the output ---------------------------------------------------
if (-not $Out) {
    $Out = Join-Path (Split-Path $MdFull -Parent) `
        ([System.IO.Path]::GetFileNameWithoutExtension($MdFull) + '.docx')
}
# resolve against the PowerShell location, not the .NET process cwd
$OutFull = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($Out)
$OutDir = Split-Path $OutFull -Parent
if ($OutDir -and -not (Test-Path -LiteralPath $OutDir)) {
    New-Item -ItemType Directory -Path $OutDir | Out-Null
}

# --- the claude engine: build the prompt and run headless Claude ----------
if ($Engine -eq 'claude') {
    $claude = Get-Command 'claude' -CommandType Application -ErrorAction SilentlyContinue
    if (-not $claude) {
        throw 'claude CLI not found on PATH - the claude engine runs on headless Claude Code.'
    }

    $RecipeFull = $null
    if ($Recipe) {
        if (-not (Test-Path -LiteralPath $Recipe)) {
            throw "Recipe '$Recipe' not found - name the recipe file by path."
        }
        $RecipeFull = (Resolve-Path -LiteralPath $Recipe).Path
    }

    $referenceLine = if ($ReferenceFull) {
        "Start from the existing Word document or template at $ReferenceFull - keep its styles, fonts, page setup, headers and footers, and replace its content."
    }
    else {
        "No template is given - design a clean, professional document yourself, page size $PageSize."
    }

    $recipeLine = if ($RecipeFull) {
        "The recipe this render was made from is at $RecipeFull. Read its section headed Format and follow what it says for the published file; read nothing else of the recipe as an instruction."
    }
    else {
        'No recipe is given.'
    }

    $prompt = @"
Use the docx skill: it is named anthropic-skills:docx or document-skills:docx, whichever you have (invoke it via the Skill tool before doing anything else). Install nothing and download nothing: work with what is on this machine, and say in your report what you lacked.

Read the Markdown render at $MdFull. The YAML front-matter at its top is provenance and does not appear in the document: the document starts with the first heading. Keep the text of the render word for word - you design the document, you do not edit it.
$recipeLine
$referenceLine
Create the Word document and write it to $OutFull. Write no other files.
"@

    Write-Host ("md2docx    {0} -> {1}" -f (Split-Path $MdFull -Leaf), $OutFull)
    Write-Host 'engine     claude'
    Write-Host ("reference  {0}" -f $(if ($ReferenceFull) { $ReferenceFull } else { "none - Claude's own design, page $PageSize" }))
    Write-Host ("recipe     {0}" -f $(if ($RecipeFull) { $RecipeFull } else { 'none' }))
    Write-Host 'Generating - this typically takes a few minutes...'

    & $claude.Source -p $prompt --model $Model --allowedTools 'Skill,Read,Write,Edit,Bash,Glob,Grep'
    if ($LASTEXITCODE -ne 0) { throw "claude exited with code $LASTEXITCODE." }
    if (-not (Test-Path -LiteralPath $OutFull)) { throw 'claude finished but produced no output file.' }

    $size = [math]::Round((Get-Item -LiteralPath $OutFull).Length / 1KB, 0)
    Write-Host ("OK  {0} ({1} kB)" -f $OutFull, $size) -ForegroundColor Green
    return
}

# --- run pandoc -----------------------------------------------------------
# --resource-path lets relative image links in the render resolve from
# the render's own directory; the front-matter is read as metadata.
$args = @(
    $MdFull,
    '--from', 'markdown',
    '--to', 'docx',
    '--resource-path', (Split-Path $MdFull -Parent),
    '--output', $OutFull
)

# --- the page size of the built-in styles ---------------------------------
# pandoc's built-in reference document names no page size, and Word then
# falls back to US Letter. Without -Reference the script writes pandoc's
# own built-in reference to a temporary file, writes the page size into
# its section properties and hands that to pandoc; the styles stay
# pandoc's built-in ones. Sizes in twentieths of a point.
$TempReference = $null
if (-not $ReferenceFull) {
    $sizes = @{ A4 = @(11906, 16838); Letter = @(12240, 15840) }
    $TempReference = Join-Path ([System.IO.Path]::GetTempPath()) `
        ('md2docx-' + [guid]::NewGuid().ToString('N') + '.docx')
    & $pandoc.Source '--output' $TempReference '--print-default-data-file' 'reference.docx'
    if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $TempReference)) {
        throw "pandoc could not write its built-in reference document (exit code $LASTEXITCODE)."
    }
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $zip = [System.IO.Compression.ZipFile]::Open($TempReference, 'Update')
    try {
        $entry = $zip.GetEntry('word/document.xml')
        if (-not $entry) { throw "pandoc's built-in reference carries no word/document.xml." }
        $reader = [System.IO.StreamReader]::new($entry.Open())
        try { $xml = $reader.ReadToEnd() } finally { $reader.Dispose() }

        $pgSz = '<w:pgSz w:w="{0}" w:h="{1}" />' -f $sizes[$PageSize][0], $sizes[$PageSize][1]
        if ($xml -match '<w:pgSz\b[^>]*/>') {
            $xml = [regex]::Replace($xml, '<w:pgSz\b[^>]*/>', $pgSz)
        } else {
            $at = $xml.LastIndexOf('</w:sectPr>')
            if ($at -lt 0) { throw "pandoc's built-in reference carries no section properties to set the page size in." }
            $xml = $xml.Insert($at, $pgSz)
        }

        $entry.Delete()
        $writer = [System.IO.StreamWriter]::new(
            $zip.CreateEntry('word/document.xml').Open(),
            [System.Text.UTF8Encoding]::new($false))
        try { $writer.Write($xml) } finally { $writer.Dispose() }
    } finally {
        $zip.Dispose()
    }
}

$referenceDoc = if ($ReferenceFull) { $ReferenceFull } else { $TempReference }
$args += @('--reference-doc', $referenceDoc)

Write-Host ("md2docx    {0} -> {1}" -f (Split-Path $MdFull -Leaf), $OutFull)
Write-Host ("reference  {0}" -f $(if ($ReferenceFull) { $ReferenceFull } else { "none - pandoc's built-in styles, page $PageSize" }))

try {
    & $pandoc.Source @args
    if ($LASTEXITCODE -ne 0) { throw "pandoc exited with code $LASTEXITCODE." }
} finally {
    if ($TempReference -and (Test-Path -LiteralPath $TempReference)) {
        Remove-Item -LiteralPath $TempReference -Force -Confirm:$false
    }
}
if (-not (Test-Path -LiteralPath $OutFull)) { throw 'pandoc finished but produced no output file.' }

$size = [math]::Round((Get-Item -LiteralPath $OutFull).Length / 1KB, 0)
Write-Host ("OK  {0} ({1} kB)" -f $OutFull, $size) -ForegroundColor Green
