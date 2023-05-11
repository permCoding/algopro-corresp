f = open('./txt/01.txt')
lst = f.readlines()
for line in lst:
    t = line.split()  # список строк
    print(max(t))
