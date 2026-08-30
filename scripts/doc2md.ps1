#Requires -Version 7.0
<#
.SYNOPSIS
    Converts documents (Word / PowerPoint / PDF / Excel) to Markdown using markitdown.

.DESCRIPTION
    Accepts three input notations, which can be mixed and repeated freely:

      1) a single file name   ./doc2md.ps1 report.docx
      2) glob / star notation ./doc2md.ps1 *.pdf, docs/**/*.pptx
      3) a list file          ./doc2md.ps1 files.txt
         (plain text, one path or glob per line; '#' or ';' starts a comment;
          relative paths are resolved against the list file's own directory)
      +) a directory          ./doc2md.ps1 docs -Recurse

    Conversion is done exclusively by markitdown (MIT, Microsoft):
        https://github.com/microsoft/markitdown

    This script never installs anything. Install the engine yourself with:
        pip install "markitdown[docx,pptx,pdf,xlsx,xls]"

    Use -Help for a short usage summary, or -ListTools to verify the engine
    is reachable.
#>
[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Position = 0, ValueFromPipeline, ValueFromPipelineByPropertyName, ValueFromRemainingArguments)]
    [Alias('FullName', 'PSPath')]
    [string[]]$Path,

    # Output directory for the .md files. Default: next to each source file.
    [Alias('o')]
    [string]$OutDir,

    # Suffix inserted before the .md extension (e.g. '.extract' -> report.extract.md).
    [string]$Suffix,

    # Explicit path to the markitdown executable (otherwise resolved from PATH).
    [string]$MarkitdownPath,

    # Recurse into directories and into globs that do not contain '**'.
    [switch]$Recurse,

    # Overwrite existing .md files (default: skip them).
    [switch]$Force,

    # Treat every input as a list file, regardless of its extension.
    [switch]$AsList,

    # Print usage summary and exit.
    [Alias('h', '?')]
    [switch]$Help,

    # Check whether markitdown is available and exit.
    [switch]$ListTools
)

