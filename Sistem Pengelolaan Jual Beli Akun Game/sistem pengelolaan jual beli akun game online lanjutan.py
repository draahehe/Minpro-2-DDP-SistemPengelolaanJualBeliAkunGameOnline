import json
from pwinput import pwinput

NAMA_FILE = "data_akun.json"

DATA_PENGGUNA = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
}


def muat_data():
    try:
        with open(NAMA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def simpan_data():
    with open(NAMA_FILE, "w", encoding="utf-8") as file:
        json.dump(daftar_akun, file, indent=4, ensure_ascii=False)


daftar_akun = muat_data()


def login():
    print("=== Login Sistem Jual Beli Akun Game ===")
    while True:
        username = input("Username: ").strip()
        password = pwinput("Password: ")
        pengguna = DATA_PENGGUNA.get(username)

        if pengguna and pengguna["password"] == password:
            print(f"Login berhasil sebagai {pengguna['role']}.")
            return username, pengguna["role"]

        print("Username atau password salah. Silakan coba lagi.")

def tampilkan_menu_admin():
    print("\n=== Menu Admin ===")
    print("1. Tambah akun")
    print("2. Lihat semua akun")
    print("3. Perbarui data akun")
    print("4. Hapus akun")
    print("5. Keluar")

def tampilkan_menu_user():
    print("\n=== Menu User ===")
    print("1. Lihat semua akun")
    print("2. Beli akun")
    print("3. Keluar")

def ambil_harga():
    while True:
        harga = input("Masukkan harga jual (Rp): ")
        if harga.isdigit():
            return int(harga)
        print("Harga harus berisi angka, tanpa huruf atau simbol.")

def ambil_status(pesan):
    while True:
        status = input(pesan).strip().title()
        if status in {"Tersedia", "Terjual"}:
            return status
        print("Status hanya boleh 'Tersedia' atau 'Terjual'.")

def tambah_akun():
    print("\n=== Tambah Akun ===")
    id_akun = input("Masukkan ID akun: ").strip()
    nama_game = input("Masukkan nama game: ").strip()

    if not id_akun or not nama_game:
        print("ID akun dan nama game tidak boleh kosong.")
        return

    akun_baru = {
        "id": id_akun,
        "game": nama_game,
        "harga": ambil_harga(),
        "status": ambil_status("Masukkan status akun (Tersedia/Terjual): ")
    }
    daftar_akun.append(akun_baru)
    simpan_data()
    print("Akun berhasil ditambahkan.")

def lihat_akun():
    print("\n=== Daftar Akun ===")
    if not daftar_akun:
        print("Belum ada data akun.")
        return

    for nomor, akun in enumerate(daftar_akun, start=1):
        print(
            f"{nomor}. ID: {akun['id']} | "
            f"Game: {akun['game']} | "
            f"Harga: Rp{akun['harga']} | "
            f"Status: {akun['status']}"
        )

def pilih_indeks_akun(pesan):
    if len(daftar_akun) == 0:
        print("Belum ada data akun.")
        return None

    if len(daftar_akun) == 1:
        return 0

    lihat_akun()
    try:
        index = int(input(pesan)) - 1
        if 0 <= index < len(daftar_akun):
            return index
        print("Nomor akun tidak valid.")
        return None
    except ValueError:
        print("Input harus berupa angka.")
        return None

def ubah_akun():
    print("\n=== Perbarui Data Akun ===")
    index = pilih_indeks_akun("Masukkan nomor akun yang ingin diubah: ")
    if index is None:
        return

    daftar_akun[index]["id"] = input("Masukkan ID akun baru: ").strip()
    daftar_akun[index]["game"] = input("Masukkan nama game baru: ").strip()
    daftar_akun[index]["harga"] = ambil_harga()
    daftar_akun[index]["status"] = ambil_status("Masukkan status baru (Tersedia/Terjual): ")
    simpan_data()
    print("Data akun berhasil diperbarui.")

def hapus_akun():
    print("\n=== Hapus Akun ===")
    index = pilih_indeks_akun("Masukkan nomor akun yang ingin dihapus: ")
    if index is None:
        return

    akun_dihapus = daftar_akun.pop(index)
    simpan_data()
    print(f"Akun {akun_dihapus['game']} berhasil dihapus.")

def beli_akun(username):
    print("\n=== Beli Akun ===")
    if not daftar_akun:
        print("Belum ada data akun.")
        return

    lihat_akun()
    nomor = input("Masukkan nomor akun yang ingin dibeli: ")
    if not nomor.isdigit() or not 1 <= int(nomor) <= len(daftar_akun):
        print("Nomor akun tidak valid.")
        return

    akun = daftar_akun[int(nomor) - 1]
    if akun["status"] == "Terjual":
        print("Akun ini sudah terjual.")
        return

    akun["status"] = "Terjual"
    simpan_data()
    print(f"Pembelian berhasil! {username} membeli akun {akun['game']} seharga Rp{akun['harga']}.")

def menu_admin():
    while True:
        tampilkan_menu_admin()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_akun()
        elif pilihan == "2":
            lihat_akun()
        elif pilihan == "3":
            ubah_akun()
        elif pilihan == "4":
            hapus_akun()
        elif pilihan == "5":
            print("\nTerima kasih sudah menggunakan sistem kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def menu_user(username):
    while True:
        tampilkan_menu_user()
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            lihat_akun()
        elif pilihan == "2":
            beli_akun(username)
        elif pilihan == "3":
            print("\nTerima kasih sudah menggunakan sistem kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def main():
    username, role = login()
    if role == "admin":
        menu_admin()
    else:
        menu_user(username)

if __name__ == "__main__":
    main()