# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
list_of_cubes = []
for i in range(1, 1000):
    if i % 2 != 0:
        list_of_cubes.append(i ** 3)

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
sum_numbers_a = 0
for i in range(len(list_of_cubes)):
    number = list_of_cubes[i]
    sum_digits = 0
    while number % 10 != 0 or number // 10 != 0:
        sum_digits += number % 10
        number //= 10
    if sum_digits % 7 == 0:
        sum_numbers_a += list_of_cubes[i]
        print(list_of_cubes[i])
print(sum_numbers_a)

# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу, не создавая новый список
sum_numbers_b = 0
for i in range(len(list_of_cubes)):
    number = list_of_cubes[i] + 17
    sum_digits = 0
    while number % 10 != 0 or number // 10 != 0:
        sum_digits += number % 10
        number //= 10
    if sum_digits % 7 == 0:
        sum_numbers_b += (list_of_cubes[i] + 17)
        print(list_of_cubes[i] + 17)
print(sum_numbers_b)
