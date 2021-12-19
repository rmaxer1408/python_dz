"""
*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""
n = int(input('Enter n: '))
gen_odd = (num for num in range(1, n + 1, 2))

print(next(gen_odd))
print(next(gen_odd))
print(next(gen_odd))