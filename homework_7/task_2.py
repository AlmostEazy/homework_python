"""2) Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны
передаваться при создании экземпляра класса. Атрибуты сделать
защищенными. Определить метод расчета массы асфальта, необходимого для
покрытия всего дорожного полотна. Использовать формулу: длинаширинамасса
асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1
см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т"""


class Road:
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


r = Road(20, 5000, 25, 5)
r.mass()
