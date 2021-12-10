# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
words = ['процент', 'процента', 'процентов']
for index in range(1, 101):
    mod = index % 10
    if mod == 1 and index != 11:
        print(f'{index} {words[0]}')
    elif (mod == 2 or mod == 3 or mod == 4) and index != 12 and index != 13 and index != 14:
        print(f'{index} {words[1]}')
    else:
        print(f'{index} {words[2]}')
