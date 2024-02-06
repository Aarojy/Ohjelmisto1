name_input = " "
set_of_names = set()

while True:
    name_input = input("Syötä nimi: ")
    if name_input == "":
        break
    if name_input in set_of_names:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        set_of_names.add(name_input)

for name in set_of_names:
    print(name)
