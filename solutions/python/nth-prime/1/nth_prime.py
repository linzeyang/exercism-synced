def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')

    if number == 1:
        return 2

    if number == 2:
        return 3

    start = 4

    while number > 2:
        start += 1
        if is_prime(start):
            number -= 1

    return start

def is_prime(num):
    if num < 2:
        raise ValueError

    if num in (2, 3, 5, 7):
        return True

    if num % 2 == 0:
        return False

    for i in range(3, num // 2):
        if num % i == 0:
            return False

    return True
