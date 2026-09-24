#Frist function 
def greet():
    print("Selamat Siang!")

#Memanggil function 
def greet(): 
    print("Selamat Malam, Hows your day?")

greet()

print("Outside Function")

print()

#Function Arguments
def keripik(bahan):
    print("Keripik", bahan)

keripik("pisang")

print()

#Functioin untuk menjumlahkan dua bilangan
def jumlah(angka1, angka2): 
    sum = angka1 + angka2
    print("Sum: ", jumlah)

jumlah(23, 12)

print() 

#The return statement 
def kuadrat(angka):
    hasil = angka * angka
    return hasil

square = kuadrat(8)

print("Hasil kuadrat: ", square)

print()

#The pass statement
def future_function():
    pass

future_function()

print() 

#Function dalam pustaka(library) python 
import math

akar_kuadrat = math.sqrt(25)

print("Akar kuadrat dari 25 adalah: ", akar_kuadrat)

pangkat = pow(2, 4)

print("Hasil dari 2 pangkat 4 adalah: ", pangkat)
