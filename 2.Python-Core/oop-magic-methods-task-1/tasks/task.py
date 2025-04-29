from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values

    def __add__(self, string):
        return [f'{value} {string}' for value in self.values ]


if __name__ == '__main__':
    assert Counter([1, 2, 3]) + "mississippi" == ["1 mississippi", "2 mississippi" , "3 mississippi"]