# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }


def thesaurus(*args):
    """args in dict"""
    dict_name = {}
    for i in range(len(args)):
        key = args[i][0]
        val = list(filter(lambda name: name.startswith(key), args))
        dict_name.setdefault(key, val)
    return dict_name


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
