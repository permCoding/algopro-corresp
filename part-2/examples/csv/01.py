import csv


with open("./csv/students.csv", encoding='utf-8') as f:
    reader = csv.reader(f, delimiter = ",")
    for row in reader:
        print(row)
