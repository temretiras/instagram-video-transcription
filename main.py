"""
Instagram Video Transcriber Pipeline
Instagram video URL'sinden doğrudan transkript çıkarma aracı.

Kullanım:
    python main.py https://www.instagram.com/p/...
"""

import os
import sys
import argparse
from downloader import download_instagram_media
from transcribe import transcribe_with_whisper

def process_instagram_video(url: str, output_path: str = None, model: str = "base", language: str = "tr") -> str:
    print("=" * 60)
    print("1. Adım: Instagram Videosu İndiriliyor...")
    print("=" * 60)
    media_file = download_instagram_media(url, output_dir="downloads")

    print("\n" + "=" * 60)
    print("2. Adım: Konuşmalar Metne Dönüştürülüyor (Whisper)...")
    print("=" * 60)
    transcript = transcribe_with_whisper(media_file, model_name=model, language=language)

    print("\n" + "=" * 60)
    print("SONUÇ: Transkript Çıkarıldı")
    print("=" * 60)
    print(transcript)

    if output_path is None:
        base_name = os.path.splitext(os.path.basename(media_file))[0]
        os.makedirs("transcripts", exist_ok=True)
        output_path = os.path.join("transcripts", f"{base_name}.md")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Transkript: {url}\n\n")
        f.write(transcript)
        f.write("\n")

    print(f"\n[+] Transkript kaydedildi: {output_path}")
    return transcript

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Instagram videosundan otomatik transkript çıkar")
    parser.add_argument("url", help="Instagram video veya Reel URL'si")
    parser.add_argument("-o", "--output", default=None, help="Çıktı Markdown/Metin dosyası")
    parser.add_argument("-m", "--model", default="base", help="Whisper model (tiny, base, small, medium)")
    parser.add_argument("-l", "--language", default="tr", help="Dil kodu (varsayılan: tr)")
    args = parser.parse_args()

    process_instagram_video(args.url, args.output, args.model, args.language)
