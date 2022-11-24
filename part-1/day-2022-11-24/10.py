lst = [23, 2, 45, 3, 22, 57, 1, 8, 100, 13, 88, 1, 20]
max_w = 120

elms = []
for i in range(len(lst)):
    if sum(elms) + lst[i] > max_w: continue
    elms += [lst[i]]

print(sum(elms), elms)
