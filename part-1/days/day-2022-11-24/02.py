# - операции: % // += -= *=  

def to_bin(x):
    result = ''
    while x > 0:
        result = str(x%2) + result # int float bool list tuple str
        x //= 2
    return result  # result[::-1]


print(to_bin(13))

# %  mod - остаток от целочисленного деления
# 17 % 7
# 1) 2
# 2) 14
# 3) 17 - 14 = 3
# 123 % 10 = 3

# 13(10) => X(2) 
# div mod
# 6   1  1
# 3   0  2
# 1   1  4
# 0   1  8