begin {
    Set-StrictMode -Version 3.0
    $ErrorActionPreference = 'Stop'

    $tokens = [System.Collections.Generic.List[string]]::new()

    # Extensions markitdown can read and that this script will pick up.
    $script:DocExt = @(
        '.pdf',
        '.docx', '.docm',
        '.pptx', '.pptm',
        '.xlsx', '.xlsm', '.xls',
        '.epub',
        '.html', '.htm',
        '.csv', '.json', '.xml',
        '.msg'
    )

    # Extensions treated as "a list of files" rather than as a document.
    $script:ListExt = @('.txt', '.lst', '.list', '.files', '.filelist')

    # Legacy binary formats markitdown cannot read - reported clearly instead of failing.
    $script:UnsupportedExt = @('.doc', '.ppt', '.odt', '.odp', '.ods', '.rtf', '.pages', '.key')

    function Show-Usage {
        @'
doc2md.ps1 - convert Word / PowerPoint / PDF / Excel documents to Markdown

USAGE
  ./doc2md.ps1 <input> [<input> ...] [-OutDir <dir>] [-Suffix <text>] [-Recurse]
               [-Force] [-AsList] [-MarkitdownPath <exe>] [-WhatIf] [-ListTools]
               [-Help]

INPUT (mix and repeat freely, also accepted from the pipeline)
  file            ./doc2md.ps1 report.docx
  glob            ./doc2md.ps1 *.pdf, docs/**/*.pptx
  list file       ./doc2md.ps1 files.txt
                  one path or glob per line; '#' or ';' = comment;
                  relative paths resolve against the list file's directory
  directory       ./doc2md.ps1 docs -Recurse

OPTIONS
  -OutDir <dir>   where to write .md files (default: next to the source file)
  -Suffix <text>  inserted before the .md extension
                  (e.g. -Suffix '.extract' -> report.extract.md)
  -Recurse        descend into directories and into globs without '**'
  -Force          overwrite existing .md files (default: skip them)
  -AsList         treat every input as a list file, whatever its extension
  -MarkitdownPath explicit path to the markitdown executable
  -WhatIf         show what would be converted, write nothing
  -ListTools      check that the engine is available, then exit
  -Help           this text        (full docs: Get-Help ./doc2md.ps1 -Full)

HANDLED EXTENSIONS
  .pdf .docx .docm .pptx .pptm .xlsx .xlsm .xls .epub .html .htm .csv .json .xml .msg
  Legacy binary .doc/.ppt/.rtf/.odt/.odp are reported as unsupported - resave
  them as .docx/.pptx first.

ENGINE
  markitdown (MIT) - https://github.com/microsoft/markitdown
  This script installs nothing. Install it yourself with:
    pip install "markitdown[docx,pptx,pdf,xlsx,xls]"

EXAMPLES
  ./doc2md.ps1 presentation.pptx
  ./doc2md.ps1 report.pdf -Suffix '.extract'
  ./doc2md.ps1 *.pdf, *.docx -OutDir md
  ./doc2md.ps1 files.txt -OutDir md -Force
  Get-ChildItem docs -Filter *.docx -Recurse | ./doc2md.ps1 -OutDir md
'@
    }

    function Resolve-Markitdown {
        if ($MarkitdownPath) {
            if (-not (Test-Path -LiteralPath $MarkitdownPath)) {
                throw "markitdown not found at '$MarkitdownPath'."
            }
            return (Resolve-Path -LiteralPath $MarkitdownPath).Path
        }
        $c = Get-Command 'markitdown' -CommandType Application -ErrorAction SilentlyContinue |
            Select-Object -First 1
        if ($c) { return $c.Source }
        return $null
    }

    # --- expand one input token into concrete file paths ------------------------
    function Resolve-Inputs {
        param(
            [string]$Token,
            [string]$BaseDir = (Get-Location).Path,
            [int]$Depth = 0
        )

        if ([string]::IsNullOrWhiteSpace($Token)) { return }
        if ($Depth -gt 5) {
            Write-Warning "List nesting too deep at '$Token' - skipped."
            return
        }

        $tok = $Token.Trim().Trim('"', "'")
        $candidate = if ([System.IO.Path]::IsPathRooted($tok)) { $tok } else { Join-Path $BaseDir $tok }

        # 1) star notation
        if ($tok -match '[*?]') {
            $deep    = $Recurse -or ($tok -match '\*\*')
            $pattern = $candidate -replace '\*\*[\\/]', '' -replace '\*\*', '*'
            $hits    = Get-ChildItem -Path $pattern -File -Recurse:$deep -ErrorAction SilentlyContinue
            if (-not $hits) { Write-Warning "Pattern '$tok' matched nothing."; return }
            foreach ($h in $hits) {
                if ($script:DocExt -contains $h.Extension.ToLower()) { $h.FullName }
            }
            return
        }

        $item = Get-Item -LiteralPath $candidate -ErrorAction SilentlyContinue
        if (-not $item) { Write-Warning "Not found: '$tok'"; return }

        # 2) directory
        if ($item.PSIsContainer) {
            Get-ChildItem -LiteralPath $item.FullName -File -Recurse:$Recurse |
                Where-Object { $script:DocExt -contains $_.Extension.ToLower() } |
                ForEach-Object { $_.FullName }
            return
        }

        $ext = $item.Extension.ToLower()

        # 3) list file
        if ($AsList -or ($script:ListExt -contains $ext)) {
            $listDir = $item.DirectoryName
            foreach ($line in (Get-Content -LiteralPath $item.FullName)) {
                $l = $line.Trim()
                if (-not $l -or $l.StartsWith('#') -or $l.StartsWith(';')) { continue }
                Resolve-Inputs -Token $l -BaseDir $listDir -Depth ($Depth + 1)
            }
            return
        }

        # 4) single document
        if ($script:DocExt -contains $ext) {
            $item.FullName
        }
        elseif ($script:UnsupportedExt -contains $ext) {
            Write-Warning "markitdown cannot read legacy format '$ext' - resave as .docx/.pptx/.xlsx: $($item.FullName)"
        }
        else {
            Write-Warning "Unsupported extension '$ext': $($item.FullName)"
        }
    }

    function Invoke-Markitdown {
        param([string]$Exe, [string]$Source, [string]$Target)

        $out = & $Exe $Source -o $Target 2>&1
        if ($LASTEXITCODE -ne 0) {
            $msg = if ($out) { ($out | Out-String).Trim() -replace '\s+', ' ' } else { '' }
            throw "markitdown exited with code $LASTEXITCODE$(if ($msg) { ": $msg" })"
        }
        if (-not (Test-Path -LiteralPath $Target)) {
            throw 'markitdown produced no output file.'
        }
    }
}

