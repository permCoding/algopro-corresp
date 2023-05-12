def scompare(a, b):
    if a[0] == b[0]: 
        return scompare(a[1:], b[1:])
    if alph.find(a[0]) > alph.find(b[0]): 
        return True
    else:
        return False

alph_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alph_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alph = alph_lower + alph_upper
print(alph.lower())

lst = [
    'ееЕ',
    'еееЕ'
    'Ёбиюпдмчгй', 
    'ЕеТизп', 
    'Ёшюдекфймн'
]

print( lst[0] > lst[1] )
print( scompare(lst[0],lst[1]) )

print( lst[1] > lst[2] )
print( scompare(lst[1],lst[2]) )
