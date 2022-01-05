"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
"""


def generator_odd(n: int):
    for i in range(1, n + 1, 2):
        yield i


gen_odd = generator_odd(5)
print(next(gen_odd))
print(next(gen_odd))
print(next(gen_odd))
