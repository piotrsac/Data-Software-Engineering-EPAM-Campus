from contextlib import ContextDecorator
import datetime
from time import time as t_time


class LogFile(ContextDecorator):
    def __init__(self, filename):
        self.filename = filename
        self.mode = "a"
        self.file = None
        self.start_datetime = datetime.datetime.now()
        self.start_time = t_time()

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        run_time = datetime.timedelta(seconds = t_time() - self.start_time)
        self.file.write(f'Start: {self.start_datetime} | Run: {run_time} | An error occurred: {exc_val}')
        self.file.close()


if __name__ == "__main__":
    pass