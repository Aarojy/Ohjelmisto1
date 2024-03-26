
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

h = Hissi(1,10)

h.siirry_kerrokseen(9)

h.siirry_kerrokseen(1)