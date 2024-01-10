while True:
    n = int(input("zadaj N (pre ukoncenie zadaj 0): "))
    print("prvocisla:", end=" ")
    for cislo in range(2, (n // 2)+ 1):
        pocet = 0
        for delitel in range(1, cislo + 1):
            if cislo % delitel == 0:
                pocet += 1

        if pocet == 2:
            print(cislo , end=" ")
    if n == 0:
        break
