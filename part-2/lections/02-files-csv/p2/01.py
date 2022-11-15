import csv


file_name = "./csv/02.csv"

f = open(file_name, mode='r', encoding='utf8')
reader = csv.reader(f, delimiter=',')

for row in reader:
    print(row)
