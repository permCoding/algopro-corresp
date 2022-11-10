import csv


def get_data(file_name):
    with open(file_name, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter = ",")
        rows = [row for row in reader]
        return (rows[0], rows[1:])


file_name = "./csv/students.csv"
titles, rows = get_data(file_name)
print(*titles)
for row in sorted(rows, key=lambda x: x[1]):
    print(row[1].ljust(8), row[4])
