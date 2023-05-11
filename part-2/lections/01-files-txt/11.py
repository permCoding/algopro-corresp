# ch = '\t'
# s = f'123{ch}567'+ch+'456'
# print(s)

f = open('./txt/01.txt')
lst = f.readlines()
for line in lst:
    line = line.strip()
    print(line)
