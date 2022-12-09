"""4) Представлен список чисел. Определить элементы списка, не имеющие
повторений. Сформировать итоговый массив чисел, соответствующих
требованию. Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор."""

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print(f"Исходные элементы:\n{my_list}\n")

new_list = [i for i in my_list if my_list.count(i) == 1]

print(f"Неповторяющиеся элементы:\n{new_list}")
