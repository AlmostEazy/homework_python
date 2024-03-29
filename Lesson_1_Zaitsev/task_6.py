"""
Задание 6.

Создать  НЕ программно (вручную) текстовый файл test_file.txt, заполнить
его тремя строками:
«сетевое программирование», «сокет», «декоратор».

Принудительно программно открыть файл в формате Unicode и вывести его
содержимое.
Что это значит? Это значит, что при чтении файла вы должны явно указать
кодировку utf-8
и файл должен открыться у ЛЮБОГО!!! человека при запуске вашего скрипта.

При сдаче задания в папке должен лежать текстовый файл!

Это значит вы должны предусмотреть случай, что вы по дефолту записали
файл в cp1251,
а прочитать пытаетесь в utf-8.

Преподаватель будет запускать ваш скрипт и ошибок НЕ ДОЛЖНО появиться!

Подсказки:
--- обратите внимание, что заполнять файл вы можете в любой кодировке
но открыть нужно ИМЕННО!!! в формате Unicode (utf-8)
--- обратите внимание на чтение файла в режиме rb
для последующей переконвертации в нужную кодировку

НАРУШЕНИЕ обозначенных условий - задание не выполнено!!!
"""

import chardet


def encoding_convert():
    with open("test_file.txt", "rb") as my_file:
        content_bytes = my_file.read()
    detected = chardet.detect(content_bytes)
    print(detected)
    encoding = detected["encoding"]
    content_text = content_bytes.decode(encoding)
    with open("test_file.txt", "w", encoding="utf-8") as my_file:
        my_file.write(content_text)


encoding_convert()

with open("test_file.txt", encoding="utf-8") as file:
    content = file.read()
    print(content)
