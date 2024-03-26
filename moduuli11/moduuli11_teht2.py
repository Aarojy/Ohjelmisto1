class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.tamanhetkinen_nopeus += nopeuden_muutos

        if self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * tuntimaara

    def print_info(self):
        print(f"Auto: {self.rekisteritunnus} on kulkenut {self.kuljettu_matka} km. Sen tämän hetkinen nopeus on {self.tamanhetkinen_nopeus} km/h ja huippunopeus on {self.huippunopeus} km/h.")


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus,huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus,huippunopeus, tankin_tilavuus):
        super().__init__(rekisteritunnus,huippunopeus)
        self.tankin_tilavuus = tankin_tilavuus


sahkoauto1 = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto1 = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto1.kiihdyta(150)
polttomoottoriauto1.kiihdyta(100)

sahkoauto1.kulje(3)
polttomoottoriauto1.kulje(3)

sahkoauto1.print_info()
polttomoottoriauto1.print_info()

