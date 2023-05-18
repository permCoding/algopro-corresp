import json


def get_records():
    fields = ['id', 'name', 'age']
    values = [
        [1, 'Николя', 23],
        [2, 'Оля', 21],
    ]
    records = []
    for elm in values:
        record = dict(zip(fields, elm))
        records.append(record)
    return records


def to_json(filename, records):
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(records, f, indent=4, ensure_ascii=False)


records = get_records()
to_json('./json/abiturs.json', records)
