#infinte while loop 
number = float(input('Masukkan angka: '))

while number >= 0.0:
    print(number)

print()

#while loop terbatas (finite)
angka = float(input('Masukkan angka: '))

while number >= 0.0:
    print(angka)

    angka = float(input("Masukkan angka lain: "))

print()

aktivitas = input('Aktivitas: ')

while aktivitas != "q":
    print("Task Done!")
    aktivitas = input("Aktivitas: ")

print("All Task Completed!")

print() 

#Print angka-angka dari 1-10 

n = 10
i = 1

while i <= n:
    print(i)
    i += 1

#menjumlahkan angka-angka hingga user memasukkan angka 0 
total = 0 
n = float(input("Masukkan angka: "))

while n != 0:
    total += n 
    n = float(input("Masukkan angka: "))

print(f"sum: {total}")

print()

#break and continue 
#1. Break 

while True:
    number = int(input("Masukkan angka: "))
    if number == 0:
        break
    print(number)

#2. Continue
i = 0

while i <= 10:
    i += 1

    if i % 2 != 0:
        continue

    print(i)

print()

#while dengan klausa else
attemps = 3

while attemps > 0:
    pin = input("Enter pin: ")

    if pin == "1234":
        print("Acces granted.")
        break
    attemps -= 1
    print(f"Wrong PIN. {attemps} tries left.")
else: 
    print("Account Locked. Too many failed attemps.")
