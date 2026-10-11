# 🎙️ Universal Media Transcriber (YouTube, Instagram & More)

Bu proje; **YouTube**, **Instagram** ve diğer video platformlarından medya indiren, konuşmaları **Whisper** yapay zekâ modeli ile yüksek doğrulukla metne dönüştüren (Speech-to-Text) ve **depolamayı minimumda tutan** açık kaynaklı bir araç setidir.

---

## ⚡ Neden Depolama Optimizasyonu?

Görsel içermeyen konuşma deşifrelerinde 1080p video indirmek gigabaytlarca gereksiz veri ve bant genişliği tüketir. Bu projede:
* **Varsayılan Mod (`audio`):** Yalnızca ses akışı (64–128 kbps MP3) indirilir. Örneğin 45 dakikalık bir YouTube videosu **~1.5 GB yerine yalnızca 21.7 MB** yer kaplar (%95+ depolama tasarrufu).
* **Düşük Kalite Video Modu (`video_low`):** Görüntüye de ihtiyaç duyulursa 144p/240p gibi minimum çözünürlükte indirilir.
* **FFmpeg Entegrasyonu:** `imageio-ffmpeg` sayesinde harici bir FFmpeg kurulumuna ihtiyaç kalmadan otomatik ses dönüştürme yapılır.

---

## 📁 Proje Yapısı

```text
instagram-video-transcription/
├── downloader.py          # Çok amaçlı medya indirici (Audio / Low-Res / High-Res)
├── transcribe.py          # OpenAI Whisper / Faster-Whisper transkripsiyon modülü
├── main.py                # Tek komutla çalışan uçtan uca transkripsiyon aracı
├── requirements.txt       # Gerekli Python bağımlılıkları (yt-dlp, imageio-ffmpeg, whisper)
├── .gitignore             # Medya dosyalarını Git'ten hariç tutar
└── transcripts/
    ├── historik49_cagdaslasma_sekulerizm_cumhuriyet.md # YouTube: ESG Historik 49 (52 dk)
    ├── historik14_diktator_franco_ispanya_ic_savasi.md # YouTube: ESG Historik 14 (45 dk)
    ├── part1_obsidian_ikinci_beyin.md                  # Instagram: İkinci Beyin Part 1
    ├── part2_otomasyon_telegram_whisper.md             # Instagram: İkinci Beyin Part 2
    └── combined_transcript.md                          # Instagram serisi birleşik metin
```

---

## 🚀 Kurulum

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/temretiras/instagram-video-transcription.git
   cd instagram-video-transcription
   ```

2. Bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Kullanım

### 1. Tek Komutla URL'den Transkript Çıkarma (Varsayılan: Depolama Dostu MP3)
```bash
# YouTube Videosu (Yalnızca ses indirir, metne dönüştürür):
python main.py "https://www.youtube.com/watch?v=esczqaVKf-I"

# Instagram Post / Reel:
python main.py "https://www.instagram.com/p/DdO9AXNgVz-/"
```

### 2. Düşük Kalitede Video İndirerek Transkript Çıkarma (144p)
```bash
python main.py "https://www.youtube.com/watch?v=..." --format video_low --max-height 144
```

### 3. Yalnızca İndirme (Transkripsiyonsuz)
```bash
# Sadece MP3 (64 kbps ses) indir:
python downloader.py "https://www.youtube.com/watch?v=..." -f audio -b 64

# En düşük kaliteli 144p video indir:
python downloader.py "https://www.youtube.com/watch?v=..." -f video_low --max-height 144
```

### 4. Yerel Dosyayı Metne Dönüştürme
```bash
python transcribe.py downloads/esczqaVKf-I.mp3 --model base --language tr --output cikti.md
```

---

## 📜 Hazır Transkriptler & Test Veri Seti

- **[@gozubuyukbaran Mayıs 2026 Arşivi](transcripts/gozubuyukbaran_may_archive.md):** Baran Gözübüyük'ün Mayıs–Ekim 2026 arasında paylaştığı **45 videoluk tam set** (Obsidian, AI araçları, Claude, Cloudflare, Resend, DJI Neo 2 vb.) ve bağlantıları.
- **[ESG Historik Test Veri Seti Kataloğu](transcripts/esg_historik_test_set.md):** 7 farklı Emrah Safa Gürkan dersinden oluşan ~6.5 saatlik ses test kümesi (Tüfek Mikrop ve Çelik, Hitler, Wallerstein, Habsburglar, Devletsiz Kapitalizm vb.) ve depolama karşılaştırmaları.
- **[Historik 49 - Çağdaşlaşma, Sekülerizm ve Cumhuriyet (Emrah Safa Gürkan)](transcripts/historik49_cagdaslasma_sekulerizm_cumhuriyet.md):** 52 dakikalık bölümün kapsamlı deşifresi, Niyazi Berkes'in sekülerizm tezleri ve modern devlet analizi.
- **[Historik 14 - Diktatör Franco ve İspanya İç Savaşı (Emrah Safa Gürkan)](transcripts/historik14_diktator_franco_ispanya_ic_savasi.md):** 45 dakikalık bölümün detaylı analizi ve deşifresi.
- **[Obsidian ile İkinci Beyin Part 1 & 2 (Baran Gözübüyük)](transcripts/combined_transcript.md):** Kişisel yapay zekâ dijital ikizi ve not alma mimarisi.

---

## 📄 Lisans
MIT License
