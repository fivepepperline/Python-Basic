#while loop tak terbatas 
angka = float(input('Masukkan angka: '))

while angka >= 0.0:
    print(angka)

print()

#while loop terbatas 
angka = float(input("Masukkan angka: "))

while angka >= 0.0:
    print(angka)

    number = float(input("Masukkan angka lagi: "))

print() 

#Indentation
pekerjaan = input("Aktivitas: ")

while pekerjaan != "q":
    print("Aktivitas Selesai!")
    pekerjaan = input("Aktivitas: ")

print("Semua Aktivitas Telah Dilakukan")

#Print angka dari 1 sampai n 
a = 10 
i = 1

while i <= a: 
    print(i)
    i += 1 

#menjumlahkan angka hingga user menginput nol 
total = 0 
n = float(input("Masukkan sebuah angka (0 hingga berhenti):"))

while n != 0.0: 
    total += n
    n - float(input("Masukkan sebuah angka (o hingga berhenti):"))

print(f"Sum: {total}")

print() 

#Break dan Continue statement 
#1. Break
while True:
    angka = int(input("Masukkan sebuah angka: "))
    if angka == 0:
        break
    print(angka)

print()

#2. Continue
i = 0

while i <= 10:
    i += 1 

    if i % 2 != 0:
        continue 
    print (i)

print()

#while loop dengan klausa else
attempts = 3

while attempts > 0: 
    pin = input("Masukkan PIN: ")

    if pin == "1616": 
        print("Akses Diberikan")
        break 
    attempts -= 1
    print(f"PIN Salah. {attempts} percobaan tersisa. ")
else: 
    print("Akun Terkunci. Terlalu banyak percobaan.")