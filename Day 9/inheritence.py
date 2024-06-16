class Motor:
    def __init__(self, merk, mesin, warna, tahun, meter):
        self.merk = merk
        self.mesin = mesin 
        self.warna = warna
        self.tahun = tahun
        self.meter = meter 

    def keterangan(self):
        print(f"Motor baru {self.merk} {self.mesin} tahun {self.tahun} warnanya {self.warna}")

    def kebengkel(self):
        print(f"Motor {self.merk} ini perlu ke bengkel ketika sudah mencapai {self.meter}")

class Electric(Motor):
    def __init__(self, merk, mesin, warna, tahun, meter, baterai):
        super().__init__(merk, mesin, warna, tahun, meter)
        self.baterai = baterai

    def daya(self):
        print(f"Motor ini memiliki daya {self.baterai} -kWh")

    def kebengkel(self):
        print(f"Motor listrik perlu ke bengkel setiap 6 bulan sekali")

Honda = Motor('Honda', '1000', 'Hitam', 2024, 500)
print(Honda.keterangan())
print(Honda.kebengkel())

aing = Electric('tesla', 150, 'putih', 2022, 50, 7500)
print(aing.daya())
print(aing.kebengkel())