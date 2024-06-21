for i in range(2):
    if i > 0:
        print(i)
    else:
        print("Angka mines")

while True:
    i1 = input(("Masukaan angka: "))
    i = int(i1)
    if i > 0:
        for i in range(i):
            print(i)
    elif i < 0:
        print("Masukkan angka positif")
    else:
        print("input tidak valdi")
        break