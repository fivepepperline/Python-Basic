#penggunaan break dalam loop 
angka = int(input("Masukkan sebuah angka: "))
for i in range (1, 6):

    if i == angka:
        break 
    print(i)

print(i)

#Memototng siklus while secara paksa
while True:
    angka = int(input("Masukkan sebuah angka: "))
    if angka < 0: 
        break 
    print(f"Angka yang kamu masukkan adalah: {angka}")

#continue dalam for loop 
for i in range (1,11):
    if i % 2 == 0: 
        continue 
    print(i)

print() 

#Jumlah dari bilangan postif-positif saja
total = 0

while True:
    angka = int(input("Masukkan sebuah angka(0 untuk stop): "))

    if angka < 0: 
        continue 

    if angka == 0: 
        break 

    total += angka

print(f"Total dari angka positif adalah: {total}")

print() 

#loop dengan klausa else 
stock = ['Laptop', 'Keyboard', 'Mouse']

order = input("Enter produt yo want to buy: ")

for product in stock: 
    if product == stock: 
        print(f"{order} is available. Adding to cart.")
        break 
else:
    print(f"Sorry, {order} is out of stock.")
