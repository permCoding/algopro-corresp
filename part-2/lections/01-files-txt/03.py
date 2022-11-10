file_name = "./txt/01.txt"
file = open(file_name)
lines = file.readlines()

for line in lines:
    print(line.strip())

print(lines)
