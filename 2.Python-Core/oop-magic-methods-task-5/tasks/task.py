import os
import shutil
import tempfile
from random import randint

class TempDir:
    def __init__(self):
        self.wd_path = None
        self.temp_dir_path = None

    def __enter__(self):
        dir_name = randint(0,9999999)
        os.mkdir(f'{tempfile.gettempdir()}/{dir_name}')
        self.temp_dir_path = f'{tempfile.gettempdir()}/{dir_name}'
        self.wd_path = os.getcwd()
        os.chdir(self.temp_dir_path)

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.wd_path)
        shutil.rmtree(self.temp_dir_path)