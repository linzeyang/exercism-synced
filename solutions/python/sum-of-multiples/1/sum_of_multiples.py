def sum_of_multiples(limit, multiples):
    return sum(n for n in range(limit) if any(n % i == 0 for i in multiples if i != 0))
