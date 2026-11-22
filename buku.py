class Buku:
    def __init__(self, kode_buku, judul, penulis, penerbit, tahun_terbit):
        self.__kode_buku = kode_buku
        self.__judul = judul
        self.__penulis = penulis
        self.__penerbit = penerbit
        self.__tahun_terbit = tahun_terbit

    # getter
    def get_kode_buku(self):
        return self.__kode_buku

    def get_judul(self):
        return self.__judul

    def get_penulis(self):
        return self.__penulis

    def get_penerbit(self):
        return self.__penerbit  
    
    def get_tahun_terbit(self):
        return self.__tahun_terbit

    # setter
    def set_judul(self, judul):
        self.__judul = judul

    def set_penulis(self, penulis):
        self.__penulis = penulis

    def set_penerbit(self, penerbit):
        self.__penerbit = penerbit

    def set_tahun_terbit(self, tahun):
        self.__tahun_terbit = tahun

    #simpan ke file
    def to_line(self):
        return f"{self.__kode_buku}|{self.__judul}|{self.__penulis}|{self.__penerbit}|{self.__tahun_terbit}\n"

    # ubah jadi objek Buku lagi
    @staticmethod
    def from_line(line):
        data = line.strip().split("|")
        kode = data[0]
        judul = data[1]
        penulis = data[2]
        penerbit = data[3]
        tahun = data[4]
        return Buku(kode, judul, penulis, penerbit, tahun)

    def tampilkan_info(self):
        print("Kode Buku :", self.__kode_buku)
        print("Judul     :", self.__judul)
        print("Penulis   :", self.__penulis)
        print("Penerbit  :", self.__penerbit)
        print("Tahun     :", self.__tahun_terbit)