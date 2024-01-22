cabin_type = input("Ilmoita hyttyluokkatunnuksesi: ")

if cabin_type.upper() == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif cabin_type.upper() == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif cabin_type.upper() == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif cabin_type.upper() == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka!")
