from time import time
from time import sleep
from typing import Dict

execution_time: Dict[str, float] = {}

def time_decorator(fn):
    """
    Create a decorator function `time_decorator`
    which has to calculate decorated function execution time
    and put this time value to `execution_time` dictionary where `key` is
    decorated function name and `value` is this function execution time.
    """
    def wrapper(*args, **kwargs):
        time_start = time()
        result = fn(*args, **kwargs)
        execution_time[fn.__name__] = time() - time_start
        return result

    return wrapper

@time_decorator
def func_add(a, b):
    sleep(0.2)
    return a + b

# print(func_add(1, 2))
# print(execution_time)

