"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?
"""

import re

EMAIL = re.compile(r'[a-z0-9_.]+@[a-z0-9]+\.[a-z]+')


def email_parse(e_addr):
    src = EMAIL.match(e_addr)
    if src:
        email_dict = dict()
        username, domain = re.split(r'@', e_addr)
        email_dict['username'] = username
        email_dict['domain'] = domain
        return email_dict
    else:
        raise ValueError(f'wrong email: {e_addr}')


print(email_parse('rmnosipov@gmail.com'))
