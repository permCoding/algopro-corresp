import json


fields = ['id', 'name', 'age']
record = [1, 'Гоша', 22]
obj = dict( zip(fields, record) )

s = json.dumps(obj, indent=4)
print(s)

s = json.dumps(obj, indent=4, ensure_ascii=False)
print(s)

with open('./json/obj.json', 'w', encoding='utf8') as f:
    json.dump(obj, f, indent=4, ensure_ascii=False)
