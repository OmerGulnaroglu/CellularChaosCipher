from chaos_engine import CellularAutomataCipher
import sys
import os

# Üst dizindeki modülü görebilmesi için yol ayarı
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def analyze_randomness(seed, length=512):
    """
    Belirli bir seed için bit dizisi üretir ve istatistiksel dağılımı ölçer.
    """
    try:
        cipher = CellularAutomataCipher(seed)
        keystream = cipher.generate_keystream(length)
        
        # Listeyi string'e çevir
        bit_string = "".join(str(b) for b in keystream)
        
        count_1 = bit_string.count('1')
        count_0 = bit_string.count('0')
        ratio_1 = (count_1 / length) * 100
        
        print(f"| {seed:<15} | {count_1:<8} | {count_0:<8} | %{ratio_1:<6.2f} |")
        return True
    except Exception as e:
        print(f"Hata: {e}")
        return False

if __name__ == "__main__":
    print("\n### OTOMATİK İSTATİSTİK TEST SONUÇLARI ###\n")
    print("| Ön Değer (Seed) | 1 Sayısı | 0 Sayısı | 1 Oranı |")
    print("| :--- | :--- | :--- | :--- |")
    
    # Hocanın istediği örnek seed değerleri
    seeds = ["FiratUniv", "CyberSecurity", "2026Project", "TestSeed123", "Elazig23"]
    
    for seed in seeds:
        analyze_randomness(seed)
    print("\n")
