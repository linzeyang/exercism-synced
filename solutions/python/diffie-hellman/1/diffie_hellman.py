def private_key(p):
    from secrets import choice

    return choice(range(1, p))


def public_key(p, g, private):
    return g ** private % p


def secret(p, public, private):
    return public ** private % p
