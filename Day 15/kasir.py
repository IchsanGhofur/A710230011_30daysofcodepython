def kasir_toko():
    total_harga = 0
    daftar_belanja = {}

    while True:
        nama_barang = input("Masukkan nama barang (atau ketik 'selesai' untuk selesai belanja): ")
        if nama_barang.lower() == 'selesai':
            break

        jumlah_barang = int(input("Masukkan jumlah barang: "))
        harga_barang = float(input("Masukkan harga per barang: "))

        total_barang = jumlah_barang * harga_barang
        total_harga += total_barang

        daftar_belanja[nama_barang] = {
            'Jumlah': jumlah_barang,
            'Harga per Barang': harga_barang,
            'Total Harga': total_barang
        }

    print("\n===== Struk Belanja =====")
    for barang, rincian in daftar_belanja.items():
        print(f"{barang}: {rincian['Jumlah']} x {rincian['Harga per Barang']} = {rincian['Total Harga']}")
    print(f"\nTotal Harga: {total_harga}")

kasir_toko()