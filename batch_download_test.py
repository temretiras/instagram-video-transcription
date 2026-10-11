import os
import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from downloader import download_media

videos = [
    {
        "id": "WCw4Et4757s",
        "url": "https://www.youtube.com/watch?v=WCw4Et4757s",
        "title": "Historik 39: Coğrafya Kader Midir - Tüfek, Mikrop ve Çelik"
    },
    {
        "id": "v2SEQHBsNH4",
        "url": "https://www.youtube.com/watch?v=v2SEQHBsNH4",
        "title": "Historik 67: Hitler'in Önlenemez Yükselişi ve Nazilerin İktidara Gelmesi"
    },
    {
        "id": "MH0Zv4N1Y4k",
        "url": "https://www.youtube.com/watch?v=MH0Zv4N1Y4k",
        "title": "Historik 53: Wallerstein - Modern Dünya Sistemi"
    },
    {
        "id": "eEMZKzDHKNM",
        "url": "https://www.youtube.com/watch?v=eEMZKzDHKNM",
        "title": "Historik 40: Din, Devlet, Hanedan - Habsburglar"
    },
    {
        "id": "72W9sF3kxnA",
        "url": "https://www.youtube.com/watch?v=72W9sF3kxnA",
        "title": "Historik 52: Devletsiz Kapitalizm Mümkün Mü?"
    }
]

print("=== 5 Yeni ESG Videosu İndiriliyor (Audio-Only 64kbps MP3) ===")
total_size = 0

for idx, vid in enumerate(videos, 1):
    print(f"\n[{idx}/5] Başlatılıyor: {vid['title']}")
    start = time.time()
    try:
        fp = download_media(vid["url"], output_dir="downloads", format_type="audio", audio_bitrate="64")
        sz = os.path.getsize(fp) / (1024 * 1024)
        total_size += sz
        elapsed = time.time() - start
        print(f"[+] Başarılı ({sz:.2f} MB, {elapsed:.1f} sn): {fp}")
    except Exception as e:
        print(f"[!] Hata ({vid['title']}): {e}")

print(f"\n=== Tamamlandı! Toplam 5 Dosya Boyutu: {total_size:.2f} MB ===")
