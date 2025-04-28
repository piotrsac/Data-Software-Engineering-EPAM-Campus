from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """
    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        abbr = {"Dollar" : "USD", "Euro" : "EUR", "Pound" : "GBP"}
        course = {"Dollar" : 50, "Euro" : 100, "Pound" : 1}
        return (f"{course[cls.__name__]/course[other_cls.__name__]} {abbr[other_cls.__name__]} "
                f"for 1 {abbr[cls.__name__]}")

    def to_currency(self, other_cls: Type[Currency]):
        raise NotImplementedError


class Euro(Currency):
    def __init__(self, value: float):
        super().__init__(value)

    def __str__(self):
        return f'{self.value} EUR'


class Dollar(Currency):
    def __init__(self, value: float):
        super().__init__(value)

    def __str__(self):
        return f'{self.value} USD'


class Pound(Currency):
    def __init__(self, value: float):
        super().__init__(value)

    def __str__(self):
        return f'{self.value} GBP'


if __name__ == "__main__":
    e = Euro(100)
    r = Pound(100)
    d = Dollar(200)
    print(f'e = {e}\n')
    print(Euro.course(Pound))
    print(Dollar.course(Pound))
    print(Pound.course(Euro))
