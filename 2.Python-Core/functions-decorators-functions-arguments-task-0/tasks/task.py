from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    return dict([(i+1, (i+1)**2) for i in range(num)])

"""
>>> generate_squares(5)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
if __name__ == '__main__':
    assert generate_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
