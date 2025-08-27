def primes(limit):
    if limit == 1:
        return []

    if limit == 2:
        return [2]

    composites = set()

    for i in range(2, limit + 1):
        if i in composites:
            continue

        j = 2
        while (x := i * j) <= limit:
            composites.add(x)
            j += 1

    return sorted(set(range(2, limit + 1)) - composites)
