"""
*(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html


Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
(не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""

import os

with open('config.yaml', encoding='utf-8') as cfg:
    src = cfg.readlines()
flag = [0] * (len(src) + 1)
mark = [0] * (len(src) + 1)
parent = src[0].strip('\n:')
for i in range(len(src)):
    src[i] = src[i].strip('\n:')
    flag[i] = (len(src[i]) - len(src[i].strip()))
    mark[i] = int((flag[i] - flag[i + 1]) / 2)
    marker = mark[i] - mark[i + 1]
    if marker == 1:
        parent = src[i].strip()
        child = src[i + 1].strip()
        path = os.path.join(parent, child)
        os.makedirs(path, exist_ok=True)
    elif marker == 0:
        child = src[i-1].strip(' :\n')
        path = os.path.join(parent, child)
        os.makedirs(path, exist_ok=True)
    print(src[i], marker)