import random


class Kilpailu:

    def __init__(self, nimi, pituus, auto_lista):
        self.nimi = nimi
        self.pituus = pituus
        self.auto_list = auto_lista

    def tunti_kuluu(self):
        for auto in self.auto_list:
            auto.kiihdyta(random.randint(-10, 15))

        for auto in self.auto_list:
            auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.auto_list:
            auto.print_info()

    def kilpailu_ohi(self):
        for auto in self.auto_list:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

    def tulosta_voittaja(self):
        more_winners = False
        for auto in self.auto_list:
            if more_winners and auto.kuljettu_matka >= self.pituus:
                print("ja")
            if auto.kuljettu_matka >= self.pituus:
                print(f"{auto.rekisteritunnus} on voittanut!")
                more_winners = True


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
        print(
            f"Auto: {self.rekisteritunnus} on kulkenut {self.kuljettu_matka} km. "
            f"Sen tämän hetkinen nopeus on {self.tamanhetkinen_nopeus} km/h "
            f"ja huippunopeus on {self.huippunopeus} km/h.")


autot = []
for i in range(1, 11):
    tunnus = f"ABC-{i}"
    max_nopeus = random.randint(100, 200)
    x = Auto(tunnus, max_nopeus)
    autot.append(x)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

i = 0
while True:
    kilpailu.tunti_kuluu()

    i += 1
    if i % 10 == 0:
        print(f"\nKilpailu on kestänyt {i} tuntia.")
        kilpailu.tulosta_tilanne()

    if kilpailu.kilpailu_ohi():
        print(f"\nKilpailu päättyy ajassa {i} tuntia.")
        kilpailu.tulosta_tilanne()
        print("")
        kilpailu.tulosta_voittaja()
        break
