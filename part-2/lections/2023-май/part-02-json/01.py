import json

obj = {
    'id': 1,
    'name': 'Гоша',
    'age': 22
}
print(obj)

record = [1, 'Гоша', 22]
obj = {
    'id': record[0],
    'name': record[1],
    'age': record[2]
}
print(obj)

fields = ['id', 'name', 'age']
record = [1, 'Гоша', 22]
obj = dict( zip(fields, record) )
print(obj)
