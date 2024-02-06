lentoasemat = {}

while True:
    print("1 = Syötä uusi lentoasema\n2 = Hae lentoasemaa\n3 = Lopeta")
    choice = input("Valitse yllä olevista vaihtoehdoista: ")

    if choice == "1":
        ICAO_code = input("Syötä lentoaseman ICAO-koodi: ")
        if ICAO_code in lentoasemat:
            print(f"Syöttämälläsi ICAO-koodilla löytyy jo lentoasema nimeltä: {lentoasemat[ICAO_code]}!")
            yes_no = input("1 = Kyllä\n2 = Ei\nHaluatko korvata vanhan lentoaseman uudella? ")
            if yes_no == "1":
                airport = input("Syötä lentoaseman nimi: ")
                lentoasemat[ICAO_code] = airport
        else:
            airport = input("Syötä lentoaseman nimi: ")
            lentoasemat[ICAO_code] = airport
    elif choice == "2":
        ICAO_code = input("Syötä etsimäsi lentokentän ICAO-koodi: ")
        if ICAO_code in lentoasemat:
            print(f"Syöttämäsi ICAO-koodia: {ICAO_code} vastaa lentoasemaa nimeltä: {lentoasemat[ICAO_code]}")
        else:
            print("Syöttämääsi ICAO-koodia ei löydy lentoasemakirjastosta.")
    elif choice == "3":
        break
    else:
        print("Syöttämäsi numero ei viittaa mihinkään vaihtoehtoon!")
