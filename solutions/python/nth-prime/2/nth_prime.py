def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')

    if number == 1:
        return 2

    if number == 2:
        return 3

    known_primes = [2, 3]

    num = 5

    while len(known_primes) < number:
        while not is_prime(num, known_primes):
            num += 2
        known_primes.append(num)
        num += 2

    return known_primes[-1]

def is_prime(num: int, known_primes: list[int]) -> bool:
    for prime in known_primes:
        if not num % prime:
            return False

    return True
