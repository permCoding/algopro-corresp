def list_to_file(filename, count=10):
    f = open(filename, 'w', encoding='utf8')
    for i in range(count):
        f.write(str(i+1)+',\n')
    f.close()


def list_to_file_(filename, count=10):
    with open(filename, 'w', encoding='utf8') as f:
        for i in range(count):
            f.write(str(i+1)+',\n')


list_to_file_('./txt/w01.txt', 18)
