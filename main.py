import sys
a = "hello world"
print(sys.getrefcount(a))

a = b = 2566
a = 2566
b=a
print(id(a), id(b))

b = 4000
print(id(a), id(b))

print(type(a))
print(type("tekst"))
print(type(False))
print(type(40.0))

import math
a,b,c,d,e = 1.5,2.5,3.5,4.5,5.5
print(a+b+c+d+e)
print(round(a)+round(b)+round(c)+round(d)+round(e))
print(int(a)+int(b)+int(c)+int(d)+int(e))
print(math.ceil(a)+math.ceil(b)+math.ceil(c)+math.ceil(d)+math.ceil(e))

10 == 11

bool(1)
bool("tekst")
nic=None
print(bool(nic))

a=21

if a > 20:
    print("a wieksze od 20")
else:
    print("czy mniejsze od 20?")

a=19

if a > 20:
    print("a wieksze od 20")
else:
    print("czy mniejsze od 20?")


a=20

if a > 20:
    print("a wieksze od 20")
elif a < 20:
    print("  mniejsze od 20")
else:
    print("a rowne 20")

tekst = 'to jest tekst'
tekst2 = 'to jest drugi tekst'
tekst2 ="'to' jest \ndrugi tekst"

print(tekst2)
a = 20.547

b = 45
print(f"to jest pierwsza liczba {a},\n to jest druga liczba {b}")
print(tekst2.upper())
print(tekst2.lower())
print(tekst2.title())

