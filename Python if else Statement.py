#python if statement 
umur = int(input("Masukkan umur Anda: "))
if umur >= 17:
    print("Anda sudah dewasa.")
print("Program selesai.")

print()

#Python if else statement
umur = int(input("Masukkan umur Anda: "))
if umur >= 17:
    print("Anda sudah dewasa.")
else:
    print("Anda belum dewasa.")
print("Program selesai.")

print()

#autentikasi login pengguna menggunakan if else  
usernam_db = "admin"
password_db = "cihuy123"

username = input("Masukkan username: ")
password = input("Masukkan password: ")

if (username == usernam_db) and (password == password_db):
    print("Login berhasil.")
else:
    print("Username atau password salah.")
print("Program selesai.")

print() 

#python if elif else statement 
umur = int(input("Masukkan umur Anda: "))

if umur < 0:
    print("Anda belum dewasa.") 
elif umur >= 17:
    print('akses diberiikan')
else:
    print("akses ditolak.")

print()

#nested if statement 
umur = int(input('masukkan umur anda: '))

if umur < 17:
    if umur < 0: 
        print("umur salah")
    else: 
        print('akses ditolak')
else: 
    print("Akses diberikan")