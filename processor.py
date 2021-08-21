import os
import yadisk

from data import TOKEN

# yadisk.exceptions.PathExistsError


class Processor:

    def __init__(self, path):
        self.path = path
        self.__yadisk = yadisk.YaDisk(token=TOKEN)

    @property
    def yadisk(self):
        return self.__yadisk

    def upload_files_2_yadisk(self):
        for address, dirs, files in os.walk(self.path):
            print(f"Address: {address}, dirs: {dirs}, files: {files}")
            print()
            catalog = address.split("/")[-1]
            if files:
                if catalog != "job":
                    self.yadisk.mkdir(f"backup/{catalog}")
                for file in files:
                    print(f"catalog {catalog}, file: {address}/{file}")
                    dst = catalog if catalog != "job" else None
                    dst_path = f"backup/{dst}/{file}" if dst is not None else f"backup/{file}"
                    self.yadisk.upload(f"{address}/{file}", dst_path)
