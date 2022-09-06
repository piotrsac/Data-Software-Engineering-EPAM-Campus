from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    res = []
    for x in range(1, n + 1):
        y = ""
        if x % 3 == 0:
            y = "Fizz"
        if x % 5 == 0:
            y += "Buzz"
        if y:
            res.append(y)
        else:
            res.append(x)

    return res
