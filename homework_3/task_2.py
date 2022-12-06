"""2) Реализовать функцию, принимающую несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон. Функция должна принимать параметры как именованные
аргументы. Реализовать вывод данных о пользователе одной строкой."""


def personal_information(name, lastname, birth_year, city, email,
                         phone_number):
    print(f"Имя: {name}, Фамилия: {lastname}, "
          f"Год рождения: {birth_year}, Город: {city}, Почта: {email}, "
          f"Телефон: {phone_number}")


personal_information(name=input("Введите имя: "),
                     lastname=input("Введите фамилию: "),
                     birth_year=int(input("Введите год рождения: ")),
                     city=input("Введите город проживания: "),
                     email=input("Введите email: "),
                     phone_number=int(input("Введите телефон: ")))
