"""2) Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк."""

a = int(input("Введите время в секундах: "))
hours = a // 3600
minutes = a // 60 % 60
seconds = a % 60

if hours < 10:
    hours = "0" + str(hours)
if minutes < 10:
    minutes = "0" + str(minutes)
if seconds < 10:
    seconds = "0" + str(seconds)

print("Время на часах: {hours}:{minutes}:{seconds}".format(
    hours=hours, minutes=minutes, seconds=seconds
    )
)
