import os
import shutil
from random import randint

class TempDir:
    def __init__(self):
        self.wd_path = None
        self.temp_dir_path = None

    def __enter__(self):
        self.wd_path = os.getcwd()
        self.temp_dir = os.path.join(self.wd_path, str(randint(0,999999)))

        os.mkdir(self.temp_dir_path)
        os.chdir(self.temp_dir_path)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.wd_path)
        shutil.rmtree(self.temp_dir_path)