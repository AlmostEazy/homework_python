"""Создать метакласс для паттерна Синглтон"""


class Singleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance


class Road(metaclass=Singleton):
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def mass(self):
        total = self._length * self._width * self.weight * \
                self.depth / 1000
        return print(f"Масса асфальта:\n{self._length} м * "
                     f"{self._width} м * {self.weight} кг * "
                     f"{self.depth} см =", total, "т")


a = Road(20, 5000, 25, 5)
b = Road(20, 5000, 25, 5)
c = Road(20, 5000, 25, 5)
print(a is b)
print(a is c)
print(b is c)
