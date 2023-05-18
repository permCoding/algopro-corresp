import json


fields = ['id', 'name', 'age']

d = dict()
d = {}

d['id'] = 1
d[fields[0]] = 1

print(d)

fields = ['id', 'name', 'age']
values = [1, 'Николя', 23]

record = {}
for i in range(len(fields)):
    record[fields[i]] = values[i]
print(record)

record = dict(zip(fields, values))

