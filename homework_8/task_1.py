"""Задание 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку
конструктора класса (метод init()), который должен принимать данные
(список списков) для формирования матрицы. [[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д."""

# import numpy as np


class Matrix:

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return str("\n".join(["\t".join([str(el) for el in i])
                              for i in self.my_list]))

    # def __add__(self, other):
    #     for i in range(len(self.my_list)):
    #         for j in range(len(other.my_list[i])):
    #             self.my_list[i][j] = self.my_list[i][j] + \
    #                                  other.my_list[i][j]
    #     return Matrix.__str__(self)

    def __add__(self, other):
        for i, _ in enumerate(self.my_list):
            for j, _ in enumerate(other.my_list):
                self.my_list[i][j] = self.my_list[i][j] + \
                                     other.my_list[i][j]
        return Matrix.__str__(self)


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(m.__add__(new_m))


"""
Тест numpy
"""

# m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# new_m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# sum_m = m + new_m
# print(sum_m)
