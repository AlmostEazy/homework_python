"""3) Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов."""


def my_func(a, b, c):
    print(f"Сумма наибольших двух аргументов: "
          f"{a + b + c - min(a, b, c)}")


first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))
third_num = int(input("Введите третье число: "))

my_func(first_num, second_num, third_num)
