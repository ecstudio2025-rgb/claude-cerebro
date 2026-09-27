# Instala el Claude de Diego en Windows: skills, agentes, kb-mercado, hook-vault, CLAUDE.md y plugins.
#
# Instalar o actualizar (PowerShell, sin login):
#   irm https://raw.githubusercontent.com/ecstudio2025-rgb/claude-cerebro/main/instalar.ps1 | iex
#
# Las carpetas quedan enlazadas (junction) al repo local: volver a lanzar la linea de arriba hace git pull y listo.
# Lo que ya hubiera en ~/.claude con el mismo nombre se renombra a .bak-FECHA, nunca se borra.
# Solo ASCII a proposito: Windows PowerShell 5.1 lee mal los acentos en UTF-8 sin BOM.

$ErrorActionPreference = 'Stop'
$RepoUrl = 'https://github.com/ecstudio2025-rgb/claude-cerebro.git'
$Repo    = Join-Path $HOME 'claude-cerebro'
$Claude  = Join-Path $HOME '.claude'
$Stamp   = Get-Date -Format 'yyyyMMdd-HHmmss'
$Utf8    = New-Object System.Text.UTF8Encoding $false

function Refrescar-Path {
    $env:Path = [Environment]::GetEnvironmentVariable('Path', 'Machine') + ';' + [Environment]::GetEnvironmentVariable('Path', 'User')
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host 'Instalando Git...'
    winget install --id Git.Git -e --silent --accept-source-agreements --accept-package-agreements
    Refrescar-Path
    if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw 'Git instalado pero no aparece. Cierra PowerShell, abre uno nuevo y repite.' }
}

if (Test-Path (Join-Path $Repo '.git')) {
    Write-Host 'Actualizando el repo...'
    git -C $Repo pull --rebase --autostash -q
} else {
    Write-Host "Descargando en $Repo ..."
    git clone -q $RepoUrl $Repo
}
if ($LASTEXITCODE -ne 0) { throw "git fallo en $Repo" }

New-Item -ItemType Directory -Force -Path $Claude | Out-Null

function Enlazar([string]$Origen, [string]$Destino) {
    if (-not (Test-Path -LiteralPath $Origen)) { return }
    if (Test-Path -LiteralPath $Destino) {
        $item = Get-Item -LiteralPath $Destino -Force
        if ($item.LinkType -eq 'Junction') {
            if (@($item.Target)[0] -eq $Origen) { return }
            cmd /c rmdir "$Destino" | Out-Null          # quita solo el enlace, no el contenido
        } else {
            Rename-Item -LiteralPath $Destino -NewName "$(Split-Path $Destino -Leaf).bak-$Stamp"
            Write-Host "  copia de seguridad: $Destino.bak-$Stamp"
        }
    }
    New-Item -ItemType Junction -Path $Destino -Target $Origen | Out-Null
    Write-Host "  enlazado: $Destino"
}

Write-Host 'Carpetas:'
foreach ($d in 'skills', 'agents', 'commands', 'kb-mercado', 'hook-vault', 'templates') {
    Enlazar (Join-Path $Repo "claude\$d") (Join-Path $Claude $d)
}

Write-Host 'CLAUDE.md y guias (rutas del Mac cambiadas a las de este equipo):'
$HomeFwd = $HOME -replace '\\', '/'
foreach ($f in 'CLAUDE.md', 'voz-diego-marca.md', 'anti-patrones-ia-redaccion.md') {
    $origen  = Join-Path $Repo "claude\$f"
    if (-not (Test-Path $origen)) { continue }
    $destino = Join-Path $Claude $f
    $texto = [System.IO.File]::ReadAllText($origen, $Utf8).Replace('/Users/diego/', "$HomeFwd/")
    if ((Test-Path $destino) -and -not (Test-Path "$destino.bak-original")) { Copy-Item $destino "$destino.bak-original" }
    [System.IO.File]::WriteAllText($destino, $texto, $Utf8)
    Write-Host "  $destino"
}

Write-Host 'Ajustes:'
$Settings  = Join-Path $Claude 'settings.json'
$Plantilla = [System.IO.File]::ReadAllText((Join-Path $Repo 'settings.windows.json'), $Utf8) | ConvertFrom-Json
if (Test-Path $Settings) {
    Copy-Item $Settings "$Settings.bak-$Stamp"
    $Actual = [System.IO.File]::ReadAllText($Settings, $Utf8) | ConvertFrom-Json
    foreach ($p in $Plantilla.PSObject.Properties) {
        if (-not $Actual.PSObject.Properties[$p.Name]) {
            $Actual | Add-Member -NotePropertyName $p.Name -NotePropertyValue $p.Value
        } elseif ($p.Name -in 'enabledPlugins', 'extraKnownMarketplaces') {
            foreach ($q in $p.Value.PSObject.Properties) {
                if (-not $Actual.($p.Name).PSObject.Properties[$q.Name]) {
                    $Actual.($p.Name) | Add-Member -NotePropertyName $q.Name -NotePropertyValue $q.Value
                }
            }
        }
    }
    [System.IO.File]::WriteAllText($Settings, ($Actual | ConvertTo-Json -Depth 20), $Utf8)
    Write-Host "  fusionado con el settings.json que ya habia (copia en .bak-$Stamp)"
} else {
    [System.IO.File]::WriteAllText($Settings, ($Plantilla | ConvertTo-Json -Depth 20), $Utf8)
    Write-Host "  creado $Settings"
}

New-Item -ItemType Directory -Force -Path (Join-Path $HOME 'Claude') | Out-Null

if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    Write-Host 'Instalando Claude Code...'
    Invoke-RestMethod https://claude.ai/install.ps1 | Invoke-Expression
}

Write-Host ''
Write-Host "Listo. Abre una terminal nueva, entra en $HOME\Claude y lanza: claude"
Write-Host 'La primera vez te pide iniciar sesion y confirmar los plugins.'
Write-Host 'No vienen (son privados): la memoria, los MCP con token (Custom Soft Lab, facturas...) ni el acceso SSH al VPS.'
