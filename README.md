# 🎙️ Instagram Video Transcriber & Second Brain Transcripts

Bu depo, Instagram videolarından/Reels içeriklerinden doğrudan video/ses indiren, konuşmaları **Whisper** yapay zekâ modeli ile metne döken (Speech-to-Text) araçları ve örnek transkriptleri içerir.

Depo içerisinde ayrıca **Baran Gözübüyük (@gozubuyukbaran)** tarafından yayınlanan *"Obsidian ile İkinci Beyin & Yapay Zekâ Dijital İkiz"* video serisinin tam metin transkriptleri yer almaktadır.

---

## 📁 Proje Yapısı

```text
instagram-video-transcription/
├── downloader.py          # yt-dlp ile Instagram video ve ses indirme modülü
├── transcribe.py          # OpenAI Whisper / Faster-Whisper transkripsiyon modülü
├── main.py                # Uçtan uca URL'den transkript çıkaran ana CLI aracı
├── requirements.txt       # Gerekli Python bağımlılıkları
├── .gitignore             # Büyük video dosyalarını (.mp4 vb.) hariç tutar
└── transcripts/
    ├── part1_obsidian_ikinci_beyin.md       # Part 1 transkripti
    ├── part2_otomasyon_telegram_whisper.md  # Part 2 transkripti
    └── combined_transcript.md               # Part 1 & 2 birleşik tam transkript
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

### 1. Tek Komutla URL'den Transkript Çıkarma (Önerilen)
```bash
python main.py "https://www.instagram.com/p/DdO9AXNgVz-/"
```
Bu komut videoyu `downloads/` klasörüne indirir, Whisper modeli ile konuşmaları deşifre eder ve sonucu `transcripts/` altına Markdown dosyası olarak kaydeder.

### 2. Yalnızca Video/Ses İndirme
```bash
# Videoyu indirmek için:
python downloader.py "https://www.instagram.com/p/DdO9AXNgVz-/"

# Yalnızca sesi (MP3) indirmek için:
python downloader.py "https://www.instagram.com/p/DdO9AXNgVz-/" --audio-only
```

### 3. Yerel Bir Ses/Video Dosyasını Transkribe Etme
```bash
python transcribe.py downloads/video.mp4 --model base --language tr --output transkript.md
```

---

## 📜 İçerik Transkriptleri

Hazır transkriptleri doğrudan `transcripts/` dizininden inceleyebilirsiniz:
- **[Part 1 Transkripti](transcripts/part1_obsidian_ikinci_beyin.md):** Obsidian mimarisi, Claude ile klasör yapısı oluşturma, Wispr Flow toplantı notu entegrasyonu.
- **[Part 2 Transkripti](transcripts/part2_otomasyon_telegram_whisper.md):** Telegram botu + Whisper ile sesli/yazılı not alma, Claude Inbox işleme ve AI ajanlar için dijital kimlik vizyonu.
- **[Birleşik Tam Transkript](transcripts/combined_transcript.md):** Her iki bölümün ardışık tam metni.

---

## 📄 Lisans
MIT License
