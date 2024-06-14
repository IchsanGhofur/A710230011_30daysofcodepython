class persegi:
    def __init__(self, sisi):
        self.sisi = sisi
    def Luas(self, sisi):
        luas = (sisi * sisi)
        print("Luas persegi adalah ", luas)
ss = persegi(5)
ss.Luas()