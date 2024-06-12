from math import pi
Nama = input(str("Nama saya adalah: "))
asal = input(str("Asal saya: "))
umur = input(("Umur saya saat ini: "))
umur1 = int(umur)
umur_lama = int(umur1 - 10) 
umur_depan = int(umur1 + 17)
print("Umur saya 10 tahun yang lalu adalah ", umur_lama)
print("17 tahun lagi umur saya adalah ", umur_depan)

A = input(("masukkan jari-jari: "))
A1 = int(A)
Luas = (A1 * A1 * pi )
print("Luas lingkaran dengan panjang jari jari {} adalah {}".format(A, Luas))