from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """
    abbr_dict = {"Dollar": "USD", "Euro": "EUR", "Pound": "GBP"}
    course_dict = {"Euro": 100, "Dollar": 50, "Pound": 1}

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        return (f"{Currency.course_dict[cls.__name__]/Currency.course_dict[other_cls.__name__]} "
                f"{Currency.abbr_dict[other_cls.__name__]} "
                f"for 1 {Currency.abbr_dict[cls.__name__]}")

    def to_currency(self, other_cls: Type[Currency]):
        rate = (Currency.course_dict[self.__class__.__name__] / Currency.course_dict[other_cls.__name__])
        converted_value = self.value * rate
        return other_cls(converted_value)

    def __add__(self, other):
        rate = (Currency.course_dict[other.__class__.__name__] / Currency.course_dict[self.__class__.__name__])
        sum_value = self.value + other.value * rate
        return self.__class__(sum_value)

    def __eq__(self, other):
        rate = (Currency.course_dict[other.__class__.__name__] / Currency.course_dict[self.__class__.__name__])
        print(self.value, other.value, rate, other.value * rate)
        return self.value == other.value * rate

    def __gt__(self, other):
        rate = (Currency.course_dict[other.__class__.__name__] / Currency.course_dict[self.__class__.__name__])
        return self.value > other.value * rate

    def __lt__(self, other):
        rate = (Currency.course_dict[other.__class__.__name__] / Currency.course_dict[self.__class__.__name__])
        return self.value < other.value * rate

class Euro(Currency):
    def __str__(self):
        return f'{self.value} EUR'


class Dollar(Currency):
    def __str__(self):
        return f'{self.value} USD'


class Pound(Currency):
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
    print(f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n")
    print(f"e.to_currency(Pound) = {e.to_currency(Pound)}\n")
    print(f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n")
    print(
        f"e + r  =>  {e + r}\n"
        f"r + d  =>  {r + d}\n"
        f"d + e  =>  {d + e}\n"
    )
    usd = Dollar(100)
    eur = Euro(50)
    print(usd == eur)