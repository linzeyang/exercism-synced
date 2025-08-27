def square_root(number):
    if number == 1:
        return 1

    lower, upper = 1, number // 2

    pick = (lower + upper) // 2

    while lower < upper:
        if pick ** 2 == number:
            return pick

        if pick ** 2 > number:
            upper = pick
        else:
            lower = pick + 1

        pick = (lower + upper) // 2

    return lower
