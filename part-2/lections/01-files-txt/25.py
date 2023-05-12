from random import randint, sample


def get_rnd_records(count=10,down=150,up=250):
    def get_rnd_name(down=3,up=12):
        alph = 'абвгдеёжзийклмнопрстуфхцчшщьъэюя'
        count = randint(down,up)  # длина фамилии
        return ''.join(sample(alph, k=count)).title()
    lst = [[i,get_rnd_name(),randint(down,up)] for i in range(1,count+1)]
    return lst


def list_to_file(filename, lst):
    with open(filename, 'w', encoding='utf8') as f:
        for elm in lst:
            f.write(f'{elm[0]},{elm[1]},{elm[2]}\n')


lst = get_rnd_records()
list_to_file('./txt/w01.txt', lst)
