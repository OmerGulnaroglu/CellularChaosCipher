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

Standart matematiksel yöntemler yerine, **Stephen Wolfram**'ın **Rule 30 Hücresel Otomat** kuralı ve **Kaos Teorisi** kullanılarak özgün bir şifreleme motoru tasarlanmıştır. Bu yapı, anahtardaki en ufak değişimin sonucu tamamen değiştirmesi (Çığ Etkisi) üzerine kuruludur.

---

## ⚙️ Teknik Yapı

Sistem, **Simetrik Şifreleme** prensiplerine dayanır.
1.  **Girdi:** Kullanıcıdan bir "Anahtar (Seed)" ve "Mesaj" alınır.
2.  **Kaos Motoru:** Rule 30 algoritması, anahtarı kullanarak karmaşık bir bit dizisi (Keystream) üretir.
3.  **Şifreleme:** Mesajın bitleri ile üretilen rastgele bitler **XOR** işlemine sokulur.

---

## 📂 Dosya Açıklamaları

* **`main.py`**: **(Ana Dosya)** Programı çalıştıran arayüzdür. Şifreleme ve çözme işlemleri buradan yapılır.
* **`chaos_engine.py`**: Algoritmanın beyni. Rule 30 mantığı burada çalışır.
* **`security_analysis.py`**: Güvenlik testi dosyasıdır. Algoritmanın "Çığ Etkisi" performansını ölçer.

---

## 🚀 Nasıl Çalıştırılır?

Proje Python 3 ile çalışır, ek kurulum gerektirmez.

1. **Şifreleme Yapmak İçin:**
   Terminalde şu komutu yazın:
   ```bash
   python main.py
