import csv
from operator import itemgetter as ig


def get_data(file_name):
    with open(file_name, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter = ",")
        rows = [row for row in reader]
        return (rows[0], rows[1:])


file_name = "./csv/students.csv"
titles, rows = get_data(file_name)

srtd = sorted(rows, key=ig(4))
srtd = sorted(rows, key=ig(1))  # так не работает
for row in srtd:
    print(row[4].ljust(6), row[1])
