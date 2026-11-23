# ==========================================
# CLASS MENU CONSOLE
# ==========================================
from buku import Buku
from perpustakaan import Perpustakaan

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

    def menu_hapus(self):
            print("\n--- Hapus Data Buku ---")
            kode = input("Masukkan Kode Buku: ").strip()
            buku = self.__perpustakaan.cari_buku(kode)
            if not buku:
                print("[X] Data buku tidak ditemukan.")
                return
    
            buku.tampilkan_info()
            konfirmasi = input("Yakin ingin menghapus buku ini? (y/n): ").strip().lower()
            if konfirmasi != "y":
                print("[!] Penghapusan dibatalkan.")
                return
    
            if self.__perpustakaan.hapus_buku(kode):
                print("[V] Data buku berhasil dihapus.")

    def menu_perbarui(self):
           print("\n--- Perbarui Data Buku ---")
           kode = input("Masukkan Kode Buku: ").strip()
           buku = self.__perpustakaan.cari_buku(kode)
           if not buku:
               print("[X] Data buku tidak ditemukan.")
               return
   
           print("(Kosongkan input jika tidak ingin mengubah)")
           judul = input(f"Judul Baru ({buku.get_judul()}): ").strip() or buku.get_judul()
           penulis = input(f"Penulis Baru ({buku.get_penulis()}): ").strip() or buku.get_penulis()
           penerbit = input(f"Penerbit Baru ({buku.get_penerbit()}): ").strip() or buku.get_penerbit()
           tahun = input(f"Tahun Baru ({buku.get_tahun_terbit()}): ").strip()
   
           if tahun == "":
               tahun = buku.get_tahun_terbit()
           elif tahun.isdigit():
               tahun = int(tahun)
           else:
               print("[X] Tahun harus berupa angka!")
               return
   
           data_baru = {
               "judul": judul,
               "penulis": penulis,
               "penerbit": penerbit,
               "tahun_terbit": tahun,
           }
           if self.__perpustakaan.perbarui_buku(kode, data_baru):
               print("[V] Data buku berhasil diperbarui.")

    def jalankan(self):
            while True:
                self.tampilkan_menu()
                pilihan = input("Pilih menu (0-4): ").strip()
    
                if pilihan == "1":
                    self.menu_tambah()
                elif pilihan == "2":
                    self.menu_cari()
                elif pilihan == "3":
                    self.menu_hapus()
                elif pilihan == "4":
                    self.menu_perbarui()
                elif pilihan == "0":
                    print("\nTerima kasih telah menggunakan Aplikasi Perpustakaan.")
                    break
                else:
                    print("\n[X] Pilihan menu tidak valid!")

if __name__ == "__main__":
    app = MenuConsole()
    app.jalankan()
