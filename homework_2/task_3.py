"""3) Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить
к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""

# Решение с использованием list

# seasons_list = ["Зима", "Весна", "Лето", "Осень"]
# month_number = int(input("Введите номер месяца: "))
#
# if month_number == 12 or 1 <= month_number <= 2:
#     print(f"Это {seasons_list[0]}!")
# elif month_number <= 5:
#     print(f"Это {seasons_list[1]}!")
# elif month_number <= 8:
#     print(f"Это {seasons_list[2]}!")
# elif month_number <= 11:
#     print(f"Это {seasons_list[3]}!")
# else:
#     print(f"Вы ввели несуществующий месяц!")

# Решение с использованием dict

seasons_dict = \
    {
        1: "Зима",
        2: "Весна",
        3: "Лето",
        4: "Осень"
    }

month_number = int(input("Введите номер месяца: "))

if month_number == 12 or 1 <= month_number <= 2:
    print(f"Это {seasons_dict[1]}!")
elif month_number <= 5:
    print(f"Это {seasons_dict[2]}!")
elif month_number <= 8:
    print(f"Это {seasons_dict[3]}!")
elif month_number <= 11:
    print(f"Это {seasons_dict[4]}!")
else:
    print(f"Вы ввели несуществующий месяц!")
