#Membuat set dalam python
student_id = {115, 114, 116, 118, 115}
print("Student id: ", student_id)

huruf_vokal = {"a", "i", "u", "e", "o"}
print("Huruf vokal yakni: ",huruf_vokal)

data_campuran = {123, 'set', 7.9, -33}
print("random: ", data_campuran)

#Membuat himpunan kosong dalam python 
empty_set = set()

empty_dictionary = { }

print('Data type of empty_set:', type(empty_set))

print('Data type of empty_dictionary:', type(empty_dictionary))

#Elemen yang sama dalam suatu kumpulan (set)
angka = {5, 6, 5, 3, 3, 5, 6, 8, 90, 1, 0, 2, 8, 8, 4, 2, 3, 6, 8, 5}
print(angka)

print() 

#Menambahkan item ke dalam sebuah set dalam python 
angka = {65, 32, 92, 45}

print("Set awal: ",angka)

angka.add(47)

print("Update set: ",angka)

print() 

#Update python set
perusahaan = {"Petronas", "HCBC", "Airbus"}
tech_companies = ["Google", "Microsoft", "Apple"]

perusahaan.update(tech_companies)

print(perusahaan)

print() 

#Menghapus elemen dari sebuah himpunan 
negara = {"Indonesia", "Belanda", "Jepang"}

print("Set Awal: ", negara)

removedValue = negara.discard("Belanda")

print("Update set: ", negara)

#Iterate over set a python 
buah_buahan = {"apel", "mangga", "jeruk"}

for f in buah_buahan:
    print(buah_buahan)

print() 

#Mengetahui jumlah elemen dari suatu set 
angka = {5, 4, 2, 7, 2, 7, 9, 1}

print("set: ", angka)

print("total elemen: ",len(angka))

print() 

#Operasi set dalam python 
#1. Union (penggabungan)
A = {2, 5, 8}
B = {9, 4, 1}

print("Union menggunakan |: ". A|B)
print("Union menggunakan union(): ", A.union(B))

print() 

#2. Intersection (perpotongan
A = {2, 5, 8}
B = {9, 4, 1}

print("Intersection Using & : ", A & B)
print("intersection using intersection()", A.intersection(B))

print()

#3. Diffrence (selisih)
A = {2, 5, 8}
B = {9, 4, 1}

print("Differnce Using - : ", A - B)
print("Differnce Using Diffrence(): ", A.difference(B))

print() 

#4. Set symmeteric diffrence (beda setangkup)
A = {2, 5, 8, 6, 3, 4}
B = {9, 4, 1, 2, 7, 3}

print("Using ^: ", A ^ B)
print("Usong symmetric.diffrence(): ", A.symmetric_difference(B))

print()

#Periksa apakah kedua himpunan itu sama
A = {2, 5, 8, 6, 3, 4}
B = {9, 4, 1, 2, 7, 3}

if A == B:
    print('Himpunan A dan Himpunan B sama')
else: 
    print("Himpunan tidak sama")
