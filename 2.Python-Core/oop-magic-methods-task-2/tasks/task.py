class Bird:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} bird can walk and fly'

    def walk(self):
        return f'{self.name} bird can walk'

    def fly(self):
        return f'{self.name} bird can fly'


class FlyingBird(Bird):
    def __init__(self, name, ration='grains'):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return f'It eats mostly {self.ration}'


class NonFlyingBird(FlyingBird):
    def __init__(self, name, ration='fish'):
        super().__init__(name)
        self.ration = ration

    def __str__(self):
        return f'{self.name} bird can walk and swim'

    def fly(self):
        raise AttributeError(f'{self.name} object has no attribute \'fly\'')

    def swim(self):
        return f'{self.name} bird can swim'

class SuperBird(FlyingBird):
    def __init__(self, name, ration='fish'):
        super().__init__(name, ration)

    def __str__(self):
        return f'{self.name} bird can walk, swim and fly'

    def swim(self):
        return f'{self.name} bird can swim'


if __name__ == '__main__':
    b = Bird("Any")
    assert b.walk() == "Any bird can walk"
    p = NonFlyingBird("Penguin", "fish")
    assert p.swim() == "Penguin bird can swim"
    #assert p.fly() == #attributeerror
    assert p.eat() == "It eats mostly fish"
    c = FlyingBird("Canary")
    assert str(c) == "Canary bird can walk and fly"
    assert c.eat() == "It eats mostly grains"
    s = SuperBird("Gull")
    assert str(s) == "Gull bird can walk, swim and fly"
    assert s.eat() == "It eats mostly fish"