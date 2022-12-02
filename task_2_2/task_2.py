"""2) Для списка реализовать обмен значений соседних элементов, т.е.
значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию
input()."""


def revert(some_list):
    for i in range(0, len(some_list) - 1, 2):
        some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
    return some_list


random_list = list(map(int, input("Введите значения списка: ").split()))
revert_list = revert(random_list)

print(f"Мы получаем: {revert_list}")
