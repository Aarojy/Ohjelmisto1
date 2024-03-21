import random
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

autot = []
for i in range(1,11):
    tunnus = f"ABC-{i}"
    max_nopeus = random.randint(100,200)
    x = Auto(tunnus, max_nopeus)
    autot.append(x)


finished = False

while finished != True:

    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))

    for auto in autot:
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            finished = True
            print(f"Auto: {auto.rekisteritunnus} on voittanut!\n")
            break

for auto in autot:
    auto.print_info()