#python boolean 

#sebuah nilsi boolean, False, ditetapkan ke variabel is_valid
is_valid = False

#sebuah nilai boolean, True, ditetapkan ke variabel is_valid
is_valid = True

#Kata Falsea dianggap sebagai sebuah variabel 
is_valid = False

#contoh < dan <= 
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))

result = (a < b)
print(f"a < b ---> {result}")
result = (a <= b)
print(f"a <= b ---> {result}")
result = (a > 10)
print(f"a > 10 ---> {result}")
result = (a >= 10)
print(f"a >= 10 ---> {result}") 

print() 

#contoh == dan !=
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))    

result = (a == b)
print(f"a == b ---> {result}")
result = (a != b)
print(f"a != b ---> {result}")
result = (a == 10)
print(f"a == 10 ---> {result}")
result = (a != 10)
print(f"a != 10 ---> {result}") 

print() 
#operasi == dan != juga bisa digunakan untuk membandingkan string

nama1 = "Londo Ireng"
print(nama1 == "Londo Ireng") #True
print(nama1 != "londo Ireng") #False
print(nama1 == "Londo Ireng") #True
print(nama1 != "Londo ireng") #False

print() 

#Operasi Logika 
#1. The and operator
umur = int(input("Masukkan umur: "))
warga_negara = input("WNI (ya/tidak)?: ")

#true jika umur (age >= 17) dan (warga_negara == "ya")
result = (umur >= 17) and (warga_negara == "ya")
print(result)

print()

#The or operator
umur = int(input("Masukkan umur: "))
warga_negara = input("WNI (ya/tidak)?: ")

#true jika salah astu (age >= 17) atau (warga_negara == "ya") adalah true 
result = (umur >= 17) or (warga_negara == "ya")
print(result)

print()
#The not operator
password = "3311"
masukkan_password = input("Masukkan password: ")

result = (password == masukkan_password)
print(f"apakah password sama dengan kode akses?: {result}")

result = not (password == masukkan_password)
print(f"apakah password tidak sama dengan kode akses?: {result}")

#Fungsi bool()
# 0 is false 
print(bool(0))

#non-zero is true
print(bool(15))

#non-empty string is true
print(bool("Londo Ireng"))
print(bool("False"))

#empty string is false
print(bool(""))