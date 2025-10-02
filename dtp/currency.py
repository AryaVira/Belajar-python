print("selamat datang di konversi mata uang ke rupiah \n 1. Euro \n 2. Dolar")

selection = int(input("Masukkan pilihan 1/2 :"))

if selection == 1 :
    euro = int(input(" masukkan jumlah uang euro:"))
    print("jika" ,euro, "euro dijumlahkan ke rupiah menjadi:", euro * 19294, "rupiah")
else:
    dolar = int(input("Masukkan jumlah dollar :"))
    print("jika", dolar, "dolar :dijumlahkan ke rupiah menjadi:", dolar * 16000, "rupiah")