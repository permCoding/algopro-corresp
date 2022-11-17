import csv


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


file_name = "./csv/02.csv"
f = open(file_name, mode='r', encoding='utf8')
reader = csv.DictReader(f, delimiter=',')

abits = get_lst3(reader)
for abit in abits:
    print(abit['group'].ljust(10,' '), abit['name'])
