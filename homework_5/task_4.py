"""4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл."""


def rewrite_file():
    n = {"One": "Один", "Two": "Два", "Three": "Три",
         "Four": "Четыре"}
    new_text = []

    try:
        with open("text_4.txt", "r+", encoding="utf8") as file:
            with open("new_text_4.txt", "w", encoding="utf8") as \
                    new_file:
                el = file.readlines()
                for i in el:
                    i = i.split(" ", 1)
                    new_text.append(n[i[0]] + " " + i[1])
                new_file.writelines(new_text)
    except FileNotFoundError:
        return "Файл не найден."


rewrite_file()
