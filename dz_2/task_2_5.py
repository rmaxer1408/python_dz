# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
prices = [57.8, 46.51, 97, 304.3, 79.15, 3024.5, 477, 170, 2099, 360, 120.5, 440.78, 11.1, 151.9, 549.9, 981.71, 354.84]

# a. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
for i in range(len(prices)):
    if i == len(prices) - 1:
        print(f'{int(prices[i])} руб {int((prices[i] - int(prices[i])) * 100):02d} коп')
    else:
        print(f'{int(prices[i])} руб {int((prices[i] - int(prices[i])) * 100):02d} коп', end=', ')

# b. Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
a = id(prices)
prices.sort()
b = id(prices)
print(f'id списка до сортировки: {a}, id списка после сортровки {b}')
print(prices)

# c. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
prices_new = prices[::-1]
print(prices_new)

# d. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print(prices_new[:5])