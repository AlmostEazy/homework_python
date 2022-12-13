"""2) Создать текстовый файл (не программно), сохранить в нем несколько
строк, выполнить подсчет количества строк, количества слов в каждой
строке."""


def count_lines_words():
    try:
        with open("text_2.txt", "r") as file:
            first_list = file.readlines()

            for i in range(len(first_list)):
                second_list = first_list[i].split()

                print(f"В {i + 1}-ой строке - {len(second_list)} "
                      f"слов(а)\n")

            print(f"Количество строк в файле: {len(first_list)}.")

    except FileNotFoundError:
        return "Файл не найден."


count_lines_words()
