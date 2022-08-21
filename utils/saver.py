import os
import shutil

import matplotlib.pyplot as plt


class Saver:

    directory_path = ""
    file_path = ""

    # save options
    file_rw_option = "w"  # overwrites existing file each time init method is called
    data_rw_option = "a"  # appends to existing file each time save method is called

    def __init__(self) -> None:
        pass

    def save_img(self, name) -> None:
        img_path = os.path.join(self.directory_path, name)
        plt.savefig(img_path)

    def init_folder(self, path: str) -> None:
        self.directory_path = path
        self.create_folder(self.directory_path)

    def init_file(self, path: str, file: str) -> None:
        self.directory_path = path
        self.create_folder(self.directory_path)
        self.init(file)

    def create_folder(self, folder: str) -> None:
        if os.path.exists(folder):
            return
        os.makedirs(folder)

    def init(self, file: str) -> None:
        self.file_path = os.path.join(self.directory_path, file)
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        open(self.file_path, self.file_rw_option)

    def save(self, lines: list) -> None:
        file = open(self.file_path, self.data_rw_option)
        for line in lines:
            file.write(str(line))
            file.write(',')
        file.write('\n')
