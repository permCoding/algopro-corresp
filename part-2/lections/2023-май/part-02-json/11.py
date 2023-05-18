import json

with open('./json/user.json', 'r', encoding='utf8') as f:
    obj = json.load(f)
    print(obj)
    print(obj['id'], obj['name'])
