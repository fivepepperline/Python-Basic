#Konversi tipe data implisit dalam python 
#1. Mengoversi bilangan bulat menjadi desimal (interger to float)
int_num = 15
float_num = 7.8 

new_num = int_num + float_num

print("Value: ", new_num)
print("Data type: ", type(new_num))

print() 

#Konversi tipe data eksplisit 
#2. Penjumlahan bilangan bulat dengan menggunankan konversi eksplisit 
num_string = '16'
num_int = 45

print("Tipe data sebelum dikonversi: ", type(num_string))

num_string = int(num_string)

print("Tipe data setelah dikonversi: ", type(num_string))

num_jumlah = num_string + num_int

print("Jumlah: ", num_jumlah)
print("Tipe data 'jumlah' adalah: ", type(num_jumlah))