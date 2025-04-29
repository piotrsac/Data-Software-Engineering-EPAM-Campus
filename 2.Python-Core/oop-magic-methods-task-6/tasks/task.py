import os


class Cd:
    def __init__(self, pointed_directory):
        self.original_path = None
        if not os.path.isdir(pointed_directory):
            raise ValueError
        self.pointed_directory = pointed_directory

    def __enter__(self):
        self.original_path = os.getcwd()
        os.chdir(self.pointed_directory)

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.original_path)