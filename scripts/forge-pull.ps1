#Requires -Version 7
<#
.SYNOPSIS
    Pull the latest Forge from its remotes - the engine (its upgrade
    channel) and every project that has an origin.

.DESCRIPTION
    Fast-forward only. Without arguments pulls the engine, then every
    projects/<slug>/.git with an origin configured; with a slug pulls
    that one repository ('forge' means the engine). A repository with
    unsaved changes is not touched: reported and skipped (bare) or
    refused (slug) - run forge-save.ps1 first, so a pull can never
    create a conflict in half-finished work. Projects without a
    repository or without an origin are reported and skipped.

.EXAMPLE
    ./scripts/forge-pull.ps1            # engine + every project with an origin
    ./scripts/forge-pull.ps1 forge      # the engine only (upgrade)
    ./scripts/forge-pull.ps1 flow-ba    # one project
#>
param(
    [Parameter(Position = 0)]
    [string]$Slug
)

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

$repos = @()
if ($Slug -and $Slug -ne 'forge') {
    $path = Join-Path $RepoRoot 'projects' $Slug
    if (-not (Test-Path $path)) { Fail "Project '$Slug' not found ($path does not exist)." }
    if (-not (Test-Path (Join-Path $path '.git'))) { Fail "Project '$Slug' is not a repository." }
    $repos += @{ Name = $Slug; Path = $path }
} else {
    $repos += @{ Name = 'forge (engine)'; Path = $RepoRoot }
    if (-not $Slug) {
        Get-ChildItem -Path (Join-Path $RepoRoot 'projects') -Directory | Where-Object { $_.Name -ne 'forge' } | ForEach-Object {
            if (Test-Path (Join-Path $_.FullName '.git')) {
                $repos += @{ Name = $_.Name; Path = $_.FullName }
            } else {
                Write-Host ("{0,-20} not under git - skipped" -f $_.Name) -ForegroundColor DarkGray
            }
        }
    }
}

$strict = [bool]$Slug
foreach ($r in $repos) {
    Push-Location $r.Path
    try {
        $origin = git remote get-url origin 2>$null
        if (-not $origin) {
            $t = "{0,-20} no origin - skipped" -f $r.Name
            if ($strict) { Fail $t } else { Write-Host $t -ForegroundColor DarkGray; continue }
        }
        if (git status --porcelain) {
            Write-Host ("{0,-20} has unsaved changes:" -f $r.Name) -ForegroundColor Yellow
            git status --short
            if ($strict) { Fail 'Run scripts/forge-save.ps1 first, then pull.' }
            Write-Host ("{0,-20} skipped" -f $r.Name) -ForegroundColor Yellow
            continue
        }
        $branch = git rev-parse --abbrev-ref HEAD
        git pull --ff-only origin $branch
        if ($LASTEXITCODE -ne 0) {
            Fail "Pull failed in $($r.Name) - local and remote history diverged. Run scripts/forge-save.ps1 (it reconciles both), or ask Claude."
        }
        Write-Host ("{0,-20} up to date" -f $r.Name) -ForegroundColor Green
    } finally {
        Pop-Location
    }
}
