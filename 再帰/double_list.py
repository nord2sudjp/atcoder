def double_list(lst):
    if lst == []:
        return []

    first = lst[0]
    rest = lst[1:]
    return [first * 2] + double_list(rest)

double_list([1,2,3])