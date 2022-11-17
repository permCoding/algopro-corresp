import csv
from functools import cmp_to_key


def get_data(file_name):
    results = []
    with open(file_name, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            results.append(row)
    return results


def get_comp(a, b, f, d):
    if len(a) > 1 and a[f[0]] == b[f[0]]:
        return get_comp(a, b, f[1:], d[1:])
    sign = +1 if d[0] == 'asc' else -1
    return sign * (+1 if a[f[0]] > b[f[0]] else -1)


def comparator(a, b):
    return get_comp(a, b, fields, directs)


file_name = "./csv/students.csv"
students = get_data(file_name)  # преобразуем в словари

fields = ['group', 'age', 'name']  # по каким полям сортировать
directs = ['asc', 'desc', 'asc']  # по каким направлениям
sorted = sorted(students, key=cmp_to_key(comparator))  # сортировать

for stud in sorted:  # вывести все
    print(stud['group'].ljust(7, ' '), stud['age'], stud['name'])
