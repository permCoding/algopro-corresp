from random import randint


def list_to_file_(filename, count=10):
    with open(filename, 'w', encoding='utf8') as f:
        for i in range(count):
            num = randint(150, 250)
            f.write(str(i+1)+','+str(num)+'\n')


def list_to_file(filename, count=10):
    with open(filename, 'w', encoding='utf8') as f:
        for i in range(1, count+1):
            num = randint(150, 250)
            f.write(f'{i},{num}\n')


list_to_file('./txt/w01.txt', 18)
