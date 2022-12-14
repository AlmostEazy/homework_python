"""3) Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов (не менее 10 строк). Определить, кто
из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32"""

with open("text_3.txt", "r", encoding="utf8") as my_file:
    salary = []
    low_salary = []
    new_list = my_file.read().split("\n")

    for i in new_list:
        i = i.split()
        if int(i[1]) < 20000:
            low_salary.append(i[0])
        salary.append(i[1])

print(f"Оклад меньше 20.000: {low_salary}.\n"
      f"Cредний доход сотрудников: "
      f"{sum(map(int, salary)) / len(salary)}")
