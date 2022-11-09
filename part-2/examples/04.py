import csv


with open("./csv/students.csv", encoding='utf-8') as f:
    reader = csv.reader(f, delimiter = ",")
    rows = [row for row in reader]

for row in filter(lambda x: x[2]=='1', rows[1:]):
    print(row)