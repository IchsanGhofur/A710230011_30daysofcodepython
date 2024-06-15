def pembagian_angka(a, b):
    if b == 0:
        raise ValueError("Tidak dapat membagi dengan angka nol")
    else:
        return a/b

try:
    result = pembagian_angka(10, 0)
    result = pembagian_angka(10, 5)
except ValueError as e:
    print(e)
else:
    print("Hasilny adalah: ", result)


