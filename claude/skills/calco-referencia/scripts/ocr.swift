// OCR local con Vision de macOS. Uso: ocr <dir_frames> > ocr.jsonl
// Cada línea: {"f":"000123.jpg","t":[{"s":"texto","c":0.98,"x":..,"y":..,"w":..,"h":..}]}
// Coordenadas normalizadas 0-1 con origen ARRIBA-izquierda (se invierte la Y de Vision).
import Foundation
import Vision
import AppKit

let args = CommandLine.arguments
guard args.count > 1 else { fputs("uso: ocr <dir>\n", stderr); exit(1) }
let dir = URL(fileURLWithPath: args[1])
let files = (try? FileManager.default.contentsOfDirectory(atPath: dir.path))?.filter { $0.hasSuffix(".jpg") || $0.hasSuffix(".png") }.sorted() ?? []

for name in files {
    autoreleasepool {
        let url = dir.appendingPathComponent(name)
        guard let img = NSImage(contentsOf: url),
              let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { return }
        let req = VNRecognizeTextRequest()
        req.recognitionLevel = .accurate
        req.recognitionLanguages = ["es-ES", "en-US"]
        req.usesLanguageCorrection = false
        let h = VNImageRequestHandler(cgImage: cg, options: [:])
        try? h.perform([req])
        var out: [[String: Any]] = []
        for o in (req.results ?? []) {
            guard let c = o.topCandidates(1).first else { continue }
            let b = o.boundingBox
            out.append(["s": c.string, "c": Double(c.confidence),
                        "x": Double(b.minX), "y": Double(1 - b.maxY),
                        "w": Double(b.width), "h": Double(b.height)])
        }
        let obj: [String: Any] = ["f": name, "t": out]
        if let d = try? JSONSerialization.data(withJSONObject: obj), let s = String(data: d, encoding: .utf8) {
            print(s)
        }
    }
}
