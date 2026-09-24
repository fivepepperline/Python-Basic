#python module addition 
def add(a, b):
    result = a + b
    return result

print() 

#import python standard library modules
import math 

print("Nilai dari pi adalah:", math.pi)

print()

#import python dengan pergantian nama
import math as m

print("Nilai pi adalah: ", m)

print() 

#python form... pernyataan import
from math import pi 

print(pi)

print() 

#import all names
from math import *

print("Nilai pi adalah: ")

print()

#the dir() built-in function 
'''print(dir(example))

['__builtins__',
'__cached__',
'__doc__',
'__file__',
'__initializing__',
'__loader__',
'__name__',
'__package__',
'add']

import example

example.__name__

a = 1
b = "hello"

import math

print(dir())

['__builtins__', '__doc__', '__name__', 'a', 'b', 'math', 'pyscripter']
'''