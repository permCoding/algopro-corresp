# and or xor - логические операции

for x in range(100):
    if x % 13 == 0 and x % 3 == 0:
        print(x)

for x in range(100):
    if x % 13 == 0 or x % 14 == 0:
        print(x)

for x in range(10):
    if x % 2 != 0:
        print(x)


def check_even(num):
    return num % 2 == 0


for x in range(10):
    if not(check_even(x)):
        print(x)
