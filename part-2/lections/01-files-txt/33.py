import locale
from functools import cmp_to_key


def get_records(filename, sep=','):
    abiturs = []
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            t = line.split(sep)
            abiturs.append([int(t[0]), t[1], int(t[2])])
    return abiturs


min_rating = 232
abiturs = get_records('./txt/abiturs.csv')

locale.setlocale(locale.LC_ALL, 'Russian_Russia.1251')
func = cmp_to_key(locale.strcoll)

filtred = [ab for ab in abiturs if ab[2]>=min_rating]
ab_sorted = sorted(filtred, key=lambda x: func(x[1]))

for ab in ab_sorted:
    print(*ab)
