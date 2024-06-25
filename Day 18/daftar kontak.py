phone_book = {}
for K in range(1, 6):
     nama = input(f"Masukkan nama teman ke-{K}: ")
     no_hp = input(f"Masukkan nomor handphone {nama}: ")
     phone_book[nama] = no_hp 
kata = 'Daftar Kontak'

print(kata.center(50))
for K, (nama, no_hp) in enumerate(phone_book.items(),1):
    print(f"{K}. {nama} = {no_hp}")