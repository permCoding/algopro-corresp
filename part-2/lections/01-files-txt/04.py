def line_strip(line):
    return line.strip()


def get_lines(file_name):
    file = open(file_name)
    lines = file.readlines()
    file.close()
    return list(map(line_strip, lines))


def get_lines_for(file_name):
    with open(file_name) as file:
        lines = file.readlines()
    lst = []
    for line in lines:
        lst.append(line.strip())
    return lst


def get_lines_gen(file_name):
    with open(file_name) as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


file_name = "./txt/01.txt"
print(get_lines(file_name))
print(get_lines_for(file_name))
print(get_lines_gen(file_name))
