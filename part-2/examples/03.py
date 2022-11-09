import csv


with open("./csv/students.csv", encoding='utf-8') as f:
    reader = csv.reader(f, delimiter = ",")
    rows = [row for row in reader]

fltr = [row for row in rows[1:] if row[2] == '1']

for row in fltr:
    print(row)