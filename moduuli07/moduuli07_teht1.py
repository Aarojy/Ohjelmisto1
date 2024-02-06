month_index = int(input("Syötä kuukauden numero: "))-1
seasons = ("Talvi", "Talvi", "Kevät", "Kevät", "Kevät", "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi")

if 0 <= month_index <= 11:
    print(f"Syöttämäsi kuukausi on {seasons[month_index].lower()}kuukausi.")
else:
    print("Syöttämäsi luku ei kelpaa.")

