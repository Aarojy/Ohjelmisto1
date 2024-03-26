
class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissi_lista = []

        for i in range(hissien_maara):
            x = Hissi(self.alin_kerros, self.ylin_kerros)
            self.hissi_lista.append(x)

    def aja_hissia(self, hissin_numero, kohde_kerros):
        print(f"Ajetaan hissiä nro {hissin_numero}.")
        self.hissi_lista[hissin_numero-1].siirry_kerrokseen(kohde_kerros)

class Hissi:

    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.sijainti_kerros = alin_kerros

    def siirry_kerrokseen(self, kerros):
        if kerros > self.ylin_kerros or kerros < self.alin_kerros:
            print("Syöttämäsi kerros ei kelpaa")
        else:
            while self.sijainti_kerros != kerros:
                if self.sijainti_kerros < kerros:
                    self.kerros_ylos()
                else:
                    self.kerros_alas()
            print("Bling!")

    def kerros_ylos(self):
        self.sijainti_kerros += 1
        print(f"Hissi on nyt kerroksessa: {self.sijainti_kerros}")
    def kerros_alas(self):
        self.sijainti_kerros -= 1
        print(f"Hissi on nyt kerroksessa: {self.sijainti_kerros}")


talo1 = Talo(1, 10, 3)

talo1.aja_hissia(1, 9)
talo1.aja_hissia(2, 3)
talo1.aja_hissia(3, 2)

talo1.aja_hissia(1, 1)
talo1.aja_hissia(2, 0)
talo1.aja_hissia(3, 10)