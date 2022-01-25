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
import yaml

with open("config.yaml", encoding='utf-8') as f_yaml:
    structure = yaml.safe_load(f_yaml)
print(structure)


def project_src(src):
    for folder, src_tmps in src.items():
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)
        for src_tmp in src_tmps:
            if isinstance(src_tmp, dict):
                project_src(src_tmp)
            else:
                if not os.path.exists(src_tmp):
                    if '.' in src_tmp:
                        with open(src_tmp, 'w') as f:
                            f.write('')
    else:
        os.chdir('../')


project_src(structure)
