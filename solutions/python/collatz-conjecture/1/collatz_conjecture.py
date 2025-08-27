def steps(number):
    if not isinstance(number, int) or number < 1:
        raise ValueError("Only positive integers are allowed")

    if number == 1:
        return 0

    count = 0

    while True:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1

        count += 1

        if number == 1:
            return count
