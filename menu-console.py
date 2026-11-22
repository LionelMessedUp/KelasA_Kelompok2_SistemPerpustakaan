# ==========================================
# 4. CLASS MENU CONSOLE
# ==========================================
class MenuConsole:
    def __init__(self):
        self.__perpustakaan = Perpustakaan()

    def __input_data_buku(self) -> Buku:
        # Method privat: meminta data buku dari pengguna
        kode = input("Masukkan Kode Buku : ").strip()
        judul = input("Masukkan Judul     : ").strip()
        penulis = input("Masukkan Penulis   : ").strip()
        penerbit = input("Masukkan Penerbit  : ").strip()
        tahun = input("Masukkan Tahun     : ").strip()

        if kode == "" or not tahun.isdigit():
            print("[X] Kode tidak boleh kosong dan tahun harus berupa angka!")
            return None
        return Buku(kode, judul, penulis, penerbit, int(tahun))

    def tampilkan_menu(self):
        print("\n==============================================")
        print("     APLIKASI PENGELOLAAN BUKU PERPUSTAKAAN   ")
        print("==============================================")
        print("1. Tambah Data Buku")
        print("2. Cari Data Buku")
        print("3. Hapus Data Buku")
        print("4. Perbarui Data Buku")
        print("0. Keluar")
        print("==============================================")