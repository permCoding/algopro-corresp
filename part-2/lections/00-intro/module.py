def get_max(lst):
    """
    получить максимальное занчение из списка
    """
    i, mx = 0, lst[0]
    while i < len(lst):
        if lst[i] > mx:
            mx = lst[i]
        i += 1
    return mx


def get_max_ind(lst):
    """
    получить максимальное занчение из списка
    """
    i, mx_ind = 0, 0
    while i < len(lst):
        if lst[i] > lst[mx_ind]:
            mx_ind = i
        i += 1
    return (lst[mx_ind], mx_ind)
