import os, csv, time, datetime

def ini_fail():
    #Tuple
    penghapus = (["FaberCastell", 14000, 550, 4800],    ["Stabilo", 16000, 500, 4200],  ["Staedler", 18000, 600, 3600]  )   
    pulpen =    (["Gel Umum", 22000, 2000, 3000],       ["Standard", 20000, 1500, 2640],["Pilot",25000, 3000, 2400]     )
    tipex =     (["Cair", 65000, 5000, 1200],           ["Kertas", 75000, 12000, 960]                                   )
    lem =       (["Fox", 100000, 35000, 480],           ["Kertas", 40000, 2000, 552],   ["Korea",60000,5000,336]        )
    buku =      (["Bewarna", 20000, 3000, 1680],        ["Tebal", 15000, 2300, 1560],   ["Tipis",15000, 2500,1500]      )
    cover =     (["Putih", 60000, 1000, 2160],          ["Bewarna", 80000, 2000, 1800]                                  )   
    if not os.path.exists('daftar_produk.csv'):
        with open('daftar_produk.csv', 'w') as csv_write:
            kolom = ['PRODUK','JENIS','HARGA','PER','STOK']
            tulis = csv.DictWriter(csv_write, fieldnames=kolom)
            tulis.writeheader()
    #DAFTAR PRODUK
        with open('daftar_produk.csv', mode='a') as csv_add:
            kolom = ['PRODUK','JENIS','HARGA','PER','STOK']
            append = csv.DictWriter(csv_add, fieldnames=kolom)
            for ini in penghapus:
                append.writerow({'PRODUK': "Penghapus", 'JENIS': ini[0], 'HARGA': ini[1], 'PER': 'lusin', 'STOK': ini[3]})
            for ini in penghapus:
                append.writerow({'PRODUK': "Penghapus", 'JENIS': ini[0], 'HARGA': ini[2], 'PER': 'unit', 'STOK': ini[3]})
            for ini in pulpen:
                append.writerow({'PRODUK': "Pulpen", 'JENIS': ini[0], 'HARGA': ini[1], 'PER': 'lusin', 'STOK': ini[3]})
            for ini in pulpen:
                append.writerow({'PRODUK': "Pulpen", 'JENIS': ini[0], 'HARGA': ini[2], 'PER': 'unit', 'STOK': ini[3]})
            for ini in tipex:
                append.writerow({'PRODUK': "Tip-Ex", 'JENIS': ini[0], 'HARGA': ini[1], 'PER': 'lusin', 'STOK': ini[3]})
            for ini in tipex:
                append.writerow({'PRODUK': "Tip-Ex", 'JENIS': ini[0], 'HARGA': ini[2], 'PER': 'unit', 'STOK': ini[3]})
            for ini in lem:
                append.writerow({'PRODUK': "Lem", 'JENIS': ini[0], 'HARGA': ini[1], 'PER': 'lusin', 'STOK': ini[3]})
            for ini in lem:
                append.writerow({'PRODUK': "Lem", 'JENIS': ini[0], 'HARGA': ini[2], 'PER': 'unit', 'STOK': ini[3]})
            for ini in buku:
                append.writerow({'PRODUK': "Buku", 'JENIS': ini[0], 'HARGA': ini[1], 'PER': 'lusin', 'STOK': ini[3]})
            for ini in buku:
                append.writerow({'PRODUK': "Buku", 'JENIS': ini[0], 'HARGA': ini[2], 'PER': 'unit', 'STOK': ini[3]})
            for ini in cover:
                append.writerow({'PRODUK': "Cover", 'JENIS': ini[0], 'HARGA': ini[1], 'PER': 'lusin', 'STOK': ini[3]})
            for ini in cover:
                append.writerow({'PRODUK': "Cover", 'JENIS': ini[0], 'HARGA': ini[2], 'PER': 'unit', 'STOK': ini[3]})   

    if not os.path.exists('data_akun.csv'):
        with open('data_akun.csv', 'w') as csv_write:
            kolom = ['NAMA', 'UMUR', 'ASAL', 'NOHP', 'USERNAME', 'PASSWORD', 'LEVEL']
            tulis = csv.DictWriter(csv_write, fieldnames=kolom)
            tulis.writeheader()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main_utama():
    clear_screen()
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("|                      MASUK SEBAGAI                    |")
    print("|_______________________________________________________|")
    print("| [1] Admin                                             |")
    print("| [2] Customer                                          |")
    print("| [0] Keluar Program                                    |")
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    masuk = str(input("| Pilih Masuk sebagai  > "))
    print("|_______________________________________________________|")
    if masuk == '1':
        masuk_admin()
    elif masuk == '2':
        masuk_customer()
    elif masuk == '0':
        print("|                                                       |")
        print("| Keluar Program...                                     |")
        time.sleep(2)
        print("|                                                       |")
        print("| Terimakasih Telah Menggunakan Program Kami!           |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        time.sleep(3)
        exit()
    else:
        print("\n _______________________________________________________")
        print("| Error:                                                |")
        print("| Input anda tidak valid!                               |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        main_utama()

def masuk_admin():
    clear_screen()
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("|                 ANDA MASUK SEBAGAI ADMIN              |")
    print("|_______________________________________________________|")
    print("| [1] Login Akun                                        |")
    print("| [2] Daftar Akun                                       |")
    print("| [0] Kembali                                           |")
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("| Pilih Masuk sebagai  > 1                              |")
    pilihan_masuk = str(input("| Masukkan Pilihan     > "))
    print("|_______________________________________________________|")
    if pilihan_masuk == '0':
        main_utama()
    elif pilihan_masuk == '1':
        clear_screen()
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
        print("|                 ANDA MASUK SEBAGAI ADMIN              |")
        print("|_______________________________________________________|")
        print("| [1] Login Akun                                        |")
        print("| [2] Daftar Akun                                       |")
        print("| [0] Kembali                                           |")
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
        print("| Pilih Masuk sebagai  > 1                              |")
        print("| Masukkan Pilihan     > 1                              |")
        print("|                                                       |")
        print("| Mengalihkan...                                        |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
        time.sleep(1.5)
        login_akun('admin')
    elif pilihan_masuk == '2':
        clear_screen()
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
        print("|                 ANDA MASUK SEBAGAI ADMIN              |")
        print("|_______________________________________________________|")
        print("| [1] Login Akun                                        |")
        print("| [2] Daftar Akun                                       |")
        print("| [0] Kembali                                           |")
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
        print("| Pilih Masuk sebagai  > 1                              |")
        print("| Masukkan Pilihan     > 2                              |")
        print("|                                                       |")
        print("| Mengalihkan...                                        |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
        time.sleep(1.5)
        daftar_akun('admin')
    else:
        print("\n _______________________________________________________")
        print("| Error:                                                |")
        print("| Input anda tidak valid!                               |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        masuk_admin()

def masuk_customer():
    clear_screen()
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("|               ANDA MASUK SEBAGAI CUSTOMER             |")
    print("|_______________________________________________________|")
    print("| [1] Login Akun                                        |")
    print("| [2] Daftar Akun                                       |")
    print("| [0] Kembali                                           |")
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("| Pilih Masuk sebagai  > 2                              |")
    pilihan_masuk = str(input("| Masukkan Pilihan     > "))
    if pilihan_masuk == '0':
        main_utama()
    elif pilihan_masuk == '1':
        clear_screen()
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
        print("|               ANDA MASUK SEBAGAI CUSTOMER             |")
        print("|_______________________________________________________|")
        print("| [1] Login Akun                                        |")
        print("| [2] Daftar Akun                                       |")
        print("| [0] Kembali                                           |")
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
        print("| Pilih Masuk sebagai  > 2                              |")
        print("| Masukkan Pilihan     > 1                              |")
        print("|                                                       |")
        print("| Mengalihkan...                                        |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
        time.sleep(1.5)
        login_akun('customer')
    elif pilihan_masuk == '2':
        clear_screen()
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
        print("|               ANDA MASUK SEBAGAI CUSTOMER             |")
        print("|_______________________________________________________|")
        print("| [1] Login Akun                                        |")
        print("| [2] Daftar Akun                                       |")
        print("| [0] Kembali                                           |")
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
        print("| Pilih Masuk sebagai  > 2                              |")
        print("| Masukkan Pilihan     > 2                              |")
        print("|                                                       |")
        print("| Mengalihkan...                                        |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
        time.sleep(1.5)
        daftar_akun('customer')
    else:
        print("|_______________________________________________________|")
        print("\n _______________________________________________________")
        print("| Error:                                                |")
        print("| Input anda tidak valid!                               |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        masuk_customer()

def daftar_akun(level):
    clear_screen()
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("|                       DAFTAR AKUN                     |")
    print("|_______________________________________________________|")
    print("|  Harap mengisi Nama, Umur, Asal, Nomor Hp, Username   |")
    print("|  dan Passworda anda dibawah ini!                      |")
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    #Input Data
    nama = str(input("| Nama                 > "))
    try:
        int(nama)*2
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Error:                                                |")
        print("| Nama tidak dapat berupa angka!                        |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        if level == 'admin':
            masuk_admin()
        elif level == 'customer':
            masuk_customer()
        exit()
    except ValueError:
        breakpoint
    if len(nama) < 4:
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Error:                                                |")
        print("| Masukkan Nama dengan minimal 4 huruf!                 |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        if level == 'admin':
            masuk_admin()
        elif level == 'customer':
            masuk_customer()
    elif len(nama) > 25:
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Error:                                                |")
        print("| Nama tidak dapat lebih dari 25 huruf!                 |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        if level == 'admin':
            masuk_admin()
        elif level == 'customer':
            masuk_customer()
    try:
        umur = int(input("| Umur                 > "))
    except ValueError:
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Error:                                                |")
        print("| Umur harusnya mengandung angka, bukan huruf!          |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        if level == 'admin':
            masuk_admin()
        elif level == 'customer':
            masuk_customer()
    if len(str(umur))>2:
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Error:                                                |")
        print("| Umur harusnya tidak lebih dari 2 digit!               |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        if level == 'admin':
            masuk_admin()
        elif level == 'customer':
            masuk_customer()
    asal = str(input("| Asal                 > "))
    try:
        int(asal)*2
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Error:                                                |")
        print("| Asal tidak dapat berupa angka!                        |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        if level == 'admin':
            masuk_admin()
        elif level == 'customer':
            masuk_customer()
        exit()
    except ValueError:
        breakpoint
    if len(asal) < 1:
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Error:                                                |")
        print("| Anda tidak dapat mengosongkan pengisian data!         |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        if level == 'admin':
            masuk_admin()
        elif level == 'customer':
            masuk_customer()
    try:
        nohp = str(input("| Nomor HP             > "))
        if int(nohp):
            if len(nohp)<10:
                print("|_______________________________________________________|")
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Masukkan Nomor Hp dengan minimal 10 digit!            |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                if level == 'admin':
                    masuk_admin()
                elif level == 'customer':
                    masuk_customer()
            elif len(nohp)>15:
                print("|_______________________________________________________|")
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Data Nomor Hp tidak bisa sebanyak itu!                |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                if level == 'admin':
                    masuk_admin()
                elif level == 'customer':
                    masuk_customer()
            else:
                breakpoint
    except ValueError:
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Error:                                                |")
        print("| Gunakan Nomor Hp yang berupa angka!                   |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        if level == 'admin':
            masuk_admin()
        elif level == 'customer':
            masuk_customer()
    username = str(input("| Username             > "))
    if len(username) < 4:
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Error:                                                |")
        print("| Gunakan username dengan minimal 4 huruf!              |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        if level == 'admin':
            masuk_admin()
        elif level == 'customer':
            masuk_customer()
    #CEK Jika Ada Uname yg Sama
    temp_data = []
    with open('data_akun.csv', mode="r") as csv_read:
        baca = csv.DictReader(csv_read)
        for ini in baca:
            temp_data.append(ini)
    data_temp = []
    i = 0
    for ini in temp_data:
        if ini['USERNAME'] == username:
            data_temp = temp_data[i]
        i+=1
        if len(data_temp) > 0:
            print("|_______________________________________________________|")
            print("\n _______________________________________________________ ")
            print("| Error:                                                |")
            print("| Username tersebut sudah digunakan, harap gunakan      |")
            print("| Username yang unik!                                   |")
            print("|                                                       |")
            print("| Tekan enter untuk kembali...                          |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            if level == 'admin':
                masuk_admin()
            elif level == 'customer':
                masuk_customer()
    password = str(input("| Password             > "))
    if len(password) < 6:
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Error:                                                |")
        print("| Gunakan Password dengan minimal 6 huruf/angka!        |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        if level == 'admin':
            masuk_admin()
        elif level == 'customer':
            masuk_customer()
    try:
        with open('data_akun.csv', mode='a') as csv_add:
            kolom = ['NAMA', 'UMUR', 'ASAL', 'NOHP', 'USERNAME', 'PASSWORD', 'LEVEL']
            append = csv.DictWriter(csv_add, fieldnames=kolom)
            append.writerow({'NAMA': nama, 'UMUR': umur, 'ASAL': asal, 'NOHP': nohp, 'USERNAME': username, 'PASSWORD': password, 'LEVEL': level})
    except PermissionError:
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Error:                                                |")
        print("| Harap menutup file Excel terlebih dahulu!             |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        if level == 'admin':
            masuk_admin()
        elif level == 'customer':
            masuk_customer()
    print("|_______________________________________________________|")
    print("\n _______________________________________________________ ")
    print("| Sukses:                                               |")
    print("| Akun berhasil dibuat dan telah didaftarkan!           |")
    print("|                                                       |")
    print("| Tekan enter untuk kembali...                          |")
    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    if level == 'admin':
        masuk_admin()
    elif level == 'customer':
        masuk_customer()

def login_akun(level):
    clear_screen()
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("|                       LOGIN AKUN                      |")
    print("|_______________________________________________________|")
    print("|          Masukkan Username & password akun anda!      |")
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    temp_data = []
    with open('data_akun.csv', mode="r") as csv_read:
        baca = csv.DictReader(csv_read)
        for ini in baca:
            temp_data.append(ini)
    data_temp = []
    i=0
    uname = str(input("| Username             > "))
    passw = str(input("| Password             > "))
    print("|_______________________________________________________|")
    for ini in temp_data:
        if ini['USERNAME'] == uname:
            data_temp = temp_data[i]
        i+=1
    if level == 'admin':
        if len(data_temp) > 0:
            if data_temp['PASSWORD'] == passw and data_temp['LEVEL'] == 'admin':
                akun_data.insert(0,data_temp['NAMA'])
                akun_data.insert(1,data_temp['USERNAME'])
                akun_data.insert(2,data_temp['PASSWORD'])
                print("\n _______________________________________________________")
                print("| Sukses:                                               |")
                print("| Berhasil login. Anda dialihkan ke menu Admin!         |")
                print("|                                                       |")
                print("| Mengalihkan...                                        |")
                print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                time.sleep(1.5)
                menu_admin()
            elif data_temp['PASSWORD'] == passw and data_temp['LEVEL'] == 'customer':
                print("\n _______________________________________________________")
                print("| Error:                                                |")
                print("| Akun tersebut merupakan akun Customer!                |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                masuk_admin()
            else:
                print("\n _______________________________________________________")
                print("| Error:                                                |")
                print("| Akun ditemukan. Password yang anda masukkan salah!    |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                masuk_admin()
        else:
            print("\n _______________________________________________________")
            print("| Error:                                                |")
            print("| Akun tidak ditemukan. Username tidak valid!           |")
            print("|                                                       |")
            print("| Tekan enter untuk kembali...                          |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            masuk_admin()
    elif level == 'customer':
        if len(data_temp) > 0:
            if data_temp['PASSWORD'] == passw and data_temp['LEVEL'] == 'customer':
                akun_data.insert(0,data_temp['NAMA'])
                akun_data.insert(1,data_temp['USERNAME'])
                akun_data.insert(2,data_temp['PASSWORD'])
                print("\n _______________________________________________________")
                print("| Sukses:                                               |")
                print("| Berhasil login. Anda dialihkan ke menu Customer!      |")
                print("|                                                       |")
                print("| Mengalihkan...                                        |")
                print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                time.sleep(1.5)
                dafbel = []
                total = 0
                daftar_produk(dafbel, total)
            elif data_temp['PASSWORD'] == passw and data_temp['LEVEL'] == 'admin':
                print("\n _______________________________________________________")
                print("| Error:                                                |")
                print("| Akun tersebut merupakan akun Admin!                   |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                masuk_customer()
            else:
                print("\n _______________________________________________________")
                print("| Error:                                                |")
                print("| Akun ditemukan. Password yang anda masukkan salah!    |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                masuk_customer()
        else:
            print("\n _______________________________________________________")
            print("| Error:                                                |")
            print("| Akun tidak ditemukan. Username tidak valid!           |")
            print("|                                                       |")
            print("| Tekan enter untuk kembali...                          |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            masuk_customer()
            
#SEARCHING
def linearSearch(array, n, x):
    ketemu = False
    for i in range(0, n):
        if array[i] == x:
            ketemu = True
            return array
    if ketemu == False:
        return 0
def linearSearch2(array, n, x):
    for i in range(0, n):
        if array[i] == x:
            return i
#SORTING
def insertionSort(array,sort):
    for step in range(1,len(array)):
        key = array[step]
        j = step - 1
        if sort == '1':
            while j >= 0 and key < array[j]:
                array[j+1] = array[j]
                j=j-1
                array[j+1] = key
        elif sort == '2':
            while j >= 0 and key > array[j]:
                array[j+1] = array[j]
                j=j-1
                array[j+1] = key
def mergeSort(arr,sort):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L,sort)
        mergeSort(R,sort)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if sort == 1:
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            elif sort == 2:
                if L[i] > R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

#ADMIN
def menu_admin():
    clear_screen()
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("|                       MENU ADMIN                      |")
    print("|_______________________________________________________|")
    print("| [1] Tampilkan Daftar Akun                             |")
    print("| [2] Daftar Produk dan Harga                           |")
    print("| [3] Ubah Pasword Akun                                 |")
    print("| [4] Keluar Program                                    |")
    print("| [0] Logout                                            |")
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    menu_adm = input(str("| Input menu                  > "))
    if menu_adm == '0':
        print("|_______________________________________________________|")
        print("\n ______________________________________________________ ")
        print("| Sukses:                                              |")
        print("| Anda berhasil Logout!                                |")
        print("|                                                      |")
        print("| Mengalihkan...                                       |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        time.sleep(1.5)
        masuk_admin()
    elif menu_adm == '1':
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Sukses:                                               |")
        print("| Menampilkan Menu & Daftar Akun!                       |")
        print("|                                                       |")
        print("| Mengalihkan...                                        |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        time.sleep(1.5)
        daftar_data_akun()
    elif menu_adm == '2':
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Sukses:                                               |")
        print("| Menampilkan Daftar Produk dan Harga.                  |")
        print("|                                                       |")
        print("| Mengalihkan...                                        |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        time.sleep(1.5)
        produk_harga = []
        daftar_produk_harga(produk_harga)
    elif menu_adm == '3':
        temp_data = []
        with open('data_akun.csv', mode="r") as csv_read:
            baca = csv.DictReader(csv_read)
            for ini in baca:
                temp_data.append(ini)
        data_temp = []
        i = 0
        for ini in temp_data:
            if ini['USERNAME'] == akun_data[1]:
                data_temp = temp_data[i]
            i+=1
        passlama = str(input("| Masukkan Password lama anda > "))
        if data_temp['PASSWORD'] == passlama:
            passbaru = str(input("| Masukkan Password baru      > "))
            print("|_______________________________________________________|")
            if len(passbaru) < 6:
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Gunakan Password dengan minimal 6 huruf/angka!        |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                menu_admin()
            if passbaru == passlama:
                print("\n _______________________________________________________")
                print("| Error:                                                |")
                print("| Password baru anda, sama dengan yang lama!            |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                menu_admin()
            else:
                i=0
                for ini in temp_data:
                    if ini['USERNAME'] == akun_data[1]:
                        temp_data[i]['PASSWORD'] = passbaru
                    i+=1
            try:
                with open('data_akun.csv', mode="w") as csv_write:
                    kolom = ['NAMA', 'UMUR', 'ASAL', 'NOHP', 'USERNAME', 'PASSWORD', 'LEVEL']
                    tulis = csv.DictWriter(csv_write, fieldnames=kolom)
                    tulis.writeheader()
                    for ini in temp_data:
                        tulis.writerow({'NAMA': ini['NAMA'], 'UMUR': ini['UMUR'], 'ASAL': ini['ASAL'], 'NOHP': ini['NOHP'], 'USERNAME': ini['USERNAME'], 'PASSWORD': ini['PASSWORD'], 'LEVEL': ini['LEVEL']})
            except PermissionError:
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Harap menutup file Excel terlebih dahulu!             |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                menu_admin()
            print("\n _______________________________________________________")
            print("| Sukses:                                               |")
            print("| Password anda berhasil di ubah!                       |")
            print("|                                                       |")
            print("| Tekan enter untuk melanjutkan...                      |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            menu_admin()
        else:
            print("|_______________________________________________________|")
            print("\n _______________________________________________________")
            print("| Error:                                                |")
            print("| Password lama yang anda masukkan salah!               |")
            print("|                                                       |")
            print("| Tekan enter untuk kembali...                          |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            menu_admin()
    elif menu_adm == '4':
        print("|_______________________________________________________|")
        print("|                                                       |")
        print("| Keluar Program...                                     |")
        time.sleep(2)
        print("|                                                       |")
        print("| Terimakasih Telah Menggunakan Program Kami!           |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        time.sleep(3)
        exit()
    else:
        print("|_______________________________________________________|")
        print("\n _______________________________________________________")
        print("| Error:                                                |")
        print("| Input yang anda masukkan tidak valid!                 |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
        menu_admin()

def daftar_produk_harga(produk_harga):
    #Dictionary
    penghapus = {0:["FaberCastell", 14000 , 550],         1:["Stabilo\t",16000,500],                2:["Staedler\t",18000,600]          }
    pulpen =    {0:["Gel Umum\t", 22000, 2000],           1:["Biasa Standard\t",20000,1500],        2:["Biasa Pilot\t",25000,3000]      }
    tipex =     {0:["Tip-Ex Cair Joyko\t",65000,5000],    1:["Tip-Ex Kertas Joyko\t",75000,12000]                                       }
    lem =       {0:["Lem Fox Kaleng\t",100000,35000],     1:["Lem Kertas Joyko\t", 40000, 2000],    2:["Lem Korea Alteco\t",60000,5000] }
    buku =      {0:["Bewarna Sidu\t" , 20000 , 3000],     1:["Tebal AlStar\t",15000, 2300],         2:["Tipis Sidu\t",15000, 2500]      }
    cover =     {0:["Cover Putih Sidu\t" , 60000, 1000],  1:["Cover Bewarna Sidu\t", 80000, 2000]                                       }   
    clear_screen()
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("|                 Daftar Produk dan Harga               |")
    print("|_______________________________________________________|")
    #Read Stock From CSV File
    temp_produk = []
    temp_penghapus = []
    penghapus_temp = []
    temp_pulpen = []
    pulpen_temp = []
    temp_tipex = []
    tipex_temp = []
    temp_lem = []
    lem_temp = []
    temp_buku = []
    buku_temp = []
    cover_temp = []
    temp_cover = []
    with open('daftar_produk.csv', mode="r") as csv_read:
        baca = csv.DictReader(csv_read)
        for ini in baca:
            temp_produk.append(ini)
            if ini['PRODUK'] == "Penghapus" and ini['PER'] == 'lusin':
                temp_penghapus.append(ini)
            if ini['PRODUK'] == "Penghapus" and ini['PER'] == 'unit':
                penghapus_temp.append(ini)
            if ini['PRODUK'] == "Pulpen" and ini['PER'] == 'lusin':
                temp_pulpen.append(ini)
            if ini['PRODUK'] == "Pulpen" and ini['PER'] == 'unit':
                pulpen_temp.append(ini)
            if ini['PRODUK'] == "Tip-Ex" and ini['PER'] == 'lusin':
                temp_tipex.append(ini)
            if ini['PRODUK'] == "Tip-Ex" and ini['PER'] == 'unit':
                tipex_temp.append(ini)
            if ini['PRODUK'] == "Lem" and ini['PER'] == 'lusin':
                temp_lem.append(ini)
            if ini['PRODUK'] == "Lem" and ini['PER'] == 'unit':
                lem_temp.append(ini)
            if ini['PRODUK'] == "Buku" and ini['PER'] == 'lusin':
                buku_temp.append(ini)
            if ini['PRODUK'] == "Buku" and ini['PER'] == 'unit':
                temp_buku.append(ini)
            if ini['PRODUK'] == "Cover" and ini['PER'] == 'lusin':
                cover_temp.append(ini)
            if ini['PRODUK'] == "Cover" and ini['PER'] == 'unit':
                temp_cover.append(ini)
    #Print Stock & Product
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    if produk_harga == []:
        x = 0
        y = 0
        for ini in temp_penghapus:
            ini = ("| Penghapus %s Rp.%d/lusin\tTersedia: %s\t|"%(penghapus[x][0],penghapus[x][1],int(int(ini['STOK'])/12)))
            x+=1
            print(ini)
            produk_harga.append(ini)
        for ini in temp_penghapus:
            ini = ("| Penghapus %s Rp.%d/unit \tTersedia: %s\t|"%(penghapus[y][0],penghapus[y][2],ini['STOK']))
            y+=1
            print(ini)
            produk_harga.append(ini)
        x = 0
        y = 0
        for ini in temp_pulpen:
            ini = ("| Pulpen %s Rp.%d/lusin Tersedia: %s\t|"%(pulpen[x][0],pulpen[x][1],int(int(ini['STOK'])/12)))
            x+=1
            print(ini)
            produk_harga.append(ini)
        for ini in pulpen_temp:
            ini = ("| Pulpen %s Rp.%d/unit \tTersedia: %s\t|"%(pulpen[y][0],pulpen[y][2],ini['STOK']))
            y+=1
            print(ini)
            produk_harga.append(ini)
        x = 0
        y = 0
        for ini in temp_tipex:
            ini = ("| %s Rp.%d/lusin Tersedia: %s\t|"%(tipex[x][0],tipex[x][1],int(int(ini['STOK'])/12)))
            x+=1
            print(ini)
            produk_harga.append(ini)
        for ini in tipex_temp:
            ini = ("| %s Rp.%d/unit \tTersedia: %s\t|"%(tipex[y][0],tipex[y][2],ini['STOK']))
            y+=1
            print(ini)
            produk_harga.append(ini)
        x = 0
        y = 0
        for ini in temp_lem:
            ini = ("| %s Rp.%d/lusin Tersedia: %s\t|"%(lem[x][0],lem[x][1],int(int(ini['STOK'])/12)))
            x+=1
            print(ini)
            produk_harga.append(ini)
        for ini in lem_temp:
            ini = ("| %s Rp.%d/unit\tTersedia: %s\t|"%(lem[y][0],lem[y][2],ini['STOK']))
            y+=1
            print(ini)
            produk_harga.append(ini)
        x = 0
        y = 0
        for ini in temp_buku:
            ini = ("| Buku %s Rp.%d/lusin Tersedia: %s\t|"%(buku[x][0],buku[x][1],int(int(ini['STOK'])/12)))
            x+=1
            print(ini)
            produk_harga.append(ini)
        for ini in buku_temp:
            ini = ("| Buku %s Rp.%d/unit\tTersedia: %s\t|"%(buku[y][0],buku[y][2],ini['STOK']))
            y+=1
            print(ini)
            produk_harga.append(ini)
        x = 0
        y = 0
        for ini in temp_cover:
            ini = ("| %s Rp.%d/lusin Tersedia: %s\t|"%(cover[x][0],cover[x][1],int(int(ini['STOK'])/12)))
            x+=1
            print(ini)
            produk_harga.append(ini)
        for ini in cover_temp:
            ini = ("| %s Rp.%d/unit\tTersedia: %s\t|"%(cover[y][0],cover[y][2],ini['STOK']))
            y+=1
            print(ini)
            produk_harga.append(ini)
        print("|_______________________________________________________|")
    #Print Dafbel
    else:
        for ini in produk_harga:
            print(ini)
        print("|_______________________________________________________|")
    #Menu
    print("| [1] Sorting                                           |")
    print("| [2] Searching                                         |")
    print("| [3] Tambah Stok                                       |")
    print("| [0] Kembali                                           |")
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    sors = str(input("| Masukkan Menu      > "))
    if sors == '0':
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Sukses:                                               |")
        print("| Beralih kembali ke Menu Admin!                        |")
        print("|                                                       |")
        print("| Mengalihkan...                                        |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        time.sleep(1.5)
        menu_admin()
    elif sors == '1':
        clear_screen()
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
        print("|                 Daftar Produk dan Harga               |")
        print("|_______________________________________________________|")
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
        for ini in produk_harga:
            print(ini)
        print("|_______________________________________________________|")
        print("| [1] Ascending                                         |")
        print("| [2] Descending                                        |")
        print("| [0] Kembali                                           |")
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
        print("| Masukkan Menu      > 1                                |")
        try:
            sort = int(input("| Pilih opsi sorting > "))
            print("|_______________________________________________________|")
            if sort == 0:
                daftar_produk_harga(produk_harga)
            elif sort == 1 or sort == 2:
                mergeSort(produk_harga,sort)
                daftar_produk_harga(produk_harga)
            else:
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Input yang anda masukkan tidak ada pada menu!         |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk_harga(produk_harga)
        except ValueError:
            print("|_______________________________________________________|")
            print("\n _______________________________________________________ ")
            print("| Error:                                                |")
            print("| Input yang anda masukkan tidak valid!                 |")
            print("|                                                       |")
            print("| Tekan enter untuk kembali...                          |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            daftar_produk_harga(produk_harga)
    elif sors == '2':
        indeks1 = 0
        indeks2 = -1
        indeks3 = -1
        list1 = []
        list2 = []
        for ini in produk_harga:
            c = produk_harga[indeks1].split()
            list1.append(c)
            indeks1+=1
        nyari = input("| Mencari produk     > ")
        print("|_______________________________________________________|")
        if nyari == 'tip-ex' or nyari == 'tIp-ex' or nyari == 'tiP-ex' or nyari == 'tipex' or nyari == 'Tipex' or nyari == 'tipEx' or nyari == 'Tip-ex' or nyari == 'tip-Ex' or nyari == 'Tip-Ex' or nyari == 'TipEx':
            cari = 'Tip-Ex'
        else:
            cari = nyari.capitalize()
        for ini in list1:
            indeks2 += 1
            hasil = linearSearch(list1[indeks2],len(list1[indeks2]),cari)
            try:
                list2.append(hasil)
                list2.remove(0)
            except ValueError:
                breakpoint
        if cari == 'Penghapus':
            print("|              Hasil Pencarian Dari Penghapus           |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            for ini in list2:
                indeks3 += 1
                cari = list2[indeks3]
                hasil = linearSearch2(list1,len(list1),cari)
                print(produk_harga[hasil])
        elif cari == 'Lem':
            print("|                 Hasil Pencarian Dari Lem              |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            for ini in list2:
                indeks3 += 1
                cari = list2[indeks3]
                hasil = linearSearch2(list1,len(list1),cari)
                print(produk_harga[hasil])
        elif cari == 'Buku' or cari == 'Cover' or cari == 'Pulpen' or cari == 'Tip-Ex':
            print("|              Hasil Pencarian Dari "+cari+"\t\t|")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            for ini in list2:
                indeks3 += 1
                cari = list2[indeks3]
                hasil = linearSearch2(list1,len(list1),cari)
                print(produk_harga[hasil])
        else:
            print("| Error:                                                |")
            print("| Produk yang anda cari tidak ditemukan.                |")
            print("| Pastikan untuk hanya menginput nama produk saja!!     |")
            print("| CONTOH: Buku, Lem, Pulpen, Tipex, dll.                |")
        print("|                                                       |")
        print("| Tekan Enter untuk Kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        daftar_produk_harga(produk_harga)
    elif sors == '3':
        stock = lambda stok: stok+tambah
        cari = str.capitalize(input("| Input nama produk  > "))
        print("|_______________________________________________________|")
        if cari == 'Penghapus':
            clear_screen()
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                 Daftar Produk dan Harga               |")
            print("|_______________________________________________________|")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            for ini in produk_harga:
                print(ini)
            print("|_______________________________________________________|")
            print("| [1] FaberCastell                                      |")
            print("| [2] Stabilo                                           |")
            print("| [3] Staedler                                          |")
            print("| [0] Kembali                                           |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("| Masukkan Menu      > 3                                |")
            print("| Input nama produk  > Penghapus                        |")
            jenis = str(input("| Pilih Jenis Produk > "))
            for ini in temp_produk:
                if jenis == '0':
                    daftar_produk_harga(produk_harga)
                    break
                elif jenis == '1' and ini['PRODUK'] == 'Penghapus' and ini['JENIS'] == 'FaberCastell':
                    if len(ini['STOK']) > 4:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Stok yang tersedia sudah tidak dapat ditambahkan!     |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    try:
                        tambah = int(input("| Input Tambahan Stok> "))
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    if tambah >= 90000:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Tidak dapat menambah stok sebanyak itu!               |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    else:
                        i=0
                        for ini in temp_produk:
                            if ini['JENIS'] == 'FaberCastell':
                                temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                            i+=1
                        END = True
                        break
                elif jenis == '2' and ini['PRODUK'] == 'Penghapus' and ini['JENIS'] == 'Stabilo':
                    if len(ini['STOK']) > 4:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Stok yang tersedia sudah tidak dapat ditambahkan!     |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    try:
                        tambah = int(input("| Input Tambahan Stok> "))
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    if tambah >= 90000:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Tidak dapat menambah stok sebanyak itu!               |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    else:
                        i=0
                        for ini in temp_produk:
                            if ini['JENIS'] == 'Stabilo':
                                temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                            i+=1
                        END = True
                        break
                elif jenis == '3' and ini['PRODUK'] == 'Penghapus' and ini['JENIS'] == 'Staedler':
                    if len(ini['STOK']) > 4:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Stok yang tersedia sudah tidak dapat ditambahkan!     |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    try:
                        tambah = int(input("| Input Tambahan Stok> "))
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    if tambah >= 90000:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Tidak dapat menambah stok sebanyak itu!               |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    else:
                        i=0
                        for ini in temp_produk:
                            if ini['JENIS'] == 'Staedler':
                                temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                            i+=1
                        END = True
                        break
                END = False
            if END == True:
                try:
                    with open('daftar_produk.csv', 'w') as csv_write:
                        kolom = ['PRODUK','JENIS','HARGA','PER','STOK']
                        tulis = csv.DictWriter(csv_write, fieldnames=kolom)
                        tulis.writeheader()
                        for ini in temp_produk:
                            tulis.writerow({'PRODUK': ini['PRODUK'], 'JENIS': ini['JENIS'], 'HARGA': ini['HARGA'], 'PER': ini['PER'], 'STOK': ini['STOK']})
                    produk_harga = []
                except PermissionError:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________ ")
                    print("| Error:                                                |")
                    print("| Harap menutup file Excel terlebih dahulu!             |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    daftar_produk_harga(produk_harga)
                print("|_______________________________________________________|")
                print("\n _______________________________________________________ ")
                print("| Sukses:                                               |")
                print("| Stok berhasil ditambahkan!                            |")
                print("|                                                       |")
                print("| Tekan Enter untuk melanjutkan...                      |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk_harga(produk_harga)
            else:
                print("|_______________________________________________________|")
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Input yang anda masukkan tidak valid!                 |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk_harga(produk_harga)
        elif cari == 'Pulpen':
            clear_screen()
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                 Daftar Produk dan Harga               |")
            print("|_______________________________________________________|")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            for ini in produk_harga:
                print(ini)
            print("|_______________________________________________________|")
            print("| [1] Gel Umum                                          |")
            print("| [2] Standard                                          |")
            print("| [3] Pilot                                             |")
            print("| [0] Kembali                                           |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("| Masukkan Menu      > 3                                |")
            print("| Input nama produk  > Pulpen                           |")
            jenis = str(input("| Pilih Jenis Produk > "))
            for ini in temp_produk:
                if jenis == '0':
                    daftar_produk_harga(produk_harga)
                    break
                elif jenis == '1' and ini['PRODUK'] == 'Pulpen' and ini['JENIS'] == 'Gel Umum':
                    if len(ini['STOK']) > 4:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Stok yang tersedia sudah tidak dapat ditambahkan!     |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    try:
                        tambah = int(input("| Input Tambahan Stok> "))
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    if tambah >= 90000:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Tidak dapat menambah stok sebanyak itu!               |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    else:
                        i=0
                        for ini in temp_produk:
                            if ini['JENIS'] == 'Gel Umum':
                                temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                            i+=1
                        END = True
                        break
                elif jenis == '2' and ini['PRODUK'] == 'Pulpen' and ini['JENIS'] == 'Standard':
                    if len(ini['STOK']) > 4:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Stok yang tersedia sudah tidak dapat ditambahkan!     |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    try:
                        tambah = int(input("| Input Tambahan Stok> "))
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    if tambah >= 90000:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Tidak dapat menambah stok sebanyak itu!               |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    else:
                        i=0
                        for ini in temp_produk:
                            if ini['JENIS'] == 'Standard':
                                temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                            i+=1
                        END = True
                        break
                elif jenis == '3' and ini['PRODUK'] == 'Pulpen' and ini['JENIS'] == 'Pilot':
                    if len(ini['STOK']) > 4:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Stok yang tersedia sudah tidak dapat ditambahkan!     |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    try:
                        tambah = int(input("| Input Tambahan Stok> "))
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    if tambah >= 90000:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Tidak dapat menambah stok sebanyak itu!               |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    else:
                        i=0
                        for ini in temp_produk:
                            if ini['JENIS'] == 'Pilot':
                                temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                            i+=1
                        END = True
                        break
                END = False
            if END == True:
                try:
                    with open('daftar_produk.csv', 'w') as csv_write:
                        kolom = ['PRODUK','JENIS','HARGA','PER','STOK']
                        tulis = csv.DictWriter(csv_write, fieldnames=kolom)
                        tulis.writeheader()
                        for ini in temp_produk:
                            tulis.writerow({'PRODUK': ini['PRODUK'], 'JENIS': ini['JENIS'], 'HARGA': ini['HARGA'], 'PER': ini['PER'], 'STOK': ini['STOK']})
                    produk_harga = []
                except PermissionError:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________ ")
                    print("| Error:                                                |")
                    print("| Harap menutup file Excel terlebih dahulu!             |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    daftar_produk_harga(produk_harga)
                print("|_______________________________________________________|")
                print("\n _______________________________________________________ ")
                print("| Sukses:                                               |")
                print("| Stok berhasil ditambahkan!                            |")
                print("|                                                       |")
                print("| Tekan Enter untuk melanjutkan...                      |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk_harga(produk_harga)
            else:
                print("|_______________________________________________________|")
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Input yang anda masukkan tidak valid!                 |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk_harga(produk_harga)
        elif cari == 'tip-ex' or cari == 'tIp-ex' or cari == 'tiP-ex' or cari == 'tipex' or cari == 'Tipex' or cari == 'tipEx' or cari == 'Tip-ex' or cari == 'tip-Ex' or cari == 'Tip-Ex' or cari == 'TipEx' or cari == 'Tip-Ex':
            clear_screen()
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                 Daftar Produk dan Harga               |")
            print("|_______________________________________________________|")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            for ini in produk_harga:
                print(ini)
            print("|_______________________________________________________|")
            print("| [1] Cair                                              |")
            print("| [2] Kertas                                            |")
            print("| [0] Kembali                                           |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("| Masukkan Menu      > 3                                |")
            print("| Input nama produk  > Tip-Ex                           |")
            jenis = str(input("| Pilih Jenis Produk > "))
            for ini in temp_produk:
                if jenis == '0':
                    daftar_produk_harga(produk_harga)
                    break
                elif jenis == '1' and ini['PRODUK'] == 'Tip-Ex' and ini['JENIS'] == 'Cair':
                    if len(ini['STOK']) > 4:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Stok yang tersedia sudah tidak dapat ditambahkan!     |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    try:
                        tambah = int(input("| Input Tambahan Stok> "))
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    if tambah >= 90000:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Tidak dapat menambah stok sebanyak itu!               |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    else:
                        i=0
                        for ini in temp_produk:
                            if ini['JENIS'] == 'Cair':
                                temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                            i+=1
                        END = True
                        break
                elif jenis == '2' and ini['PRODUK'] == 'Tip-Ex' and ini['JENIS'] == 'Kertas':
                    if len(ini['STOK']) > 4:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Stok yang tersedia sudah tidak dapat ditambahkan!     |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    try:
                        tambah = int(input("| Input Tambahan Stok> "))
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    if tambah >= 90000:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Tidak dapat menambah stok sebanyak itu!               |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    else:
                        i=0
                        for ini in temp_produk:
                            if ini['PRODUK'] == 'Tip-Ex' and ini['JENIS'] == 'Kertas':
                                temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                            i+=1
                        END = True
                        break
                END = False
            if END == True:
                try:
                    with open('daftar_produk.csv', 'w') as csv_write:
                        kolom = ['PRODUK','JENIS','HARGA','PER','STOK']
                        tulis = csv.DictWriter(csv_write, fieldnames=kolom)
                        tulis.writeheader()
                        for ini in temp_produk:
                            tulis.writerow({'PRODUK': ini['PRODUK'], 'JENIS': ini['JENIS'], 'HARGA': ini['HARGA'], 'PER': ini['PER'], 'STOK': ini['STOK']})
                    produk_harga = []
                except PermissionError:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________ ")
                    print("| Error:                                                |")
                    print("| Harap menutup file Excel terlebih dahulu!             |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    daftar_produk_harga(produk_harga)
                print("|_______________________________________________________|")
                print("\n _______________________________________________________ ")
                print("| Sukses:                                               |")
                print("| Stok berhasil ditambahkan!                            |")
                print("|                                                       |")
                print("| Tekan Enter untuk melanjutkan...                      |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk_harga(produk_harga)
            else:
                print("|_______________________________________________________|")
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Input yang anda masukkan tidak valid!                 |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk_harga(produk_harga)
        elif cari == 'Lem':
            clear_screen()
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                 Daftar Produk dan Harga               |")
            print("|_______________________________________________________|")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            for ini in produk_harga:
                print(ini)
            print("|_______________________________________________________|")
            print("| [1] Lem Fox                                           |")
            print("| [2] Lem Kertas                                        |")
            print("| [3] Lem Korea                                         |")
            print("| [0] Kembali                                           |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("| Masukkan Menu      > 3                                |")
            print("| Input nama produk  > Lem                              |")
            jenis = str(input("| Pilih Jenis Produk > "))
            for ini in temp_produk:
                if jenis == '0':
                    daftar_produk_harga(produk_harga)
                    break
                elif jenis == '1' and ini['PRODUK'] == 'Lem' and ini['JENIS'] == 'Fox':
                    if len(ini['STOK']) > 4:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Stok yang tersedia sudah tidak dapat ditambahkan!     |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    try:
                        tambah = int(input("| Input Tambahan Stok> "))
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    if tambah >= 90000:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Tidak dapat menambah stok sebanyak itu!               |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    else:
                        i=0
                        for ini in temp_produk:
                            if ini['JENIS'] == 'Fox':
                                temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                            i+=1
                        END = True
                        break
                elif jenis == '2' and ini['PRODUK'] == 'Lem' and ini['JENIS'] == 'Kertas':
                    if len(ini['STOK']) > 4:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Stok yang tersedia sudah tidak dapat ditambahkan!     |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    try:
                        tambah = int(input("| Input Tambahan Stok> "))
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    if tambah >= 90000:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Tidak dapat menambah stok sebanyak itu!               |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    else:
                        i=0
                        for ini in temp_produk:
                            if ini['PRODUK'] == 'Lem' and ini['JENIS'] == 'Kertas':
                                temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                            i+=1
                        END = True
                        break
                elif jenis == '3' and ini['PRODUK'] == 'Lem' and ini['JENIS'] == 'Korea':
                    if len(ini['STOK']) > 4:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Stok yang tersedia sudah tidak dapat ditambahkan!     |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    try:
                        tambah = int(input("| Input Tambahan Stok> "))
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    if tambah >= 90000:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Tidak dapat menambah stok sebanyak itu!               |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    else:
                        i=0
                        for ini in temp_produk:
                            if ini['JENIS'] == 'Korea':
                                temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                            i+=1
                        END = True
                        break
                END = False
            if END == True:
                try:
                    with open('daftar_produk.csv', 'w') as csv_write:
                        kolom = ['PRODUK','JENIS','HARGA','PER','STOK']
                        tulis = csv.DictWriter(csv_write, fieldnames=kolom)
                        tulis.writeheader()
                        for ini in temp_produk:
                            tulis.writerow({'PRODUK': ini['PRODUK'], 'JENIS': ini['JENIS'], 'HARGA': ini['HARGA'], 'PER': ini['PER'], 'STOK': ini['STOK']})
                    produk_harga = []
                except PermissionError:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________ ")
                    print("| Error:                                                |")
                    print("| Harap menutup file Excel terlebih dahulu!             |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    daftar_produk_harga(produk_harga)
                print("|_______________________________________________________|")
                print("\n _______________________________________________________ ")
                print("| Sukses:                                               |")
                print("| Stok berhasil ditambahkan!                            |")
                print("|                                                       |")
                print("| Tekan Enter untuk melanjutkan...                      |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk_harga(produk_harga)
            else:
                print("|_______________________________________________________|")
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Input yang anda masukkan tidak valid!                 |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk_harga(produk_harga)
        elif cari == 'Buku':
            clear_screen()
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                 Daftar Produk dan Harga               |")
            print("|_______________________________________________________|")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            for ini in produk_harga:
                print(ini)
            print("|_______________________________________________________|")
            print("| [1] Buku Bewarna Sidu                                 |")
            print("| [2] Buku Tebal Alstar                                 |")
            print("| [3] Buku Tipis Sidu                                   |")
            print("| [0] Kembali                                           |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("| Masukkan Menu      > 3                                |")
            print("| Input nama produk  > Buku                             |")
            jenis = str(input("| Pilih Jenis Produk > "))
            for ini in temp_produk:
                if jenis == '0':
                    daftar_produk_harga(produk_harga)
                    break
                elif jenis == '1' and ini['PRODUK'] == 'Buku' and ini['JENIS'] == 'Bewarna':
                    if len(ini['STOK']) > 4:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Stok yang tersedia sudah tidak dapat ditambahkan!     |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    try:
                        tambah = int(input("| Input Tambahan Stok> "))
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    if tambah >= 90000:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Tidak dapat menambah stok sebanyak itu!               |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    else:
                        i=0
                        for ini in temp_produk:
                            if ini['PRODUK'] == 'Buku' and ini['JENIS'] == 'Bewarna':
                                temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                            i+=1
                        END = True
                        break
                elif jenis == '2' and ini['PRODUK'] == 'Buku' and ini['JENIS'] == 'Tebal':
                    if len(ini['STOK']) > 4:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Stok yang tersedia sudah tidak dapat ditambahkan!     |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    try:
                        tambah = int(input("| Input Tambahan Stok> "))
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    if tambah >= 90000:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Tidak dapat menambah stok sebanyak itu!               |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    else:
                        i=0
                        for ini in temp_produk:
                            if ini['JENIS'] == 'Tebal':
                                temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                            i+=1
                        END = True
                        break
                elif jenis == '3' and ini['PRODUK'] == 'Buku' and ini['JENIS'] == 'Tipis':
                    if len(ini['STOK']) > 4:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Stok yang tersedia sudah tidak dapat ditambahkan!     |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    try:
                        tambah = int(input("| Input Tambahan Stok> "))
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    if tambah >= 90000:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Tidak dapat menambah stok sebanyak itu!               |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    else:
                        i=0
                        for ini in temp_produk:
                            if ini['JENIS'] == 'Tipis':
                                temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                            i+=1
                        END = True
                        break
                END = False
            if END == True:
                try:
                    with open('daftar_produk.csv', 'w') as csv_write:
                        kolom = ['PRODUK','JENIS','HARGA','PER','STOK']
                        tulis = csv.DictWriter(csv_write, fieldnames=kolom)
                        tulis.writeheader()
                        for ini in temp_produk:
                            tulis.writerow({'PRODUK': ini['PRODUK'], 'JENIS': ini['JENIS'], 'HARGA': ini['HARGA'], 'PER': ini['PER'], 'STOK': ini['STOK']})
                    produk_harga = []
                except PermissionError:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________ ")
                    print("| Error:                                                |")
                    print("| Harap menutup file Excel terlebih dahulu!             |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    daftar_produk_harga(produk_harga)
                print("|_______________________________________________________|")
                print("\n _______________________________________________________ ")
                print("| Sukses:                                               |")
                print("| Stok berhasil ditambahkan!                            |")
                print("|                                                       |")
                print("| Tekan Enter untuk melanjutkan...                      |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk_harga(produk_harga)
            else:
                print("|_______________________________________________________|")
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Input yang anda masukkan tidak valid!                 |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk_harga(produk_harga)
        elif cari == 'Cover':
            clear_screen()
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                 Daftar Produk dan Harga               |")
            print("|_______________________________________________________|")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            for ini in produk_harga:
                print(ini)
            print("|_______________________________________________________|")
            print("| [1] Cover Putih                                       |")
            print("| [2] Cover Bewarna                                     |")
            print("| [0] Kembali                                           |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("| Masukkan Menu      > 3                                |")
            print("| Input nama produk  > Cover                            |")
            jenis = str(input("| Pilih Jenis Produk > "))
            for ini in temp_produk:
                if jenis == '0':
                    daftar_produk_harga(produk_harga)
                    break
                elif jenis == '1' and ini['PRODUK'] == 'Cover' and ini['JENIS'] == 'Putih':
                    if len(ini['STOK']) > 4:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Stok yang tersedia sudah tidak dapat ditambahkan!     |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    try:
                        tambah = int(input("| Input Tambahan Stok> "))
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    if tambah >= 90000:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Tidak dapat menambah stok sebanyak itu!               |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    else:
                        i=0
                        for ini in temp_produk:
                            if ini['JENIS'] == 'Putih':
                                temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                            i+=1
                        END = True
                        break
                elif jenis == '2' and ini['PRODUK'] == 'Cover' and ini['JENIS'] == 'Bewarna':
                    if len(ini['STOK']) > 4:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Stok yang tersedia sudah tidak dapat ditambahkan!     |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    try:
                        tambah = int(input("| Input Tambahan Stok> "))
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    if tambah >= 90000:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Tidak dapat menambah stok sebanyak itu!               |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_produk_harga(produk_harga)
                        break
                    else:
                        i=0
                        for ini in temp_produk:
                            if ini['PRODUK'] == 'Cover' and ini['JENIS'] == 'Bewarna':
                                temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                            i+=1
                        END = True
                        break
                END = False
            if END == True:
                try:
                    with open('daftar_produk.csv', 'w') as csv_write:
                        kolom = ['PRODUK','JENIS','HARGA','PER','STOK']
                        tulis = csv.DictWriter(csv_write, fieldnames=kolom)
                        tulis.writeheader()
                        for ini in temp_produk:
                            tulis.writerow({'PRODUK': ini['PRODUK'], 'JENIS': ini['JENIS'], 'HARGA': ini['HARGA'], 'PER': ini['PER'], 'STOK': ini['STOK']})
                    produk_harga = []
                except PermissionError:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________ ")
                    print("| Error:                                                |")
                    print("| Harap menutup file Excel terlebih dahulu!             |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    daftar_produk_harga(produk_harga)
                print("|_______________________________________________________|")
                print("\n _______________________________________________________ ")
                print("| Sukses:                                               |")
                print("| Stok berhasil ditambahkan!                            |")
                print("|                                                       |")
                print("| Tekan Enter untuk melanjutkan...                      |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk_harga(produk_harga)
            else:
                print("|_______________________________________________________|")
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Input yang anda masukkan tidak valid!                 |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk_harga(produk_harga)
        else:
            print("| Error:                                                |")
            print("| Produk tidak ditemukan.                               |")
            print("| Pastikan untuk hanya menginput nama produk saja!!     |")
            print("| CONTOH: Buku, Lem, Pulpen, Tipex, dll.                |")
            print("|                                                       |")
            print("| Tekan Enter untuk Kembali...                          |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            daftar_produk_harga(produk_harga)
    else:
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Error:                                                |")
        print("| Input yang anda masukkan tidak valid!                 |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        daftar_produk_harga(produk_harga)

def daftar_data_akun():
    clear_screen()
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("|                   DAFTAR DATA AKUN                    |")
    data_admin = []
    data_customer = []
    mix_data = [] 
    with open('data_akun.csv', mode="r") as csv_read:
        baca = csv.DictReader(csv_read)
        for ini in baca:
            if ini['LEVEL'] == 'admin':
                data_admin.append(ini)
            if ini['LEVEL'] == 'customer':
                data_customer.append(ini)
            mix_data.append(ini)
    i = 1
    if len(data_admin) > 0:
        for ini in data_admin:
            print("|_______________________________________________________|")
            print("| Akun ke-%d                             \t\t|" %i)
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("| Nama                   : %s " % (ini['NAMA']))
            print("| Umur                   : %s " % (ini['UMUR']))
            print("| Asal                   : %s " % (ini['ASAL']))
            print("| Nomor HP               : %s " % (ini['NOHP']))
            print("| Username               : %s " % (ini['USERNAME']))
            print("| Password               : %s " % (ini['PASSWORD']))
            print("| Data Akun              : Admin")
            i += 1
    else:
        print("|_______________________________________________________|")
        print("|              Data Akun Admin Tidak Tersedia           |")
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    if len(data_customer) > 0:
        for ini in data_customer:
            print("|_______________________________________________________|")
            print("| Akun ke-%d                             \t\t|"%i)
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("| Nama                   : %s " % (ini['NAMA']))
            print("| Umur                   : %s " % (ini['UMUR']))
            print("| Asal                   : %s " % (ini['ASAL']))
            print("| Nomor HP               : %s " % (ini['NOHP']))
            print("| Username               : %s " % (ini['USERNAME']))
            print("| Password               : %s " % (ini['PASSWORD']))
            print("| Data Akun              : Customer")
            i+=1
    else:
        print("|_______________________________________________________|")
        print("|             Data Akun Customer Tidak Tersedia         |")
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("|_______________________________________________________|")
    print("| [1] Hapus Akun                                        |")
    print("| [2] Edit Data Akun                                    |")
    print("| [0] Kembali                                           |")
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    opsi = str(input("| Pilih Menu             > "))
    if opsi == '0':
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Sukses:                                               |")
        print("| Beralih kembali ke Menu Admin!                        |")
        print("|                                                       |")
        print("| Mengalihkan...                                        |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        time.sleep(1.5)
        menu_admin()
    elif opsi == '1':
        uname = str(input("| Masukkan Username Akun > "))
        print("|_______________________________________________________|")
        j = 0
        for ini in mix_data:
            if uname == akun_data[1]:
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Anda tidak dapat menghapus Akun anda sendiri!         |")
                print("|                                                       |")
                print("| Tekan Enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_data_akun()
            else:
                if ini['USERNAME'] == uname:
                    mix_data.remove(mix_data[j])
                    try:
                        with open('data_akun.csv', mode="w") as csv_write:
                            kolom = ['NAMA', 'UMUR', 'ASAL', 'NOHP', 'USERNAME', 'PASSWORD', 'LEVEL']
                            tulis = csv.DictWriter(csv_write, fieldnames=kolom)
                            tulis.writeheader()
                            for ini in mix_data:
                                tulis.writerow({'NAMA': ini['NAMA'], 'UMUR': ini['UMUR'], 'ASAL': ini['ASAL'], 'NOHP': ini['NOHP'], 'USERNAME': ini['USERNAME'], 'PASSWORD': ini['PASSWORD'], 'LEVEL': ini['LEVEL']})
                    except PermissionError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________ ")
                        print("| Error:                                                |")
                        print("| Harap menutup file Excel terlebih dahulu!             |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        daftar_data_akun()
                    print("\n _______________________________________________________ ")
                    print("| Sukses:                                               |")
                    print("| Akun berhasil dihapus!                                |")
                    print("|                                                       |")
                    print("| Tekan Enter untuk melanjutkan...                      |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    daftar_data_akun()
                j+=1
        print("\n _______________________________________________________ ")
        print("| Error:                                                |")
        print("| Tidak ada akun yang memiliki Username tersebut!       |")
        print("|                                                       |")
        print("| Tekan Enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        daftar_data_akun()
    elif opsi == '2':
        uname = str(input("| Masukkan Username Akun > "))
        k = 0
        for ini in mix_data:
            if ini['USERNAME'] == uname:
                print("|_______________________________________________________|")
                print("\n _______________________________________________________ ")
                print("| Sukses:                                               |")
                print("| Username ditemukan!                                   |")
                print("|                                                       |")
                print("| Masukkan data baru!                                   |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                nama = str(input("| Nama                 > "))
                try:
                    int(nama)*2
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________ ")
                    print("| Error:                                                |")
                    print("| Nama tidak dapat berupa angka!                        |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    daftar_data_akun()
                except ValueError:
                    breakpoint
                if len(nama) < 4:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________ ")
                    print("| Error:                                                |")
                    print("| Masukkan Nama dengan minimal 4 huruf!                 |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    daftar_data_akun()
                elif len(nama) > 25:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________ ")
                    print("| Error:                                                |")
                    print("| Nama tidak dapat lebih dari 25 huruf!                 |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    daftar_data_akun()
                try:
                    umur = int(input("| Umur                 > "))
                except ValueError:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________ ")
                    print("| Error:                                                |")
                    print("| Umur harusnya mengandung angka, bukan huruf!          |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    daftar_data_akun()
                if len(str(umur))>2:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________ ")
                    print("| Error:                                                |")
                    print("| Umur harusnya tidak lebih dari 2 digit!               |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    daftar_data_akun()
                asal = str(input("| Asal                 > "))
                try:
                    int(asal)*2
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________ ")
                    print("| Error:                                                |")
                    print("| Asal tidak dapat berupa angka!                        |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    daftar_data_akun()
                except ValueError:
                    breakpoint
                if len(asal) < 1:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________ ")
                    print("| Error:                                                |")
                    print("| Anda tidak dapat mengosongkan pengisian data!         |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    daftar_data_akun()
                try:
                    nohp = str(input("| Nomor HP             > "))
                    if int(nohp):
                        if len(nohp)<10:
                            print("|_______________________________________________________|")
                            print("\n _______________________________________________________ ")
                            print("| Error:                                                |")
                            print("| Masukkan Nomor Hp dengan minimal 10 digit!            |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            daftar_data_akun()
                        elif len(nohp)>15:
                            print("|_______________________________________________________|")
                            print("\n _______________________________________________________ ")
                            print("| Error:                                                |")
                            print("| Data Nomor Hp tidak bisa sebanyak itu!                |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            daftar_data_akun()
                        else:
                            breakpoint
                except ValueError:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________ ")
                    print("| Error:                                                |")
                    print("| Gunakan Nomor Hp yang berupa angka!                   |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    daftar_data_akun()
                mix_data[k]['NAMA'] = nama
                mix_data[k]['UMUR'] = umur
                mix_data[k]['ASAL'] = asal
                mix_data[k]['NOHP'] = nohp
                try:
                    with open('data_akun.csv', mode="w") as csv_write:
                        kollom = ['NAMA', 'UMUR', 'ASAL', 'NOHP', 'USERNAME', 'PASSWORD', 'LEVEL']
                        tulis = csv.DictWriter(csv_write, fieldnames=kollom)
                        tulis.writeheader()
                        for ini in mix_data:
                            tulis.writerow({'NAMA': ini['NAMA'], 'UMUR': ini['UMUR'], 'ASAL': ini['ASAL'], 'NOHP': ini['NOHP'], 'USERNAME': ini['USERNAME'], 'PASSWORD': ini['PASSWORD'], 'LEVEL': ini['LEVEL']})
                except PermissionError:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________ ")
                    print("| Error:                                                |")
                    print("| Harap menutup file Excel terlebih dahulu!             |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                print("|_______________________________________________________|")
                print("\n _______________________________________________________ ")
                print("| Sukses:                                               |")
                print("| Data Akun berhasil diubah!                            |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_data_akun()
            k+=1
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Error:                                                |")
        print("| Tidak ada akun yang memiliki Username tersebut!       |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        daftar_data_akun()
    else:
        print("|_______________________________________________________|")
        print("\n _______________________________________________________ ")
        print("| Error:                                                |")
        print("| Input yang anda masukkan tidak valid!                 |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        daftar_data_akun()

#CUSTOMER
def daftar_produk(dafbel, total):
    #Nested List
    penghapus = [[0,"FaberCastell", 14000 , 550],   [1,"Stabilo",16000,500] ,           [2, "Staedler",18000,600]]
    pulpen =    [[0,"GelUmum", 22000, 2000],        [1,"Standard",20000,1500],          [2,"Pilot",25000,3000]]
    tipex =     [[0,"Tip-Ex Cair",65000,5000],      [1,"Tip-Ex Kertas",75000,12000]]
    lem =       [[0,"Lem Fox",100000,35000],        [1,"Lem Kertas", 40000, 2000],      [2,"Lem Korea",60000,5000]]
    buku =      [[0, "Bewarna Sidu" , 20000 , 3000],[1, "Tebal AlStar",15000, 2300],    [2, "Tipis Sidu",15000, 2500]]
    cover =     [[0,"Cover Putih" , 60000, 1000],   [1, "Cover Bewarna", 80000, 2000]]
    total0 = lambda x: x+total
    berapa = lambda y: y*banyak
    stock = lambda z: z-banyak
    temp_produk = []
    with open('daftar_produk.csv', mode="r") as csv_read:
        baca = csv.DictReader(csv_read)
        for ini in baca:
            temp_produk.append(ini)
    clear_screen()
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("|                      DAFTAR PRODUK                    |")
    print("|_______________________________________________________|")
    print("| [1] Penghapus                                         |")
    print("| [2] Pulpen                                            |")
    print("| [3] Tip-Ex                                            |")
    print("| [4] Lem                                               |")
    print("| [5] Buku                                              |")
    print("| [6] Cover                                             |")
    print("| [7] Menu Customer & Daftar Belanja                    |")
    print("| [0] Logout                                            |")
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    daftar = input(str("| Pilih menu atau produk        > "))
    print("|_______________________________________________________|")
    if daftar == "0":
        print("\n ______________________________________________________ ")
        print("| Sukses:                                              |")
        print("| Anda berhasil Logout!                                |")
        print("|                                                      |")
        print("| Mengalihkan...                                       |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        time.sleep(1.5)
        masuk_customer()
    #PENGHAPUS
    elif daftar == "1":
        while True:
            clear_screen()
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                      DAFTAR PRODUK                    |")
            print("|_______________________________________________________|")
            print("| [1] Penghapus                                         |")
            print("| [2] Pulpen                                            |")
            print("| [3] Tip-Ex                                            |")
            print("| [4] Lem                                               |")
            print("| [5] Buku                                              |")
            print("| [6] Cover                                             |")
            print("| [7] Menu Customer & Daftar Belanja                    |")
            print("| [0] Logout                                            |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("| Pilih menu atau produk        > 1                     |")
            print("|_______________________________________________________|")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                     Jenis Penghapus                   |")
            print("|_______________________________________________________|")
            print("| [1] FaberCastell                                      |")
            print("| [2] Stabilo                                           |")
            print("| [3] Staedler                                          |")
            print("| [0] Kembali                                           |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            pengh = input(str("| Pilih jenis Penghapus         > "))
            print("|_______________________________________________________|")
            for ini in temp_produk:
                if ini['PRODUK'] == "Penghapus" and ini['JENIS'] == "FaberCastell" and ini['PER'] == "lusin":
                    a = int(ini['STOK'])
                if ini['PRODUK'] == "Penghapus" and ini['JENIS'] == "Stabilo" and ini['PER'] == "lusin":
                    b = int(ini['STOK'])
                if ini['PRODUK'] == "Penghapus" and ini['JENIS'] == "Staedler" and ini['PER'] == "lusin":
                    c = int(ini['STOK'])
            if pengh == '0':
                daftar_produk(dafbel,total)
                break
            elif pengh == '1':
                clear_screen()
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                      DAFTAR PRODUK                    |")
                print("|_______________________________________________________|")
                print("| [1] Penghapus                                         |")
                print("| [2] Pulpen                                            |")
                print("| [3] Tip-Ex                                            |")
                print("| [4] Lem                                               |")
                print("| [5] Buku                                              |")
                print("| [6] Cover                                             |")
                print("| [7] Menu Customer & Daftar Belanja                    |")
                print("| [0] Logout                                            |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih menu atau produk        > 1                     |")
                print("|_______________________________________________________|")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|               Jenis Penghapus FaberCastell            |")
                print("|_______________________________________________________|")
                if a == 0:
                    print("| [1] Grosir : Rp.14000/lusin  -Stok Tidak Tersedia-    |")
                    print("| [2] Eceran : Rp.550 /unit    -Stok Tidak Tersedia-    |")
                else:
                    print("| [1] Grosir : Rp.14000/lusin  Tersisa: %d\tLusin   |"%int(a/12))
                    print("| [2] Eceran : Rp.550 /unit    Tersisa: %s\tUnit    |"%a)
                print("| [0] Kembali                                           |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih jenis Penghapus         > 1                     |")
                opsi = input(str("| Pilih opsi pembelian          > "))
                if opsi == '0':
                    breakpoint
                    END = False
                elif opsi == '1':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak*12 > a:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                apus = int(berapa(penghapus[0][2]))
                                total = int(total0(apus))
                                baru = ("| Penghapus "+penghapus[0][1]+" ; %d lusin \tRp.%d \t|"%(banyak,apus))
                                dafbel.append(baru)
                                banyak = banyak*12
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                elif opsi == '2':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak > a:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                apus = int(berapa(penghapus[0][3]))
                                total = int(total0(apus))
                                if banyak == 1:
                                    baru = ("| Penghapus "+penghapus[0][1]+" ; %d unit  \tRp.%d \t\t|"%(banyak,apus))
                                else:
                                    baru = ("| Penghapus "+penghapus[0][1]+" ; %d unit  \tRp.%d \t|"%(banyak,apus))
                                dafbel.append(baru)
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                else:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________")
                    print("| Error:                                                |")
                    print("| Opsi yang anda masukkan tidak ada dalam pilihan!      |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    breakpoint
                    END = False
                if END == True:
                    i=0
                    for ini in temp_produk:
                        if ini['PRODUK'] == "Penghapus" and ini['JENIS'] == "FaberCastell":
                            temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                        i+=1
                    break
            elif pengh == '2':
                clear_screen()
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                      DAFTAR PRODUK                    |")
                print("|_______________________________________________________|")
                print("| [1] Penghapus                                         |")
                print("| [2] Pulpen                                            |")
                print("| [3] Tip-Ex                                            |")
                print("| [4] Lem                                               |")
                print("| [5] Buku                                              |")
                print("| [6] Cover                                             |")
                print("| [7] Menu Customer & Daftar Belanja                    |")
                print("| [0] Logout                                            |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih menu atau produk        > 1                     |")
                print("|_______________________________________________________|")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                 Jenis Penghapus Stabilo               |")
                print("|_______________________________________________________|")
                if b == 0:
                    print("| [1] Grosir : Rp.16000/lusin  -Stok Tidak Tersedia-    |")
                    print("| [2] Eceran : Rp.500 /unit    -Stok Tidak Tersedia-    |")
                else:
                    print("| [1] Grosir : Rp.16000/lusin  Tersisa: %d\tLusin   |"%int(b/12))
                    print("| [2] Eceran : Rp.500 /unit    Tersisa: %s\tUnit    |"%b)
                print("| [0] Kembali                                           |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih jenis Penghapus         > 2                     |")
                opsi = input(str("| Pilih opsi pembelian          > "))
                if opsi == '0':
                    breakpoint
                    END = False
                elif opsi == '1':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak*12 > b:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                apus = int(berapa(penghapus[1][2]))
                                total = int(total0(apus))
                                baru = ("| Penghapus "+penghapus[1][1]+"\t ; %d lusin \tRp.%d \t|"%(banyak,apus))
                                dafbel.append(baru)
                                banyak = banyak*12
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                elif opsi == '2':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak > b:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                apus = int(berapa(penghapus[1][3]))
                                total = int(total0(apus))
                                if banyak == 1:
                                    baru = ("| Penghapus "+penghapus[1][1]+"\t ; %d unit  \tRp.%d \t\t|"%(banyak,apus))
                                else:
                                    baru = ("| Penghapus "+penghapus[1][1]+"\t ; %d unit  \tRp.%d \t|"%(banyak,apus))
                                dafbel.append(baru)
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                else:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________")
                    print("| Error:                                                |")
                    print("| Opsi yang anda masukkan tidak ada dalam pilihan!      |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    breakpoint
                    END = False
                if END == True:
                    i=0
                    for ini in temp_produk:
                        if ini['PRODUK'] == "Penghapus" and ini['JENIS'] == "Stabilo":
                            temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                        i+=1
                    break
            elif pengh == '3':
                clear_screen()
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                      DAFTAR PRODUK                    |")
                print("|_______________________________________________________|")
                print("| [1] Penghapus                                         |")
                print("| [2] Pulpen                                            |")
                print("| [3] Tip-Ex                                            |")
                print("| [4] Lem                                               |")
                print("| [5] Buku                                              |")
                print("| [6] Cover                                             |")
                print("| [7] Menu Customer & Daftar Belanja                    |")
                print("| [0] Logout                                            |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih menu atau produk        > 1                     |")
                print("|_______________________________________________________|")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                Jenis Penghapus Staedler               |")
                print("|_______________________________________________________|")
                if c == 0:
                    print("| [1] Grosir : Rp.18000/lusin  -Stok Tidak Tersedia-    |")
                    print("| [2] Eceran : Rp.800 /unit    -Stok Tidak Tersedia-    |")
                else:
                    print("| [1] Grosir : Rp.18000/lusin  Tersisa: %d\tLusin   |"%int(c/12))
                    print("| [2] Eceran : Rp.800 /unit    Tersisa: %s\tUnit    |"%c)
                print("| [0] Kembali                                           |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih jenis Penghapus         > 3                     |")
                opsi = input(str("| Pilih opsi pembelian          > "))
                if opsi == '0':
                    breakpoint
                    END = False
                elif opsi == '1':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak*12 > c:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                apus = int(berapa(penghapus[2][2]))
                                total = int(total0(apus))
                                baru = ("| Penghapus "+penghapus[2][1]+"\t ; %d lusin \tRp.%d \t|"%(banyak,apus))
                                dafbel.append(baru)
                                banyak = banyak*12
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                elif opsi == '2':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak > c:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                apus = int(berapa(penghapus[2][3]))
                                total = int(total0(apus))
                                if banyak == 1:
                                    baru = ("| Penghapus "+penghapus[2][1]+"\t ; %d unit  \tRp.%d \t\t|"%(banyak,apus))
                                else:
                                    baru = ("| Penghapus "+penghapus[2][1]+"\t ; %d unit  \tRp.%d \t|"%(banyak,apus))
                                dafbel.append(baru)
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                else:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________")
                    print("| Error:                                                |")
                    print("| Opsi yang anda masukkan tidak ada dalam pilihan!      |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    breakpoint
                    END = False
                if END == True:
                    i=0
                    for ini in temp_produk:
                        if ini['PRODUK'] == "Penghapus" and ini['JENIS'] == "Staedler":
                            temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                        i+=1
                    break
            else:
                print("\n _______________________________________________________")
                print("| Error:                                                |")
                print("| Input yang anda masukkan tidak valid!                 |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                breakpoint
                END = False
        if END == True:
            try:
                with open('daftar_produk.csv', 'w') as csv_write:
                    kolom = ['PRODUK','JENIS','HARGA','PER','STOK']
                    tulis = csv.DictWriter(csv_write, fieldnames=kolom)
                    tulis.writeheader()
                    for ini in temp_produk:
                        tulis.writerow({'PRODUK': ini['PRODUK'], 'JENIS': ini['JENIS'], 'HARGA': ini['HARGA'], 'PER': ini['PER'], 'STOK': ini['STOK']})
            except PermissionError:
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Harap menutup file Excel terlebih dahulu!             |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk(dafbel, total)
            print("\n _______________________________________________________")
            print("| Sukses:                                               |")
            print("| Produk ditambahkan ke daftar belanja anda!            |")
            print("|                                                       |")
            print("| Tekan enter untuk melanjutkan...                      |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            daftar_produk(dafbel, total)
    #PULPEN
    elif daftar == "2":
        while True:
            clear_screen()
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                      DAFTAR PRODUK                    |")
            print("|_______________________________________________________|")
            print("| [1] Penghapus                                         |")
            print("| [2] Pulpen                                            |")
            print("| [3] Tip-Ex                                            |")
            print("| [4] Lem                                               |")
            print("| [5] Buku                                              |")
            print("| [6] Cover                                             |")
            print("| [7] Menu Customer & Daftar Belanja                    |")
            print("| [0] Logout                                            |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("| Pilih menu atau produk        > 2                     |")
            print("|_______________________________________________________|")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                      Jenis Pulpen                     |")
            print("|_______________________________________________________|")
            print("| [1] Gel Umum                                          |")
            print("| [2] Standard                                          |")
            print("| [3] Pilot                                             |")
            print("| [0] Kembali                                           |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            pul = input(str("| Pilih jenis Pulpen            > "))
            print("|_______________________________________________________|")
            for ini in temp_produk:
                if ini['PRODUK'] == "Pulpen" and ini['JENIS'] == "Gel Umum" and ini['PER'] == "lusin":
                    a = int(ini['STOK'])
                if ini['PRODUK'] == "Pulpen" and ini['JENIS'] == "Standard" and ini['PER'] == "lusin":
                    b = int(ini['STOK'])
                if ini['PRODUK'] == "Pulpen" and ini['JENIS'] == "Pilot" and ini['PER'] == "lusin":
                    c = int(ini['STOK'])
            if pul == '0':
                daftar_produk(dafbel, total)
                break
            elif pul == '1':
                clear_screen()
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                      DAFTAR PRODUK                    |")
                print("|_______________________________________________________|")
                print("| [1] Penghapus                                         |")
                print("| [2] Pulpen                                            |")
                print("| [3] Tip-Ex                                            |")
                print("| [4] Lem                                               |")
                print("| [5] Buku                                              |")
                print("| [6] Cover                                             |")
                print("| [7] Menu Customer & Daftar Belanja                    |")
                print("| [0] Logout                                            |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih menu atau produk        > 2                     |")
                print("|_______________________________________________________|")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                  Jenis Pulpen Gel Umum                |")
                print("|_______________________________________________________|")
                if a == 0:
                    print("| [1] Grosir : Rp.22000/lusin  -Stok Tidak Tersedia-    |")
                    print("| [2] Eceran : Rp.2000/unit    -Stok Tidak Tersedia-    |")
                else:
                    print("| [1] Grosir : Rp.22000/lusin  Tersisa: %d\tLusin   |"%int(a/12))
                    print("| [2] Eceran : Rp.2000/unit    Tersisa: %s\tUnit    |"%a)
                print("| [0] Kembali                                           |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih jenis Pulpen            > 1                     |")
                opsi = input(str("| Pilih opsi pembelian          > "))
                if opsi == '0':
                    breakpoint
                    END = False
                elif opsi == '1':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak*12 > a:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                pen = int(berapa(pulpen[0][2]))
                                total = int(total0(pen))
                                baru = ("| Pulpen "+pulpen[0][1]+"\t ; %d lusin \tRp.%d \t|"%(banyak,pen))
                                dafbel.append(baru)
                                banyak = banyak*12
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                elif opsi == '2':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak > a:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                pen = int(berapa(pulpen[0][3]))
                                total = int(total0(pen))
                                baru = ("| Pulpen "+pulpen[0][1]+"\t ; %d unit  \tRp.%d \t|"%(banyak,pen))
                                dafbel.append(baru)
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                else:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________")
                    print("| Error:                                                |")
                    print("| Opsi yang anda masukkan tidak ada dalam pilihan!      |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    breakpoint
                    END = False
                if END == True:
                    i=0
                    for ini in temp_produk:
                        if ini['PRODUK'] == "Pulpen" and ini['JENIS'] == "Gel Umum":
                            temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                        i+=1
                    break
            elif pul == '2':
                clear_screen()
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                      DAFTAR PRODUK                    |")
                print("|_______________________________________________________|")
                print("| [1] Penghapus                                         |")
                print("| [2] Pulpen                                            |")
                print("| [3] Tip-Ex                                            |")
                print("| [4] Lem                                               |")
                print("| [5] Buku                                              |")
                print("| [6] Cover                                             |")
                print("| [7] Menu Customer & Daftar Belanja                    |")
                print("| [0] Logout                                            |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih menu atau produk        > 2                     |")
                print("|_______________________________________________________|")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                  Jenis Pulpen Standard                |")
                print("|_______________________________________________________|")
                if b == 0:
                    print("| [1] Grosir : Rp.20000/lusin  -Stok Tidak Tersedia-    |")
                    print("| [2] Eceran : Rp.1500 /unit   -Stok Tidak Tersedia-    |")
                else:
                    print("| [1] Grosir : Rp.20000/lusin  Tersisa: %d\tLusin   |"%int(b/12))
                    print("| [2] Eceran : Rp.1500/unit    Tersisa: %s\tUnit    |"%b)
                print("| [0] Kembali                                           |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih jenis Pulpen            > 2                     |")
                opsi = input(str("| Pilih opsi pembelian          > "))
                if opsi == '0':
                    breakpoint
                    END = False
                elif opsi == '1':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak*12 > b:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                pen = int(berapa(pulpen[1][2]))
                                total = int(total0(pen))
                                baru = ("| Pulpen "+pulpen[1][1]+"\t ; %d lusin \tRp.%d \t|"%(banyak,pen))
                                dafbel.append(baru)
                                banyak = banyak*12
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                elif opsi == '2':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak > b:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                pen = int(berapa(pulpen[1][3]))
                                total = int(total0(pen))
                                baru = ("| Pulpen "+pulpen[1][1]+"\t ; %d unit  \tRp.%d \t|"%(banyak,pen))
                                dafbel.append(baru)
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                else:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________")
                    print("| Error:                                                |")
                    print("| Opsi yang anda masukkan tidak ada dalam pilihan!      |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    breakpoint
                    END = False
                if END == True:
                    i=0
                    for ini in temp_produk:
                        if ini['PRODUK'] == "Pulpen" and ini['JENIS'] == "Standard":
                            temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                        i+=1
                    break
            elif pul == '3':
                clear_screen()
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                      DAFTAR PRODUK                    |")
                print("|_______________________________________________________|")
                print("| [1] Penghapus                                         |")
                print("| [2] Pulpen                                            |")
                print("| [3] Tip-Ex                                            |")
                print("| [4] Lem                                               |")
                print("| [5] Buku                                              |")
                print("| [6] Cover                                             |")
                print("| [7] Menu Customer & Daftar Belanja                    |")
                print("| [0] Logout                                            |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih menu atau produk        > 2                     |")
                print("|_______________________________________________________|")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                   Jenis Pulpen Pilot                  |")
                print("|_______________________________________________________|")
                if c == 0:
                    print("| [1] Grosir : Rp.25000/lusin  -Stok Tidak Tersedia-    |")
                    print("| [2] Eceran : Rp.3000/unit    -Stok Tidak Tersedia-    |")
                else:
                    print("| [1] Grosir : Rp.25000/lusin  Tersisa: %d\tLusin   |"%int(c/12))
                    print("| [2] Eceran : Rp.3000/unit    Tersisa: %s\tUnit    |"%c)
                print("| [0] Kembali                                           |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih jenis Pulpen            > 3                     |")
                opsi = input(str("| Pilih opsi pembelian          > "))
                if opsi == '0':
                    breakpoint
                    END = False
                elif opsi == '1':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak*12 > c:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                pen = int(berapa(pulpen[2][2]))
                                total = int(total0(pen))
                                baru = ("| Pulpen "+pulpen[2][1]+"\t\t ; %d lusin \tRp.%d \t|"%(banyak,pen))
                                dafbel.append(baru)
                                banyak = banyak*12
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                elif opsi == '2':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak > c:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                pen = int(berapa(pulpen[2][3]))
                                total = int(total0(pen))
                                baru = ("| Pulpen "+pulpen[2][1]+"\t\t ; %d unit  \tRp.%d \t|"%(banyak,pen))
                                dafbel.append(baru)
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                else:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________")
                    print("| Error:                                                |")
                    print("| Opsi yang anda masukkan tidak ada dalam pilihan!      |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    breakpoint
                    END = False
                if END == True:
                    i=0
                    for ini in temp_produk:
                        if ini['PRODUK'] == "Pulpen" and ini['JENIS'] == "Pilot":
                            temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                        i+=1
                    break
            else:
                print("\n _______________________________________________________")
                print("| Error:                                                |")
                print("| Input yang anda masukkan tidak valid!                 |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                breakpoint
                END = False
        if END == True:
            try:
                with open('daftar_produk.csv', 'w') as csv_write:
                    kolom = ['PRODUK','JENIS','HARGA','PER','STOK']
                    tulis = csv.DictWriter(csv_write, fieldnames=kolom)
                    tulis.writeheader()
                    for ini in temp_produk:
                        tulis.writerow({'PRODUK': ini['PRODUK'], 'JENIS': ini['JENIS'], 'HARGA': ini['HARGA'], 'PER': ini['PER'], 'STOK': ini['STOK']})
            except PermissionError:
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Harap menutup file Excel terlebih dahulu!             |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk(dafbel, total)
            print("\n _______________________________________________________")
            print("| Sukses:                                               |")
            print("| Produk ditambahkan ke daftar belanja anda!            |")
            print("|                                                       |")
            print("| Tekan enter untuk melanjutkan...                      |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            daftar_produk(dafbel, total)
    #TIPEX
    elif daftar == "3":
        while True:
            clear_screen()
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                      DAFTAR PRODUK                    |")
            print("|_______________________________________________________|")
            print("| [1] Penghapus                                         |")
            print("| [2] Pulpen                                            |")
            print("| [3] Tip-Ex                                            |")
            print("| [4] Lem                                               |")
            print("| [5] Buku                                              |")
            print("| [6] Cover                                             |")
            print("| [7] Menu Customer & Daftar Belanja                    |")
            print("| [0] Logout                                            |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("| Pilih menu atau produk        > 3                     |")
            print("|_______________________________________________________|")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                      Jenis Tip-Ex                     |")
            print("|_______________________________________________________|")
            print("| [1] Tip-Ex Cair                                       |")
            print("| [2] Tip-Ex Kertas                                     |")
            print("| [0] Kembali                                           |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            tip = input(str("| Pilih jenis TipEx             > "))
            print("|_______________________________________________________|")
            for ini in temp_produk:
                if ini['PRODUK'] == "Tip-Ex" and ini['JENIS'] == "Cair" and ini['PER'] == "lusin":
                    a = int(ini['STOK'])
                if ini['PRODUK'] == "Tip-Ex" and ini['JENIS'] == "Kertas" and ini['PER'] == "lusin":
                    b = int(ini['STOK'])
            if tip == '0':
                daftar_produk(dafbel, total)
                break
            elif tip == '1':
                clear_screen()
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                      DAFTAR PRODUK                    |")
                print("|_______________________________________________________|")
                print("| [1] Penghapus                                         |")
                print("| [2] Pulpen                                            |")
                print("| [3] Tip-Ex                                            |")
                print("| [4] Lem                                               |")
                print("| [5] Buku                                              |")
                print("| [6] Cover                                             |")
                print("| [7] Menu Customer & Daftar Belanja                    |")
                print("| [0] Logout                                            |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih menu atau produk        > 3                     |")
                print("|_______________________________________________________|")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                   Jenis Tip-Ex Cair                   |")
                print("|_______________________________________________________|")
                if a == 0:
                    print("| [1] Grosir : Rp.65000/lusin  -Stok Tidak Tersedia-    |")
                    print("| [2] Eceran : Rp.5000/unit    -Stok Tidak Tersedia-    |")
                else:
                    print("| [1] Grosir : Rp.65000/lusin  Tersisa: %d\tLusin   |"%int(a/12))
                    print("| [2] Eceran : Rp.5000/unit    Tersisa: %s\tUnit    |"%a)
                print("| [0] Kembali                                           |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih jenis Tip-Ex            > 1                     |")
                opsi = input(str("| Pilih opsi pembelian          > "))
                if opsi == '0':
                    breakpoint
                    END = False
                elif opsi == '1':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak*12 > a:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                ex = int(berapa(tipex[0][2]))
                                total = int(total0(ex))
                                baru = ("| "+tipex[0][1]+" Joyko\t ; %d lusin \tRp.%d \t|"%(banyak,ex))
                                dafbel.append(baru)
                                banyak = banyak*12
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                elif opsi == '2':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak > a:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                ex = int(berapa(tipex[0][3]))
                                total = int(total0(ex))
                                baru = ("| "+tipex[0][1]+" Joyko\t ; %d unit  \tRp.%d \t|"%(banyak,ex))
                                dafbel.append(baru)
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                else:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________")
                    print("| Error:                                                |")
                    print("| Opsi yang anda masukkan tidak ada dalam pilihan!      |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    breakpoint
                    END = False
                if END == True:
                    i=0
                    for ini in temp_produk:
                        if ini['PRODUK'] == "Tip-Ex" and ini['JENIS'] == "Cair":
                            temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                        i+=1
                    break
            elif tip == '2':
                clear_screen()
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                      DAFTAR PRODUK                    |")
                print("|_______________________________________________________|")
                print("| [1] Penghapus                                         |")
                print("| [2] Pulpen                                            |")
                print("| [3] Tip-Ex                                            |")
                print("| [4] Lem                                               |")
                print("| [5] Buku                                              |")
                print("| [6] Cover                                             |")
                print("| [7] Menu Customer & Daftar Belanja                    |")
                print("| [0] Logout                                            |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih menu atau produk        > 3                     |")
                print("|_______________________________________________________|")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                  Jenis Tip-Ex Kertas                  |")
                print("|_______________________________________________________|")
                if b == 0:
                    print("| [1] Grosir : Rp.75000/lusin  -Stok Tidak Tersedia-    |")
                    print("| [2] Eceran : Rp.12000 /unit  -Stok Tidak Tersedia-    |")
                else:
                    print("| [1] Grosir : Rp.75000/lusin  Tersisa: %d\tLusin   |"%int(b/12))
                    print("| [2] Eceran : Rp.12000/unit   Tersisa: %s\tUnit    |"%b)
                print("| [0] Kembali                                           |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih jenis Tip-Ex            > 2                     |")
                opsi = input(str("| Pilih opsi pembelian          > "))
                if opsi == '0':
                    breakpoint
                    END = False
                elif opsi == '1':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak*12 > b:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                ex = int(berapa(tipex[1][2]))
                                total = int(total0(ex))
                                baru = ("| "+tipex[1][1]+" Joyko\t ; %d lusin \tRp.%d \t|"%(banyak,ex))
                                dafbel.append(baru)
                                banyak = banyak*12
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                elif opsi == '2':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak > b:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                ex = int(berapa(tipex[1][3]))
                                total = int(total0(ex))
                                baru = ("| "+tipex[1][1]+" Joyko\t ; %d unit  \tRp.%d \t|"%(banyak,ex))
                                dafbel.append(baru)
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                else:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________")
                    print("| Error:                                                |")
                    print("| Opsi yang anda masukkan tidak ada dalam pilihan!      |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    breakpoint
                    END = False
                if END == True:
                    i=0
                    for ini in temp_produk:
                        if ini['PRODUK'] == "Tip-Ex" and ini['JENIS'] == "Kertas":
                            temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                        i+=1
                    break
            else:
                print("\n _______________________________________________________")
                print("| Error:                                                |")
                print("| Input yang anda masukkan tidak valid!                 |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                breakpoint
                END = False
        if END == True:
            try:
                with open('daftar_produk.csv', 'w') as csv_write:
                    kolom = ['PRODUK','JENIS','HARGA','PER','STOK']
                    tulis = csv.DictWriter(csv_write, fieldnames=kolom)
                    tulis.writeheader()
                    for ini in temp_produk:
                        tulis.writerow({'PRODUK': ini['PRODUK'], 'JENIS': ini['JENIS'], 'HARGA': ini['HARGA'], 'PER': ini['PER'], 'STOK': ini['STOK']})
            except PermissionError:
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Harap menutup file Excel terlebih dahulu!             |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk(dafbel, total)
            print("\n _______________________________________________________")
            print("| Sukses:                                               |")
            print("| Produk ditambahkan ke daftar belanja anda!            |")
            print("|                                                       |")
            print("| Tekan enter untuk melanjutkan...                      |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            daftar_produk(dafbel, total)
    #LEM
    elif daftar == "4":
        while True:
            clear_screen()
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                      DAFTAR PRODUK                    |")
            print("|_______________________________________________________|")
            print("| [1] Penghapus                                         |")
            print("| [2] Pulpen                                            |")
            print("| [3] Tip-Ex                                            |")
            print("| [4] Lem                                               |")
            print("| [5] Buku                                              |")
            print("| [6] Cover                                             |")
            print("| [7] Menu Customer & Daftar Belanja                    |")
            print("| [0] Logout                                            |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("| Pilih menu atau produk        > 4                     |")
            print("|_______________________________________________________|")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                       Jenis Lem                       |")
            print("|_______________________________________________________|")
            print("| [1] Lem Fox                                           |")
            print("| [2] Lem Kertas                                        |")
            print("| [3] Lem Korea                                         |")
            print("| [0] Kembali                                           |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            el = input(str("| Pilih jenis Lem               > "))
            print("|_______________________________________________________|")
            for ini in temp_produk:
                if ini['PRODUK'] == "Lem" and ini['JENIS'] == "Fox" and ini['PER'] == "lusin":
                    a = int(ini['STOK'])
                if ini['PRODUK'] == "Lem" and ini['JENIS'] == "Kertas" and ini['PER'] == "lusin":
                    b = int(ini['STOK'])
                if ini['PRODUK'] == "Lem" and ini['JENIS'] == "Korea" and ini['PER'] == "lusin":
                    c = int(ini['STOK'])
            if el == '0':
                daftar_produk(dafbel, total)
                break
            elif el == '1':
                clear_screen()
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                      DAFTAR PRODUK                    |")
                print("|_______________________________________________________|")
                print("| [1] Penghapus                                         |")
                print("| [2] Pulpen                                            |")
                print("| [3] Tip-Ex                                            |")
                print("| [4] Lem                                               |")
                print("| [5] Buku                                              |")
                print("| [6] Cover                                             |")
                print("| [7] Menu Customer & Daftar Belanja                    |")
                print("| [0] Logout                                            |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih menu atau produk        > 4                     |")
                print("|_______________________________________________________|")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                     Jenis Lem Fox                     |")
                print("|_______________________________________________________|")
                if a == 0:
                    print("| [1] Grosir : Rp.100000/lusin -Stok Tidak Tersedia-    |")
                    print("| [2] Eceran : Rp.35000/unit   -Stok Tidak Tersedia-    |")
                else:
                    print("| [1] Grosir : Rp.100000/lusin Tersisa: %d\tLusin   |"%int(a/12))
                    print("| [2] Eceran : Rp.35000/unit   Tersisa: %s\tUnit    |"%a)
                print("| [0] Kembali                                           |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih jenis Lem               > 1                     |")
                opsi = input(str("| Pilih opsi pembelian          > "))
                if opsi == '0':
                    breakpoint
                    END = False
                elif opsi == '1':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak*12 > a:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                em = int(berapa(lem[0][2]))
                                total = int(total0(em))
                                baru = ("| "+lem[0][1]+" Kaleng\t ; %d lusin \tRp.%d \t|"%(banyak,em))
                                dafbel.append(baru)
                                banyak = banyak*12
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                elif opsi == '2':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak > a:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                em = int(berapa(lem[0][3]))
                                total = int(total0(em))
                                baru = ("| "+lem[0][1]+" Kaleng\t ; %d unit \tRp.%d \t|"%(banyak,em))
                                dafbel.append(baru)
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                else:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________")
                    print("| Error:                                                |")
                    print("| Opsi yang anda masukkan tidak ada dalam pilihan!      |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    breakpoint
                    END = False
                if END == True:
                    i=0
                    for ini in temp_produk:
                        if ini['PRODUK'] == "Lem" and ini['JENIS'] == "Fox":
                            temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                        i+=1
                    break
            elif el == '2':
                clear_screen()
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                      DAFTAR PRODUK                    |")
                print("|_______________________________________________________|")
                print("| [1] Penghapus                                         |")
                print("| [2] Pulpen                                            |")
                print("| [3] Tip-Ex                                            |")
                print("| [4] Lem                                               |")
                print("| [5] Buku                                              |")
                print("| [6] Cover                                             |")
                print("| [7] Menu Customer & Daftar Belanja                    |")
                print("| [0] Logout                                            |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih menu atau produk        > 4                     |")
                print("|_______________________________________________________|")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                    Jenis Lem Kertas                   |")
                print("|_______________________________________________________|")
                if b == 0:
                    print("| [1] Grosir : Rp.40000/lusin  -Stok Tidak Tersedia-    |")
                    print("| [2] Eceran : Rp.2000 /unit   -Stok Tidak Tersedia-    |")
                else:
                    print("| [1] Grosir : Rp.40000/lusin  Tersisa: %d\tLusin   |"%int(b/12))
                    print("| [2] Eceran : Rp.2000 /unit   Tersisa: %s\tUnit    |"%b)
                print("| [0] Kembali                                           |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih jenis Lem               > 2                     |")
                opsi = input(str("| Pilih opsi pembelian          > "))
                if opsi == '0':
                    breakpoint
                    END = False
                elif opsi == '1':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak*12 > b:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                em = int(berapa(lem[1][2]))
                                total = int(total0(em))
                                baru = ("| "+lem[1][1]+" Joyko\t ; %d lusin \tRp.%d \t|"%(banyak,em))
                                dafbel.append(baru)
                                banyak = banyak*12
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                elif opsi == '2':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak > b:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                em = int(berapa(lem[1][3]))
                                total = int(total0(em))
                                baru = ("| "+lem[1][1]+" Joyko\t ; %d unit \tRp.%d \t|"%(banyak,em))
                                dafbel.append(baru)
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                else:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________")
                    print("| Error:                                                |")
                    print("| Opsi yang anda masukkan tidak ada dalam pilihan!      |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    breakpoint
                    END = False
                if END == True:
                    i=0
                    for ini in temp_produk:
                        if ini['PRODUK'] == "Lem" and ini['JENIS'] == "Kertas":
                            temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                        i+=1
                    break
            elif el == '3':
                clear_screen()
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                      DAFTAR PRODUK                    |")
                print("|_______________________________________________________|")
                print("| [1] Penghapus                                         |")
                print("| [2] Pulpen                                            |")
                print("| [3] Tip-Ex                                            |")
                print("| [4] Lem                                               |")
                print("| [5] Buku                                              |")
                print("| [6] Cover                                             |")
                print("| [7] Menu Customer & Daftar Belanja                    |")
                print("| [0] Logout                                            |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih menu atau produk        > 4                     |")
                print("|_______________________________________________________|")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                    Jenis Lem Korea                    |")
                print("|_______________________________________________________|")
                if c == 0:
                    print("| [1] Grosir : Rp.60000/lusin  -Stok Tidak Tersedia-    |")
                    print("| [2] Eceran : Rp.5000/unit    -Stok Tidak Tersedia-    |")
                else:
                    print("| [1] Grosir : Rp.60000/lusin  Tersisa: %d\tLusin   |"%int(c/12))
                    print("| [2] Eceran : Rp.5000/unit    Tersisa: %s\tUnit    |"%c)
                print("| [0] Kembali                                           |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih jenis Lem               > 3                     |")
                opsi = input(str("| Pilih opsi pembelian          > "))
                if opsi == '0':
                    breakpoint
                    END = False
                elif opsi == '1':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak*12 > c:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                em = int(berapa(lem[2][2]))
                                total = int(total0(em))
                                baru = ("| "+lem[2][1]+" Alteco\t ; %d lusin \tRp.%d \t|"%(banyak,em))
                                dafbel.append(baru)
                                banyak = banyak*12
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                elif opsi == '2':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak > c:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                em = int(berapa(lem[2][3]))
                                total = int(total0(em))
                                baru = ("| "+lem[2][1]+" Alteco\t ; %d unit \tRp.%d \t|"%(banyak,em))
                                dafbel.append(baru)
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                else:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________")
                    print("| Error:                                                |")
                    print("| Opsi yang anda masukkan tidak ada dalam pilihan!      |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    breakpoint
                    END = False
                if END == True:
                    i=0
                    for ini in temp_produk:
                        if ini['PRODUK'] == "Lem" and ini['JENIS'] == "Korea":
                            temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                        i+=1
                    break
            else:
                print("\n _______________________________________________________")
                print("| Error:                                                |")
                print("| Input yang anda masukkan tidak valid!                 |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                breakpoint
                END = False
        if END == True:
            try:
                with open('daftar_produk.csv', 'w') as csv_write:
                    kolom = ['PRODUK','JENIS','HARGA','PER','STOK']
                    tulis = csv.DictWriter(csv_write, fieldnames=kolom)
                    tulis.writeheader()
                    for ini in temp_produk:
                        tulis.writerow({'PRODUK': ini['PRODUK'], 'JENIS': ini['JENIS'], 'HARGA': ini['HARGA'], 'PER': ini['PER'], 'STOK': ini['STOK']})
            except PermissionError:
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Harap menutup file Excel terlebih dahulu!             |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk(dafbel, total)
            print("\n _______________________________________________________")
            print("| Sukses:                                               |")
            print("| Produk ditambahkan ke daftar belanja anda!            |")
            print("|                                                       |")
            print("| Tekan enter untuk melanjutkan...                      |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            daftar_produk(dafbel, total)
    #BUKU
    elif daftar == "5": 
        while True:
            clear_screen()
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                      DAFTAR PRODUK                    |")
            print("|_______________________________________________________|")
            print("| [1] Penghapus                                         |")
            print("| [2] Pulpen                                            |")
            print("| [3] Tip-Ex                                            |")
            print("| [4] Lem                                               |")
            print("| [5] Buku                                              |")
            print("| [6] Cover                                             |")
            print("| [7] Menu Customer & Daftar Belanja                    |")
            print("| [0] Logout                                            |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("| Pilih menu atau produk        > 5                     |")
            print("|_______________________________________________________|")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                       Jenis Buku                      |")
            print("|_______________________________________________________|")
            print("| [1] Buku Bewarna Sidu                                 |")
            print("| [2] Buku Tebal Alstar                                 |")
            print("| [3] Buku Tipis Sidu                                   |")
            print("| [0] Kembali                                           |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            bu = input(str("| Pilih jenis Buku              > "))
            print("|_______________________________________________________|")
            for ini in temp_produk:
                if ini['PRODUK'] == "Buku" and ini['JENIS'] == "Bewarna" and ini['PER'] == "lusin":
                    a = int(ini['STOK'])
                if ini['PRODUK'] == "Buku" and ini['JENIS'] == "Tebal" and ini['PER'] == "lusin":
                    b = int(ini['STOK'])
                if ini['PRODUK'] == "Buku" and ini['JENIS'] == "Tipis" and ini['PER'] == "lusin":
                    c = int(ini['STOK'])
            if bu == '0':
                daftar_produk(dafbel, total)
                break
            elif bu == '1':
                clear_screen()
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                      DAFTAR PRODUK                    |")
                print("|_______________________________________________________|")
                print("| [1] Penghapus                                         |")
                print("| [2] Pulpen                                            |")
                print("| [3] Tip-Ex                                            |")
                print("| [4] Lem                                               |")
                print("| [5] Buku                                              |")
                print("| [6] Cover                                             |")
                print("| [7] Menu Customer & Daftar Belanja                    |")
                print("| [0] Logout                                            |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih menu atau produk        > 5                     |")
                print("|_______________________________________________________|")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                 Jenis Buku Bewarna Sidu               |")
                print("|_______________________________________________________|")
                if a == 0:
                    print("| [1] Grosir : Rp.20000/lusin  -Stok Tidak Tersedia-    |")
                    print("| [2] Eceran : Rp.3000/unit    -Stok Tidak Tersedia-    |")
                else:
                    print("| [1] Grosir : Rp.20000/lusin  Tersisa: %d\tLusin   |"%int(a/12))
                    print("| [2] Eceran : Rp.3000/unit    Tersisa: %d\tUnit    |"%a)
                print("| [0] Kembali                                           |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih jenis Buku              > 1                     |")
                opsi = input(str("| Pilih opsi pembelian          > "))
                if opsi == '0':
                    breakpoint
                    END = False
                elif opsi == '1':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak*12 > a:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                ku =int(berapa(buku[0][2]))
                                total = int(total0(ku))
                                baru = ("| Buku "+buku[0][1]+"\t ; %d lusin \tRp.%d \t|"%(banyak,ku))
                                dafbel.append(baru)
                                banyak = banyak*12
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                elif opsi == '2':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak > a:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                ku =int(berapa(buku[0][3]))
                                total = int(total0(ku))
                                baru = ("| Buku "+buku[0][1]+"\t ; %d unit \tRp.%d \t|"%(banyak,ku))
                                dafbel.append(baru)
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                else:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________")
                    print("| Error:                                                |")
                    print("| Opsi yang anda masukkan tidak ada dalam pilihan!      |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    breakpoint
                    END = False
                if END == True:
                    i=0
                    for ini in temp_produk:
                        if ini['PRODUK'] == "Buku" and ini['JENIS'] == "Bewarna":
                            temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                        i+=1
                    break
            elif bu == '2':
                clear_screen()
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                      DAFTAR PRODUK                    |")
                print("|_______________________________________________________|")
                print("| [1] Penghapus                                         |")
                print("| [2] Pulpen                                            |")
                print("| [3] Tip-Ex                                            |")
                print("| [4] Lem                                               |")
                print("| [5] Buku                                              |")
                print("| [6] Cover                                             |")
                print("| [7] Menu Customer & Daftar Belanja                    |")
                print("| [0] Logout                                            |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih menu atau produk        > 5                     |")
                print("|_______________________________________________________|")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                 Jenis Buku Tebal Alstar               |")
                print("|_______________________________________________________|")
                if b == 0:
                    print("| [1] Grosir : Rp.15000/lusin  -Stok Tidak Tersedia-    |")
                    print("| [2] Eceran : Rp.2300/unit    -Stok Tidak Tersedia-    |")
                else:
                    print("| [1] Grosir : Rp.15000/lusin  Tersisa: %d\tLusin   |"%int(b/12))
                    print("| [2] Eceran : Rp.2300/unit    Tersisa: %s\tUnit    |"%b)
                print("| [0] Kembali                                           |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih jenis Buku              > 2                     |")
                opsi = input(str("| Pilih opsi pembelian          > "))
                if opsi == '0':
                    breakpoint
                    END = False
                elif opsi == '1':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak*12 > b:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                ku =int(berapa(buku[1][2]))
                                total = int(total0(ku))
                                baru = ("| Buku "+buku[1][1]+"\t ; %d lusin \tRp.%d \t|"%(banyak,ku))
                                dafbel.append(baru)
                                banyak = banyak*12
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                elif opsi == '2':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak > b:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                ku =int(berapa(buku[1][3]))
                                total = int(total0(ku))
                                baru = ("| Buku "+buku[1][1]+"\t ; %d unit \tRp.%d \t|"%(banyak,ku))
                                dafbel.append(baru)
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                else:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________")
                    print("| Error:                                                |")
                    print("| Opsi yang anda masukkan tidak ada dalam pilihan!      |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    breakpoint
                    END = False
                if END == True:
                    i=0
                    for ini in temp_produk:
                        if ini['PRODUK'] == "Buku" and ini['JENIS'] == "Tebal":
                            temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                        i+=1
                    break
            elif bu == '3':
                clear_screen()
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                      DAFTAR PRODUK                    |")
                print("|_______________________________________________________|")
                print("| [1] Penghapus                                         |")
                print("| [2] Pulpen                                            |")
                print("| [3] Tip-Ex                                            |")
                print("| [4] Lem                                               |")
                print("| [5] Buku                                              |")
                print("| [6] Cover                                             |")
                print("| [7] Menu Customer & Daftar Belanja                    |")
                print("| [0] Logout                                            |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih menu atau produk        > 5                     |")
                print("|_______________________________________________________|")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                 Jenis Buku Tipis Sidu                 |")
                print("|_______________________________________________________|")
                if c == 0:
                    print("| [1] Grosir : Rp.15000/lusin  -Stok Tidak Tersedia-    |")
                    print("| [2] Eceran : Rp.2500/unit    -Stok Tidak Tersedia-    |")
                else:
                    print("| [1] Grosir : Rp.15000/lusin  Tersisa: %d\tLusin   |"%int(c/12))
                    print("| [2] Eceran : Rp.2500/unit    Tersisa: %s\tUnit    |"%c)
                print("| [0] Kembali                                           |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih jenis Buku              > 2                     |")
                opsi = input(str("| Pilih opsi pembelian          > "))
                if opsi == '0':
                    breakpoint
                    END = False
                elif opsi == '1':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak*12 > c:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                ku =int(berapa(buku[2][2]))
                                total = int(total0(ku))
                                baru = ("| Buku "+buku[2][1]+"\t ; %d lusin \tRp.%d \t|"%(banyak,ku))
                                dafbel.append(baru)
                                banyak = banyak*12
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                elif opsi == '2':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak > c:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                ku =int(berapa(buku[2][3]))
                                total = int(total0(ku))
                                baru = ("| Buku "+buku[2][1]+"\t ; %d unit \tRp.%d \t|"%(banyak,ku))
                                dafbel.append(baru)
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                else:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________")
                    print("| Error:                                                |")
                    print("| Opsi yang anda masukkan tidak ada dalam pilihan!      |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    breakpoint
                    END = False
                if END == True:
                    i=0
                    for ini in temp_produk:
                        if ini['PRODUK'] == "Buku" and ini['JENIS'] == "Tipis":
                            temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                        i+=1
                    break
            else:
                print("\n _______________________________________________________")
                print("| Error:                                                |")
                print("| Input yang anda masukkan tidak valid!                 |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                breakpoint
                END = False
        if END == True:
            try:
                with open('daftar_produk.csv', 'w') as csv_write:
                    kolom = ['PRODUK','JENIS','HARGA','PER','STOK']
                    tulis = csv.DictWriter(csv_write, fieldnames=kolom)
                    tulis.writeheader()
                    for ini in temp_produk:
                        tulis.writerow({'PRODUK': ini['PRODUK'], 'JENIS': ini['JENIS'], 'HARGA': ini['HARGA'], 'PER': ini['PER'], 'STOK': ini['STOK']})
            except PermissionError:
                print("|_______________________________________________________|")
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Harap menutup file Excel terlebih dahulu!             |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk(dafbel, total)
            print("\n _______________________________________________________")
            print("| Sukses:                                               |")
            print("| Produk ditambahkan ke daftar belanja anda!            |")
            print("|                                                       |")
            print("| Tekan enter untuk melanjutkan...                      |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            daftar_produk(dafbel, total)
    #COVER
    elif daftar == "6":
        while True:
            clear_screen()
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                      DAFTAR PRODUK                    |")
            print("|_______________________________________________________|")
            print("| [1] Penghapus                                         |")
            print("| [2] Pulpen                                            |")
            print("| [3] Tip-Ex                                            |")
            print("| [4] Lem                                               |")
            print("| [5] Buku                                              |")
            print("| [6] Cover                                             |")
            print("| [7] Menu Customer & Daftar Belanja                    |")
            print("| [0] Logout                                            |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("| Pilih menu atau produk        > 6                     |")
            print("|_______________________________________________________|")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                      Jenis Cover                      |")
            print("|_______________________________________________________|")
            print("| [1] Cover Putih                                       |")
            print("| [2] Cover Bewarna                                     |")
            print("| [0] Kembali                                           |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            cov = input(str("| Pilih jenis Cover             > "))
            print("|_______________________________________________________|")
            for ini in temp_produk:
                if ini['PRODUK'] == "Cover" and ini['JENIS'] == "Putih" and ini['PER'] == "lusin":
                    a = int(ini['STOK'])
                if ini['PRODUK'] == "Cover" and ini['JENIS'] == "Bewarna" and ini['PER'] == "lusin":
                    b = int(ini['STOK'])
            if cov == '0':
                daftar_produk(dafbel, total)
                break
            elif cov == '1':
                clear_screen()
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                      DAFTAR PRODUK                    |")
                print("|_______________________________________________________|")
                print("| [1] Penghapus                                         |")
                print("| [2] Pulpen                                            |")
                print("| [3] Tip-Ex                                            |")
                print("| [4] Lem                                               |")
                print("| [5] Buku                                              |")
                print("| [6] Cover                                             |")
                print("| [7] Menu Customer & Daftar Belanja                    |")
                print("| [0] Logout                                            |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih menu atau produk        > 6                     |")
                print("|_______________________________________________________|")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                   Jenis Cover Putih                   |")
                print("|_______________________________________________________|")
                if a == 0:
                    print("| [1] Grosir : Rp.60000/lusin  -Stok Tidak Tersedia-    |")
                    print("| [2] Eceran : Rp.1000/unit    -Stok Tidak Tersedia-    |")
                else:
                    print("| [1] Grosir : Rp.60000/lusin  Tersisa: %d\tLusin   |"%int(a/12))
                    print("| [2] Eceran : Rp.1000/unit    Tersisa: %s\tUnit    |"%a)
                print("| [0] Kembali                                           |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih jenis Buku              > 1                     |")
                opsi = input(str("| Pilih opsi pembelian          > "))
                if opsi == '0':
                    breakpoint
                    END = False
                elif opsi == '1':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak*12 > a:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                ver = int(berapa(cover[0][2]))
                                total = int(total0(ver))
                                baru = ("| "+cover[0][1]+" Sidu\t ; %d lusin \tRp.%d \t|"%(banyak,ver))
                                dafbel.append(baru)
                                banyak = banyak*12
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                elif opsi == '2':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak > a:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                ver = int(berapa(cover[0][3]))
                                total = int(total0(ver))
                                baru = ("| "+cover[0][1]+" Sidu\t ; %d unit \tRp.%d \t|"%(banyak,ver))
                                dafbel.append(baru)
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                else:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________")
                    print("| Error:                                                |")
                    print("| Opsi yang anda masukkan tidak ada dalam pilihan!      |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    breakpoint
                    END = False
                if END == True:
                    i=0
                    for ini in temp_produk:
                        if ini['PRODUK'] == "Cover" and ini['JENIS'] == "Putih":
                            temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                        i+=1
                    break
            elif cov == '2':
                clear_screen()
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                      DAFTAR PRODUK                    |")
                print("|_______________________________________________________|")
                print("| [1] Penghapus                                         |")
                print("| [2] Pulpen                                            |")
                print("| [3] Tip-Ex                                            |")
                print("| [4] Lem                                               |")
                print("| [5] Buku                                              |")
                print("| [6] Cover                                             |")
                print("| [7] Menu Customer & Daftar Belanja                    |")
                print("| [0] Logout                                            |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih menu atau produk        > 6                     |")
                print("|_______________________________________________________|")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                  Jenis Cover Bewarna                  |")
                print("|_______________________________________________________|")
                if b == 0:
                    print("| [1] Grosir : Rp.80000/lusin  -Stok Tidak Tersedia-    |")
                    print("| [2] Eceran : Rp.2000/unit    -Stok Tidak Tersedia-    |")
                else:
                    print("| [1] Grosir : Rp.80000/lusin  Tersisa: %d\tLusin   |"%int(b/12))
                    print("| [2] Eceran : Rp.2000/unit    Tersisa: %s\tUnit    |"%b)
                print("| [0] Kembali                                           |")
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("| Pilih jenis Buku              > 2                     |")
                opsi = input(str("| Pilih opsi pembelian          > "))
                if opsi == '0':
                    breakpoint
                    END = False
                elif opsi == '1':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak*12 > b:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                ver = int(berapa(cover[0][2]))
                                total = int(total0(ver))
                                baru = ("| "+cover[1][1]+" Sidu\t ; %d lusin \tRp.%d \t|"%(banyak,ver))
                                dafbel.append(baru)
                                banyak = banyak*12
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                elif opsi == '2':
                    try:
                        banyak = int(input("| Masukkan banyak yg diinginkan > "))
                        print("|_______________________________________________________|")
                        if banyak > b:
                            print("\n _______________________________________________________")
                            print("| Error:                                                |")
                            print("| Stok tidak tersedia sebanyak itu!                     |")
                            print("|                                                       |")
                            print("| Tekan enter untuk kembali...                          |")
                            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                            breakpoint
                            END = False
                        else:
                            if banyak == 0:
                                print("\n _______________________________________________________")
                                print("| Error:                                                |")
                                print("| Anda tidak dapat mengosongkan pembelian!              |")
                                print("|                                                       |")
                                print("| Tekan enter untuk kembali...                          |")
                                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                breakpoint
                                END = False
                            else:
                                ver = int(berapa(cover[1][3]))
                                total = int(total0(ver))
                                baru = ("| "+cover[1][1]+" Sidu\t ; %d unit \tRp.%d \t|"%(banyak,ver))
                                dafbel.append(baru)
                                END = True
                    except ValueError:
                        print("|_______________________________________________________|")
                        print("\n _______________________________________________________")
                        print("| Error:                                                |")
                        print("| Anda harusnya menginput angka!                        |")
                        print("|                                                       |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        breakpoint
                        END = False
                else:
                    print("|_______________________________________________________|")
                    print("\n _______________________________________________________")
                    print("| Error:                                                |")
                    print("| Opsi yang anda masukkan tidak ada dalam pilihan!      |")
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    breakpoint
                    END = False
                if END == True:
                    i=0
                    for ini in temp_produk:
                        if ini['PRODUK'] == "Cover" and ini['JENIS'] == "Bewarna":
                            temp_produk[i]['STOK'] = int(stock(int(ini['STOK'])))
                        i+=1
                    break
            else:
                print("\n _______________________________________________________")
                print("| Error:                                                |")
                print("| Input yang anda masukkan tidak valid!                 |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                breakpoint
                END = False
        if END == True:
            try:
                with open('daftar_produk.csv', 'w') as csv_write:
                    kolom = ['PRODUK','JENIS','HARGA','PER','STOK']
                    tulis = csv.DictWriter(csv_write, fieldnames=kolom)
                    tulis.writeheader()
                    for ini in temp_produk:
                        tulis.writerow({'PRODUK': ini['PRODUK'], 'JENIS': ini['JENIS'], 'HARGA': ini['HARGA'], 'PER': ini['PER'], 'STOK': ini['STOK']})
            except PermissionError:
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Harap menutup file Excel terlebih dahulu!             |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                daftar_produk(dafbel, total)
            print("\n _______________________________________________________")
            print("| Sukses:                                               |")
            print("| Produk ditambahkan ke daftar belanja anda!            |")
            print("|                                                       |")
            print("| Tekan enter untuk melanjutkan...                      |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            daftar_produk(dafbel, total)
    elif daftar == "7":
        print("\n _______________________________________________________")
        print("| Sukses:                                               |")
        print("| Anda akan dialihkan ke menu Customer!                 |")
        print("|                                                       |")
        print("| Mengalihkan...                                        |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        time.sleep(1.5)
        menu_customer(dafbel, total)
    else:
        print("\n _______________________________________________________")
        print("| Error:                                                |")
        print("| Input yang anda masukkan tidak valid!                 |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        daftar_produk(dafbel, total)

def menu_customer(dafbel, total):
    clear_screen()
    if dafbel == [] or total == 0:
        print(" _______________________________________________________ ")
        print("|               [Belum Ada Daftar Belanja]              |")
    else:
        print(" _______________________________________________________ ")
        print("|                     Daftar Belanja                    |")
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
        for ini in dafbel:
            print(ini)
        print("|_______________________________________________________|")
        if len(str(total))<10:
            print("| Total Belanjaan = Rp.%d               \t\t|"%total)
        else:
            print("| Total Belanjaan = Rp.%d                 \t|"%total)
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("|                     MENU CUSTOMER                     |")
    print("|_______________________________________________________|")
    print("| [1] Lakukan Pembayaran                                |")
    print("| [2] Edit Daftar Belanja                               |")
    print("| [3] Ubah Pasword Akun                                 |")
    print("| [4] Keluar Program                                    |")
    print("| [0] Kembali                                           |")
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    menu_cust = str(input("| Input menu                  > "))
    if menu_cust == '0':
        print("|_______________________________________________________|")
        print("\n _______________________________________________________")
        print("| Sukses:                                               |")
        print("| Beralih kembali ke Daftar Produk!                     |")
        print("|                                                       |")
        print("| Mengalihkan...                                        |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        time.sleep(1.5)
        daftar_produk(dafbel, total)
    elif menu_cust == '1':
        if dafbel == []:
            print("|_______________________________________________________|")
            print("\n _______________________________________________________")
            print("| Error:                                                |")
            print("| Daftar belanja belum ada, tidak dapat membayar!       |")
            print("|                                                       |")
            print("| Tekan enter untuk kembali...                          |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            menu_customer(dafbel, total)
        try:
            bayar = int(input("| Masukkan uang anda          > Rp."))
            print("|_______________________________________________________|\n")
        except ValueError:
            print("|_______________________________________________________|")
            print("\n _______________________________________________________")
            print("| Error:                                                |")
            print("| Anda harusnya menginput angka!                        |")
            print("|                                                       |")
            print("| Tekan enter untuk kembali...                          |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            menu_customer(dafbel, total)
        if total > bayar:
            print(" _______________________________________________________")
            print("| Error:                                                |")
            print("| Uang anda tidak mencukupi!                            |")
            print("|                                                       |")
            print("| Tekan enter untuk kembali...                          |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            menu_customer(dafbel, total)
        else:
            kembalian = bayar - total
            #Atur Bulan
            saat_ini = datetime.datetime.now()
            if saat_ini.month == 1:
                bulan = "Januari"
                waktu = "%d %s %d %d-%d-%d" % (saat_ini.day,bulan,saat_ini.year,saat_ini.hour,saat_ini.minute,saat_ini.second)
            elif saat_ini.month == 2:
                bulan = "Februari"   
                waktu = "%d %s %d %d-%d-%d" % (saat_ini.day,bulan,saat_ini.year,saat_ini.hour,saat_ini.minute,saat_ini.second)
            elif saat_ini.month == 3:
                bulan = "Maret"   
                waktu = "%d %s %d %d-%d-%d" % (saat_ini.day,bulan,saat_ini.year,saat_ini.hour,saat_ini.minute,saat_ini.second)
            elif saat_ini.month == 4:
                bulan = "April"   
                waktu = "%d %s %d %d-%d-%d" % (saat_ini.day,bulan,saat_ini.year,saat_ini.hour,saat_ini.minute,saat_ini.second)
            elif saat_ini.month == 5:
                bulan = "Mei" 
                waktu = "%d %s %d %d-%d-%d" % (saat_ini.day,bulan,saat_ini.year,saat_ini.hour,saat_ini.minute,saat_ini.second)
            elif saat_ini.month == 6:
                bulan = "Juni"   
                waktu = "%d %s %d %d-%d-%d" % (saat_ini.day,bulan,saat_ini.year,saat_ini.hour,saat_ini.minute,saat_ini.second)
            elif saat_ini.month == 7:
                bulan = "Juli"   
                waktu = "%d %s %d %d-%d-%d" % (saat_ini.day,bulan,saat_ini.year,saat_ini.hour,saat_ini.minute,saat_ini.second)
            elif saat_ini.month == 8:
                bulan = "Agustus"   
                waktu = "%d %s %d %d-%d-%d" % (saat_ini.day,bulan,saat_ini.year,saat_ini.hour,saat_ini.minute,saat_ini.second)
            elif saat_ini.month == 9:
                bulan = "September"
                waktu = "%d %s %d %d-%d-%d" % (saat_ini.day,bulan,saat_ini.year,saat_ini.hour,saat_ini.minute,saat_ini.second)
            elif saat_ini.month == 10:
                bulan = "Oktober"   
                waktu = "%d %s %d %d-%d-%d" % (saat_ini.day,bulan,saat_ini.year,saat_ini.hour,saat_ini.minute,saat_ini.second)
            elif saat_ini.month == 11:
                bulan = "November"   
                waktu = "%d %s %d %d-%d-%d" % (saat_ini.day,bulan,saat_ini.year,saat_ini.hour,saat_ini.minute,saat_ini.second)
            elif saat_ini.month == 12:
                bulan = "Desember"
                waktu = "%d %s %d %d-%d-%d" % (saat_ini.day,bulan,saat_ini.year,saat_ini.hour,saat_ini.minute,saat_ini.second)
            print(",=======================================================,")
            print("|=============== S T R U K   B E L A N J A =============|")
            print("|=======================================================|")
            for ini in dafbel:
                print(ini)
            print("|=======================================================|")
            if bulan == "September":
                print("| Tanggal Pembelian      : %s \t|"%waktu)
            elif len(waktu) <17:
                print("| Tanggal Pembelian      : %s    \t\t|"%waktu)
            else:
                print("| Tanggal Pembelian      : %s    \t|"%waktu)
            if len(akun_data[0]) <9:
                print("| Atas Nama              : %s    \t\t\t|"%akun_data[0])
            elif len(akun_data[0]) <17:
                print("| Atas Nama              : %s    \t\t|"%akun_data[0])
            elif len(akun_data[0]) <25:
                print("| Atas Nama              : %s    \t|"%akun_data[0])
            else:
                print("| Atas Nama              : %s    |"%akun_data[0])
            if len(str(total))<9:
                print("| Tagihan                : Rp.%d \t\t\t|"%total)
            else:
                print("| Tagihan                : Rp.%d \t\t|"%total)
            if len(str(bayar))<9:
                print("| Uang Anda              : Rp.%d \t\t\t|"%bayar)
            else:
                print("| Uang Anda              : Rp.%d \t\t|"%bayar)
            if len(str(bayar))<9:
                print("| Kembalian              : Rp.%d \t\t\t|"%kembalian)
            else:
                print("| Kembalian              : Rp.%d \t\t|"%kembalian)
            print("\=======================================================/")
            time.sleep(1)
            while True:
                print("\n _______________________________________________________")
                print("| Sukses: Daftar belanjaan berhasil dibayar!            |")
                simpen  = str(input("| Simpan struk belanja? (y/t) > "))
                if simpen == 'y' or simpen == 'Y':
                    with open('Struk Daftar Belanjaan ({0}).txt'.format(waktu), 'w', encoding = 'utf-8') as txt_write:
                        txt_write.write(",=======================================================,\n")
                        txt_write.write("|=============== S T R U K   B E L A N J A =============|\n")
                        txt_write.write("|=======================================================|\n")
                        for ini in dafbel:
                            txt_write.write(ini+'\n')
                        txt_write.write("|=======================================================|\n")
                        if bulan == "September":
                            txt_write.write("| Tanggal Pembelian      : %s \t|\n"%waktu)
                        elif len(waktu) <17:
                            txt_write.write("| Tanggal Pembelian      : %s    \t\t|\n"%waktu)
                        else:
                            txt_write.write("| Tanggal Pembelian      : %s    \t|\n"%waktu)
                        if len(akun_data[0]) <9:
                            txt_write.write("| Atas Nama              : %s    \t\t\t|\n"%akun_data[0])
                        elif len(akun_data[0]) <17:
                            txt_write.write("| Atas Nama              : %s    \t\t|\n"%akun_data[0])
                        elif len(akun_data[0]) <25:
                            txt_write.write("| Atas Nama              : %s    \t|\n"%akun_data[0])
                        else:
                            txt_write.write("| Atas Nama              : %s    |\n"%akun_data[0])
                        if len(str(total))<9:
                            txt_write.write("| Tagihan                : Rp.%d \t\t\t|\n"%total)
                        else:
                            txt_write.write("| Tagihan                : Rp.%d \t\t|\n"%total)
                        if len(str(bayar))<9:
                            txt_write.write("| Uang Anda              : Rp.%d \t\t\t|\n"%bayar)
                        else:
                            txt_write.write("| Uang Anda              : Rp.%d \t\t|\n"%bayar)
                        if len(str(bayar))<9:
                            txt_write.write("| Kembalian              : Rp.%d \t\t\t|\n"%kembalian)
                        else:
                            txt_write.write("| Kembalian              : Rp.%d \t\t|\n"%kembalian)
                        txt_write.write("\=======================================================/\n")
                        print("| Struk berhasil disimpan!                              |")
                        print("| Tekan enter untuk kembali...                          |")
                        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        dafbel = []
                        total = 0
                        menu_customer(dafbel, total)
                        break
                elif simpen == 't' or simpen == 'T':
                    print("|                                                       |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    dafbel = []
                    total = 0
                    menu_customer(dafbel, total)
                    break
                else:
                    print("| Input yang anda masukkan tidak valid!                 |")
                    print("| Tekan enter untuk kembali...                          |")
                    input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    breakpoint
    elif menu_cust == '2':
        if dafbel == [] and total == 0:
            print("|_______________________________________________________|")
            print("\n _______________________________________________________")
            print("| Error:                                                |")
            print("| Daftar belanja belum ada, tidak dapat mengedit daftar!|")
            print("|                                                       |")
            print("| Tekan enter untuk kembali...                          |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            menu_customer(dafbel, total)
        else:
            print("|_______________________________________________________|")
            print("\n _______________________________________________________")
            print("| Sukses:                                               |")
            print("| Anda akan dialihkan ke menu Edit Daftar Belanja!      |")
            print("|                                                       |")
            print("| Mengalihkan...                                        |")
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            time.sleep(1.5)
            edit_dafbel(dafbel, total)
    elif menu_cust == '3':
        temp_data = []
        with open('data_akun.csv', mode="r") as csv_read:
            baca = csv.DictReader(csv_read)
            for ini in baca:
                temp_data.append(ini)
        data_temp = []
        i = 0
        for ini in temp_data:
            if ini['USERNAME'] == akun_data[1]:
                data_temp = temp_data[i]
            i+=1
        passlama = str(input("| Masukkan Password lama anda > "))
        if data_temp['PASSWORD'] == passlama:
            passbaru = str(input("| Masukkan Password baru      > "))
            print("|_______________________________________________________|")
            if len(passbaru) < 6:
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Gunakan Password dengan minimal 6 huruf/angka!        |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                menu_customer(dafbel, total)
            if passbaru == passlama:
                print("\n _______________________________________________________")
                print("| Error:                                                |")
                print("| Password baru anda, sama dengan yang lama!            |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                menu_customer(dafbel, total)
            else:
                i=0
                for ini in temp_data:
                    if ini['USERNAME'] == akun_data[1]:
                        temp_data[i]['PASSWORD'] = passbaru
                    i+=1
            try:
                with open('data_akun.csv', mode="w") as csv_write:
                    kolom = ['NAMA', 'UMUR', 'ASAL', 'NOHP', 'USERNAME', 'PASSWORD', 'LEVEL']
                    tulis = csv.DictWriter(csv_write, fieldnames=kolom)
                    tulis.writeheader()
                    for ini in temp_data:
                        tulis.writerow({'NAMA': ini['NAMA'], 'UMUR': ini['UMUR'], 'ASAL': ini['ASAL'], 'NOHP': ini['NOHP'], 'USERNAME': ini['USERNAME'], 'PASSWORD': ini['PASSWORD'], 'LEVEL': ini['LEVEL']})
            except PermissionError:
                print("\n _______________________________________________________ ")
                print("| Error:                                                |")
                print("| Harap menutup file Excel terlebih dahulu!             |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                menu_customer(dafbel, total)
            print("\n _______________________________________________________")
            print("| Sukses:                                               |")
            print("| Password anda berhasil di ubah!                       |")
            print("|                                                       |")
            print("| Tekan enter untuk melanjutkan...                      |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            menu_customer(dafbel, total)
        else:
            print("|_______________________________________________________|")
            print("\n _______________________________________________________")
            print("| Error:                                                |")
            print("| Password lama yang anda masukkan salah!               |")
            print("|                                                       |")
            print("| Tekan enter untuk kembali...                          |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            menu_customer(dafbel, total)
    elif menu_cust == '4':
        print("|_______________________________________________________|")
        print("|                                                       |")
        print("| Keluar Program...                                     |")
        time.sleep(2)
        print("|                                                       |")
        print("| Terimakasih Telah Menggunakan Program Kami!           |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        time.sleep(3)
        exit()
    else:
        print("|_______________________________________________________|")
        print("\n _______________________________________________________")
        print("| Error:                                                |")
        print("| Input yang anda masukkan tidak valid!                 |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        menu_customer(dafbel, total)

def edit_dafbel(dafbel, total):
    clear_screen()
    print(" _______________________________________________________ ")
    print("|                     Daftar Belanja                    |")
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    for ini in dafbel:
        print(ini)
    print("|_______________________________________________________|")
    if len(str(total))<10:
        print("| Total Belanjaan = Rp.%d               \t\t|"%total)
    else:
        print("| Total Belanjaan = Rp.%d                 \t|"%total)
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("|                      EDIT DAFTAR                      |")
    print("|_______________________________________________________|")
    print("| [1] Menghapus 1 Daftar                                |")
    print("| [2] Menghapus Banyak                                  |")
    print("| [3] Hapus Semua Daftar                                |")
    print("| [4] Hitung Banyaknya Daftar                           |")
    print("| [5] Sorting Daftar Belanja                            |")
    print("| [6] Mencari Harga terkecil & terbesar                 |")
    print("| [0] Kembali                                           |")
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    menu_dafbel = str(input("| Input menu                  > "))
    if menu_dafbel == '0':
        print("|_______________________________________________________|")
        print("\n _______________________________________________________")
        print("| Sukses:                                               |")
        print("| Beralih kembali ke Menu Customer!                     |")
        print("|                                                       |")
        print("| Mengalihkan...                                        |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        time.sleep(1.5)
        menu_customer(dafbel, total)
    elif menu_dafbel == '1':
        try:
            hap = int(input("| Masukkan indeks daftar      > "))
            if hap < 0:
                print("|_______________________________________________________|")
                print("\n _______________________________________________________")
                print("| Error:                                                |")
                print("| Input yang anda masukkan tidak valid!                 |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                edit_dafbel(dafbel, total)
            #Kurang Total
            else:
                x = dafbel[hap].split()
                try:
                    y = x[7].split("Rp.")
                    total = total - int(y[1])
                except IndexError:
                    y = x[6].split("Rp.")
                    total = total - int(y[1])
            #Hapus List
            dafbel.pop(hap)
            print("|_______________________________________________________|")
            print("\n _______________________________________________________")
            print("| Sukses:                                               |")
            print("| Daftar berhasil dihapus!                              |")
            print("|                                                       |")
            print("| Mengalihkan...                                        |")
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            time.sleep(2)
            if dafbel == [] or total == 0:
                menu_customer(dafbel, total)
            else:
                edit_dafbel(dafbel, total)
        except ValueError:
            print("|_______________________________________________________|")
            print("\n _______________________________________________________")
            print("| Error:                                                |")
            print("| Input yang anda masukkan tidak valid!                 |")
            print("|                                                       |")
            print("| Tekan enter untuk kembali...                          |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            edit_dafbel(dafbel, total)
        except IndexError:
            print("|_______________________________________________________|")
            print("\n _______________________________________________________")
            print("| Error:                                                |")
            print("| Indeks yang anda masukkan tidak valid!                |")
            print("|                                                       |")
            print("| Tekan enter untuk kembali...                          |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            edit_dafbel(dafbel, total)
    elif menu_dafbel == '2':
        try:
            pus = int(input("| Menghapus dari daftar       > "))
            pus1 = pus-1
            if pus1 > len(dafbel):
                print("|_______________________________________________________|")
                print("\n _______________________________________________________")
                print("| Error:                                                |")
                print("| Indeks yang anda masukkan tidak valid!                |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                edit_dafbel(dafbel, total)
            pus2 = int(input("| Menghapus hingga daftar     > "))
            if pus2 > len(dafbel):
                print("|_______________________________________________________|")
                print("\n _______________________________________________________")
                print("| Error:                                                |")
                print("| Indeks yang anda masukkan tidak valid!                |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                edit_dafbel(dafbel, total)
            del dafbel[pus1:pus2]
            total = 0
            #Tambah Total
            dafbel2 = []
            x = -1
            y = 0
            for ini in dafbel:
                a = dafbel[y].split()
                dafbel2.append(a)
                y+=1
            for ini in dafbel2:
                try:
                    if '|' in ini[8]:
                        x += 1
                        z = dafbel2[x][7].split("Rp.")
                        total = total + int(z[1]) #1
                except IndexError:
                    x += 1
                    z = dafbel2[x][6].split("Rp.")
                    total = total + int(z[1]) #2
            print("|_______________________________________________________|")
            print("\n _______________________________________________________")
            print("| Sukses:                                               |")
            print("| Daftar berhasil dihapus!                              |")
            print("|                                                       |")
            print("| Mengalihkan...                                        |")
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            time.sleep(2)
            if dafbel == []:
                menu_customer(dafbel, total)
            else:
                edit_dafbel(dafbel, total)
        except ValueError:
            print("|_______________________________________________________|")
            print("\n _______________________________________________________")
            print("| Error:                                                |")
            print("| Input yang anda masukkan tidak valid!                 |")
            print("|                                                       |")
            print("| Tekan enter untuk kembali...                          |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            edit_dafbel(dafbel, total)
    elif menu_dafbel == '3':
        print("| Yakin ingin menghapus semua daftar?")
        cls = str(input("| (y/t)                       > "))
        if cls == 'y' or cls == 'Y':
            dafbel.clear()
            total = 0
            print("|_______________________________________________________|")
            print("\n _______________________________________________________")
            print("| Sukses:                                               |")
            print("| Semua daftar berhasil dihapus!                        |")
            print("|                                                       |")
            print("| Mengalihkan...                                        |")
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            time.sleep(2)
            menu_customer(dafbel, total)
        elif cls == 't' or cls == 'T':
            print("|_______________________________________________________|")
            print("\n _______________________________________________________")
            print("| Sukses:                                               |")
            print("| Menghapus semua daftar digagalkan!                    |")
            print("|                                                       |")
            print("| Mengalihkan...                                        |")
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            time.sleep(2)
            edit_dafbel(dafbel, total)
        else:
            print("|_______________________________________________________|")
            print("\n _______________________________________________________")
            print("| Error:                                                |")
            print("| Input yang anda masukkan tidak valid!                 |")
            print("|                                                       |")
            print("| Tekan enter untuk kembali...                          |")
            input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            edit_dafbel(dafbel, total)
    elif menu_dafbel == '4':
        print("| Total daftar belanjaan anda > %d        \t\t|"%len(dafbel))
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        edit_dafbel(dafbel, total)
    elif menu_dafbel == '5':
        while True:
            clear_screen()
            print(" _______________________________________________________ ")
            print("|                     Daftar Belanja                    |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            for ini in dafbel:
                print(ini)
            print("|_______________________________________________________|")
            if len(str(total))<10:
                print("| Total Belanjaan = Rp.%d               \t\t|"%total)
            else:
                print("| Total Belanjaan = Rp.%d                 \t|"%total)
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|                      EDIT DAFTAR                      |")
            print("|_______________________________________________________|")
            print("| [1] Ascending                                         |")
            print("| [2] Descending                                        |")
            print("| [0] Kembali                                           |")
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("| Input menu                  > 5                       |")
            sort = str(input("| Pilih opsi sorting          > "))
            print("|_______________________________________________________|")
            if sort == '0':
                edit_dafbel(dafbel, total)
                break
            elif sort == '1':
                insertionSort(dafbel,sort)
                print("\n _______________________________________________________")
                print("| Sukses:                                               |")
                print("| Daftar belanja berhasil di sorting Ascending!         |")
                print("|                                                       |")
                print("| Mengalihkan...                                        |")
                print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                time.sleep(2)
                edit_dafbel(dafbel, total)
                break
            elif sort == '2':
                insertionSort(dafbel,sort)
                print("\n _______________________________________________________")
                print("| Sukses:                                               |")
                print("| Daftar belanja berhasil di sorting Descending!        |")
                print("|                                                       |")
                print("| Mengalihkan...                                        |")
                print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                time.sleep(2)
                edit_dafbel(dafbel, total)
                break
            else:
                print("\n _______________________________________________________")
                print("| Error:                                                |")
                print("| Input yang anda masukkan tidak valid!                 |")
                print("|                                                       |")
                print("| Tekan enter untuk kembali...                          |")
                input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    elif menu_dafbel == '6':
        #Memisahkan Nilai Harga dan String
        temp = []
        z = -1
        for ini in dafbel:
            z += 1
            try:
                x = dafbel[z].split()
                y = (x[6].split('Rp.'))
                temp.append(int(y[1]))
            except IndexError:
                x = dafbel[z].split()
                y = (x[7].split('Rp.'))
                temp.append(int(y[1]))
        print("|                                                       |")
        #Mencari Nilai Terkecil
        nilai_min = min(temp)
        indeks_cocok = []
        i = 0
        length = len(temp)
        while i < length:
            if nilai_min == temp[i]:
                indeks_cocok.append(i)
            i += 1
        print("| Harga terkecil adalah       >                         |")
        for ini in indeks_cocok:
            print(dafbel[ini])
        print("|                                                       |")
        #Mencari Nilai Terbesar
        nilai_max = max(temp)
        indeks_cocok = []
        i = 0
        length = len(temp)
        while i < length:
            if nilai_max == temp[i]:
                indeks_cocok.append(i)
            i += 1
        print("| Harga terbesar adalah       >                         |")
        for ini in indeks_cocok:
            print(dafbel[ini])
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        edit_dafbel(dafbel, total)
    else:
        print("|_______________________________________________________|")
        print("\n _______________________________________________________")
        print("| Error:                                                |")
        print("| Input yang anda masukkan tidak valid!                 |")
        print("|                                                       |")
        print("| Tekan enter untuk kembali...                          |")
        input(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        edit_dafbel(dafbel, total)

if __name__ == "__main__":
    akun_data = []
    ini_fail()
    clear_screen()
    print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("|            T O K O  P E R A L A T A N  A T K          |")
    print("|_______________________________________________________|")
    print("|                Projek Akhir Kelompok 9                |")
    print("|        Praktikum Algoritma & Pemrograman Lanjut       |")
    print("|                  Informatika A 2020                   |")
    print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
    time.sleep(2)
    while True:
        main_utama()