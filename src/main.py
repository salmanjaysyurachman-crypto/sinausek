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