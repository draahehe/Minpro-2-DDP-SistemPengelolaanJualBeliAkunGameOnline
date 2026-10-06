# Mini Project 2
Nama : Muhammad Indra Pratama<br>
NIM : 083<br>
Kelas : C

# Sistem Jual Beli Akun Game
## 1. Deskripsi Singkat Program

Ini program jual beli akun game yang dijalankan lewat terminal, dibuat pakai Python. Sebelum masuk, user harus login dulu pakai username dan password. Password yang diketik nggak kelihatan di layar (jadi bintang-bintang) karena pakai library `pwinput`.

Ada dua role dengan hak akses yang beda:

- **Admin** bisa ngatur semuanya: tambah akun, lihat semua akun, perbarui data akun, dan hapus akun.
- **User** cuma bisa lihat daftar akun dan beli akun.

Semua data akun disimpan di file `data_akun.json`, jadi nggak hilang walaupun program ditutup. Penyimpanannya otomatis, setiap ada perubahan langsung ditulis ke file.

**Akun buat login:**

| Username | Password | Role |
|----------|----------|------|
| admin | admin123 | Admin |
| user | user123 | User |

**Cara menginstall pwinput:**

```bash
pip install pwinput
```

Pastikan `akun_game_json.py` dan `data_akun.json` ada di folder yang sama.

---

## 2. Flowchart

Flowchart yang saya pakai adalah draw.io 

### 2.1 Alur Utama (Login)

<br>
<img width="2802" height="1312" alt="Flowchart Sistem Pengelolaan Jual Beli Game Online Tambahan drawio" src="https://github.com/user-attachments/assets/8265e4c8-08c8-484b-bc0c-aabc179c1e25" />


**Penjelasan alur:**

Begitu program jalan, data akun langsung dimuat dari `data_akun.json`. Kalau filenya belum ada atau kosong, program mulai dari daftar akun yang kosong. Setelah itu user diminta mengisi username dan password. Kalau salah, muncul pesan "Username atau password salah" lalu diminta mengisi ulang, terus begitu sampai benar. Kalau sudah benar, program ngecek rolenya. Role admin diarahkan ke menu admin, selain itu ke menu user. Program selesai setelah user memilih keluar dari menunya.

### 2.2 Menu Admin

<br>
<img width="303" height="223" alt="image" src="https://github.com/user-attachments/assets/208af17d-8a37-4391-828c-1d8cbc5e37fd" />


**Penjelasan alur:**

Admin bisa mengkases menu 1 sampai 5, lalu memasukkan pilihannya. Pilihan dicek satu per satu, mirip rantai if-elif di kodenya:

- **1. Tambah akun**: isi ID, nama game, harga, dan status, lalu akun ditambahkan ke `daftar_akun` dan disimpan ke JSON.
- **2. Lihat akun**: menampilkan semua akun, tidak ada yang diubah jadi tidak perlu simpan.
- **3. Perbarui akun**: pilih nomor akun, isi data barunya, lalu disimpan ke JSON.
- **4. Hapus akun**: pilih nomor akun, dihapus dari daftar, lalu disimpan ke JSON.
- **5. Keluar**: menampilkan ucapan terima kasih dan program selesai.

Kalau pilihannya bukan 1 sampai 5, muncul "Pilihan tidak valid". Setelah selesai satu aksi (atau pilihan tidak valid), alurnya balik lagi ke menu, ditandai lingkaran **A** di flowchart.

### 2.3 Menu User

<br>
<img width="296" height="167" alt="image" src="https://github.com/user-attachments/assets/ba23b550-f36c-43b0-9e25-ce45064fa9f7" />


**Penjelasan alur:**

User cuma punya tiga pilihan: lihat akun, beli akun, atau keluar. Lihat akun dan keluar alurnya sama kayak di admin. Yang beda adalah alur **beli akun**:

1. Daftar akun ditampilkan, lalu user memasukkan nomor akun yang mau dibeli.
2. Kalau nomornya nggak valid (bukan angka atau di luar daftar), muncul pesan error lalu balik ke menu.
3. Kalau valid, program ngecek statusnya. Kalau akunnya sudah Terjual, pembelian ditolak.
4. Kalau masih Tersedia, statusnya diubah jadi Terjual, disimpan ke JSON, dan muncul pesan pembelian berhasil.

---

## 3. Dokumentasi Program dan Output

### 3.1 Data awal dan penyimpanan JSON

```python
def muat_data():
    try:
        with open(NAMA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def simpan_data():
    with open(NAMA_FILE, "w", encoding="utf-8") as file:
        json.dump(daftar_akun, file, indent=4, ensure_ascii=False)
```

`muat_data()` dipanggil sekali di awal buat ngisi `daftar_akun` dari file `data_akun.json`. Kalau filenya nggak ada atau isinya rusak, hasilnya list kosong biar program nggak error. `simpan_data()` nulis isi `daftar_akun` balik ke file, dan dipanggil otomatis setiap ada perubahan data.

**Screenshot: isi file `data_akun.json`**

<br>
<img width="597" height="407" alt="image" src="https://github.com/user-attachments/assets/ae991019-5081-4335-a829-2a4fb386434d" />


