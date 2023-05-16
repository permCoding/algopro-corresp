f = open('./txt/01.txt')
lst = f.readlines()
for line in lst:
    t = line.split()  # список строк
    nums = [int(elm) for elm in t]
    print(max(nums))
