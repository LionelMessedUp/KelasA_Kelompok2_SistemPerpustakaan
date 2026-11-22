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

    def menu_tambah(self):
            print("\n--- Tambah Data Buku ---")
            buku = self.__input_data_buku()
            if not buku:
                return
            if self.__perpustakaan.tambah_buku(buku):
                print("[V] Data buku berhasil ditambahkan.")
            else:
                print("[X] Gagal: Kode buku sudah terdaftar!")
    
    def menu_cari(self):
            print("\n--- Cari Data Buku ---")
            kode = input("Masukkan Kode Buku: ").strip()
            buku = self.__perpustakaan.cari_buku(kode)
            if buku:
                buku.tampilkan_info()
            else:
                print("[X] Data buku tidak ditemukan.")