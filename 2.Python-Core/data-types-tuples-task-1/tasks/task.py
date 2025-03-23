from typing import Tuple
from math import log10

def get_tuple(num: int) -> Tuple[int]:
    if num==0:
        n=1
    else:
        n=int(log10(abs(num)))+1
    t=[]
    for i in range(n):
        t.append(num%10)
        num=num//10
    t.reverse()

    return tuple(t)

if __name__ == '__main__':
    assert get_tuple(87178291199) == (8,7,1,7,8,2,9,1,1,9,9)
