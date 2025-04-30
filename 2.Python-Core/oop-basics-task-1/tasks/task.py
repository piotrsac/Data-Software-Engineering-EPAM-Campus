class Field:
    __value = None

    def __init__(self):
        self.__value = None

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

if __name__ == '__main__':
    test_object = Field()
    assert test_object.get_value() is None
    test_object.set_value(50)
    assert test_object.get_value() == 50