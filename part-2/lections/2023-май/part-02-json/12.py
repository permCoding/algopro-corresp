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
]

for obj in sorted(lst, key=lambda e: e['balls']):
    print(obj)
