"""1) Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль."""


def divide(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        return "Деление на ноль!"


first_arg = int(input("Введите делимое: "))
second_arg = int(input("Введите делитель: "))

print(f"Результат деления: {divide(first_arg, second_arg)}")
