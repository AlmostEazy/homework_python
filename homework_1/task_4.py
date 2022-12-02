"""4) Пользователь вводит целое положительное число. Найдите самую
большую цифру в числе. Для решения используйте цикл while и
арифметические операции."""

n = abs(int(input("Введите число: ")))

temp = n
max_digit = temp % 10

while temp > 0:
    temp = temp // 10
    if temp % 10 > max_digit:
        max_digit = temp % 10

print(f"Самая большая цифра в числе {n}: {max_digit}")
