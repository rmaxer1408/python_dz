from requests import get, utils
from decimal import Decimal
from datetime import date


def currency_rates(currency: str):
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
    currency = currency.upper()
    if currency not in content_list:
        return
    char_code_index = content_list.index(currency)
    nominal_index = char_code_index + 3
    nominal = Decimal(content_list[nominal_index])
    v_index = content_list[nominal_index:].index('Value')
    value_index = v_index + nominal_index + len(content_list[nominal_index:v_index]) + 1
    value_cur = Decimal(content_list[value_index].translate(trans_table_val))
    cur = Decimal(value_cur / nominal).quantize(Decimal('1.00'))
    date_el = content.split()[4]
    date_el = date_el[6:16].split('.')
    date_cur = date(year=int(date_el[2]), month=int(date_el[1]), day=int(date_el[0]))
    return f'{cur} {date_cur}'


if __name__ == '__main__':
    print(currency_rates('usd'))