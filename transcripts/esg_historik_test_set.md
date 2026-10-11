# 📚 Emrah Safa Gürkan (ESG) - Historik Test Veri Seti Kataloğu

Bu doküman, projede ses/video indirme, boyut optimizasyonu ve konuşma tanıma (Whisper ASR) testleri için oluşturulan **Emrah Safa Gürkan (Historik / Omnibus)** test kümesinin detaylarını içerir.

---

## 📊 Depolama Tasarrufu Özeti

| # | Video Başlığı | YouTube ID | Süre | Standart Video (1080p) | Optimize Edilmiş MP3 (64kbps) | Tasarruf Oranı |
|---|---------------|------------|------|------------------------|-------------------------------|----------------|
| 1 | **Historik 14:** Diktatör Franco ve İspanya İç Savaşı | `esczqaVKf-I` | 45:18 | ~1.5 GB | **20.73 MB** | **%98.6** |
| 2 | **Historik 49:** Çağdaşlaşma, Sekülerizm ve Cumhuriyet | `NfYX1MWUHYs` | 52:25 | ~2.1 GB | **24.00 MB** | **%98.8** |
| 3 | **Historik 39:** Coğrafya Kader Midir: Tüfek, Mikrop ve Çelik | `WCw4Et4757s` | 57:35 | ~2.3 GB | **26.35 MB** | **%98.8** |
| 4 | **Historik 67:** Hitler'in Önlenemez Yükselişi ve Naziler | `v2SEQHBsNH4` | 75:36 | ~3.0 GB | **34.61 MB** | **%98.8** |
| 5 | **Historik 53:** Wallerstein: Modern Dünya Sistemi | `MH0Zv4N1Y4k` | 58:08 | ~2.4 GB | **26.61 MB** | **%98.9** |
| 6 | **Historik 40:** Din, Devlet, Hanedan: Habsburglar | `eEMZKzDHKNM` | 42:57 | ~1.7 GB | **19.66 MB** | **%98.8** |
| 7 | **Historik 52:** Devletsiz Kapitalizm Mümkün Mü? | `72W9sF3kxnA` | 45:26 | ~1.8 GB | **20.79 MB** | **%98.8** |
| **TOPLAM** | **7 Farklı Kapsamlı Tarih Dersi** | — | **~6 Saat 17 Dk** | **~14.8 GB** | **172.75 MB** | **%98.8 Ortalama** |

---

## 📌 Test Kümesindeki Bölümler ve Temaları

### 1. Historik 39: Coğrafya Kader Midir: Tüfek, Mikrop ve Çelik
* **URL:** https://www.youtube.com/watch?v=WCw4Et4757s
* **Dosya:** `downloads/WCw4Et4757s.mp3` (26.35 MB)
* **Temel Konular:** Jared Diamond'ın ünlü coğrafi determinizm tezi, Avrasya kıtasının doğu-batı ekseni avantajı, evcilleştirilebilir hayvan ve tahıl türleri, mikropların sömürgecilikteki rolü ve Akdeniz uygarlıklarının gelişimi.

### 2. Historik 67: Hitler'in Önlenemez Yükselişi ve Nazilerin İktidara Gelmesi
* **URL:** https://www.youtube.com/watch?v=v2SEQHBsNH4
* **Dosya:** `downloads/v2SEQHBsNH4.mp3` (34.61 MB)
* **Temel Konular:** Weimar Cumhuriyeti'nin krizi, 1929 Ekonomik Buhranı'nın Almanya'ya yıkıcı etkisi, NSDAP'nin seçim başarıları, muhafazakâr sağ elitlerin (Hindenburg, Papen) Hitler'i kontrol edebilecekleri yanılgısıyla şansölye yapmaları ve totaliter rejimin inşası.

### 3. Historik 53: Wallerstein: Modern Dünya Sistemi
* **URL:** https://www.youtube.com/watch?v=MH0Zv4N1Y4k
* **Dosya:** `downloads/MH0Zv4N1Y4k.mp3` (26.61 MB)
* **Temel Konular:** Immanuel Wallerstein'ın dünya sistemleri analizi, Merkez (Core), Çevre (Periphery) ve Yarı-Çevre (Semi-Periphery) ülkeler arasındaki artı-değer transferi, küresel kapitalizmin eşitsiz gelişim dinamikleri ve Osmanlı'nın bu sistemdeki konumu.

### 4. Historik 40: Din, Devlet, Hanedan: Habsburglar
* **URL:** https://www.youtube.com/watch?v=eEMZKzDHKNM
* **Dosya:** `downloads/eEMZKzDHKNM.mp3` (19.66 MB)
* **Temel Konular:** Avrupa'nın en uzun soluklu hanedanı Habsburgların evlilik politikaları ("Savaşları başkaları yapsın, sen evlen mutlu Avusturya"), V. Karl (Şarlken) imparatorluğu, Reformasyon ve Din Savaşları, Osmanlı-Habsburg rekabeti.

### 5. Historik 52: Devletsiz Kapitalizm Mümkün Mü?
* **URL:** https://www.youtube.com/watch?v=72W9sF3kxnA
* **Dosya:** `downloads/72W9sF3kxnA.mp3` (20.79 MB)
* **Temel Konular:** Kapitalizmin devlet eli olmadan doğup doğamayacağı sorusu, mülkiyet haklarının korunması, tekel mekanizmaları, askeri harcamaların kapitalizmi beslemesi ve serbest piyasa mitleri.

---

## 🚀 Test Kümesini Çalıştırma

Tüm bu test dosyaları üzerinde transkripsiyon veya kalite değerlendirmesi yapmak için:
```bash
python transcribe.py downloads/WCw4Et4757s.mp3 --model base --language tr
```
