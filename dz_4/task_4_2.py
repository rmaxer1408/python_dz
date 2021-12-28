"""
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и
возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
"""
from requests import get, utils
from decimal import Decimal

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
trans_table = str.maketrans({
    '>': ' ',
    '<': ' ',
    '/': ' '
})
trans_table_val = str.maketrans(',', '.')
content = content.translate(trans_table)
content_list = content.split()[8:]
print(content_list)


def currency_rates(currency: str):
    currency = currency.upper()
    if currency not in content_list:
        return
    char_code_index = content_list.index(currency)
    nominal_index = char_code_index + 3
    nominal = Decimal(content_list[nominal_index])
    v_index = content_list[nominal_index:].index('Value')
    value_index = v_index + nominal_index + len(content_list[nominal_index:v_index]) + 1
    print(value_index)
    value_cur = Decimal(content_list[value_index].translate(trans_table_val))
    return Decimal(value_cur / nominal)


print(currency_rates('eur'))
