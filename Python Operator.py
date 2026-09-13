#operasi aritmatika
a = 9
b = 3

print(" a + b = ", a + b)
print(" a - b = ", a - b)
print(" a * b = ", a * b)
print(" a / b = ", a / b)   
print(" a // b = ", a // b)
print(" a ** b = ", a ** b)   

print() 

#perbandingan
a = 9
b = 3

print(" a > b = ", a > b)   
print(" a < b = ", a < b)
print(" a == b = ", a == b)
print(" a != b = ", a != b)
print(" a >= b = ", a >= b)
print(" a <= b = ", a <= b)

print() 

#operasi logika
a = True
b = False
print(" a and b = ", a and b)
print(" a or b = ", a or b)
print(" not a = ", not a)

print()

#bitwise operator
a = 9  
b = 3

print(" a & b = ", a & b)
print(" a | b = ", a | b)
print(" a ^ b = ", a ^ b)
print(" ~a = ", ~a)
print("a ^ b = ", a ^ b)
print(" a << 1 = ", a << 1)
print(" a >> 1 = ", a >> 1)

print()

#assigment operator 
a = 6

print("a = ", a)
print("a += 6 -> ", a + 6)
print("a -= 6 -> ", a - 6)
print("a *= 6 -> ", a * 6)
print("a /= 6 -> ", a / 6)
print("a %= 6 -> ", a % 6)
print("a //= 6 -> ", a // 6)
print("a **= 6 -> ", a ** 6)
print("a &= 6 -> ", a & 6)
print("a |= 6 -> ", a | 6)
print("a ^= 6 -> ", a ^ 6)
print("a >>= 6 -> ", a >> 6)
print("a <<= 6 -> ", a << 6)

print()

#Special Operators, ada dua jenis yang pertama yaitu: 
#1. Identity Operator
a = 9
b = 3
a2 = 'hai'
b2 = 'hai'
a3 = [1, 2, 3]
b3 = [1, 2, 3]
print("a is b = ", a is b)
print("a2 is b2 = ", a2 is b2)
print("a3 is b3 = ", a3 is b3)

print() 

#2. Membership Operator
a = "hai sipil"
b = {1: 'a', 2: 'b'}
print("h" in a)
print("Hai" not in a)
print(1 in b)
print('a' in b)
