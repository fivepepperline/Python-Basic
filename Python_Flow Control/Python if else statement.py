#contoh penggunaan if dalam python 
umur = int(input("Masukkan umur Anda: "))

if umur >= 17:
    print("Anda sudah bisa membuat KTP")

print("Program selesai")

print() 

#contoh if else
tinggi_badan = int(input("Masukkkan tinggi badan anda(dalam cm20): "))

if tinggi_badan >= 160:
    print("Silahkan Masuk")
else: 
    print("Maaf, Anda tidak boleh masuk")


#simpel autentikasi dengan py
username_db = "admin"
password_db = "1145"

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == username_db and password == password_db:
    print("Welcome back")
else: 
    print("Acces denied")

print()

#py if elif else
suhu = int(input('Masukkan suhu (Celcius): '))

if suhu >= 35:
    print("Sangat Panas")
elif suhu >= 30:
    print("Panas")
elif suhu >= 25:
    print("Sejuk")
else:
    print("Dingin")

print()

#nested if statement
umur = int(input("Nasukkan umur Anda: "))

if umur < 18:

    if umur < 0: 
        print("Umur tudak sah")
    else: 
        print("Akses ditolak")
else:
    print("Akses diberikan")

#short hand if else 
umur = 22
status = "Adult" if umur >= 18 else "Minor"
print(status)

print()

#mencari angka terbesar dari 3 angka 
a1 = float(input('Masukkan angka pertama: '))
a2 = float(input('Masukkan angka kedua: '))
a3 = float(input("Masukkan angka ketiga: "))

if a1 >= a2 and a2 >= a3: 
    terbesar = a1
elif a2 >= a1 and a2 >= a3:
    terbesar = a2 
else: 
    terbesar = a3

print("Angka paling besar adalah: ", terbesar)



