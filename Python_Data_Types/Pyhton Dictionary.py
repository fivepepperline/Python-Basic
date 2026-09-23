#Membuat Dictionary 
ibukota_negara = {
    "Indonesia": "Jakarta",
    "Malaysia": "Kuala Lumpur", 
    "Thailand": "Bangkok"
}

print(ibukota_negara)

print() 

#Keys dalam kamus harus bersifat tidak dapat diubah.
my_dict = {1: "one", 2: "two", 3: "three"}

my_dict = {(1, 2): "one two", 3: "three"}

#my_dict = {1: "Hello", [1, 2]: "Hello Hi"}

my_dict = {"USA": ["Chicago", "California", "New York"]}

#baris kode yang ditandai dengan pagar artinya tidak boleh, yakni menggunakan list sebagai key 

#Keys dalam sebuah kamus harus bersifat unik
hogwarts_houses = {
    "Harry Potter": "Gryffindor",
    "Hermione Granger": "Gryffindor",
    "Ron Weasley": "Gryffindor",
    # duplicate key with a different house
    "Harry Potter": "Slytherin"
}

print(hogwarts_houses)

print() 


#Acces dictionary items 
ibukota_negara = {
    "Indonesia" : "Jakarta",
    "Malaysia" : "Kuala Lumpur", 
    "Thailand" : "Bangkok"
}

print(ibukota_negara["Indonesia"])
print(ibukota_negara["Thailand"])

print() 

#Menambah item ke dalam dictionary 
ibukota_negara = {
    "Indonesia" : "Jakarta",
    "Malaysia" : "Kuala Lumpur", 
    "Thailand" : "Bangkok"
}

ibukota_negara["Vietnam"] = "Hanoi"

print(ibukota_negara)

print() 

#Remove dictionary items 
ibukota_negara = {
    "Indonesia" : "Jakarta",
    "Malaysia" : "Kuala Lumpur", 
    "Thailand" : "Bangkok"
}

del ibukota_negara ["Indonesia"]

print(ibukota_negara, "\n")

#mengahpus menggunakan metode clear
ibukota_negara = {
    "Indonesia" : "Jakarta",
    "Malaysia" : "Kuala Lumpur", 
    "Thailand" : "Bangkok"
}

ibukota_negara.clear() 

print(ibukota_negara)

print() 

#Mengubah entri-entri dalam dictionary 
ibukota_negara = {
    "Indonesia" : "Jakarta",
    "Malaysia" : "Kuala Lumpur", 
    "Thailand" : "Bangkok",
    "Vietnam" : "Ho Chi Minh"
}

ibukota_negara["Vietnam"] = "Hanoi"

print(ibukota_negara)

print() 

#Iterate through a dictionary 
ibukota_negara = {
    "Indonesia" : "Jakarta",
    "Malaysia" : "Kuala Lumpur", 
    "Thailand" : "Bangkok",
    "Vietnam" : "Hanoi"
}

for negara in ibukota_negara: 
    print(negara)

print() 

for negara in ibukota_negara:
    ibukota = ibukota_negara[negara]
    print(ibukota)

print() 

#Find dictionary length (cari panjang kamus)
ibukota_negara = {
    "Indonesia" : "Jakarta",
    "Malaysia" : "Kuala Lumpur", 
    "Thailand" : "Bangkok",
    "Vietnam" : "Ho Chi Minh"
}

print(len(ibukota_negara))

print() 

#Dictionary member test (tes keanggotaan kamus)
file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image",
}

# use of in and not in operators
print(".pdf" in file_types)       # Output: True
print(".mp3" in file_types)       # Output: False
print(".mp3" not in file_types)   # Output: True