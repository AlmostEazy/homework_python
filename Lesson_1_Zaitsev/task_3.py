"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode
decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""


def change_type(some_list):
    arr = []

# проверяем список на наличие кириллицы. При нахождении - заносим в
# новый список

    for i in some_list:
        if not i.isascii():
            arr.append(i)

# если "отловленный" список не пуст, поднимаем ошибку и печатаем
# "слова - ошибки", иначе печатаем наш список

    if len(arr) != 0:
        raise ValueError(f"{arr} данные слова невозможно записать в "
                         f"байтовом типе")
    else:
        print(f"{some_list} данные слова можно записать в байтовом "
              f"типе")


my_list = ["attribute", "класс", "функция", "type"]
change_type(my_list)
