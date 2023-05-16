def get_records(filename, sep=','):
    abiturs = []
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            t = line.split(sep)
            abiturs.append([int(t[0]), t[1], int(t[2])])
    return abiturs


min_rating = 232
abiturs = get_records('./txt/abiturs.csv')

filtred = [ab for ab in abiturs if ab[2]>=min_rating]
ab_sorted = sorted(filtred, key=lambda x: x[2], reverse=True)

for ab in ab_sorted:
    print(*ab)
