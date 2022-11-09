import csv


with open("./csv/students.csv", encoding='utf-8') as f:
    reader = csv.reader(f, delimiter = ",")
    rows = [row for row in reader][1:]

for row in sorted(rows[1:], key=lambda x: int(x[3]), reverse=True):
    print(row)