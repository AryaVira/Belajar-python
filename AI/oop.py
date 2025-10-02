class Hewan:
    def __init__(self, nama):
        self.nama = nama

class gajah(Hewan):
    def metodesuara(self):
        return f" gajah ini bernama {self.nama} dan bersuara dengan cara Honk honk"

class kucing(Hewan):
    def metodesuara(self):
        return f"kucing ini bernama {self.nama} dan bersuara dengan cara miaw miaw"

gajah_hewan = gajah("jumbo")
kucing_hewan= kucing("cinamorol")

suara_gajah= gajah_hewan.metodesuara()
suara_kucing= kucing_hewan.metodesuara()

print(suara_gajah)
print(suara_kucing)