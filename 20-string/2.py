retazec = input("zadaj slovo:")
print(retazec)


for i,znak in enumerate(retazec):
     print(i, znak)

# for i in reversed(range(len(retazec))):
#        print(i,retazec[i])

# for i in range(1,len(retazec)+1):
#         print(-i,retazec[i])

for i in range(-1,-len(retazec)-1,-1):
        print(i,retazec[i])

