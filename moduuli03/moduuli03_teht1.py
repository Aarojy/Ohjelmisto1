fish_lenght = float(input("Ilmoita kuhan pituus senttimetreinä: "))

if fish_lenght < 37:
    print(f"Kuhasi on {37-fish_lenght} cm alimittainen!")
else:
    print("Kuhasi on riittävän pitkä!")
