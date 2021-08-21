import os


class Processor:

    def __init__(self, path):
        self.path = path

    def get_files(self):
        for address, dirs, files in os.walk(self.path):
            print(f"Address: {address}, dirs: {dirs}, files: {files}")