import functools


def validate(func):
    def wrapper(*args):
        for arg in args:
            if arg < 0 or arg > 256:
                return "Function call is not valid!"
        else:
            func(*args)
            return "Pixel created!"
    return wrapper

@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"

if __name__ == '__main__':
    assert set_pixel(1, 2, 3) == "Pixel created!"
    assert set_pixel(256, 256, 256) == "Pixel created!"
    assert set_pixel(0, 0, 0) == "Pixel created!"
    assert set_pixel(-1, 2, 4) == "Function call is not valid!"
    assert set_pixel(1, -2, 5) == "Function call is not valid!"
    assert set_pixel(1, 2, -6) == "Function call is not valid!"
    assert set_pixel(257, 2, 7) == "Function call is not valid!"
    assert set_pixel(1, 257, 8) == "Function call is not valid!"
    assert set_pixel(1, 2, 257) == "Function call is not valid!"
