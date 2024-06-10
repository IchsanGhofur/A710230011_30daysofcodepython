import hashlib

def menguhabah_hash(password):
    hash_object = hashlib.sha3_256(password.encode())
    return hash_object.hexdigest()

def daftar(users):
    user = input("Masukkan username: ")
    if user in users:
        print("Usernmae sudah terdaftar, masukkan yang lainya")
    password = input("Masukkan paswword: ")
    hashed_password = menguhabah_hash(password)
    users[user] = {
        'password': hashed_password
    }
    print("pengguna berhasil terdaftar")

def login(users):
    username = ("masukkan username: ")
    if username in users:
        password = input("Masukkan password: ")

        # Membandingkan nilai hash yang dimasukkan dengan nilai hash yang disimpan
        if check_password(users[username]['password'], password):
            print("Login berhasil.")
        else:
            print("Login gagal. Periksa kembali password.")
    else:
        print("Username tidak ditemukan.")

def check_password(stored_hashed_password, password):
    # Menghasilkan nilai hash dari password yang dimasukkan
    hashed_password = menguhabah_hash(password)

    # Membandingkan nilai hash yang dihasilkan dengan nilai hash yang disimpan
    return hashed_password == stored_hashed_password

#main program
user = {}
while True:
    print("\n1. Register\n2. Login\n3. selesai")
    pilih = input('pilih tindakan 1/2/3: ')
    if pilih == '1':
        daftar(user)
    elif pilih == '2':
        login(user)
    elif pilih =='3':
        print('program selesai.')
        break
    else:
        print("pilihan tidak valid.")
        