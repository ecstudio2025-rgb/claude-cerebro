// Mismo render que server/index.mjs (composición Calco, h264 crf 17, master 'ventana')
// pero con concurrency 1 y caché de OffthreadVideo pequeña: el Mac está sin disco/swap.
import { spawn, execFileSync } from 'node:child_process'
import fs from 'node:fs'
import path from 'node:path'
import { createRequire } from 'node:module'
const [ROOT, id, out] = process.argv.slice(2)
const req = createRequire(path.join(ROOT, 'package.json'))
const { bundle } = await import(req.resolve('@remotion/bundler'))
const { renderMedia, selectComposition } = await import(req.resolve('@remotion/renderer'))
const { withGlb } = await import(path.join(ROOT, 'remotion', 'webpack-glb.mjs'))
const port = 4628
const data = path.join(ROOT, 'data', 'projects')
const srv = spawn(process.execPath, [path.join(ROOT, 'server', 'index.mjs')], { cwd: ROOT, env: { ...process.env, CALCO_PORT: String(port), CALCO_DATA_DIR: data }, stdio: 'ignore' })
let serveUrl
try {
  for (let i = 0; i < 60; i++) { try { await fetch(`http://127.0.0.1:${port}/api/projects`); break } catch { await new Promise((r) => setTimeout(r, 500)) } }
  serveUrl = await bundle({ entryPoint: path.join(ROOT, 'remotion', 'index.ts'), webpackOverride: withGlb })
  const plan = JSON.parse(fs.readFileSync(path.join(data, id, 'plan.json'), 'utf8'))
  const transcript = JSON.parse(fs.readFileSync(path.join(data, id, 'transcript.json'), 'utf8'))
  const inputProps = { src: `http://127.0.0.1:${port}/media/${id}/source.mp4`, plan, transcript }
  const chromiumOptions = { gl: 'angle' }
  const composition = await selectComposition({ serveUrl, id: 'Calco', inputProps, chromiumOptions })
  // Por tramos de 300 fotogramas: el TMPDIR de Remotion solo guarda un tramo cada vez (el Mac anda justo de disco)
  const tmp = out.replace(/\.mp4$/, '.tmp.mp4')
  const dir = out.replace(/\.mp4$/, '.partes'); fs.mkdirSync(dir, { recursive: true })
  const N = composition.durationInFrames, STEP = 300, partes = []
  for (let a = 0; a < N; a += STEP) {
    const b = Math.min(N - 1, a + STEP - 1), f = path.join(dir, `p${String(a).padStart(5, '0')}.mp4`)
    if (!fs.existsSync(f)) await renderMedia({ composition, serveUrl, codec: 'h264', crf: 17, outputLocation: f, inputProps, chromiumOptions, concurrency: 2, muted: true, frameRange: [a, b],
      offthreadVideoCacheSizeInBytes: 256 * 1024 * 1024 })
    partes.push(f); console.log('render', b + 1, '/', N)
  }
  const wav = path.join(dir, 'audio.wav')
  await renderMedia({ composition, serveUrl, codec: 'wav', outputLocation: wav, inputProps, chromiumOptions })
  fs.writeFileSync(path.join(dir, 'lista.txt'), partes.map((f) => `file '${f}'`).join('\n'))
  execFileSync('ffmpeg', ['-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', path.join(dir, 'lista.txt'), '-i', wav, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'pcm_s16le', tmp.replace(/\.mp4$/, '.mov')])
  const master = plan.template === 'ventana'
    ? 'acompressor=threshold=-26dB:ratio=4:attack=5:release=90:makeup=4,loudnorm=I=-17.6:TP=-1:LRA=3'
    : 'loudnorm=I=-14:TP=-1.2:LRA=7'
  execFileSync('ffmpeg', ['-y', '-v', 'error', '-i', tmp.replace(/\.mp4$/, '.mov'), '-c:v', 'copy', '-af', master, '-c:a', 'aac', '-b:a', '192k', out])
  fs.rmSync(tmp.replace(/\.mp4$/, '.mov'), { force: true }); fs.rmSync(dir, { recursive: true, force: true })
  console.log('ok', out)
} finally {
  srv.kill()
  if (serveUrl) fs.rmSync(serveUrl, { recursive: true, force: true })
}
