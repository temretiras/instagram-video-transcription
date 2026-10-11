"""
Universal Media Transcriber Pipeline
YouTube, Instagram ve diğer platformlardan otomatik ses/video indirme ve transkripsiyon.

Depolama Optimizasyonu:
- Varsayılan olarak transkript için sadece ses (64kbps MP3) indirilir.
- Depolamada %90-%95 tasarruf sağlanır.
- İsteğe bağlı olarak 144p gibi ultra düşük kaliteli video da indirilebilir.

Kullanım:
    python main.py https://www.youtube.com/watch?v=...
    python main.py https://www.instagram.com/p/...
    python main.py <url> --format video_low --max-height 144
"""

import os
import sys
import argparse

# Windows cp1252 karakter kodlama hatalarını önle
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from downloader import download_media
from transcribe import transcribe_with_whisper

def process_media_url(
    url: str,
    output_path: str = None,
    format_type: str = "audio",
    audio_bitrate: str = "64",
    max_height: int = 144,
    model: str = "base",
    language: str = "tr"
) -> str:
    print("=" * 65)
    print(f"1. ADIM: Medya İndiriliyor (Format: {format_type})...")
    print("=" * 65)
    media_file = download_media(
        url,
        output_dir="downloads",
        format_type=format_type,
        audio_bitrate=audio_bitrate,
        max_height=max_height
    )

    file_size_mb = os.path.getsize(media_file) / (1024 * 1024)
    print(f"\n[i] İndirilen Dosya Boyutu: {file_size_mb:.2f} MB")

    print("\n" + "=" * 65)
    print(f"2. ADIM: Whisper Yapay Zekâ Modeli ile Deşifre Ediliyor (Model: {model})...")
    print("=" * 65)
    transcript = transcribe_with_whisper(media_file, model_name=model, language=language)

    print("\n" + "=" * 65)
    print("SONUÇ: Transkripsiyon Başarılı!")
    print("=" * 65)

    if output_path is None:
        base_name = os.path.splitext(os.path.basename(media_file))[0]
        os.makedirs("transcripts", exist_ok=True)
        output_path = os.path.join("transcripts", f"{base_name}.md")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Transkript: {url}\n\n")
        f.write(f"- Dosya: `{os.path.basename(media_file)}` ({file_size_mb:.2f} MB)\n")
        f.write(f"- Format: `{format_type}`\n\n")
        f.write("---\n\n")
        f.write(transcript)
        f.write("\n")

    print(f"\n[+] Transkript kaydedildi: {output_path}")
    return transcript

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Çok Amaçlı Ses/Video İndirici & Transkript Çıkarıcı")
    parser.add_argument("url", help="YouTube veya Instagram URL'si")
    parser.add_argument("-f", "--format", choices=["audio", "video_low", "video_high"], default="audio",
                        help="İndirme formatı: audio (varsayılan MP3), video_low (144p), video_high")
    parser.add_argument("-b", "--bitrate", default="64", help="Ses kalitesi kbps (ör: 64, 128)")
    parser.add_argument("--max-height", type=int, default=144, help="video_low için maksimum yükseklik (ör: 144)")
    parser.add_argument("-m", "--model", default="base", help="Whisper model boyutu (tiny, base, small, medium)")
    parser.add_argument("-l", "--language", default="tr", help="Dil kodu (varsayılan: tr)")
    parser.add_argument("-o", "--output", default=None, help="Çıktı Markdown/Metin dosyası")
    args = parser.parse_args()

    process_media_url(
        args.url,
        output_path=args.output,
        format_type=args.format,
        audio_bitrate=args.bitrate,
        max_height=args.max_height,
        model=args.model,
        language=args.language
    )
