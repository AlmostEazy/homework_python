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
        length = self._length
        width = self._width
        weight = self.weight
        depth = self.depth
        total = length * width * weight * depth / 1000
        return print(f"Масса асфальта:\n{length} м * {width} м * "
                     f"{weight} кг * {depth} см = ", total, "т")


r = Road(20, 5000, 25, 5)
r.mass()
