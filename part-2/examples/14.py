import csv
from operator import attrgetter as ag
from functools import cmp_to_key


class Student():
    def __init__(self, a,b,c,d,e):
        self.id = int(a)
        self.name = b
        self.gender = 'f' if c == '0' else 'm'
        self.age = int(d)
        self.group = e

    def __repr__(self):
        return f"{self.name.ljust(9)} {self.gender} {self.age} {self.group}"


def get_data(file_name):
    results = []
    with open(file_name, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            results.append(row)
    return results


file_name = "./csv/students.csv"
students = get_data(file_name)  # получим словари
objs = map(lambda x: Student(x["id"],x["name"],x["gender"],x["age"],x["group"]), students)  # преобразуем в объекты
for stud in sorted(objs, key=ag("name"), reverse=True):  # отсортировать и вывести все объекты
    print(stud)
