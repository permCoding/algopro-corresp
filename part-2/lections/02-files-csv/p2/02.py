import csv


file_name = "./csv/02.csv"

f = open(file_name, mode='r', encoding='utf8')
reader = csv.DictReader(f, delimiter=',')


def get_lst1(reader):
    abits = []
    for abit in reader:
        abits.append(abit)
    return abits

def get_lst2(reader):
    abits = []
    for abit in reader:
        abits += [abit]
    return abits


def get_lst3(reader):
    return [abit for abit in reader]


print(get_lst3(reader))
