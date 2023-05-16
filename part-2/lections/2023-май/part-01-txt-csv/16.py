f = open('./txt/01.txt')
lst = f.readlines()
for line in lst:
    t = line.split()  # список строк
    nums = list(map(int, t))
    print(max(nums))
