class Hewan:
    def __init__(self, jenis, hidup):
        self.jenis = jenis
        self.hidup = hidup

    def makan(self):
        print(f"hewan ini ber jenis {self.jenis} dan hidup di {self.hidup}")
hwn = Hewan("mamalia", "air")
hwn.makan()