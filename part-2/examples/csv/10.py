import csv
from operator import itemgetter as ig
from functools import cmp_to_key


def get_data(file_name):
    with open(file_name, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter = ",")
        rows = [row for row in reader]
        return (rows[0], rows[1:])


def comparator(a, b):
    if a[flds[0]] == b[flds[0]]:
        return dirs[1]*(+1 if a[flds[1]] > b[flds[1]] else -1)
    return dirs[0]*(+1 if a[flds[0]] > b[flds[0]] else -1)


file_name = "./csv/students.csv"
titles, rows = get_data(file_name)

flds = [4, 1]  # по каким полям сортировать
dirs = [-1, +1]  # по каким направлениям
srtd = sorted(rows, key=cmp_to_key(comparator))


for row in srtd:
    print(row[4].ljust(6), row[1])
