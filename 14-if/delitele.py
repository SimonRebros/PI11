# while True:
#     cislo = int(input("zadaj cislo(pre ukoncenie zadaj 0): "))
#     if cislo == 0:
#         print("cislo je nula")
#         break
#     elif cislo % 2 ==0:
#             print("parne")
#     else:
#             print("neparne")
while True:

    cislo = int(input("zadaj cislo(pre ukoncenie zadaj 0): "))
    pocet = 0
    print("delitele:", end =" ")
    for delitel in range(1, cislo + 1):
        if cislo % delitel == 0:
            print(delitel, end=" ")
            pocet += 1
    print()
    print("pocet delitelov je:", pocet )
    if cislo == 0:
        break
    if cislo % cislo and 1:
        print("cislo je prvocislo")

