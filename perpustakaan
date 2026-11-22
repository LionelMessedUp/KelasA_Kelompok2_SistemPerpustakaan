from buku import Buku
from file_storage import FileStorage
class Perpustakaan:
    def __init__(self):
        self.__daftar_buku = {}
        self.__storage = FileStorage("buku.txt")
        self.muat_data()
    def muat_data(self):
        self.__daftar_buku = self.__storage.load()
def kode_ada(self, kode: str) -> bool:
        return kode in self.__daftar_buku
    def tambah_buku(self, buku: Buku) -> bool:
        if self.kode_ada(buku.get_kode_buku()):
            return False
        self.__daftar_buku[buku.get_kode_buku()] = buku
        self.__storage.append(buku)
        return True
def cari_buku(self, kode: str) -> Buku:
        return self.__daftar_buku.get(kode)
def hapus_buku(self, kode: str) -> bool:
        if not self.kode_ada(kode):
            return False
        del self.__daftar_buku[kode]
        self.__storage.save(self.__daftar_buku)
        return True
def perbarui_buku(self, kode: str, data_baru: dict) -> bool:
        buku = self.cari_buku(kode)
        if not buku:
            return False
        buku.set_judul(data_baru["judul"])
        buku.set_penulis(data_baru["penulis"])
        buku.set_penerbit(data_baru["penerbit"])
        buku.set_tahun_terbit(data_baru["tahun_terbit"])
        self.__storage.save(self.__daftar_buku)
        return True
