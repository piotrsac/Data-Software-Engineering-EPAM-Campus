from time import time, sleep

def log(fn):
    """
    Add your code here or call it from here   
    """
    file=open('log.txt','a')
    def wrapper(*args, **kwargs):
        time_start = time()
        fn(*args, **kwargs)
        execution_time = time() - time_start
        # line = [f'{fn.__name__}; args:{args}; kwargs:{kwargs}; execution_time: {execution_time}sec.\n']
        arg_str = ', '.join(f'{arg}' for arg in args)
        kwarg_str = ', '.join(f'{key}={value}' for key,value in kwargs.items())
        file.write(f'{fn.__name__}; args: {arg_str}; kwargs: {kwarg_str}; execution_time: {execution_time} sec.\n')
    return wrapper

@log
def foo(a, b, c):
    sleep(0.2)
    return a + b + c/a + c/b * 5/a

foo(1, 2, c=3)

"""
Example of using
@log
def foo(a, b, c):
    ...

foo(1, 2, c=3)
log.txt
...
foo; args: a=1, b=2; kwargs: c=3; execution time: 0.12 sec.
..."""
