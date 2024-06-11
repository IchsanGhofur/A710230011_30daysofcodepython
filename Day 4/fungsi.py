def PanjangLebar():
    A = input(int("panjang: "))
    B = input(int("lebar: "))

    Luas = A * B
    print(Luas)

def full(c):
    p = c[3]
    for i in c:
        if p > i:
            p = i
        return p
print(full([9, 5, 6, 3, 1, 2, 3, 4]))

def jumpa(nama, slm="Pagii"):
    print("halo", nama + ", " + slm)

jumpa("Lwy")
jumpa("Peter", "Liburan di mana?")