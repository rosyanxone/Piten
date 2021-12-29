import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("Selamat Datang di,")
    print("--TOKO KUE SULE!--\n")

    print("================================")
    print("| [1] Kue Keju   : Rp.6000/kue |")
    print("| [2] Kue Cokelat: Rp.3500/kue |")
    print("| [0] Exit                     |")
    print("================================")
    kue = str(input("Kue apa yg ingin anda pesan? "))

    if kue == "1":
        kue_keju()
    elif kue == "2":
        kue_cokelat()
    elif kue == "0":
        close_app()
    else:
        print("Input tidak valid!")
        print("Masukkan angka yang di tentukan!")
        back_to_menu()

#KueKeju
def kue_keju():
    EROR = True
    while (EROR): 
        clear_screen()
        print("Anda memesan kue Keju.")
        print("\n==========================================")
        print("| Selamat! Kami sedang mengadakan promo. |")
        print("| Beli  4 kue keju /lebih. Diskon: 10%   |")
        print("| Beli 16 kue keju /lebih. Diskon: 15%   |")
        print("==========================================")
        print("\n(kue terbatas tidak lebih dari 25)")
        try:
            kue1 = int(input("Berapa kue keju yang ingin di pesan? "))
            clear_screen()
            print("--------------------------------")
            salah = True
            while(salah):
                if kue1 < 4:
                    c = kue1 * 6000
                    print("Anda memesan {0} kue keju." .format(kue1))
                    print("Total harga: Rp.%d" % (c))
                    back_to_menu()
                elif kue1 >= 4 and kue1 <= 15:
                    c = kue1 * 6000 * 10 / 100
                    print("Anda mendapat diskon 10%")
                    print("Anda memesan {0} kue keju." .format(kue1))
                    print("Total harga: Rp.%d" % (c))
                    back_to_menu()
                elif kue1 >= 16 and kue1 <= 25:
                    c = kue1 * 6000 * 15 / 100
                    print("Anda mendapat diskon 15%")
                    print("Anda memesan {0} kue keju." .format(kue1))
                    print("Total harga: Rp.%d" % (c))
                    back_to_menu()
                else:
                    print("Kue tidak tersedia lebih dari 25.")
                    back_to_kue_keju()
            EROR = False
        except ValueError:
            print("\nInput yg dimasukkan tidak valid!")
            back_to_kue_keju()

#KueCokelat
def kue_cokelat():
    EROR = True
    while (EROR):
        clear_screen()
        print("Anda memesan kue Cokelat.")
        print("\n==========================================")
        print("| Selamat! Kami sedang mengadakan promo. |")
        print("| Beli  5 kue cokelat /lebih, Diskon: 7% |")
        print("| Beli 21 kue cokelat /lebih, Diskon: 12%|")
        print("==========================================")
        print("\n(kue terbatas tidak lebih dari 35)")
        try:
            kue2 = int(input("Berapa kue cokelat yang ingin di pesan? "))
            clear_screen()
            print("--------------------------------")
            salah = True
            while(salah):
                if kue2 < 5:
                    c = kue2 * 3500
                    print("Anda memesan {0} kue cokelat." .format(kue2))
                    print("Total harga: Rp.%d" % (c))
                    back_to_menu()
                elif kue2 >= 5 and kue2 <= 20:
                    c = kue2 * 3500 * 7 / 100
                    print("Anda memesan {0} kue cokelat." .format(kue2))
                    print("Anda mendapat diskon 7%")
                    print("Total harga: Rp.%d" % (c))
                    back_to_menu()
                elif kue2 >= 21 and kue2 <= 35:
                    c = kue2 * 3500 * 12 / 100
                    print("Anda memesan {0} kue cokelat." .format(kue2))
                    print("Anda mendapat diskon 12%")
                    print("Total harga: Rp.%d" % (c))
                    back_to_menu()
                else:
                    print("Kue tidak tersedia lebih dari 35.")
                    back_to_kue_cokelat()
        except ValueError:
            print("\nInput yg dimasukkan tidak valid!")
            back_to_kue_cokelat()

def back_to_menu():
    print("\nLanjutkan..?")
    input("Tekan Enter untuk kembali...")
    show_menu()

def back_to_kue_keju():
    input("Tekan Enter untuk kembali...")
    kue_keju()

def back_to_kue_cokelat():
    input("Tekan Enter untuk kembali...")
    kue_cokelat()

def close_app():
    print("Terimakasih telah berbelanja di, Toko Kue Sule!\n")
    time.sleep(2)
    exit()

if __name__ == "__main__":
    while True:
        show_menu()