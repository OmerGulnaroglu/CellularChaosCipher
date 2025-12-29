"""
Cellular Chaos Engine
Bu modül, Rule 30 Hücresel Otomat kuralını kullanarak sözde rastgele bitler üretir.
"""

class CellularAutomataCipher:
    def __init__(self, seed_key):
        """
        Başlangıç tohumunu (seed) alır ve binary formata çevirir.
        """
        self.seed = seed_key
        # Anahtarı binary diziye çevir (Örn: 'A' -> 01000001)
        self.state = self._string_to_bits(str(seed_key))
        # Başlangıç durumu çok kısaysa güvenliği artırmak için padding ekle
        while len(self.state) < 64:
            self.state = self.state + self.state[::-1] # Aynalama yöntemiyle uzat

    def _string_to_bits(self, s):
        """String ifadeyi 0 ve 1 listesine çevirir."""
        result = []
        for c in s:
            bits = bin(ord(c))[2:]
            bits = '00000000'[len(bits):] + bits
            result.extend([int(b) for b in bits])
        return result

    def _bits_to_string(self, bits):
        """0 ve 1 listesini tekrar String ifadeye çevirir."""
        chars = []
        for i in range(0, len(bits), 8):
            byte = bits[i:i+8]
            if len(byte) < 8: break
            s_byte = "".join(str(b) for b in byte)
            chars.append(chr(int(s_byte, 2)))
        return "".join(chars)

    def _rule30_step(self, current_row):
        """
        Rule 30 Mantığı:
        Yeni Hücre = Sol_Komşu XOR (Kendisi OR Sağ_Komşu)
        """
        next_row = []
        # Sınır değerleri için padding (0 ekle)
        padded = [0] + current_row + [0]
        
        for i in range(1, len(padded) - 1):
            left = padded[i-1]
            center = padded[i]
            right = padded[i+1]
            
            new_val = left ^ (center | right)
            next_row.append(new_val)
        return next_row

    def generate_keystream(self, length):
        """
        İstenilen uzunlukta rastgele bit dizisi (keystream) üretir.
        Her adımda satırın ortasındaki biti alır.
        """
        keystream = []
        current_row = self.state.copy()
        
        for _ in range(length):
            current_row = self._rule30_step(current_row)
            # Kaosun en yoğun olduğu orta noktayı al
            mid_index = len(current_row) // 2
            keystream.append(current_row[mid_index])
            
        return keystream

    def encrypt(self, plaintext):
        """Metni şifreler."""
        plaintext_bits = self._string_to_bits(plaintext)
        keystream = self.generate_keystream(len(plaintext_bits))
        
        # XOR İşlemi (Şifreleme)
        cipher_bits = [p ^ k for p, k in zip(plaintext_bits, keystream)]
        
        # Şifreli veriyi hex formatında döndür (okunabilir olması için)
        cipher_hex = "".join(str(b) for b in cipher_bits)
        # Binary string'i hex'e çevirerek daha kısa gösterim sağla
        return hex(int(cipher_hex, 2))[2:]

    def decrypt(self, cipher_hex):
        """Hex formatındaki şifreli veriyi çözer."""
        # Hex'ten binary listesine dön
        binary_str = bin(int(cipher_hex, 16))[2:]
        # Baştaki kayıp 0'ları tamamla (mod 8'e göre)
        while len(binary_str) % 8 != 0:
            binary_str = '0' + binary_str
            
        cipher_bits = [int(b) for b in binary_str]
        
        # Aynı seed ile aynı keystream'i üret
        keystream = self.generate_keystream(len(cipher_bits))
        
        # XOR İşlemi (Çözme - XOR'un tersi yine XOR'dur)
        plaintext_bits = [c ^ k for c, k in zip(cipher_bits, keystream)]
        
        return self._bits_to_string(plaintext_bits)
