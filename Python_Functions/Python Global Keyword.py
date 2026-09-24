#Akses dan mengubah variabel global dalam python 
#1. Define the global 
a = 1

def jumlah():
    print(a)

jumlah()

print()

#2. Mengubah nilai variabel (ditulis menggunakan triple quote supaya kode tidak dieksekusi yang akan menyebabkan error)
'''
a = 1 
def jumlah():
    a = a + 2
    
    print(a)

jumlah()'''

#3. Mengubah nilai variabel global dari dalam suatu fungsi dengan menggunakan keyword 'global'
a = 1

def jumlah():

    global a

    a = a + 5
    print(a)

jumlah()

print()