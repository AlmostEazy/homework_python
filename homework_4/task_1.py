"""1) Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать
формулу: (выработка в часах*ставка в час) + премия. Для выполнения
расчета для конкретных значений необходимо запускать скрипт с
параметрами."""

from sys import argv

script_name, working_time, rate_per_hour, cash_bonus = argv

print("Имя скрипта: ", script_name)
print("Сотрудник отработал (часов): ", working_time)
print("Ставка в час: ", rate_per_hour)
print("Премия: ", cash_bonus)
print("Зарплата сотрудника: ", (float(working_time) *
      float(rate_per_hour)) + float(cash_bonus))