### 3.2 Login

```python
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
```

Data login disimpan di dictionary `DATA_PENGGUNA`. Fungsi ini minta username dan password (pakai `pwinput` jadi password disamarkan), terus dicocokkan. Kalau salah, diulang terus. Kalau benar, fungsi mengembalikan username dan rolenya buat nentuin menu mana yang dibuka.

**Screenshot: login salah lalu login berhasil**

**Salah input**

<img width="385" height="68" alt="image" src="https://github.com/user-attachments/assets/930a1c5c-110d-4fca-82ac-0630671eef4c" />

**Login Berhasil**

<img width="247" height="52" alt="image" src="https://github.com/user-attachments/assets/ae924ecf-da1c-499a-a1eb-953ee86d98a2" />


### 3.3 Menu Admin

**Tampilan menu admin**

Setelah login sebagai admin, muncul menu dengan lima pilihan.

<br>
<img width="303" height="223" alt="Screenshot 2026-10-06 190709" src="https://github.com/user-attachments/assets/65f9fa99-b461-4a4f-a3bb-d73dfb4b855d" />


**1. Tambah akun** (`tambah_akun()`)

Admin mengisi ID akun, nama game, harga, dan status. ID dan nama game tidak boleh kosong, harga harus angka (dicek di `ambil_harga()`), dan status hanya boleh Tersedia atau Terjual (dicek di `ambil_status()`). Setelah itu akun masuk ke `daftar_akun` dan langsung disimpan.

<br>
<img width="430" height="119" alt="Screenshot 2026-10-06 191355" src="https://github.com/user-attachments/assets/e12a8262-1f18-41f6-ab27-31be8dbb721a" />


**2. Lihat semua akun** (`lihat_akun()`)

Menampilkan semua akun lengkap dengan nomor urut, ID, game, harga, dan status. Kalau belum ada data, muncul "Belum ada data akun."

<br>
<img width="585" height="113" alt="image" src="https://github.com/user-attachments/assets/0bbe2aa0-aeb6-4790-a901-7a80852f8112" />


**3. Perbarui data akun** (`ubah_akun()`)

Admin memilih nomor akun (dicek dulu lewat `pilih_indeks_akun()` supaya nomornya valid), lalu mengisi ID, nama game, harga, dan status yang baru. Setelah itu data disimpan.

<br>
<img width="608" height="201" alt="image" src="https://github.com/user-attachments/assets/621e13d7-417a-455c-9d35-d04f3f3b3e84" />


**4. Hapus akun** (`hapus_akun()`)

Admin memilih nomor akun yang mau dihapus, akunnya di-pop dari `daftar_akun`, lalu perubahan disimpan. Muncul pesan nama game yang berhasil dihapus.

<br>
<img width="620" height="141" alt="image" src="https://github.com/user-attachments/assets/e143be03-06d6-457d-affd-a8d227c74ed9" />


**5. Keluar**

Menampilkan ucapan terima kasih lalu program berhenti.

<br>
<img width="361" height="55" alt="image" src="https://github.com/user-attachments/assets/361469c5-5eaa-498a-a42e-d54c0ac096e8" />


### 3.4 Menu User

**Tampilan menu user**

User cuma dapat tiga pilihan: lihat akun, beli akun, dan keluar.

<br>
<img width="219" height="113" alt="image" src="https://github.com/user-attachments/assets/1800c858-4afe-419f-9190-14a1896e1bbb" />


**Beli akun** (`beli_akun()`)

```python
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
```

Program nampilin daftar akun, user memilih nomor, lalu dicek dulu nomornya valid atau nggak. Akun yang statusnya sudah Terjual nggak bisa dibeli lagi. Kalau masih Tersedia, statusnya diubah jadi Terjual dan langsung disimpan ke JSON.

**Screenshot: pembelian berhasil**

<br>
<img width="626" height="130" alt="image" src="https://github.com/user-attachments/assets/cd58e614-4c37-4e19-b292-a523ad6310b8" />


**Screenshot: beli akun yang sudah terjual**

<br>
<img width="573" height="111" alt="image" src="https://github.com/user-attachments/assets/85cc2232-f144-4589-9b5c-1b98500a6e15" />


**Screenshot: nomor akun tidak valid**

<br>
<img width="371" height="34" alt="image" src="https://github.com/user-attachments/assets/48debe2e-ce25-4356-b2bf-63f070020aff" />


### 3.5 Data Tetap Tersimpan

Karena penyimpanannya otomatis, data yang sudah diubah tetap ada setelah program ditutup dan dijalankan lagi. Contohnya status akun yang sudah dibeli tetap Terjual.

**Screenshot: daftar akun setelah program dijalankan ulang**

<br>
<img width="702" height="340" alt="image" src="https://github.com/user-attachments/assets/82b5bce8-50ab-443f-82ef-2f91d0cf324b" />


<br><br>

**Screenshot: isi `data_akun.json` setelah ada pembelian**

<br>
<img width="477" height="423" alt="image" src="https://github.com/user-attachments/assets/7a24ee9e-e509-4b97-9359-a8a14bd293d3" />


---
