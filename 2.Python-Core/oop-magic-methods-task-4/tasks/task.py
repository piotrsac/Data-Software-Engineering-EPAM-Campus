class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        try:
            return instance.__dict__[self.private_name]
        except KeyError:
            raise AttributeError(f'{owner.__name__} has no attribute {self.private_name}')

    def __set__(self, instance, value):
        if value < 0 or value > 100:
            raise ValueError('Price must be between 0 and 100')
        instance.__dict__[self.private_name] = value


class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """
    def __set_name__(self, owner, name):
        self.private_name = "_" + name
        self.public_name = name.capitalize()

    def __get__(self, instance, owner):
        try:
            return instance.__dict__[self.private_name]
        except KeyError:
            raise AttributeError(f'{owner.__name__} has no attribute {self.private_name}')

    def __set__(self, instance, value):
        if self.private_name in instance.__dict__:
            raise ValueError(f'{self.public_name} can not be changed.')
        instance.__dict__[self.private_name] = value


class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price


if __name__ == '__main__':
    b = Book('William Shakespeare', 'Macbeth', 70)
    print(b.author)
    print(b.name)
    print(b.price)
    b.author = "Adam Mickiewicz"