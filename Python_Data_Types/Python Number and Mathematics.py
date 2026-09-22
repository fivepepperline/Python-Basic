#Tipe data int, float dan complex 
a= 6 
b = 6.71
c = 6 + 5j 

print(a, 'type datanya adalah: ', type(a))
print(b, 'type datanya adalah: ', type(b))
print(c, 'type datanya adalah: ', type(c))

#sistem bilangan
print(0b1101011)  

print(0xFB + 0b10)  

print(0o15)  

print() 

#konversi tipe data 
angka1 = int(2.3)
print(angka1)

angka2 = int(-2.8)
print(angka2)

angka3 = complex(4+6j)
print(angka3)

angka4 = float(5.8)
print(angka4)

print()

#Module acak python 
import random 

print(random.randrange(10, 20))

list1 = ['a', 'b', 'c', 'd', 'e']

print(random.choice(list1))

random.shuffle(list1)

print(list1)

print(random.random)

print() 

#Matematika dengan Python 
import math 

print(math.pi)

print(math.cos(math.pi))

print(math.exp(10))

print(math.log10(1000))

print(math.sinh(10))

print(math.factorial(6))