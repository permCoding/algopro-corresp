# операторы и операции
# тернарная операция 

def ex_01(x):
    if x > 0:
        x *= 2  # операция
    else:
        x //= 2  # операция - округляется в низ
    print(x)


def ex_02(x):
    """ тернарная операция 
    return agr1 if True else arg2
    """
    return x*2 if x > 0 else x//2  # x > 0? x*2: x//2
    

func = ex_01
func(-9)
print(ex_02(-9))
