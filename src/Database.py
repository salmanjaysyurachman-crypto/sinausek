import sqlite3

def get_connection():
    conn = sqlite3.connect("perpus.db")
    return conn

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS buku (
        kode TEXT PRIMARY KEY,
        judul TEXT,
        penulis TEXT,
        stok INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transaksi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_peminjam TEXT,
        kode_buku TEXT,
        tanggal TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()
