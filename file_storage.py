class FileStorage:
    def __init__(self, nama_file: str):
        self.__nama_file = nama_file

    def load (self) -> dict:
        data = {}
        with open(self.__nama_file, "r") as file:
            for line in file:
                buku = Buku.from_line(line)
                data[buku.get_kode_buku()] = buku
        return data

    def save(self, data: dict):
        with open(self.__nama_file, "w") as file:
            for buku in data.values():
                file.write(buku.to_line())

    def append(self, buku: Buku):
        with open(self.__nama_file, "a") as file:
            file.write(buku.toline())