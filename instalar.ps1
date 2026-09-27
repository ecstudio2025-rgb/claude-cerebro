# Instala el Claude de Diego en Windows: skills, agentes, kb-mercado, CLAUDE.md, plugins y, con la clave del equipo, su memoria.
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

# --- Capa privada: memoria de Diego y skills con casos de clientes (clave del equipo) ---
$PrivUrl = 'https://socialimpulso.es/cerebro/privado.tar.gz'
$Priv    = Join-Path $Claude 'cerebro-privado'
$Clave   = $env:CEREBRO_CLAVE
if (-not $Clave) {
    $seg = Read-Host 'Clave del equipo para la memoria de Diego (Enter para saltar)' -AsSecureString
    $Clave = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($seg))
}
if ($Clave) {
    $tgz = Join-Path $env:TEMP "cerebro-$Stamp.tgz"
    $auth = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("equipo:$Clave"))
    try {
        Invoke-WebRequest -Uri $PrivUrl -Headers @{ Authorization = "Basic $auth" } -OutFile $tgz -UseBasicParsing
        if (Test-Path $Priv) { Remove-Item -Recurse -Force $Priv }
        tar -xzf $tgz -C $Claude
        $lista = Get-ChildItem -Recurse -File (Join-Path $Priv 'claude') | ForEach-Object { 'claude/' + $_.FullName.Substring((Join-Path $Priv 'claude').Length + 1).Replace('\', '/') }
        [System.IO.File]::WriteAllLines((Join-Path $Repo '.git\info\exclude'), $lista, $Utf8)
        Copy-Item -Recurse -Force (Join-Path $Priv 'claude\*') (Join-Path $Repo 'claude')
        Write-Host "  capa privada instalada en $Priv"
    } catch {
        Write-Host '  clave incorrecta o sin conexion: sigo sin la capa privada'
    }
    Remove-Item -Force $tgz -ErrorAction SilentlyContinue
}

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

Copy-Item -Force (Join-Path $Repo 'claude\EQUIPO.md') (Join-Path $Claude 'EQUIPO.md')
$EquipoFwd = (Join-Path $Claude 'EQUIPO.md') -replace '\\', '/'
[System.IO.File]::AppendAllText((Join-Path $Claude 'CLAUDE.md'), "`n@$EquipoFwd`n", $Utf8)
Write-Host "  reglas del equipo: $EquipoFwd"

if (Test-Path (Join-Path $Priv 'memoria')) {
    $PrivFwd = $Priv -replace '\\', '/'
    $bloque = @"

## Memoria de Diego (solo lectura, capa privada del equipo)
Indices de lo que Diego y Claude han hecho con cada cliente, proyecto y herramienta. Cada linea apunta a un fichero de su misma carpeta:
- $PrivFwd/memoria/claude/ (trabajo reciente)
- $PrivFwd/memoria/documents/ (ecosistema: One, Chat, Setter, facturas, clientes)
Antes de tocar un cliente o un sistema, busca aqui. No edites estos ficheros: se sobrescriben al actualizar. Tu propia memoria va aparte.
Las contrasenas y tokens estan tachados a proposito: pideselos a Diego, no los busques.

@$PrivFwd/memoria/claude/MEMORY.md
@$PrivFwd/memoria/documents/MEMORY.md
"@
    [System.IO.File]::AppendAllText((Join-Path $Claude 'CLAUDE.md'), $bloque, $Utf8)
    Write-Host '  memoria de Diego enlazada en CLAUDE.md'
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

# Carpeta de trabajo con la configuracion Ruflo (swarm) de Diego
New-Item -ItemType Directory -Force -Path (Join-Path $HOME 'Claude') | Out-Null
$ProyMd = Join-Path $HOME 'Claude\CLAUDE.md'
if (-not (Test-Path $ProyMd)) {
    [System.IO.File]::WriteAllText($ProyMd, [System.IO.File]::ReadAllText((Join-Path $Repo 'claude\proyecto-CLAUDE.md'), $Utf8), $Utf8)
    Write-Host "  $ProyMd (Ruflo)"
}

if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    Write-Host 'Instalando Claude Code...'
    Invoke-RestMethod https://claude.ai/install.ps1 | Invoke-Expression
}

Refrescar-Path
if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    Write-Host '  Ruflo se conecta la proxima vez que lances esta linea (Claude aun no esta en el PATH)'
} elseif (Get-Command npx -ErrorAction SilentlyContinue) {
    $ya = (& claude mcp list 2>$null) -join ' '
    if ($ya -notmatch 'claude-flow') {
        & claude mcp add --scope user claude-flow -- npx -y '@claude-flow/cli@latest' *> $null
        if ($LASTEXITCODE -eq 0) { Write-Host '  Ruflo (claude-flow) conectado' } else { Write-Host '  Ruflo no se pudo conectar: Claude funciona igual' }
    }
} else {
    Write-Host '  Sin Node.js: Ruflo queda para luego (winget install OpenJS.NodeJS.LTS y repite esta linea)'
}

Write-Host ''
Write-Host "Listo. Abre una terminal nueva, entra en $HOME\Claude y lanza: claude"
Write-Host 'La primera vez te pide iniciar sesion: usa la cuenta de Claude del equipo. Despues reinicia el ordenador.'
Write-Host 'Instala tambien la extension Claude in Chrome (solo Chrome) e inicia sesion con la misma cuenta.'
Write-Host 'No vienen nunca: contrasenas, tokens de los MCP ni acceso SSH al VPS. Eso se pide a Diego.'
