username = input("masukkan username anda")
password = input("masukkan password anda")

if username == "admin" and password == "12345":
    print("anda berhasil login")
elif username == "admin":
    print("password error")
else:
    print("error, silahkan masukkan username dan password")