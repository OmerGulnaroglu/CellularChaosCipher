import os
from chaos_engine import CellularAutomataCipher

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print("========================================")
        print("   HÜCRESEL KAOS ŞİFRELEME SİSTEMİ      ")
        print("   (Cellular Automata Based Cipher)     ")
        print("========================================")
        print("1. Metin Şifrele (Encrypt)")
        print("2. Şifre Çöz (Decrypt)")
        print("3. Çıkış")
        print("========================================")
        
        choice = input("Seçiminiz (1/2/3): ")
        
        if choice == '1':
            seed = input("\nAnahtar (Seed) giriniz: ")
            text = input("Şifrelenecek metni giriniz: ")
            
            cipher = CellularAutomataCipher(seed)
            encrypted_text = cipher.encrypt(text)
            
            print(f"\n[BAŞARILI] Şifreli Metin (Hex):")
            print(f"{encrypted_text}")
            input("\nDevam etmek için Enter'a basın...")
            
        elif choice == '2':
            seed = input("\nÇözme Anahtarı (Seed) giriniz: ")
            encrypted_hex = input("Şifreli Hex kodunu yapıştırın: ")
            
            try:
                cipher = CellularAutomataCipher(seed)
                decrypted_text = cipher.decrypt(encrypted_hex)
                print(f"\n[BAŞARILI] Çözülen Metin:")
                print(f"{decrypted_text}")
            except Exception as e:
                print(f"\n[HATA] Şifre çözülemedi! Anahtar yanlış olabilir.")
                print(f"Hata Detayı: {e}")
            
            input("\nDevam etmek için Enter'a basın...")
            
        elif choice == '3':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
