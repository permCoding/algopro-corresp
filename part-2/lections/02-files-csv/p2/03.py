import csv


def get_lst(file_name):
    f = open(file_name, mode='r', encoding='utf8')
    return [abit for abit in csv.DictReader(f, delimiter=',')]


file_name = "./csv/02.csv"
abits = get_lst(file_name)
sorted = sorted(abits, key=lambda x: x["rat"], reverse=True)
for abit in sorted:
    print(abit["rat"], abit['group'].ljust(10,' '), abit['name'])
