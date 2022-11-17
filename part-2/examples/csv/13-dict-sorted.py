import csv


def get_data(file_name):
    results = []
    with open(file_name, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            results.append(row)
    return results


file_name = "./csv/students.csv"
students = get_data(file_name)
for stud in sorted(students, key=lambda x: int(x["age"]), reverse=True):  # сортируем словари по ключу
    print(stud)
