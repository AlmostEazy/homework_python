# from timeit import timeit
# import numpy as np
# import time

# """
# Сортировка от меньшего к большему. Использование собственной функции
# sort_arr() и встроенной функции sorted()
# """
# from temp_func import sort_arr
#
# numbers = [5, 2, 3, 1, 4]
#
# print(timeit("sort_arr(numbers)", globals=globals()))
#
# print(timeit("sorted(numbers)", globals=globals()))
#
# """
# Встроенная функция гораздо быстрее.
# Для оптимизации лучше использовать ее.
#
# sort_arr(numbers): 1.323654
# sorted(numbers): 0.12952819999999998
# """
#
#
# """
# Возведение в отрицательную степень. Использование собственной функции
# my_func(), функции pow() и функции np.power()
# """
# from temp_func import my_func
#
# x = int(input("Введите основание степени: "))
# y = int(input("Введите отрицательный показатель степени: "))
#
# print(timeit("my_func(x, y)", globals=globals()))
# print(timeit("pow(x, y)", globals=globals()))
# print(timeit("np.power(np.float64(x), y)", globals=globals()))
#
# """
# Для результата 7 в степени -7. Для других чисел так же лучше
# использовать pow(), так как у нее самое быстрое время выполнения.
# Удивили результаты np.power(), читал, что он должен быть самым
# быстрым, поэтому и добавил в сравнение.
#
# my_func(x, y): 0.6350961000000002
# pow(x, y): 0.16703630000000036
# np.power(np.float64(x), y): 1.1168101999999998
# """
#
#
# """
# Перевод секунд в часы:минуты:секунды. Использование собственной
# функции calc_time() и встроенного модуля времени time.gmtime
# """
# from temp_func import calc_time
#
# a = int(input("Введите время в секундах: "))
#
# print(timeit("calc_time(a)", globals=globals()))
#
# time_format = time.strftime("%H:%M:%S", time.gmtime(a))
#
# print(timeit("time_format", globals=globals()))
#
# """
# Встроенный модуль гораздо быстрее. Для оптимизации скорости лучше
# использовать его.
#
# calc_time(a): 0.5356216999999996
# time_format: 0.014686500000000269
# """

# """
# Итог: Все собственные функции меняются на встроенные функции и задача
# выполняется быстрее
# """
