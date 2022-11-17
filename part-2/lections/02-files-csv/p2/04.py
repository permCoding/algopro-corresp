import csv


def get_lst(file_name):
    f = open(file_name, mode='r', encoding='utf8')
    return [abit for abit in csv.DictReader(f, delimiter=',')]


file_name = "./csv/students.csv"
studs = get_lst(file_name)  # получить список объектов
filtred = filter(lambda x: x['gender']=='1', studs)  # отфильтровать по значению
sorted = sorted(filtred, key=lambda x: x["name"])  # сортировать по полю
for row in sorted:
    print(row['name'])

'''
вывести только имена мужиков в алф порядке
'''