from random import randint as rnd, sample

def get_rnd_name_(down=3,up=12):
    # alph = 'абвгде'
    count = rnd(down,up)  # длина фамилии
    left, right = 1072, 1103  # диапазон в таблице символов
    lst = [chr(rnd(left,right)) for _ in range(count)]
    last_name = ''.join(lst)
    return last_name.title()


def get_rnd_name(down=3,up=12):
    alph = 'абвгдеёжзийклмнопрстуфхцчшщьъэюя'
    count = rnd(down,up)  # длина фамилии
    return ''.join(sample(alph, k=count)).title()


print(get_rnd_name())
