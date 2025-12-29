from chaos_engine import CellularAutomataCipher

def calculate_change_percentage(str1, str2):
    """İki binary string arasındaki fark yüzdesini hesaplar."""
    # Hex'i binary'e çevir
    bin1 = bin(int(str1, 16))[2:].zfill(256)
    bin2 = bin(int(str2, 16))[2:].zfill(256)
    
    # Uzunlukları eşitle
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)
    
    diff_count = sum(1 for a, b in zip(bin1, bin2) if a != b)
    return (diff_count / max_len) * 100

print("==================================================")
print("   GÜVENLİK ANALİZİ: ÇIĞ ETKİSİ (AVALANCHE EFFECT) ")
print("==================================================")
print("Test: Anahtarda 1 karakterlik değişim çıktıya nasıl yansıyor?\n")

text = "Bilgi Guvenligi Dersi Final Projesi"

# Durum 1: Orijinal Anahtar
seed1 = "Anahtar123"
cipher1 = CellularAutomataCipher(seed1)
out1 = cipher1.encrypt(text)

# Durum 2: Sadece 1 karakter değişmiş anahtar (3 -> 4)
seed2 = "Anahtar124"
cipher2 = CellularAutomataCipher(seed2)
out2 = cipher2.encrypt(text)

print(f"Girdi Metni: {text}")
print("-" * 50)
print(f"Anahtar 1 ({seed1}) Çıktısı (İlk 30 hane): {out1[:30]}...")
print(f"Anahtar 2 ({seed2}) Çıktısı (İlk 30 hane): {out2[:30]}...")
print("-" * 50)

change_percent = calculate_change_percentage(out1, out2)

print(f"\nSONUÇ: Anahtardaki minik değişim, şifreli metni %{change_percent:.2f} oranında değiştirdi.")

if change_percent > 40:
    print("✅ BAŞARILI: Yüksek Çığ Etkisi Gözlemlendi (İyi bir şifreleme özelliği).")
else:
    print("❌ BAŞARISIZ: Çıktılar birbirine çok benziyor.")
