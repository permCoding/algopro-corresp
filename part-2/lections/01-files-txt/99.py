def scompare(a, b):
    if a == '': return False
    if b == '': return True
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
    'еёе',
    'ееЕ',
    'еееЕ',
    'ё',
    'е',
    'Ё',
    'Е',
    'деревня',
    'жаба',
    'Ёбиюпдмчгй', 
    'ЕеТизп', 
    'Ёшюдекфймн'
]
print( lst[0] > lst[1] )
print( scompare(lst[0],lst[1]) )

print( lst[1] > lst[2] )
print( scompare(lst[1],lst[2]) )

# lst = [9,8,0,0,3,4,1,2]

n = len(lst)
for i in range(n-1):
    for j in range(n-1-i):
        # if lst[j]>lst[j+1]:
        if scompare(lst[j],lst[j+1]):
            lst[j], lst[j+1] = lst[j+1], lst[j]
for elm in lst: print(elm)
