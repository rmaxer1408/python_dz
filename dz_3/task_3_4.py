# *Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
# и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
# реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
# Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }


def thesaurus(*args):
    dict_name = {}
    for i in range(len(args)):
        key = args[i][0]
        val = list(filter(lambda name: name.startswith(key), args))
        dict_name.setdefault(key, val)
    return dict_name


def thesaurus_adv(*args):
    dict_names = {}
    for i in range(len(args)):
        list_name = args[i].split()
        key_one = list_name[1][0]
        val = filter(lambda name: (name.split())[1].startswith(key_one), args)
        dict_names.setdefault(key_one, thesaurus(*val))
    return dict_names


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
