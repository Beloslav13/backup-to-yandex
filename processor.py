import os
from datetime import datetime

import yadisk

from data import TOKEN

# change_date = os.stat(f"{address}/{file}").st_mtime
# print(file, datetime.utcfromtimestamp(int(change_date)).strftime('%Y-%m-%d %H:%M:%S'))


class Processor:

    def __init__(self, path):
        self.path = path
        self.__yadisk = yadisk.YaDisk(token=TOKEN)

    @property
    def yadisk(self):
        return self.__yadisk

    def get_info(self):
        i = self.yadisk.listdir("backup")
        for f in i:
            print(f["name"], f["modified"])
        print()

    def run(self):
        self._prepare_upload()

    def _prepare_upload(self):
        for address, dirs, files in os.walk(self.path):
            print(f"Address: {address}, dirs: {dirs}, files: {files}")
            print()
            if not files:
                continue

            current_dir = self.path.split("/")[-1]
            catalog = address.split("/")[-1]
            if catalog != current_dir:
                try:
                    self.yadisk.mkdir(f"backup/{catalog}")
                except yadisk.exceptions.DirectoryExistsError:
                    print("Папка существует")
            for file in files:
                dst = catalog if catalog != current_dir else None
                dst_path = f"backup/{dst}/{file}" if dst is not None else f"backup/{file}"
                self._upload_to_yadisk(address, file, dst_path)

    def _upload_to_yadisk(self, address, file, dst_path):
        try:
            self.yadisk.upload(f"{address}/{file}", dst_path)
        except yadisk.exceptions.PathExistsError:
            print("File Exists")
            self.yadisk.remove(dst_path, permanently=True)
            self.yadisk.upload(f"{address}/{file}", dst_path)
        print(f"Файл {file} загружен в {dst_path}")
