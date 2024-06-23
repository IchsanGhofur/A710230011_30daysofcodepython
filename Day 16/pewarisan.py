class Tiket:
    def __init__(self, jumlah_tiket):
        self.jumlah_Tiket = jumlah_tiket
    def total_harga(self):
        pass

class TiketBiasa(Tiket):
    harga_tiket = 75000
    def total_harga(self):
        return self.jumlah_Tiket * self.harga_tiket

class TiketVIP(Tiket):
    harga_tiket = 120000
    def total_harga(self):
        return self.jumlah_Tiket * self.harga_tiket

class TiketGold(Tiket):
    harga_tiket = 200000
    def total_harga(self):
        return self.jumlah_Tiket * self.harga_tiket

def main():
    tiket = input("Masukkan jenis Tiket (biasa/vip/gold): ")
    jumlah_tiket = int(input("Masukkan jumlah tiket: "))
    if tiket == 'biasa':
        tiket = TiketBiasa(jumlah_tiket)
    elif tiket == 'vip':
        tiket = TiketVIP(jumlah_tiket)
    elif tiket == 'gold':
        tiket = TiketGold(jumlah_tiket)
    else:
        print("Jenis tiket tidak valid!")
        return
    total_harga = tiket.total_harga()
    print("Total Harga Tiket: Rp {}".format(total_harga))

if __name__ == "__main__":
    main()