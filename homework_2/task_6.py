"""6) *Реализовать структуру данных «Товары». Она должна представлять
собой список кортежей. Каждый кортеж хранит информацию об отдельном
товаре. В кортеже должно быть два элемента — номер товара и словарь с
параметрами (характеристиками товара: название, цена, количество,
единица измерения). Структуру нужно сформировать программно, т.е.
запрашивать все данные у пользователя."""

products = []

for i in range(1, 4):

    print(f"Введите данные по {i}-му товару")

    product_name = input("Название: ")
    product_price = int(input("Цена: "))
    product_count = int(input("Количество: "))
    product_measure = input("Единица измерения: ")
    products.append((i, {'название': product_name,
                         'цена': product_price,
                         'количество': product_count,
                         'eд': product_measure}))

print(f"Cписок товаров: \n{products}")

product_names = []
product_prices = []
product_counts = []
product_measures = []

for i in products:
    product_names.append(i[1].get('название'))
    product_prices.append(i[1].get('цена'))
    product_counts.append(i[1].get('количество'))
    product_measures.append(i[1].get('eд'))

report = \
    {
        'название': list(set(product_names)),
        'цена': list(set(product_prices)),
        'количество': list(set(product_counts)),
        'eд': list(set(product_measures))
    }

print(f"Ваш отчет: \n{report}")
