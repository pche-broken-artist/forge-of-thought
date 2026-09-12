#Requires -Version 7.0
<#
.SYNOPSIS
    Converts a Markdown render into a Word document with pandoc.

.DESCRIPTION
    The conversion is deterministic: pandoc reads the Markdown and
    writes a .docx, nothing is interpreted by a model. The Markdown
    render stays the source of truth; the .docx is a derivation for
    recipients who read Word.

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
    .docx>, typically a file in a library project (projects/lib-<company>/
    sources/). pandoc takes the styles of the reference document and
    ignores its content. Without -Reference, pandoc's built-in styles
    apply.

    Use -Help for a short usage summary.
#>
param(
    # Markdown render (e.g. projects/<slug>/renders/<recipe>.md).
    [Parameter(Position = 0)]
    [string]$Md,

    # Path to a .docx whose styles the output takes (pandoc
    # --reference-doc). Default: none - pandoc's built-in styles.
    [string]$Reference,

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
md2docx.ps1 - convert a Markdown render into a Word document with pandoc

USAGE
  ./md2docx.ps1 <render.md> [-Reference <styles.docx>] [-Out <file.docx>]

  <render.md>         the Markdown render; its YAML front-matter is
                      metadata and does not appear in the document
  -Reference <path>   a .docx whose styles the output takes (its
                      content is ignored), e.g. a file in a library
                      project's sources/; without it pandoc's built-in
                      styles apply
  -Out <file.docx>    output path (default: next to the input, same name)
  -Help               this text

ENGINE
  pandoc, resolved from PATH. This script installs nothing; install
  pandoc once from https://pandoc.org/installing.html.

LIMITS
  Mermaid diagrams are not rendered - they appear as blocks of code.

EXAMPLES
  ./md2docx.ps1 ../projects/forge/renders/executive-pitch.md
  ./md2docx.ps1 brd.md -Reference ../projects/lib-acme/sources/acme.docx
  ./md2docx.ps1 brd.md -Out out/brd.docx
'@
}

if ($Help -or -not $Md) { Show-Usage; return }

$pandoc = Get-Command 'pandoc' -CommandType Application -ErrorAction SilentlyContinue
if (-not $pandoc) {
    throw 'pandoc not found on PATH - install it from https://pandoc.org/installing.html.'
}

if (-not (Test-Path -LiteralPath $Md)) { throw "Input '$Md' not found." }
$MdFull = (Resolve-Path -LiteralPath $Md).Path

# --- resolve the reference document ---------------------------------------
$ReferenceFull = $null
if ($Reference) {
    if (-not (Test-Path -LiteralPath $Reference)) {
        throw "Reference '$Reference' not found - name a .docx file by path."
    }
    if ([System.IO.Path]::GetExtension($Reference) -ne '.docx') {
        throw "Reference '$Reference' is not a .docx file."
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
if ($ReferenceFull) { $args += @('--reference-doc', $ReferenceFull) }

Write-Host ("md2docx    {0} -> {1}" -f (Split-Path $MdFull -Leaf), $OutFull)
Write-Host ("reference  {0}" -f $(if ($ReferenceFull) { $ReferenceFull } else { "none - pandoc's built-in styles" }))

& $pandoc.Source @args
if ($LASTEXITCODE -ne 0) { throw "pandoc exited with code $LASTEXITCODE." }
if (-not (Test-Path -LiteralPath $OutFull)) { throw 'pandoc finished but produced no output file.' }

$size = [math]::Round((Get-Item -LiteralPath $OutFull).Length / 1KB, 0)
Write-Host ("OK  {0} ({1} kB)" -f $OutFull, $size) -ForegroundColor Green
