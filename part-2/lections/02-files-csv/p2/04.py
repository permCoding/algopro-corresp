import csv


def get_lst(file_name):
    f = open(file_name, mode='r', encoding='utf8')
    return [abit for abit in csv.DictReader(f, delimiter=',')]


file_name = "./csv/students.csv"
studs = get_lst(file_name)
filtred = filter(lambda x: x['gender']=='1', studs)
for row in filtred:
    print(row)

'''
вывести только имена мужиков
в алф порядке
'''