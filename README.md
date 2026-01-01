# Cellular Chaos Cipher (Hücresel Kaos Şifreleme Algoritması)

![Project Status](https://img.shields.io/badge/Status-Educational-orange)
![Python](https://img.shields.io/badge/Language-Python_3-blue)
![Course](https://img.shields.io/badge/Course-Information_Systems_Security-green)

## 🎓 Proje Künyesi

* **Üniversite:** Fırat Üniversitesi
* **Fakülte:** Teknoloji Fakültesi
* **Bölüm:** Yazılım Mühendisliği
* **Ders:** Bilgi Sistemleri Güvenliği (ISG)
* **Geliştirici:** Ömer Gülnaroğlu
* **Konu:** Hücresel Otomatlar ile Sözde Rastgele Sayı Üretimi ve Şifreleme

---

## 📝 Proje Özeti

Bu proje, **Bilgi Sistemleri Güvenliği** dersi kapsamında; kriptografik sistemlerin temeli olan **"Rastgelelik"** ve **"Akış Şifreleme (Stream Cipher)"** kavramlarını uygulamalı olarak göstermek amacıyla geliştirilmiştir.

Standart aritmetik yöntemler (Collatz vb.) yerine, **Stephen Wolfram**'ın **Rule 30 Hücresel Otomat** kuralı ve **Kaos Teorisi** kullanılarak özgün bir şifreleme motoru tasarlanmıştır.

---

## 🧠 Algoritma Tarifi ve Matematiksel Model ($g$ Fonksiyonu)

Proje, istenilen **"İteratif Dönüşüm Fonksiyonu ($g$) ile Anahtar Dizisi Üretimi"** prensibine dayanır.

### 1. Dönüşüm Fonksiyonu ($g$)
Algoritmanın çekirdeği olan **Rule 30** fonksiyonu, bir bitin yeni değerini belirlerken şu matematiksel kuralı uygular:

$$g(C) = C_{sol} \oplus (C_{merkez} \lor C_{sağ})$$

* **Sözel İfade:** Bir hücrenin yeni değeri; **Sol Komşu** ile **(Kendisi VEYA Sağ Komşu)** değerinin **XOR** işlemine sokulmasıyla bulunur.

### 2. Adım Adım Çalışma Mantığı
Algoritma (Generator) şu döngüyü takip eder:

1.  **Başlangıç (Initialization):** Kullanıcıdan alınan "Anahtar" (Seed) ikili sisteme (binary) çevrilir ve ilk satır oluşturulur.
2.  **Dönüşüm ($g$ Uygulaması):** Dizideki her bit için yukarıdaki $g$ fonksiyonu uygulanır ve yeni bir satır üretilir.
3.  **Seçim (Extraction):** Kaosun en yoğun olduğu **orta bit** seçilerek "Anahtar Akışı"na (Keystream) eklenir.
4.  **Döngü (Loop):** Mesaj uzunluğu kadar bit üretilene kadar işlem tekrarlanır (Her yeni satır, bir sonrakinin girdisi olur).
5.  **Şifreleme:** Elde edilen rastgele dizi ile mesaj **XOR** işlemine tabi tutulur.

---

## 🛡️ Güvenlik Analizi: Çığ Etkisi

Algoritmanın "Kaotik" yapısı, **Çığ Etkisi (Avalanche Effect)** testleri ile doğrulanmıştır.
* **Test:** Anahtardaki (Seed) sadece **1 bitlik değişim**, üretilen şifreli metinde **%40-%50** oranında değişime yol açmaktadır.
* Bu durum, algoritmanın girdiye karşı son derece hassas ve tahmin edilemez olduğunu gösterir.

---

## 📂 Dosya Açıklamaları

* **`main.py`**: **(Ana Dosya)** Programı çalıştıran arayüzdür. Şifreleme ve çözme işlemleri buradan yapılır.
* **`chaos_engine.py`**: Algoritmanın beyni. $g$ fonksiyonu ve döngü burada çalışır.
* **`security_analysis.py`**: Güvenlik testi dosyasıdır. Algoritmanın "Çığ Etkisi" performansını ölçer.

---

## 🚀 Nasıl Çalıştırılır?

Proje Python 3 ile çalışır, ek kurulum gerektirmez.

1. **Şifreleme Yapmak İçin:**
   Terminalde şu komutu yazın:
   ```bash
   python main.py
