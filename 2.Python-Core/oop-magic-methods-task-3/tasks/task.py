from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Type


class Currency(ABC):
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """
    @property
    @abstractmethod
    def abbr(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def conv_rate(self) -> int:
        raise NotImplementedError

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def rate(cls, other_cls: Type[Currency]) -> float:
        return cls.conv_rate / other_cls.conv_rate

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        return (f"{cls.rate(other_cls)} "
                f"{other_cls.abbr} "
                f"for 1 {cls.abbr}")

    def to_currency(self, other_cls: Type[Currency]) -> Currency:
        converted_value = self.value * self.rate(other_cls)
        return other_cls(converted_value)

    def __str__(self) -> str:
        return f'{self.value} {self.abbr}'

    def __add__(self, other) -> Currency:
        sum_value = self.value + other.value * other.rate(self)
        return self.__class__(sum_value)

    def __eq__(self, other) -> bool:
        return self.value == other.value * other.rate(self)

    def __gt__(self, other) -> bool:
        return self.value > other.value * other.rate(self)

    def __lt__(self, other) -> bool:
        return self.value < other.value * other.rate(self)


class Euro(Currency):
    abbr = "EUR"
    conv_rate = 100


class Dollar(Currency):
    abbr = "USD"
    conv_rate = 50


class Pound(Currency):
    abbr = "GBP"
    conv_rate = 1


if __name__ == "__main__":
    e = Euro(100)
    r = Pound(100)
    d = Dollar(200)
    assert f'e = {e}' == "e = 100 EUR"
    assert Euro.course(Pound) == "100.0 GBP for 1 EUR"
    assert Dollar.course(Pound) == "50.0 GBP for 1 USD"
    assert Pound.course(Euro) == "0.01 EUR for 1 GBP"
    assert f'{e.to_currency(Dollar)}' == "200.0 USD"
    assert f'{e.to_currency(Pound)}' == "10000.0 GBP"
    assert f'{e.to_currency(Euro)}' == "100.0 EUR"
    assert f'{e + r}' == "101.0 EUR"
    assert f'{r + d}' == "10100.0 GBP"
    assert f'{d + e}' == "400.0 USD"
    usd = Dollar(100)
    eur = Euro(50)
    assert (usd == eur) is True
    assert (e == r) is False
    assert (e > r) is True
    assert (e < r) is False