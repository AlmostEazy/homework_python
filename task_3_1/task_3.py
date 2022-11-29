"""3) Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
 Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""

first_n = input("Введите число n: ")
second_n = first_n + first_n
third_n = first_n + first_n + first_n
count = int(first_n) + int(second_n) + int(third_n)

print(f"Ваши значения: {first_n}, {second_n}, {third_n}")
print(f"Значение выражения n + nn + nnn = {count}")
