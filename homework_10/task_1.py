"""Создать не менее двух дескрипторов для атрибутов классов, которые вы
создали ранее в ДЗ"""


class ValidationString:
    def __set__(self, instance, value):
        if type(value) != str:
            raise TypeError(f"Вы должны использовать строки!")
        elif not value.istitle():
            raise ValueError(f"Пишите с заглавной буквы!")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class ValidationNumber:
    def __set__(self, instance, value):
        if type(value) not in (int, float):
            raise TypeError(f"Вы должны использовать числа!")
        elif value < 0:
            raise ValueError(f"Числа не могут быть отрицательными!")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = ValidationString()
    surname = ValidationString()
    position = ValidationString()
    wage = ValidationNumber()
    bonus = ValidationNumber()
    
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self.wage + self.bonus


information = Position("Иван", "Иванов", "Инженер", 30000, 20000)
print(information.get_full_name())
print(information.position)
print(information.get_total_income())

# Проверка
# information.bonus = -30000.25
# print(information.get_total_income())

# information.name = "иван"
# print(information.get_full_name())
