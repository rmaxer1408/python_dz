"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи —
верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
"""

import os
from collections import defaultdict

sizes = []
cur_path = './'
for r, d, f in os.walk(cur_path):
    for file in f:
        file_path = os.path.join(r, file)
        sizes.append(os.stat(file_path).st_size)
max_size = max(sizes)
size_dict = defaultdict(int)
for size in sorted(sizes):
    size_dict[10 ** len(str(size))] += 1
print((dict(size_dict)))
