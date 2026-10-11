"""
Instagram Video & Audio Downloader
Kullanım:
    python downloader.py https://www.instagram.com/p/...
"""

import os
import sys
import argparse
import yt_dlp

def download_instagram_media(url: str, output_dir: str = "downloads", extract_audio_only: bool = False) -> str:
    """
    Instagram videosunu veya sesini indirir.
    Dönen değer: İndirilen dosyanın yerel dosya yolu.
    """
    os.makedirs(output_dir, exist_ok=True)
    out_tmpl = os.path.join(output_dir, "%(id)s.%(ext)s")

    ydl_opts = {
        "outtmpl": out_tmpl,
        "quiet": False,
        "no_warnings": False,
    }

    if extract_audio_only:
        ydl_opts.update({
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        })
    else:
        # En iyi tek parça (progressive) MP4 veya video+ses formatını seçer
        ydl_opts.update({
            "format": "best",
        })

    print(f"[*] İndiriliyor: {url}")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info)
        
        # Audio dönüştürme yapıldıysa uzantı mp3 olabilir
        if extract_audio_only:
            base, _ = os.path.splitext(file_path)
            mp3_path = base + ".mp3"
            if os.path.exists(mp3_path):
                file_path = mp3_path

    print(f"[+] İndirme tamamlandı: {file_path}")
    return file_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Instagram video ve ses indirici")
    parser.add_argument("url", help="Instagram video veya Reel URL'si")
    parser.add_argument("-o", "--output-dir", default="downloads", help="Çıktı klasörü (varsayılan: downloads)")
    parser.add_argument("-a", "--audio-only", action="store_true", help="Yalnızca ses olarak indir")
    args = parser.parse_args()

    download_instagram_media(args.url, args.output_dir, args.audio_only)
