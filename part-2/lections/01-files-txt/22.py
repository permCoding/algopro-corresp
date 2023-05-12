from random import randint


def get_rnd_records(count=10,down=150,up=250):
    lst = [randint(down,up) for _ in range(count)]
    return lst


def list_to_file(filename, lst):
    with open(filename, 'w', encoding='utf8') as f:
        for elm in lst:
            f.write(f'{elm},\n')


lst = get_rnd_records()
list_to_file('./txt/w01.txt', lst)
