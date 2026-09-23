#Membuat list 
cart = ["T-shirt", "lamp", "pen"]
print(cart)

listgw = (1, "Hdp JKW", 2.3)
print(listgw)

blank = []
print(blank)

print()

huruf_vokal = "AIUEO"

huruf_vokal_list = list(huruf_vokal)
print(huruf_vokal_list)

print()

#Mengakses item-item dalam daftar 
kopi = ['Robusta', 'Arabica', 'cappucino']

print(f"kopi[0] = {kopi[0]}")
print(f"kopi[1] = {kopi[1]}")


print() 

#index negatif
kopi = ['Robusta', 'Arabica', 'cappucino']

print(f"kopi[-1] = {kopi[-1]}")
print(f"kopi[-2] = {kopi[-2]}")

#Menambahkan dan memperbarui item 
#1. Updating item
kopi = ["Robusta", "Arabica", "Cappucino"]

kopi[1] = "Coffe Latte"

print(kopi)

print() 

#2. Menambah item 
kopi = ["Robusta", "Arabica", "Cappucino"]

kopi.append("Coffe Latte")

print(kopi)

#3. Menambahkan semua elemen dari daftar yang tersedia 
menu = ["Robusta", "Arabica", "Cappucino"]
side_dish = ["French fries", "Onion ring", "Chicken nugget"]

menu.extend(side_dish)

print(menu)

#4. Memasukkan elemen ke posisi tertentu
menu = ["Nasi goreng", "Sate padang", "Rendang"]

menu.insert(1, "Tunjang")

print(menu)

print() 

#Menghapus item dari daftar
menu = ["Robusta", "Arabica", "Cappucino", "Caffe Latte", "Mocha"]

kopi.remove("Robusta")

#Menghapus item terakhir 
last_item = kopi.pop() 
print(kopi)
print(last_item)

#Clear list 
kopi.clear
print(kopi)

#Juga dapat menggunakan "Del" untuk menghapus item-item tertentu, atau bahkan seluruh daftar 
menu = ["Robusta", "Arabica", "Cappucino", "Caffe Latte", "Mocha"]

del menu[2]
print(menu)

del menu

print() 

#Menyalin daftar 
menu = ["Robusta", "Arabica", "Cappucino", "Caffe Latte", "Mocha"]

keranjang = menu.copy()

keranjang.append("Espresso")

print(f"Menu = {menu}")
print(f"Keranjang = {keranjang}")

print() 

#The function len() 
kopi = ["Robusta", "Arabica", "Cappucino", "Caffe Latte", "Mocha"]

size = len(kopi)
print(size)

#List membership test
kopi = ["Robusta", "Arabica", "Cappucino", "Caffe Latte", "Mocha"]

result = "Cappucino" in kopi
print(result)

result = "Palm Sugar Coffe" in kopi 
print(result)

#Iterating through a list 
menu = ["Robusta", "Arabica", "Cappucino", "Caffe Latte", "Mocha"]

for kopi in menu:
    print(kopi)
