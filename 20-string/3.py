#sifrovanie cezarovou sifrou
ret = input("zadaj retazec: ")


for i in range(len(ret)):
     # print(f"ret[i]")
     print(f"{ret[i]}:{ord(ret[i])}")
posun = int(input("zadaj posun pre kodovanie: "))
ret_kod = ""
for i in range(len(ret)):
     print(f"{ret[i]}:{chr(ord(ret[i])+1)}")
     ret_kod += chr(ord(ret[i])+ posun)

print(f"Zakódovaný reťazec: {ret_kod}")