import csv


def get_data(file_name):
    results = []
    with open(file_name, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            results.append(row)
    return (results[0].keys(), results)


def write_to_file(file_name, dicts, fields):
    with open(file_name, mode="w", encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=",", lineterminator="\r", fieldnames=fields)
        writer.writeheader()
        for obj in dicts:
            if obj["gender"] == "1":
                writer.writerow(obj)


file_name = "./csv/students.csv"
fields, students = get_data(file_name)
write_to_file("./csv/filtred.csv", students, fields)
