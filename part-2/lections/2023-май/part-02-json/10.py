import json


lst = [
    {
        'id': 1,
        'team': 'ЦСКА',
        'balls': 56    
    },
    {
        'id': 2,
        'team': 'Парма',
        'balls': 34 
    },
    {
        "id": 59761,
        "isActive": True,
        "age": 35,
        "name": "Кошмар Кошмаров",
        "gender": "male",
        "company": "CEDWARD",
        "email": "koshma@cedward.com",
        "phone": "+8 (890) 543-2508",
        "address": {
            "city": "Кунгур",
            "street": "Ленина",
            "apartment": "2-21"
        }
    },
]

print(len(lst))
print(lst[2])

s = json.dumps(lst[2], indent=4)
print(s)

s = json.dumps(lst[2], indent=4, ensure_ascii=False)
print(s)

with open('./json/user.json', 'w', encoding='utf8') as f:
    json.dump(lst[2], f, indent=4, ensure_ascii=False)
