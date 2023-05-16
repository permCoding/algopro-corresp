f = open('./txt/01.txt')
lst = f.readlines()
for line in lst:
    t = line.split()  # список строк
    mx = 0
    for elm in t:
        if int(elm) > mx:
            mx = int(elm)
    print(mx)
