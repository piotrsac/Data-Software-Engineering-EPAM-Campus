class Counter:
    def __init__(self, start = 0, stop = float('inf')):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.start < self.stop:
            self.start += 1
        else:
            print('Maximal value is reached.')

    def get(self):
        return self.start

if __name__ == '__main__':
    c=Counter(start = 42)
    c.increment()
    assert c.get() == 43

    c=Counter()
    c.increment()
    assert c.get() == 1
    c.increment()
    assert c.get() == 2

    c=Counter(start = 42, stop = 43)
    c.increment()
    assert c.get() == 43
    c.increment() #max value is reached
    assert c.get() == 43