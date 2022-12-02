"""5) Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел. У пользователя необходимо
запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
с одинаковыми значениями, то новый элемент с тем же значением должен
разместиться после них."""

rating = [7, 5, 3, 3, 2]

rating_number = int(input("Введите Вашу оценку: "))

for i in range(len(rating)):
    if rating_number == rating[i]:
        rating.insert(i + 1, rating_number)
        break
    elif rating_number > rating[0]:
        rating.insert(0, rating_number)
    elif rating_number < rating[-1]:
        rating.append(rating_number)
    elif rating[i] > rating_number > rating[i + 1]:
        rating.insert(i + 1, rating_number)
        break

print(f"Текущий рейтинг: {rating}")
