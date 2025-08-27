def factors(value):
    if value == 1:
        return []

    if value in {2, 3}:
        return [value]

    prime = 2
    out = []

    while value > 1:
        if value % prime != 0:
            prime += 2 if prime % 2 == 1 else 1
            continue
        else:
            out.append(prime)
            value //= prime

    return out
