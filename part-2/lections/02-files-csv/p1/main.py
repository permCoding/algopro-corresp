import module


lines = module.get_lines('./txt/02.txt')
titles = lines[0]
data = lines[1:]

mx_i, mx_r = 0, 0
for i in range(len(data)):
    rat = int(data[i].split(',')[2])
    if rat > mx_r:
        mx_i, mx_r = i, rat

print(data[mx_i])
