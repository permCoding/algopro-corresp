def get_records(filename, sep=','):
    abiturs = []
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            t = line.split(sep)
            abiturs.append([int(t[0]), t[1], int(t[2])])
    return abiturs


abiturs = get_records('./txt/abiturs.csv')
abiturs = [
    [1,23],
    [2,45],
    [3,12]
]

# abiturs.sort(key=lambda elm: elm[1], reverse=True)  # сортировка на месте

# def get_key(elm): return elm[1]
# abiturs.sort(key=get_key, reverse=True)  # сортировка на месте

ab_sorted = sorted(abiturs, key=lambda x: x[1])

for elm in abiturs: print(elm)
for elm in ab_sorted: print(elm)

# list_sorted = sorted(abiturs)  # return
