#mengubah interger ke float
a = 16
b =  1.1

nomor_baru = a + b 

print("value: ", nomor_baru)
print("Data type: ", type(nomor_baru))

print() 

#Penjumlahan string dan interger menggunakan konversi eksplisit
nomor_string = "100"
nomor_interger = 50 

print("Tipe data nomor_string sebelum type casting: ", type(nomor_string))

#eksplist konversi tipe data 
nomor_string = int(nomor_string)

print("Tipe data nomor_string setelah type casting: ", type(nomor_string))

jumlah = nomor_string + nomor_interger

print("hasil penjumlahan: ", jumlah)
print("Tipe data hasil penjumlahan: ", type(jumlah))

print()