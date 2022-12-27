"""Задание 3. Создайте собственный класс-исключение, обрабатывающий
ситуацию деления на нуль."""


class CustomError(Exception):
    def __init__(self, txt):
        self.txt = txt


def division(x, y):
    try:
        x = int(x)
        y = int(y)
        if y == 0:
            raise CustomError("Деление на ноль!")
        else:
            result = x / y
            return result
    except ValueError:
        return "Вы ввели не число!"


"""3) Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
 Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""


def sum_numbers(first_n):

    second_n = first_n + first_n
    third_n = first_n + first_n + first_n
    count = int(first_n) + int(second_n) + int(third_n)

    return count


"""4) Программа принимает действительное положительное число x и целое
отрицательное число y. Необходимо выполнить возведение числа x в степень
y."""


def my_func(a, b):
    count = 1
    result = 1 / a
    while count < abs(b):
        result *= 1 / a
        count += 1
    return result


"""4) Представлен список чисел. Определить элементы списка, не имеющие
повторений."""


def n_list(some_list):

    new_list = [i for i in some_list if some_list.count(i) == 1]

    return new_list




