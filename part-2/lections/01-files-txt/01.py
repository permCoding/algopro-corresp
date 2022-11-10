# print(ord('\r'))
# print(ord('\n'))
# chr(13)
# chr(10)

file_name = "./txt/01.txt"
file = open(file_name)
for line in file:
    print(line, end='')
