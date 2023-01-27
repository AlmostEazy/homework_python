"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""


def check_info(some_list):
    for i in some_list:
        print(type(i))
        print(i)
        print(len(i))


my_list = [b"class", b"function", b"method"]
check_info(my_list)
