"""
Universal Media Downloader (Instagram, YouTube, etc.)
Ses ve Video optimizasyonlu indirme modülü.
"""

import os
import sys
import argparse
import yt_dlp

def get_ffmpeg_path() -> str | None:
    """Sistemde veya imageio-ffmpeg kütüphanesinde bulunan ffmpeg yolunu döndürür."""
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        return None

def download_media(
    url: str,
    output_dir: str = "downloads",
    format_type: str = "audio",
    audio_bitrate: str = "64",
    max_height: int = 144
) -> str:
    """
    URL'den (YouTube, Instagram vb.) medya indirir.

    format_type seçenekleri:
        - 'audio'     : Yalnızca ses (MP3). Depolamayı %90-%95 oranında azaltır. (Transkripsiyon için önerilen)
        - 'video_low' : En düşük çözünürlüklü video (ör. 144p/240p). Depolama dostu video.
        - 'video_high': En yüksek kaliteli video.

    Dönen değer: İndirilen yerel dosya yolu.
    """
    os.makedirs(output_dir, exist_ok=True)
    out_tmpl = os.path.join(output_dir, "%(id)s.%(ext)s")
    ffmpeg_exe = get_ffmpeg_path()

    ydl_opts = {
        "outtmpl": out_tmpl,
        "quiet": False,
        "no_warnings": False,
    }

    if ffmpeg_exe:
        ydl_opts["ffmpeg_location"] = ffmpeg_exe

    if format_type == "audio":
        print(f"[*] Ses modu seçildi ({audio_bitrate} kbps MP3). Depolama tasarrufu devrede...")
        ydl_opts.update({
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": audio_bitrate,
            }],
        })
    elif format_type == "video_low":
        print(f"[*] Düşük kaliteli video modu seçildi (Maks. {max_height}p)...")
        # En düşük çözünürlüklü video ve ses
        ydl_opts.update({
            "format": f"worstvideo[height<={max_height}]+worstaudio/worst[height<={max_height}]/worst",
        })
    else:  # video_high
        print("[*] Yüksek kaliteli video modu seçildi...")
        ydl_opts.update({
            "format": "bestvideo+bestaudio/best",
        })

    print(f"[*] İndiriliyor: {url}")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info)

        if format_type == "audio":
            base, _ = os.path.splitext(file_path)
            mp3_path = base + ".mp3"
            if os.path.exists(mp3_path):
                file_path = mp3_path

    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    print(f"[+] İndirme tamamlandı: {file_path} ({file_size_mb:.2f} MB)")
    return file_path

# Geriye dönük uyumluluk
download_instagram_media = download_media

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Çok Amaçlı Ses & Video İndirici (Depolama Dostu)")
    parser.add_argument("url", help="İndirilecek video URL'si (YouTube, Instagram vb.)")
    parser.add_argument("-o", "--output-dir", default="downloads", help="Çıktı klasörü")
    parser.add_argument("-f", "--format", choices=["audio", "video_low", "video_high"], default="audio",
                        help="İndirme formatı: audio (varsayılan), video_low (144p), video_high")
    parser.add_argument("-b", "--bitrate", default="64", help="Ses kalitesi kbps (ör: 64, 128, 192)")
    parser.add_argument("--max-height", type=int, default=144, help="video_low için maksimum yükseklik (ör: 144)")
    args = parser.parse_args()

    download_media(args.url, args.output_dir, args.format, args.bitrate, args.max_height)
