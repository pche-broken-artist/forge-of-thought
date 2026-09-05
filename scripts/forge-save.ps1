#Requires -Version 7
<#
.SYNOPSIS
    Save the Forge to git: commit and push - the engine and every
    project that is a repository of its own.

.DESCRIPTION
    The engine (this repository) and the projects under projects/ are
    separate git repositories; the engine does not track projects/
    (only its own project, projects/forge). Without arguments the
    script visits the engine and every projects/<slug>/.git and gives
    each one with changes its own commit. With a slug it saves that one
    repository only ('forge' means the engine). A project directory
    without a repository is skipped with a note (bare) or refused
    (slug).

    Per repository: stage everything, commit (message from -m, or a
    generated one), then - when an origin is configured - integrate
    remote changes by rebase and push. Without an origin the commit is
    kept locally and reported. With -Tag <name> (one repository, so a
    slug is required) the commit is tagged and the tag pushed with it;
    when there is nothing to commit, the current HEAD is tagged, so a
    tag can mark a state before a large change. An existing tag is
    refused. The script never sets an identity, a
    remote or initialises a repository: those are one-off acts at a
    project's creation, and instance facts never live in the scripts.
    It never uses git add -f and never git clean.

.EXAMPLE
    ./scripts/forge-save.ps1                  # every repository with changes
    ./scripts/forge-save.ps1 flow-ba          # only projects/flow-ba
    ./scripts/forge-save.ps1 forge            # only the engine
    ./scripts/forge-save.ps1 -m "my message"  # custom commit message
    ./scripts/forge-save.ps1 forge -Tag v3.33  # save the engine and tag the commit
#>
param(
    [Parameter(Position = 0)]
    [string]$Slug,

    [Alias('m')]
    [string]$Message,

    [string]$Tag
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
if ($Tag -and -not $Slug) {
    Fail "-Tag needs one repository: name the slug ('forge' for the engine)."
}

# --- the repositories to visit ------------------------------------------
# Each entry: Name (label), Path (directory). The engine first.
$repos = @()
if ($Slug -and $Slug -ne 'forge') {
    $path = Join-Path $RepoRoot 'projects' $Slug
    if (-not (Test-Path $path)) { Fail "Project '$Slug' not found ($path does not exist)." }
    if (-not (Test-Path (Join-Path $path '.git'))) {
        Fail "Project '$Slug' is not a repository - run 'git -C projects/$Slug init -b main' once, then save."
    }
    $repos += @{ Name = $Slug; Path = $path }
} else {
    $repos += @{ Name = 'forge (engine)'; Path = $RepoRoot }
    if (-not $Slug) {
        $projectsDir = Join-Path $RepoRoot 'projects'
        Get-ChildItem -Path $projectsDir -Directory | Where-Object { $_.Name -ne 'forge' } | ForEach-Object {
            if (Test-Path (Join-Path $_.FullName '.git')) {
                $repos += @{ Name = $_.Name; Path = $_.FullName }
            } else {
                Write-Host ("{0,-20} not under git - skipped" -f $_.Name) -ForegroundColor DarkGray
            }
        }
    }
}

# --- save one repository ------------------------------------------------
function Save-Repo([string]$Name, [string]$Path) {
    Push-Location $Path
    try {
        if (-not (git config user.email)) {
            Write-Host ("{0,-20} no commit identity - set it once: git -C '{1}' config user.name/user.email" -f $Name, $Path) -ForegroundColor Yellow
            return
        }

        if ($Tag) {
            git rev-parse --verify --quiet "refs/tags/$Tag" *> $null
            if ($LASTEXITCODE -eq 0) { Fail "Tag '$Tag' already exists in $Name - nothing was changed." }
        }

        git add -A
        git diff --cached --quiet
        $nothingToCommit = ($LASTEXITCODE -eq 0)
        if ($nothingToCommit -and -not $Tag) {
            Write-Host ("{0,-20} nothing to save" -f $Name) -ForegroundColor DarkGray
            return
        }

        $msg = $Message
        if (-not $msg -and -not $nothingToCommit) {
            $files = @(git diff --cached --name-only)
            $scope = if ($Name -like 'forge*') { 'forge' } else { $Name }
            $shown = ($files | Select-Object -First 5) -join ', '
            $more = if ($files.Count -gt 5) { ", +$($files.Count - 5) more" } else { '' }
            $msg = "${scope}: $($files.Count) file(s) - $shown$more"
        }

        if ($nothingToCommit) {
            Write-Host ("{0,-20} nothing to commit - tagging the current state" -f $Name) -ForegroundColor DarkGray
        } else {
            git commit -m $msg | Out-Null
            if ($LASTEXITCODE -ne 0) { Fail "Commit failed in $Name." }
            Write-Host ("{0,-20} committed: {1}" -f $Name, $msg)
            git diff-tree --no-commit-id --stat -r HEAD | Write-Host
        }

        if ($Tag) {
            git tag $Tag
            if ($LASTEXITCODE -ne 0) { Fail "Tag '$Tag' could not be created in $Name." }
            Write-Host ("{0,-20} tagged: {1}" -f $Name, $Tag)
        }

        $origin = git remote get-url origin 2>$null
        if (-not $origin) {
            $kept = if ($Tag) { 'commit and tag kept locally' } else { 'commit kept locally' }
            Write-Host ("{0,-20} not pushed - no origin configured ({1})" -f $Name, $kept) -ForegroundColor Yellow
            return
        }

        $branch = git rev-parse --abbrev-ref HEAD
        git ls-remote --exit-code --heads origin $branch *> $null
        if ($LASTEXITCODE -eq 0) {
            git pull --rebase origin $branch
            if ($LASTEXITCODE -ne 0) {
                git rebase --abort 2>$null
                Fail "Remote changes in $Name conflict with yours. Nothing was lost - ask Claude for help before doing anything else."
            }
        }

        git push -u origin $branch
        if ($LASTEXITCODE -ne 0) { Fail "Push failed in $Name. Check network / remote access and try again." }
        if ($Tag) {
            git push origin $Tag
            if ($LASTEXITCODE -ne 0) { Fail "Tag '$Tag' was created but could not be pushed from $Name. Push it later: git -C '$Path' push origin $Tag" }
        }
        $what = if ($Tag) { "saved and pushed (with tag $Tag) to {1}" } else { 'saved and pushed to {1}' }
        Write-Host (("{0,-20} " + $what) -f $Name, $origin) -ForegroundColor Green
    } finally {
        Pop-Location
    }
}

foreach ($r in $repos) { Save-Repo $r.Name $r.Path }
