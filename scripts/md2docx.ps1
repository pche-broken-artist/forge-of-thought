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
    its own paper.

    Use -Help for a short usage summary.
#>
param(
    # Markdown render (e.g. projects/<slug>/renders/<recipe>.md).
    [Parameter(Position = 0)]
    [string]$Md,

    # Path to a .docx, .dotx or .dotm whose styles the output takes (pandoc
    # --reference-doc). Default: none - pandoc's built-in styles.
    [string]$Reference,

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
md2docx.ps1 - convert a Markdown render into a Word document with pandoc

USAGE
  ./md2docx.ps1 <render.md> [-Reference <styles.docx>] [-PageSize A4|Letter] [-Out <file.docx>]

  <render.md>         the Markdown render; its YAML front-matter is
                      metadata and does not appear in the document
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
