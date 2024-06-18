class Mobil:
    def Move(self):
        print('Berjalan di jalan raya')
class Pesawat:
    def Move(self):
        print('Terbang di udara')
class Kapal:
    def Move(self):
        print('Berlayar di laut')
        
my_kendaraan = Mobil()
my_kendaraan.Move()
my_peswat = Pesawat()
my_peswat.Move()
my_kapal = Kapal()
my_kapal.Move()