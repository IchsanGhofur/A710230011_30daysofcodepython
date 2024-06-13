class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    def makan(self):
        print(f"Hewan {self.nama} merupakan salah satu hewan berjenis {self.jenis}")

hewan = Hewan("harimau", "karnivora")
print(hewan.makan())