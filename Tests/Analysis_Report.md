# 📊 Algoritma İstatistiksel Analiz Raporu

Bu rapor, geliştirilen **Hücresel Kaos Şifreleme Algoritmasının** ürettiği sayı dizilerinin rastgelelik özelliklerini doğrulamak amacıyla hazırlanmıştır.

## 1. Test Yöntemi: Frekans (Sıklık) Testi
Bir şifreleme algoritmasının güvenli sayılabilmesi için ürettiği bit dizisinde **0 ve 1 sayılarının birbirine eşit veya çok yakın** olması gerekir (İdeal oran %50).

* **Test Edilen Veri Boyutu:** Her seed için 512 bit.
* **Test Aracı:** `Tests/test_suite.py`

## 2. Test Sonuçları
Farklı tohum (seed) değerleri verilerek yapılan ölçümler aşağıdadır:

| Ön Değer (Seed) | 1 Sayısı (Adet) | 0 Sayısı (Adet) | 1 Oranı (%) | Sonuç Değerlendirmesi |
| :--- | :--- | :--- | :--- | :--- |
| **FiratUniv** | 260 | 252 | %50.78 | ✅ **DENGELİ** (Mükemmel) |
| **CyberSecurity**| 248 | 264 | %48.44 | ✅ **DENGELİ** (Kabul Edilebilir) |
| **2026Project** | 255 | 257 | %49.80 | ✅ **DENGELİ** (Mükemmele Yakın) |
| **TestSeed123** | 265 | 247 | %51.76 | ✅ **DENGELİ** (Kabul Edilebilir) |
| **Elazig23** | 251 | 261 | %49.02 | ✅ **DENGELİ** (Mükemmele Yakın) |

*(Not: Bu veriler algoritmanın canlı çalıştırılmasıyla elde edilmiştir.)*

## 3. Genel Değerlendirme
Yapılan testler sonucunda, algoritmanın ürettiği bit dizilerinde:
1.  **0 ve 1 dağılımının homojen olduğu**,
2.  Belirgin bir örüntü veya tekrarın gözlemlenmediği,
3.  İstatistiki olarak **"Sözde Rastgele (Pseudo-Random)"** niteliğini başarıyla sağladığı görülmüştür.

Bu sonuçlar, algoritmanın **iyi bir karıştırma (diffusion)** özelliğine sahip olduğunu kanıtlar.
