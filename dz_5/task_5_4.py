"""
Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
"""
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res = [src[i] for i in range(len(src)) if src[i] > src[i - 1]]
print(res)
