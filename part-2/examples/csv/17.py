import csv


def get_data(file_name):
    with open(file_name, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter = ",")
        rows = [row for row in reader]
        return (rows[0], rows[1:])


def write_to_file(file_name, dicts, fields):
    with open(file_name, mode="w", encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=",", lineterminator="\r")
        writer.writerow(fields)  # заголовки
        for obj in dicts:
            if obj[2] == "1":
                writer.writerow(obj)


file_name = "./csv/students.csv"
fields, students = get_data(file_name)
write_to_file("./csv/filtred.csv", students, fields)
