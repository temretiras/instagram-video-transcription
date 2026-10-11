"""
Batch Downloader for @gozubuyukbaran May+ Reels
Tüm videoları optimize edilmiş 64kbps MP3 (veya video) olarak indirir.
"""

import os
import sys
import json
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from downloader import download_media

json_path = r"C:\Users\ucuct\.gemini\antigravity\scratch\baran_may_posts.json"
output_dir = os.path.join("downloads", "gozubuyukbaran")
os.makedirs(output_dir, exist_ok=True)

with open(json_path, "r", encoding="utf-8") as f:
    posts = json.load(f)

print(f"=== @gozubuyukbaran Mayıs 2026 İtibariyle Toplam {len(posts)} Video İndiriliyor ===")

results = []
success_count = 0
failed_count = 0

for idx, p in enumerate(posts, 1):
    reel_url = p.get("reel_url")
    title = p.get("title")
    date = p.get("date")
    slug = p.get("slug")

    if not reel_url:
        print(f"[{idx}/{len(posts)}] Atlandı (Link yok): {title}")
        continue

    print(f"\n[{idx}/{len(posts)}] [{date}] İndiriliyor: {title}")
    try:
        # download as 64kbps MP3
        fp = download_media(reel_url, output_dir=output_dir, format_type="audio", audio_bitrate="64")
        sz_mb = os.path.getsize(fp) / (1024 * 1024)
        results.append({
            "date": date,
            "title": title,
            "slug": slug,
            "reel_url": reel_url,
            "file_path": fp,
            "size_mb": sz_mb,
            "status": "success"
        })
        success_count += 1
        print(f"[+] Başarılı ({sz_mb:.2f} MB): {fp}")
    except Exception as e:
        print(f"[!] Hata ({reel_url}): {e}")
        results.append({
            "date": date,
            "title": title,
            "slug": slug,
            "reel_url": reel_url,
            "error": str(e),
            "status": "failed"
        })
        failed_count += 1

    # Brief delay to respect rate limits
    time.sleep(0.5)

catalog_path = os.path.join("transcripts", "baran_may_archive.json")
with open(catalog_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\n" + "=" * 60)
print(f"BİTTİ! Başarılı: {success_count}, Başarısız: {failed_count}")
print(f"Katalog kaydedildi: {catalog_path}")
print("=" * 60)
