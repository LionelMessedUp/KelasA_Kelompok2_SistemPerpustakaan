class FileStorage:
    def __init__(self, nama_file: str):
        self.__nama_file = nama_file

    def save(self, data: dict):
        with open(self.__nama_file, "w") as file:
            for buku in data.values():
                file.write(buku.to_line())