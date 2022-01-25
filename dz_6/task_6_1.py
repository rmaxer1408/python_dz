"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
    ...
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('173.255.199.22', 'GET', '/downloads/product_2'),
    ...
]
"""
from requests import utils, get
import pprint

response = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
src_list = []
with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    f.writelines(content)
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        a = line.split()
        src_list.append((a[0], a[5][1:], a[6]))
pprint.pprint(src_list)
