import json


fields = ['id', 'name', 'age']
a = [1, 'Гоша', 22]
b = [2, 'Оля', 21]
c = [3, 'Глаша', 27]
records = [a, b, c]
print(records)

lst = [dict(zip(fields, record)) for record in records]
print(lst)

print(json.dumps(lst, indent=4, ensure_ascii=False))

f = open('./json/records.json', 'w', encoding='utf8')
json.dump(lst, f, indent=4, ensure_ascii=False)
f.close()
