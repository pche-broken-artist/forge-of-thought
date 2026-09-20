#Requires -Version 7
<#
.SYNOPSIS
    Report the git state of the Forge: the engine and every project.

.DESCRIPTION
    Read-only, changes nothing. First the global configuration file
    git actually reads, which /setup needs to know. Then, for the
    engine and each projects/<slug>: unsaved changes (or "clean"), the
    branch it is on, the last commit, and the origin - or "no origin" /
    "not under git". Exists so that even reading git state goes through
    the scripts (CLAUDE.md, Persistence).

.EXAMPLE
    ./scripts/forge-status.ps1
#>
$ErrorActionPreference = 'Stop'
$RepoRoot = Split-Path -Parent $PSScriptRoot

function Fail([string]$Text) {
    Write-Host "ERROR: $Text" -ForegroundColor Red
    exit 1
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Fail 'git is not installed.'
}
if (-not (Test-Path (Join-Path $RepoRoot '.git'))) {
    Fail 'The engine is not a git repository (clone it, do not copy it).'
}

function Show-Repo([string]$Name, [string]$Path) {
    Write-Host "== $Name" -ForegroundColor Cyan
    if (-not (Test-Path (Join-Path $Path '.git'))) {
        Write-Host '   not under git'
        Write-Host ''
        return
    }
    Push-Location $Path
    try {
        $changes = @(git status --short)
        if ($changes.Count -gt 0) {
            $changes | ForEach-Object { Write-Host "   $_" }
        } else {
            Write-Host '   clean - nothing to save' -ForegroundColor Green
        }
        $branch = git rev-parse --abbrev-ref HEAD 2>$null
        Write-Host ("   branch:      " + $(if ($branch) { $branch } else { 'none yet' }))
        $last = git log -1 --format='%h %s' 2>$null
        Write-Host ("   last commit: " + $(if ($last) { $last } else { 'none yet' }))
        $origin = git remote get-url origin 2>$null
        Write-Host ("   origin:      " + $(if ($origin) { $origin } else { 'no origin' }))
    } finally {
        Pop-Location
    }
    Write-Host ''
}

# The global configuration file git actually reads, named here so that
# /setup never has to ask git directly (CLAUDE.md, Persistence). With
# includes in play git names every file it read; the first is the
# global file itself.
$globalFiles = @(git config --global --list --show-origin 2>$null |
    ForEach-Object { if ($_ -match '^file:(.+?)\t') { $Matches[1] } } |
    Select-Object -Unique)
Write-Host ('global git config: ' + $(if ($globalFiles.Count -gt 0) { $globalFiles -join ', ' } else { 'none yet - git creates ~/.gitconfig at its first write' }))
Write-Host ''

Show-Repo 'forge (engine)' $RepoRoot
Get-ChildItem -Path (Join-Path $RepoRoot 'projects') -Directory | Where-Object { $_.Name -ne 'forge' } | ForEach-Object {
    Show-Repo $_.Name $_.FullName
}
