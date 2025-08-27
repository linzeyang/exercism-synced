def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    if number == 1:
        return "deficient"

    s = sum_of_factors(number)

    if s == number:
        return "perfect"

    if s > number:
        return "abundant"

    return "deficient"


def sum_of_factors(number):
    factors = []

    fac = number // 2

    while fac > 1:
        if number % fac == 0:
            factors.append(fac)
        fac -= 1

    factors.append(1)
    
    return sum(factors)
