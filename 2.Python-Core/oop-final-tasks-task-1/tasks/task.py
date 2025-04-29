class Sun:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if Sun._instance is not None:
            raise RuntimeError("Use 'Sun.inst()' to get the instance")

    @classmethod
    def inst(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance


if __name__ == '__main__':
    p = Sun.inst()
    f = Sun.inst()
    assert (p is f) is True