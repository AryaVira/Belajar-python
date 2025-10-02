# 1. Impor modul 'random' untuk menghasilkan angka acak
import random

# 2. Komputer memilih angka rahasia antara 1 dan 20
angka_rahasia = random.randint(1, 20)
jumlah_tebakan = 0

print("Halo! Aku sedang memikirkan sebuah angka antara 1 sampai 20.")
print("Coba tebak angka itu!")

# 3. Mulai perulangan (loop) yang akan terus berjalan
while True:
    # 4. Minta pemain memasukkan tebakan
    # Kita bungkus dengan int() untuk mengubah teks input menjadi angka (integer)
    try:
        tebakan_pemain = int(input("Masukkan tebakanmu: "))
        jumlah_tebakan += 1 # Tambah jumlah tebakan setiap kali pemain menebak

        # 5. Bandingkan tebakan dengan angka rahasia
        if tebakan_pemain < angka_rahasia:
            print("Tebakanmu terlalu RENDAH! Coba lagi.")
        elif tebakan_pemain > angka_rahasia:
            print("Tebakanmu terlalu TINGGI! Coba lagi.")
        else:
            # 6. Jika tebakan benar, hentikan loop dan tampilkan pesan kemenangan
            print(f"Selamat! Kamu berhasil menebak angkanya, yaitu {angka_rahasia}.8")
            print(f"Kamu memerlukan {jumlah_tebakan} kali tebakan.")
            break # Hentikan perulangan 'while'
    except ValueError:
        # Menangani jika input bukan angka
        print("Oops! Itu bukan angka. Coba masukkan angka yang valid.")