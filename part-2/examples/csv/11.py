import csv
from functools import cmp_to_key


def get_data(file_name):
    with open(file_name, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter = ",")
        rows = [row for row in reader]
        return (rows[0], rows[1:])


def get_comp(a, b, f, d):
    if len(a) > 1 and a[f[0]] == b[f[0]]:
        return get_comp(a, b, f[1:], d[1:])
    return d[0]*(+1 if a[f[0]] > b[f[0]] else -1)


def comparator(a, b):
    return get_comp(a, b, flds, dirs)


file_name = "./csv/students.csv"
titles, rows = get_data(file_name)

flds = [4, 3, 1]  # по каким полям сортировать
dirs = [-1, -1, +1]  # по каким направлениям
srtd = sorted(rows, key=cmp_to_key(comparator))


for row in srtd:
    print(row[4].ljust(6), row[3], row[1])
