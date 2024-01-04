# Fungsi ini mengimplementasikan algoritma Euclidean untuk mencari Greatest Common Divisor (GCD) dari dua bilangan.
# Mengembalikan tuple (g, x, y), di mana g adalah GCD dan x, y adalah koefisien untuk representasi GCD.
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

# Menggunakan fungsi egcd untuk mencari invers modular dari a modulo m.
# Mengembalikan nilai x yang memenuhi (a * x) % m = 1.
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse tidak ada')
    else:
        return x % m

# affine cipher
def affine_cipher(text, a, b, mode):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_,.'"
    mod_value = len(characters)

    result = ""
    for char in text:
        if char in characters:
            char_index = characters.index(char)
            if mode == 'encrypt':
                result += characters[(a * char_index + b) % mod_value]
            elif mode == 'decrypt':
                a_inv = modinv(a, mod_value)
                result += characters[(a_inv * (char_index - b)) % mod_value]
        else:
            result += char
    return result

# vigenere cipher
def vigenere_cipher(text, key, mode):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_,.'"
    mod_value = len(characters)
    key_length = len(key)
    result = ""

    for i, char in enumerate(text):
        if char in characters:
            char_index = characters.index(char)
            key_index = characters.index(key[i % key_length])
            if mode == 'encrypt':
                result += characters[(char_index + key_index) % mod_value]
            elif mode == 'decrypt':
                result += characters[(char_index - key_index) % mod_value]
        else:
            result += char
    return result

def vigenere_decipher(text, key):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_,.'"
    mod_value = len(characters)
    key_length = len(key)
    result = ""

    for i, char in enumerate(text):
        if char in characters:
            char_index = characters.index(char)
            key_index = characters.index(key[i % key_length])
            result += characters[(char_index - key_index) % mod_value]
        else:
            result += char
    return result

def affine_decipher(text, a, b):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_,.'"
    mod_value = len(characters)
    a_inv = modinv(a, mod_value)
    result = ""

    for char in text:
        if char in characters:
            char_index = characters.index(char)
            result += characters[(a_inv * (char_index - b)) % mod_value]
        else:
            result += char
    return result

# Meminta input dari pengguna
option = input("Pilih opsi:\n1. Enkripsi\n2. Dekripsi\nPilihan (1/2): ")
text = input("Masukkan teks: ")

if option == '1':
    # Melakukan Affine Cipher
    a = int(input("Masukkan kunci a untuk Affine Cipher (integer): "))
    b = int(input("Masukkan kunci b untuk Affine Cipher (integer): "))
    vigenere_key = input("Masukkan kunci Vigenere Cipher: ")

    affine_result = affine_cipher(text, a, b, 'encrypt')
    print(f"Hasil Enkripsi Affine Cipher: {affine_result}")

    final_result = vigenere_cipher(affine_result, vigenere_key, 'encrypt')
    print(f"Hasil Enkripsi modifikasi: {final_result}")

elif option == '2':
    # Melakukan dekripsi Vigenere Cipher
    vigenere_key = input("Masukkan kunci Vigenere Cipher: ")
    vigenere_decrypted = vigenere_decipher(text, vigenere_key)

    # Cetak hasil Vigenere Cipher
    print(f"Hasil Dekripsi sementara: {vigenere_decrypted}")

    # Melakukan dekripsi Affine Cipher
    a = int(input("Masukkan kunci a untuk Affine Cipher (integer): "))
    b = int(input("Masukkan kunci b untuk Affine Cipher (integer): "))
    final_decrypted = affine_decipher(vigenere_decrypted, a, b)
    print(f"Hasil Dekripsi modifikasi cipher: {final_decrypted}")

else:
    print("Opsi tidak valid. Pilih '1' untuk enkripsi atau '2' untuk dekripsi.")
