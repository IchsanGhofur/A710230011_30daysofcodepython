class persegi:
    def __init__(self, sisi):
        self.sisi = sisi
    def Luas(self, sisi):
        luas = (sisi * sisi)
        print("Luas persegi adalah ", luas)
    def Keliling(self, sisi):
        kl = (sisi * 4) 
        print("Keliling persegi adalah ", kl)
ss = persegi(24)
klk = persegi(24)
ss.Luas()
klk.Keliling()