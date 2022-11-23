b = '10011'
base = 2
p = 0
i = len(b) - 1
res = 0
while i >= 0:
    dig = int(b[i])
    res += dig * base ** p
    p += 1
    i -= 1
print(res)
