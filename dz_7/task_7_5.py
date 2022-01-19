"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же, а значения —
кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
    {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""

import os
import json

sizes = []
cur_path = './'
for r, d, f in os.walk(cur_path):
    for file in f:
        f_path = os.path.join(r, file)
        sizes.append((f_path.split('.')[-1], os.stat(f_path).st_size))
max_size = max(sizes, key=lambda x: x[1])[1]
i = 1
src = {}
for _ in range(len(str(max_size))):
    i *= 10
    src[i] = (0, [])
for size in sizes:
    num, file_ext = src[10 ** len(str(size[1]))]
    file_ext.append(size[0])
    file_ext = list(set(file_ext))
    src[10 ** len(str(size[1]))] = (num + 1, file_ext)

print(src)

with open(os.path.basename(os.getcwd()) + '_summary.json', 'w') as f_json:
    json.dump(src, f_json)
