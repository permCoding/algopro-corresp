lst = [23, 2, 45, 3, 22, 7, 1, 88, 20]
max_w = 150

res, elms = 0, []
for elm in lst:
    if res + elm <= max_w:
        res += elm
        elms += [elm]
    else:
        break

print(res, elms)
