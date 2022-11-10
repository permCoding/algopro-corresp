import csv

rows = []
with open("./csv/students.csv", encoding='utf-8') as f:
    reader = csv.reader(f, delimiter = ",")
    for row in reader:
        rows.append(row)

titles = rows[0]
rows = rows[1:]
print(titles)
for row in rows:
    print(row)
print(f"Записей в таблице - {len(rows)}")
