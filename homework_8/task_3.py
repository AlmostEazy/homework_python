"""Задание 3. Создайте собственный класс-исключение, обрабатывающий
ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе
пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой."""


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
    except CustomError as err:
        return err


divisible = input("Введите делимое: ")
divisor = input("Введите делитель: ")

print(division(divisible, divisor))
