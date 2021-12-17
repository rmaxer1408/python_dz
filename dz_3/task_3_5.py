"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""
from random import choices, sample


def get_jokes(n: int, flag=0):
    """
    Return n jokes from three lists.
    If flag=0 takes uniq words from list.
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if flag == 0:
        if n > len(nouns):
            print('No uniq words')
            return
        else:
            noun = sample(nouns, k=n)
            adverb = sample(adverbs, k=n)
            adjective = sample(adjectives, k=n)
    else:
        noun = choices(nouns, k=n)
        adverb = choices(adverbs, k=n)
        adjective = choices(adjectives, k=n)
    joke_list = []
    for a, b, c in zip(noun, adverb, adjective):
        joke = [a, b, c]
        joke_str = ' '.join(joke)
        joke_list.append(joke_str)
    return joke_list


print(get_jokes(6, 1))
