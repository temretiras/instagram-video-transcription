"""
Audio & Video Transcriber (Whisper Tabanlı)
Destekler:
    - openai-whisper
    - faster-whisper
"""

import os
import sys
import argparse

def transcribe_with_whisper(media_path: str, model_name: str = "base", language: str = "tr") -> str:
    """
    Yerel Whisper modeli ile video veya ses dosyasını metne dönüştürür.
    """
    if not os.path.exists(media_path):
        raise FileNotFoundError(f"Dosya bulunamadı: {media_path}")

    # 1. Öncelikli olarak faster-whisper kontrolü (daha hızlı ve hafif)
    try:
        from faster_whisper import WhisperModel
        print(f"[*] faster-whisper ({model_name}) ile işleniyor...")
        model = WhisperModel(model_name, device="auto", compute_type="auto")
        segments, info = model.transcribe(media_path, language=language)
        
        results = []
        for segment in segments:
            results.append(segment.text)
        return " ".join(results).strip()
    except ImportError:
        pass

    # 2. Standart openai-whisper kütüphanesi
    try:
        import whisper
        print(f"[*] openai-whisper ({model_name}) ile işleniyor...")
        model = whisper.load_model(model_name)
        result = model.transcribe(media_path, language=language)
        return result["text"].strip()
    except ImportError:
        pass

    raise RuntimeError(
        "Herhangi bir Whisper kütüphanesi bulunamadı! "
        "Lütfen 'pip install openai-whisper' veya 'pip install faster-whisper' komutunu çalıştırın."
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ses/Video dosyasını Whisper ile metne dönüştürür")
    parser.add_argument("media_path", help="İşlenecek ses veya video dosyasının yolu")
    parser.add_argument("-m", "--model", default="base", help="Whisper model boyutu (tiny, base, small, medium, large)")
    parser.add_argument("-l", "--language", default="tr", help="Dil kodu (varsayılan: tr)")
    parser.add_argument("-o", "--output", default=None, help="Transkripti kaydedecek dosya yolu (.txt veya .md)")
    args = parser.parse_args()

    transcript = transcribe_with_whisper(args.media_path, args.model, args.language)
    print("\n--- TRANSKRİPT ---\n")
    print(transcript)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(transcript)
        print(f"\n[+] Transkript kaydedildi: {args.output}")
