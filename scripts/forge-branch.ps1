#Requires -Version 7
<#
.SYNOPSIS
    Switch one Forge repository to a branch, creating it if needed -
    or report which branch it is on.

.DESCRIPTION
    Branches are voluntary in the Forge: whoever wants one gets it
    through this script and never types git; whoever does not works on
    main and never meets it. The script does two things and nothing
    else: with a branch name it switches the repository to that
    branch, creating it from the current state when it does not exist
    yet ('main' switches back); without a name it reports the current
    branch and lists the branches the repository has.

    The repository is named by its slug ('forge' means the engine);
    there is no bare form, since switching every repository at once
    is never what anyone wants. Unsaved changes stop the switch: save
    first (forge-save), then switch, so nothing is carried across or
    lost. Merging, deleting and pushing branches stay with git: a new
    branch reaches the remote by the first forge-save made on it, a
    merge into main is done by hand or by merge request, and a
    release is made from main only.

.EXAMPLE
    ./scripts/forge-branch.ps1 forge              # which branch is the engine on
    ./scripts/forge-branch.ps1 forge work-release # switch the engine to work-release, creating it
    ./scripts/forge-branch.ps1 flow-ba main       # switch projects/flow-ba back to main
#>
param(
    [Parameter(Position = 0, Mandatory = $true)]
    [string]$Slug,

    [Parameter(Position = 1)]
    [string]$Branch
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

# --- the repository -----------------------------------------------------
if ($Slug -eq 'forge') {
    $Name = 'forge (engine)'
    $Path = $RepoRoot
} else {
    $Name = $Slug
    $Path = Join-Path $RepoRoot 'projects' $Slug
    if (-not (Test-Path $Path)) { Fail "Project '$Slug' not found ($Path does not exist)." }
}
if (-not (Test-Path (Join-Path $Path '.git'))) {
    Fail "'$Slug' is not a repository - nothing to switch."
}

Push-Location $Path
try {
    $current = git rev-parse --abbrev-ref HEAD 2>$null
    if ($LASTEXITCODE -ne 0 -or -not $current) { Fail "Cannot read the current branch of $Name." }

    # --- report -----------------------------------------------------------
    if (-not $Branch) {
        Write-Host ("{0,-20} on branch {1}" -f $Name, $current)
        $branches = @(git branch --format='%(refname:short)')
        if ($branches.Count -gt 1) {
            Write-Host ("{0,-20} branches: {1}" -f '', ($branches -join ', ')) -ForegroundColor DarkGray
        }
        exit 0
    }

    # --- switch -----------------------------------------------------------
    if ($Branch -eq $current) {
        Write-Host ("{0,-20} already on {1}" -f $Name, $Branch) -ForegroundColor DarkGray
        exit 0
    }

    $dirty = @(git status --porcelain)
    if ($dirty.Count -gt 0) {
        Fail "$Name has unsaved changes ($($dirty.Count) file(s)). Save first (forge-save $Slug), then switch."
    }

    git rev-parse --verify --quiet "refs/heads/$Branch" *> $null
    if ($LASTEXITCODE -eq 0) {
        git switch $Branch *> $null
        if ($LASTEXITCODE -ne 0) { Fail "Could not switch $Name to '$Branch'." }
        Write-Host ("{0,-20} switched to {1}" -f $Name, $Branch) -ForegroundColor Green
    } else {
        git switch -c $Branch *> $null
        if ($LASTEXITCODE -ne 0) { Fail "Could not create branch '$Branch' in $Name." }
        Write-Host ("{0,-20} created {1} from {2} and switched to it" -f $Name, $Branch, $current) -ForegroundColor Green
        Write-Host ("{0,-20} the branch reaches the remote with the first forge-save made on it" -f '') -ForegroundColor DarkGray
    }
} finally {
    Pop-Location
}
