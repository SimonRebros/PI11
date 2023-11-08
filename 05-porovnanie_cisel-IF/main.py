"""
a = int(input("zadajcislo a: "))
b = int(input("zadajcislo b: "))
c = int(input("zadajcislo c: "))
if a == b == c:
    print("cisla sa rovnaju")
else:
  if a > b:
    if a > c:
        print("najvacsie cislo je", a)
    else:
        print("najvacie cislo je", c)
  else:
   if b > c:
    print("najvacsie cislo je", b)
   else:
     print("najvacsie cislo je", c)
"""
a = int(input("zadajcislo a: "))
b = int(input("zadajcislo b: "))
c = int(input("zadajcislo c: "))
d = int(input("zadajcislo d: "))
e = int(input("zadajcislo e: "))
max = a
if max < b:
    max = b
if max < c:
    max = c
if max < d:
    max = d
if max < e:
    max = e
print("najvacsie cislo je", max)
