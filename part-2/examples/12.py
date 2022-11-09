import csv


def get_data(file_name):
    results = []
    with open(file_name, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            results.append(row)
    return results


file_name = "./csv/students.csv"
students = get_data(file_name)  # преобразуем в словари
for stud in students:  # вывести все словари
    print(stud)


"""
fieldnames — Определяет заголовки для столбцов, 
    если не определить атрибут, то в него запишутся 
    элементы из первой прочитанной строки файла. 
    Заголовки нужны для того, чтобы легко было понять, 
    какая информация содержится или должна содержаться в столбце.

    Например, если бы в students.csv не было бы первой строки 
    с заголовками, то можно было бы его открыть следующим образом:

fieldnames = ['id', 'name', 'gender', 'age', 'group']
file_reader = csv.DictReader(csvfile, fieldnames=fieldnames)
"""
