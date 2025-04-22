class HistoryDict:
    def __init__(self, dictionary = None) -> None:
        self.dictionary = dictionary
        self.history = []
        self.index = 0
    def set_value(self, key, value):
        self.dictionary[key] = value
        self.index += 1
        if self.index > 5:
            self.history[(self.index % 5) - 1] = key
        else:
            self.history.append(key)
    def get_history(self):
        return [self.history[(i + self.index) % len(self.history)] for i in range(len(self.history))]
        #return in order: first is the oldest one, last is the freshest (latest)

if __name__ == '__main__':
    d = HistoryDict({"foo": 42})
    d.set_value("bar", 43)
    assert d.get_history() == ["bar"]
    d.set_value("foo", 44)
    assert d.get_history() == ["bar", "foo"]