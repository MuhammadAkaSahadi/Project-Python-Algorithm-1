import csv
import os
import time
import pandas as pd
from tabulate import tabulate


if not os.path.exists("data.csv"):
    header = ["Tgl-Bln-Thn", "Nama Ikan", "Pakan", "PH Air", "Suhu Air (C)", "Luas Kolam (m/persegi)","Volume Kolam (m/kubik)", "Hasil Panen (kg)"]
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)


if not os.path.exists("rekomendasi_catatan_admin.csv"):
    header = ["Nama Ikan", "Jenis Pakan", "PH Air", "Suhu Air (C)"]
    with open("rekomendasi_catatan_admin.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)


if not os.path.exists("users.csv"):
    header = ["Username", "Password"]
    with open("users.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# =================================================================================================================

# Sign-In User
def sign_in():
    clear_screen()
    print('''+-+-+ +-+-+ +- SIGN-IN -+ +-+-+ +-+-+''')
    print("=====================================")
    username = input('Masukan Username : ')
    password = input('Masukan Password : ')
    user = []
    with open("users.csv", "r") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            user.append({'Username': row[0], 'Password': row[1]})

    data_signin = []
    for i in user:
        if username == i['Username'] and password == i['Password']:
            data_signin.append(i)
            print("Berhasil Sign-In")
            Menu()
            break

    if len(data_signin) == 0:
        print("Akun Tidak Ditemukan!")
        print("Silahkan Log-In Ulang")
        print("Mohon Bersabar, Sedang Memuat Ulang")
        time.sleep(3)
        clear_screen()
        sign_in()


# Sign-Up User
def sign_up():
    clear_screen()
    print('''+-+-+ +-+-+ +- SIGN-UP -+ +-+-+ +-+-+''')
    print("=====================================")
    username = input('Masukan Username Baru : ')
    password = input('Masukan Password Baru : ')
    user = []
    with open("users.csv", "r") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            user.append({'Username': row[0], 'Password': row[1]})

    for i in user:
        if username == i['Username'] and password == i['Password']:
            print("Akun telah Ditemukan!")
            print("Username dan password tidak boleh sama!")
            print("Silahkan Langsung Log-In")
            print("Mohon Bersabar, Sedang Memuat Ulang")
            time.sleep(3)
            clear_screen()
            sign_up()

    username_ada = False

    for akun in user:
        if username == akun['Username']:
            print("Username sudah ada, coba yang lain!")
            username_ada = True

    if not username_ada:
        databaru = {'Username': username, 'Password': password}
        with open('users.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=databaru.keys())
            writer.writerow(databaru)

        print("Akun baru berhasil ditambahkan!")
        print("Anda akan diarahkan ke Sign-In, Tunggu beberapa saat!")
        time.sleep(3)
        clear_screen()
        sign_in()


# Sign-In Admin
def sign_in_admin():
    clear_screen()
    print('''+-+-+ +-+-+ +- SIGN-IN ADMIN -+ +-+-+ +-+-+''')
    print("===========================================")
    username = input('Masukan Username : ')
    password = input('Masukan Password : ')

    user = []

    with open("users_admin.csv", "r") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            user.append({'Username': row[0], 'Password': row[1]})

    data_signin = []
    for i in user:
        if username == i['Username'] and password == i['Password']:
            data_signin.append(i)
            print("Berhasil Sign-In Admin")
            menu_admin()
            break

    if len(data_signin) == 0:
        print("Akun tidak ditemukan!")
        print("Silahkan buat 'users_admin.csv' dan sign-in admin kembali")
        time.sleep(3)
        clear_screen()
        sign_in_admin()


# =================================================================================================================


# Menu Admin
def menu_admin():
    clear_screen()
    print('''
············································
:+-+-+ +-+-+ +-+ MENU ADMIN +-+ +-+-+ +-+-+:
:|1. Buat Rekomendasi Catatan             |:
:|2. Update Rekomendasi Catatan           |:
:|3. Hapus Rekomendasi Catatan            |:
:|4. Tampilkan Rekomendasi Catatan        |:
:|5. Hapus Akun User                      |:
:|6. Kembali Ke Start/Awalan Page         |:
:|7. Exit                                 |:
:+-+-+ +-+-+- +--+ -+-+-+ +-+-+ +-+-+ +-+-+:
············································
''')
    menu = input("Pilih Fitur yang ingin dijalankan:")
    if menu == '1':
        rekomendasi_admin_catatan()
    elif menu == '2':
        update_rekomendasi_catatan()
    elif menu == '3':
        hapus_rekomendasi_catatan()
    elif menu == '4':
        tampilkan_rekomendasi_admin_catatan()
    elif menu == '5':
        hapus_user()
    elif menu == '6':
        clear_screen()
        start()
    elif menu == '7':
        exit()
    else:
        print("Pilihan tidak valid!")
        menu_admin()


# Fitur Admin, Buat Rekomendasi Catatan
def rekomendasi_admin_catatan():
    clear_screen()
    print('''+-+-+ +-+-+ +- BUAT REKOMENDASI CATATAN -+ +-+-+ +-+-+''')
    print("=========================================================")
    rekomendasi_catatan_admin = []
    nama_ikan = input('Masukkan Rekomendasi Nama Ikan: ')
    rekomendasi_nama_pakan = input('Masukkan Rekomendasi Pakan: ')
    rekomendasi_PH_air = input('Masukkan Rekomendasi PH Air: ')
    rekomendasi_suhu_air = input('Masukkan Rekomendasi Suhu Air (C): ')
    rekomendasi_catatan_admin.append(nama_ikan)
    rekomendasi_catatan_admin.append(rekomendasi_nama_pakan)
    rekomendasi_catatan_admin.append(rekomendasi_PH_air)
    rekomendasi_catatan_admin.append(rekomendasi_suhu_air)
    with open("rekomendasi_catatan_admin.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(rekomendasi_catatan_admin)
    print('Catatan berhasil ditambahkan')
    input("Tekan Enter untuk kembali ke Menu Admin")
    menu_admin()


# Fitur Admin, Update Rekomendasi Catatan
def update_rekomendasi_catatan():
    clear_screen()
    print('''+-+-+ +-+-+ +- UPDATE REKOMENDASI CATATAN -+ +-+-+ +-+-+''')
    print("===========================================================")

    df = pd.read_csv('rekomendasi_catatan_admin.csv')
    df = df.rename_axis('index').reset_index(drop=True)
    df.index += 1
    df.index.name= "Index"
    print(tabulate(df, headers='keys', tablefmt='grid'))
    with open("rekomendasi_catatan_admin.csv", 'r') as file:
        reader = list(csv.reader(file))

    try:
        # nomor_catatan_update = int(input('Masukan Index Catatan Yang Akan Di Update: ')) + 1
        nomor_catatan_update = int(input('Masukan Index Catatan Yang Akan Di Update: ')) 
    except ValueError:
        print("Input Tidak Valid. Harap masukkan angka.")
        time.sleep(1)
        update_rekomendasi_catatan()
    if 0 <= nomor_catatan_update < len(reader):
        reader[nomor_catatan_update][0] = input('Masukan Nama Ikan: ')
        reader[nomor_catatan_update][1] = input('Masukan Rekomendasi Jenis Pakan: ')
        reader[nomor_catatan_update][2] = input('Masukan Rekomendasi Suhu Air (C): ')
        reader[nomor_catatan_update][3] = input('Masukan Rekomendasi PH Air: ')

        with open("rekomendasi_catatan_admin.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)
        print("Update berhasil!")
    else:
        # print(f"Index {nomor_catatan_update - 1} melebihi batas, masukkan antara 0 dan {len(reader)-2}")
        print(f"Index {nomor_catatan_update } melebihi batas, masukkan antara 1 dan {len(reader)-1}")
        input("Tekan Enter untuk kembali update data ")
        return update_rekomendasi_catatan()
    input("Tekan Enter untuk kembali ke Menu Admin")
    menu_admin()


# Fitur Admin, Hapus Rekomendasi Catatan
def hapus_rekomendasi_catatan():
    clear_screen()
    print('''+-+-+ +-+-+ +- HAPUS REKOMENDASI CATATAN -+ +-+-+ +-+-+''')
    print("========================================================")

    df = pd.read_csv('rekomendasi_catatan_admin.csv')
    df = df.rename_axis('index').reset_index(drop=True)
    df.index += 1
    df.index.name= "Index"
    print(tabulate(df, headers='keys', tablefmt='grid'))

    with open("rekomendasi_catatan_admin.csv", 'r') as file:
        reader = list(csv.reader(file))
    
    try:
        # index_hapus_catatan = int(input('Masukan index catatan yang akan di hapus: ')) + 1
        index_hapus_catatan = int(input('Masukan index catatan yang akan di hapus: '))
    except ValueError:
        print("Input Tidak Valid. Harap masukkan angka.")
        time.sleep(1)
        hapus_rekomendasi_catatan()
    if 0 <= index_hapus_catatan <= len(reader) - 1 :
        reader.pop(index_hapus_catatan)
        with open("rekomendasi_catatan_admin.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)
        print('Catatan berhasil dihapus')
        input("Tekan Enter untuk kembali ke Menu Admin ")
        menu_admin()
    else :
        # print(f"Index {index_hapus_catatan - 1} melebihi batas, masukkan antara 0 dan {len(reader)-2}")
        print(f"Index {index_hapus_catatan } melebihi batas, masukkan antara 1 dan {len(reader)-1}")
        input("Tekan Enter untuk kembali ke hapus rekomendasi catatan")
        return hapus_rekomendasi_catatan()


# Fitur Admin, Tampilkan Rekomendasi Catatan
def tampilkan_rekomendasi_admin_catatan():
    clear_screen()
    print('''+-+-+ +-+-+ +- REKOMENDASI CATATAN -+ +-+-+ +-+-+''')
    print("=================================================")
    df = pd.read_csv('rekomendasi_catatan_admin.csv')

    df = df.rename_axis('index').reset_index(drop=True)
    df.index += 1
    df.index.name= "Index"

    print(tabulate(df, headers='keys', tablefmt='grid'))
    print("Inilah Rekomendasinya")
    input("Tekan Enter untuk kembali ke Menu Admin")
    menu_admin()


# Fitur Admin, Hapus Akun
def hapus_user():
    clear_screen()
    print('''+-+-+ +-+-+ +- HAPUS AKUN USER -+ +-+-+ +-+-+''')
    print("================================================")

    df = pd.read_csv('users.csv')
    df = df.rename_axis('index').reset_index(drop=True)
    df.index += 1
    df.index.name= "Index"
    print(tabulate(df, headers='keys', tablefmt='grid'))

    with open("users.csv", 'r') as file:
        reader = list(csv.reader(file))

    try:
        # index_hapus_catatan = int(input('Masukan index catatan yang akan di hapus: ')) + 1
        index_hapus_catatan = int(input('Masukan index catatan yang akan di hapus: ')) 
    except ValueError:
        print("Input Tidak Valid. Harap masukkan angka.")
        time.sleep(1)
        hapus_user()
    if 0<= index_hapus_catatan <= len(reader)-1:
        reader.pop(index_hapus_catatan)
        with open("users.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)
        print('Akun berhasil dihapus')
        input("Tekan Enter untuk kembali ke Menu Admin ")
        menu_admin()
    else:
        # print(f"Index {index_hapus_catatan - 1} melebihi batas, masukkan antara 0 dan {len(reader)-2}")
        print(f"Index {index_hapus_catatan } melebihi batas, masukkan antara 1 dan {len(reader)-1}")
        input("Tekan Enter untuk kembali ke hapus user")
        return hapus_user()



# =================================================================================================================

# Menu User
def Menu():
    clear_screen()
    print('''
······································
:+-+-+ +-+-+ +-+ MENU +-+ +-+-+ +-+-+:
:|1. Tambah Catatan                 |:
:|2. Tampilkan Catatan              |:
:|3. Update Catatan                 |:
:|4. Hapus Catatan                  |:
:|5. Tampilkan Rekomendasi Catatan  |:
:|6. Exit                           |:
:+-+-+ +-+-+- +--+ -+-+-+ +-+-+ +-+-+: 
······································
''')
    menu = input("Pilih Fitur yang ingin dijalankan:")
    if menu == '1':
        entry_catatan()
    elif menu == '2':
        tampilkan_catatan()
    elif menu == '3':
        update_catatan()
    elif menu == '4':
        hapus_catatan()
    elif menu == '5':
        tampilkan_rekomendasi_catatan()
    elif menu == '6':
        exit()
    # elif menu == '7':
    #     infinite()
    else:
        print('Pilihan Menu tidak valid ! ')
        Menu()


# Fitur User, Tambah Catatan
def entry_catatan():
    clear_screen()
    print('''+-+-+ +-+-+ +- TAMBAH CATATAN -+ +-+-+ +-+-+''')
    print("============================================")
    data = []
    Tanggal = input('Masukan Tgl-Bln-Thn: ')
    if Tanggal == "0-0-0":
        print("Tanggal tidak Valid")
        time.sleep(1)
        entry_catatan()
    elif Tanggal == "0":
        print("Tanggal Tidak Valid")
        time.sleep(1)
        entry_catatan()

    Nama_ikan = input('Masukan Nama Ikan: ')
    Nama_pakan = input('Masukan Nama Pakan Ikan: ')

    try:
        Keadaan_PH_air = float(input('Masukan PH air: '))
        if Keadaan_PH_air == 0:
            print("Input Tidak Valid")
            time.sleep(1)
            entry_catatan()

        Suhu_air = float(input('Masukan Suhu Air (C): '))
        if Suhu_air == 0:
            print("Input Tidak Valid")
            time.sleep(1)
            entry_catatan()

        Luas_kolam = float(input('Masukan Luas Kolam (m/persegi): '))
        if Luas_kolam == 0:
            print("Input Tidak Valid")
            time.sleep(1)
            entry_catatan()

        Volume_kolam = float(input('Masukan Volume Kolam (m/kubik): '))
        if Volume_kolam == 0:
            print("Input Tidak Valid")
            time.sleep(1)
            entry_catatan()

        Hasil_panen = float(input('Masukan Hasil Panen (kg): '))
        if Hasil_panen == 0:
            print("Input Tidak Valid")
            time.sleep(1)
            entry_catatan()
    except ValueError:
        print("Input Tidak Valid. Harap masukkan angka.")
        time.sleep(1)
        entry_catatan()

    data.append(Tanggal)
    data.append(Nama_ikan)
    data.append(Nama_pakan)
    data.append(Keadaan_PH_air)
    data.append(Suhu_air)
    data.append(Luas_kolam)
    data.append(Volume_kolam)
    data.append(Hasil_panen)
    with open("data.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print('Catatan berhasil ditambahkan')
    while True:
        user_input = input("Tekan Enter untuk kembali ke Menu ")
        if user_input.lower() == '':
            Menu()




# Fitur User, Tampilkan Catatan
def tampilkan_catatan():
    clear_screen()
    print('''+-+-+ +-+-+ +- TAMPILKAN CATATAN -+ +-+-+ +-+-+''')
    print("===============================================")
    df = pd.read_csv('data.csv')
    df = df.rename_axis('index').reset_index(drop=True)
    df.index += 1
    df.index.name= "Nomor"
    print(tabulate(df, headers='keys', tablefmt='grid'))
    input("Tekan Enter untuk kembali ke Menu ")
    Menu()


# Fitur User, Update Catatan
def update_catatan():
    clear_screen()
    print('''+-+-+ +-+-+ +- UPDATE -+ +-+-+ +-+-+''')
    print("====================================")

    with open("data.csv", 'r') as file:
        reader = list(csv.reader(file))
        df = pd.DataFrame(reader[1:], columns=reader[0])
        df = df.rename_axis('index').reset_index(drop=True)
        df.index += 1
        df.index.name= "Index"
        table = tabulate(df, headers='keys', tablefmt='grid', colalign=("Left",) * len(df.columns))
        print(table)
    with open("data.csv", 'r') as file:
        reader = list(csv.reader(file))

    try:
        # nomor_catatan_update = int(input('Masukan Index Catatan Yang Akan Di Update: ')) + 1
        nomor_catatan_update = int(input('Masukan Index Catatan Yang Akan Di Update: ')) 
    except ValueError:
        print("Input Tidak Valid. Harap masukkan angka.")
        time.sleep(1)
        update_catatan()
    if 0 <= nomor_catatan_update < len(reader):
        reader[nomor_catatan_update][0] = input('Masukan Tgl-Bln-Thn: ')
        if reader[nomor_catatan_update][0] == "0-0-0":
            print("Tanggal tidak Valid")
            time.sleep(1)
            update_catatan()
        elif reader[nomor_catatan_update][0] == "0":
            print("Tanggal Tidak Valid")
            time.sleep(1)
            update_catatan()
        reader[nomor_catatan_update][1] = input('Masukan Nama Ikan: ')
        reader[nomor_catatan_update][2] = input('Masukan Nama Jenis Pakan: ')
        reader[nomor_catatan_update][3] = float(input('Masukan PH Air: '))
        reader[nomor_catatan_update][4] = float(input('Masukan Suhu Air (C): '))
        reader[nomor_catatan_update][5] = float(input('Masukan Luas Kolam (m²): '))
        reader[nomor_catatan_update][6] = float(input('Masukan Volume Kolam (m³): '))
        reader[nomor_catatan_update][7] = float(input('Masukan Hasil Panen (kg): '))

        with open("data.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)
        print("Update berhasil, silahkan kembali ke 'Menu' dan pergi ke 'Tampilkan Catatan'")
    else:
        print(f"Index {nomor_catatan_update } melebihi batas, masukkan antara 1 dan {len(reader)-1}")
        input("Tekan Enter untuk kembali update data ")
        return update_catatan()
    input("Tekan Enter untuk kembali ke Menu ")
    Menu()


# Fitur User, Hapus Catatan
def hapus_catatan():
    clear_screen()
    print('''+-+-+ +-+-+ +- HAPUS CATATAN -+ +-+-+ +-+-+''')
    print("===========================================")
    with open("data.csv", 'r') as file:
        reader = list(csv.reader(file))
        df = pd.DataFrame(reader[1:], columns=reader[0])
        df = df.rename_axis('index').reset_index(drop=True)
        df.index += 1
        df.index.name= "Index"
        table = tabulate(df, headers='keys', tablefmt='grid', colalign=("Left",) * len(df.columns))
        print(table)

    try:
        index_hapus_catatan = int(input('Masukkan index catatan yang akan dihapus: '))
    except ValueError:
        print("Input Tidak Valid. Harap masukkan angka.")
        time.sleep(1)
        hapus_catatan()

    if 0 <= index_hapus_catatan <= len(reader) - 1:
        reader.pop(index_hapus_catatan)
        with open("data.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)
        print('Catatan berhasil dihapus')
        input("Tekan Enter untuk kembali ke Menu ")
        Menu()
    else:
        # print(f"Index {index_hapus_catatan - 1} melebihi batas, masukkan antara 0 dan {len(reader)-2}")
        print(f"Index {index_hapus_catatan } melebihi batas, masukkan antara 1 dan {len(reader)-1}")
        input("Tekan Enter untuk kembali ke hapus catatan")
        return hapus_catatan()

# Fitur User, Tampilkan Rekomendasi Catatan
def tampilkan_rekomendasi_catatan():
    clear_screen()
    print('''+-+-+ +-+-+ +- REKOMENDASI CATATAN -+ +-+-+ +-+-+''')
    print("=================================================")
    df = pd.read_csv('rekomendasi_catatan_admin.csv')
    df = df.rename_axis('index').reset_index(drop=True)
    df.index += 1
    df.index.name= "Index"
    print(tabulate(df, headers='keys', tablefmt='grid'))
    print("Inilah Rekomendasinya")
    input("Tekan Enter untuk kembali ke Menu")
    Menu()


# Fitur User & Admin, Exit
def exit():
    clear_screen()
    while True:
        print("Anda telah keluar. Terima kasih telah menggunakan program ini :)")
        break

def start():
    with open('Logo 1.ini', 'r') as file:
        logo = file.read()
        print(logo)
    print('''
=============
|1. Sign In |
|2. Sign Up |
|3. Admin   |
=============
    ''')
    menu = input("Pilih : ")
    if menu == '1':
        sign_in()
    elif menu == '2':
        sign_up()
    elif menu == '3':
        sign_in_admin()
    else:
        print("Pilihan Tidak Valid")
        time.sleep(1)
        clear_screen()
        start()
clear_screen()
start()
# tampilkan_rekomendasi_admin_catatan()
# index()