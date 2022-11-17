import csv


def get_lst(file_name):
    with open(file_name, mode='r', encoding='utf8') as f:
        return [abit for abit in csv.DictReader(f, delimiter=',')]


def set_lst(file_name, data):
    with open(file_name, mode='w', encoding='utf8') as f:
        writer = csv.DictWriter(f, delimiter=',', \
            lineterminator='\r', fieldnames=['id','name','gender','age','group'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)


file_name = "./csv/students.csv"
studs = get_lst(file_name)  # получить список объектов
filtred = filter(lambda x: x['gender']=='1', studs)  # отфильтровать по значению
sorted = sorted(filtred, key=lambda x: x["name"])  # сортировать по полю

set_lst("./csv/mens.csv", sorted)  # записать данные в файл

'''
сохранить изменённые данные в новый файл
'\r' - return caret
'\n' - new line
'''