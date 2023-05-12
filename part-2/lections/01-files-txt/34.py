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

with open('results.csv', 'w', encoding='utf8') as f:
    f.write('id,name,rat\n')
    for ab in ab_sorted:
        f.write(f'{ab[0]},{ab[1]},{ab[2]}\n')
