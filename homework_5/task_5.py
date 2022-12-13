"""5) Создать (программно) текстовый файл, записать в него программно
набор чисел, разделенных пробелами. Программа должна подсчитывать сумму
чисел в файле и выводить ее на экран."""


def rewrite_file():
    try:
        with open("text_5.txt", "w+") as file:

            line = input("Введите цифры через пробел: ")

            file.writelines(line)
            res = line.split()

            print(sum(map(int, res)))

    except FileNotFoundError:
        return "Файл не найден."


rewrite_file()
