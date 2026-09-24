#python function arguments 
def angka(a, b):
    sum = a + b
    print("Jumlah: ", sum)

angka(4, 16)

print() 

#Function argument with default value
def angka(a = 5, b = 10):
    sum = a + b
    print("Hasil Penjumlahan: ", sum)

angka(2, 6)

angka(a = 21)

angka() 

print()

#Python keyword arguments
def display_info(nama_depan, nama_belakang):
    print("Nama depan: ", nama_depan)
    print("Nama belakang: ", nama_belakang)

display_info(nama_belakang = "Burgers", nama_depan = "Allison")

print()

#Function with abitrary arguments
def find_jumlah(*angka):
    hasil = 0

    for i in angka:
        hasil = hasil + i

    print('Jumlah: ', hasil)

find_jumlah(8, 9, 4, 1)

find_jumlah(3, 5, 1, 7, 1)
