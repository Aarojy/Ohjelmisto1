class Auto:
        def __init__(self, rekisteritunnus, huippunopeus):
            self.rekisteritunnus = rekisteritunnus
            self.huippunopeus = huippunopeus
            self.tamanhetkinen_nopeus = 0
            self.kuljettu_matka = 0

auto1 = Auto("ABC-123",142)

print(f"Auton rekisteritunnus: {auto1.rekisteritunnus}, huippunopeus: {auto1.huippunopeus} km/h, tämänhetkinen nopeus: {auto1.tamanhetkinen_nopeus} km/h, kuljettu matka: {auto1.kuljettu_matka} km")