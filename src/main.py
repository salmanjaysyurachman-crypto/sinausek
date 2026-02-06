from database import setup_database
from buku import tampilkan_buku, tambah_buku, buku_terpopuler
from transaksi import pinjam_buku, kembalikan_buku


def menu():
    print("\n=== SISTEM INFORMASI PERPUSTAKAAN ===")
    print("1. Tampilkan Buku")
    print("2. Tambah Buku")
    print("3. Pinjam Buku")
    print("4. Kembalikan Buku")
    print("5. Buku Terpopuler")
    print("0. Keluar")

def main():
    # Setup database & tabel (aman dipanggil berkali-kali)
    setup_database()

    while True:
        menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_buku()

        elif pilihan == "2":
            tambah_buku()

        elif pilihan == "3":
            pinjam_buku()

        elif pilihan == "4":
            kembalikan_buku()

        elif pilihan == "5":
            buku_terpopuler()

        elif pilihan == "0":
            print("Terima kasih, program selesai.")
            break

        else:
            print("❌ Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()