def to_int(line, base=2):
    """ перевести в ДСС """
    p = 0
    i = len(line) - 1
    res = 0
    while i >= 0:
        dig = int(line[i])
        res += dig * base ** p
        p += 1
        i -= 1
    return res
