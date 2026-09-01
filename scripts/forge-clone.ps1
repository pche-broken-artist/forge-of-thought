#Requires -Version 7
<#
.SYNOPSIS
    Bring an existing project into the Forge - clone its repository
    into projects/ and, when given one, set its local commit identity.

.DESCRIPTION
    Clones the repository at the given URL into
    projects/<repository name> - the directory name falls out of the
    URL, and an existing directory is never overwritten. With -Name
    and -Email (both or neither) the repository's local commit
    identity is set; the script itself carries no identity and no URL.
    Afterwards it reports facts: the last commit, the origin, and
    whether the project carries a ledger with a kind: header - the
    absence of one is a fact, not a defect.

.EXAMPLE
    ./scripts/forge-clone.ps1 https://example.com/team/my-idea.git
    ./scripts/forge-clone.ps1 git@example.com:team/my-idea.git -Name 'A. User' -Email 'a.user@example.com'
#>
param(
    [Parameter(Mandatory, Position = 0)]
    [string]$Url,
    [string]$Name,
    [string]$Email
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
if (([bool]$Name) -ne ([bool]$Email)) {
    Fail 'Give -Name and -Email together, or neither.'
}

$repoName = ($Url.TrimEnd('/') -split '[/:]')[-1] -replace '\.git$', ''
if (-not $repoName) { Fail "Cannot derive a repository name from '$Url'." }

$target = Join-Path $RepoRoot 'projects' $repoName
if (Test-Path $target) {
    Fail "projects/$repoName already exists - never overwritten. Rename or remove it first."
}

git clone $Url $target
if ($LASTEXITCODE -ne 0) { Fail "Clone of $Url failed." }

if ($Name) {
    git -C $target config user.name $Name
    git -C $target config user.email $Email
}

$origin = git -C $target remote get-url origin 2>$null
$last = git -C $target log -1 --format='%h %ad %s' --date=short 2>$null

Write-Host ''
Write-Host "Cloned into projects/$repoName" -ForegroundColor Green
Write-Host "  origin:      $origin"
Write-Host "  last commit: $last"
if ($Name) {
    Write-Host "  identity:    $Name <$Email> (set locally)"
} else {
    Write-Host '  identity:    not set - forge-save will ask before the first commit'
}

$ledger = Join-Path $target 'ledger.md'
if (Test-Path $ledger) {
    $kind = (Select-String -Path $ledger -Pattern '^kind:\s*(\S+)' | Select-Object -First 1).Matches.Groups[1].Value
    if ($kind) {
        Write-Host "  ledger:      present, kind: $kind"
    } else {
        Write-Host '  ledger:      present, no kind: header'
    }
} else {
    Write-Host '  ledger:      none - not scaffolded by the forge (a fact, not a defect)'
}
