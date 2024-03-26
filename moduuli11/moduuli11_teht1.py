class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi: str, kirjoittaja: str, sivumaara: int):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(f"Kirjan nimi: {self.nimi}, Kirjoittaja: {self.kirjoittaja}, Sivumäärä: {self.sivumaara}")

class Lehti(Julkaisu):
    def __init__(self, nimi: str, paatoimittaja: str):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Lehden nimi: {self.nimi}, Päätoimittaja: {self.paatoimittaja}")

kirja1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
lehti1 = Lehti("Aku Ankka", "Aki Hyyppä")

kirja1.tulosta_tiedot()
lehti1.tulosta_tiedot()