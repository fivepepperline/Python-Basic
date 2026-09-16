#iterasi melalui list 
models = ['ChatGpt', 'Claude', 'Gemini']

for model in models:
    print(model)
    print("---")

print()

#indentation in loop 
numbers = [1,2,3]

for num in numbers:
    print(f"Processing: {num}")
    print(f"Done With: {num}")

print("all done")

print() 

#for loop dalam jangkauan (range())
values = range(1, 5)

for i in range (1, 11):
    print(f"Display product: {i}")

print()

#iterasi melalui string 
minum = "air putih"
for i in minum:
    print(i)

print()

#Break dan Continue Statement 
#1. Break 

for num in range(1, 11):
    if num == 3: 
        break 
    print(num)

print() 

#2. Continue 
for num in range(1, 11):
    if num == 3: 
        continue 
    print(num)

print() 

#for loop with else 
stock = ['76 Apel', 'Surya 12', 'Magnum']

pesan = input("Masukkan produk yang dibeli: ")

for produk in stock: 
    if produk == stock:
        print(f'{pesan} tersedia. Ditambahkan ke keranjang.')
        break
else: 
    print(f"Maaf, {pesan} habis")

print()

#menggunakan loop tanpa menggunakan elemen-elemen tertentu
for _ in range (0, 4):
    print('Hidup JKW')

print() 
total = 0 

for i in range (1, 11): 
    total += i 

print(f'jumlah: {total}')

#mested loop (perulangan bersarang)
attributes = ['Electric', 'fast']
cars = ['Tesla', "BMW", 'Mercedes']

for attribute in attributes:
    for car in cars: 
        print(attribute, car)

    print('----')