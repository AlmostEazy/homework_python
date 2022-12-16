from memory_profiler import memory_usage
from functools import reduce
from random import randint


# def memory(func):
#     def wrapper(*args, **kwargs):
#         m1 = memory_usage()
#         res = func(*args)
#         m2 = memory_usage()
#         mem_diff = m2[0] - m1[0]
#         print(f"Выполнение заняло {mem_diff} Mib")
#         return res
#
#     return wrapper
#
#
# """
# Поиск четных чисел от 100 до 1000 и их произведение.
# """
#
#
# @memory
# def check_numbers():
#     my_list = [i for i in range(100, 1001, 2)]
#
#     print(f"Список чётных чисел в диапазоне [100..1000]:\n
#     {my_list}\n")
#     print(f"Произведение всех элементов списка:"
#           f"\n{reduce(lambda x, y: x * y, my_list)}")
#
#
# check_numbers()
#
#
# @memory
# def check_numbers():
#     my_list = filter(lambda x: x % 2 == 0, range(100, 1001))
#
#     print(f"Список чётных чисел в диапазоне [100..1000]:\n
#     {my_list}\n")
#     print(f"Произведение всех элементов списка:"
#           f"\n{reduce(lambda x, y: x * y, my_list)}")
#
#
# check_numbers()
#
# """
# Выполнение с помощью filter() заняло меньше памяти.
# Выполнение заняло 0.0234375 Mib
# Выполнение заняло 0.00390625 Mib
# """

