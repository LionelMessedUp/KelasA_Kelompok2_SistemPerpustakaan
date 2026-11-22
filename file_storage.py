from buku import Buku

class FileStorage:

    def __init__(self, nama_file: str):
        self.__nama_file = nama_file

    def load (self) -> dict:
        data = {}
        try:
            with open(self.__nama_file, "r", encoding="utf-8") as file:
                for line in file:
                    if line.strip() == "":
                        continue
                buku = Buku.from_line(line)
                data[buku.get_kode_buku()] = buku
        except FileNotFoundError:
            pass
        return data

    def save(self, data: dict):
        with open(self.__nama_file, "w", encoding="utf-8") as file:
            for buku in data.values():
                file.write(buku.to_line())

    def append(self, buku: Buku):
        with open(self.__nama_file, "a") as file:
            file.write(buku.toline())