process {
    if ($Path) { foreach ($p in $Path) { $tokens.Add($p) } }
}

end {
    if ($Help) { Show-Usage; return }

    $exe = Resolve-Markitdown

    if ($ListTools) {
        if ($exe) {
            Write-Host "markitdown  OK   $exe" -ForegroundColor Green
        }
        else {
            Write-Host 'markitdown  --   not found on PATH' -ForegroundColor Red
            Write-Host ''
            Write-Host 'Install it with:' -ForegroundColor Yellow
            Write-Host '  pip install "markitdown[docx,pptx,pdf,xlsx,xls]"'
            Write-Host 'Then reopen the shell, or pass -MarkitdownPath <exe>.'
        }
        return
    }

    if ($tokens.Count -eq 0) {
        Show-Usage
        return
    }

    # -WhatIf only previews the resolved file list, so the engine is not needed there.
    if (-not $exe -and -not $WhatIfPreference) {
        throw 'markitdown not found. Install it with: pip install "markitdown[docx,pptx,pdf,xlsx,xls]" (or pass -MarkitdownPath).'
    }

    # 1) expand every input token
    $files = @()
    foreach ($t in $tokens) { $files += Resolve-Inputs -Token $t }
    $files = @($files | Sort-Object -Unique)

    if ($files.Count -eq 0) { Write-Warning 'No supported documents found.'; return }

    if ($OutDir) {
        $OutDir = [System.IO.Path]::GetFullPath($OutDir, (Get-Location).Path)
        if (-not (Test-Path -LiteralPath $OutDir)) {
            if ($WhatIfPreference) {
                Write-Host "What if: would create output directory '$OutDir'."
            }
            else {
                New-Item -ItemType Directory -Path $OutDir -Force | Out-Null
            }
        }
    }

    $written = [System.Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
    $ok = 0; $skipped = 0; $failed = 0
    $i = 0

    foreach ($f in $files) {
        $i++
        $name = Split-Path $f -Leaf
        Write-Progress -Activity 'doc2md' -Status "[$i/$($files.Count)] $name" `
            -PercentComplete ([int](100 * $i / $files.Count))

        $base   = [System.IO.Path]::GetFileNameWithoutExtension($f)
        $dir    = if ($OutDir) { $OutDir } else { Split-Path $f -Parent }
        $target = Join-Path $dir "$base$Suffix.md"

        # name collision within this run (e.g. flat -OutDir) -> _1, _2, ...
        if ($written.Contains($target)) {
            $n = 1
            do { $target = Join-Path $dir "${base}${Suffix}_$n.md"; $n++ } while ($written.Contains($target))
        }
        elseif ((Test-Path -LiteralPath $target) -and -not $Force) {
            Write-Host ("SKIP  {0}  -> already exists (use -Force)" -f $name) -ForegroundColor DarkYellow
            $skipped++
            continue
        }

        if (-not $PSCmdlet.ShouldProcess($f, "convert to '$target'")) { continue }

        try {
            Invoke-Markitdown -Exe $exe -Source $f -Target $target
            [void]$written.Add($target)
            $ok++
            $size = [math]::Round((Get-Item -LiteralPath $target).Length / 1KB, 1)
            Write-Host ("OK    {0,-45} -> {1} ({2} kB)" -f $name, (Split-Path $target -Leaf), $size) -ForegroundColor Green
        }
        catch {
            $failed++
            Write-Host ("FAIL  {0,-45} -> {1}" -f $name, $_.Exception.Message) -ForegroundColor Red
        }
    }

    Write-Progress -Activity 'doc2md' -Completed
    Write-Host ''
    Write-Host ("Done: {0} converted, {1} skipped, {2} failed." -f $ok, $skipped, $failed) `
        -ForegroundColor $(if ($failed) { 'Yellow' } else { 'Cyan' })

    if ($failed) { exit 1 }
}
