class Tumbuhan:
    def __init__(self, pohon, akar, daun):
        self.pohon = pohon
        self.akar = akar
        self.daun = daun
        
    def root(self):
        print(f"Pohon {self.pohon}  memiliki akar {self.akar} dan berdaun {self.daun} ")

class Tinggi(Tumbuhan):
    def __init__(self, pohon, akar, daun, tinggi):
        super().__init__(pohon, akar, daun)
        self.tinggi = tinggi

    def high(self):
        print(f"Pohon tersebut memiliki tinggi {self.tinggi} meter")
    
wit = Tumbuhan("pepaya", "tunggang", "menjari" )
ti = Tinggi("pepaya", "tunggang", "menjari", 3)
wit.root()
(ti.high())