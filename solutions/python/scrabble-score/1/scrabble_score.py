def score(word):
    mapping = {
        ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
        ("D", "G"): 2,
        ("B", "C", "M", "P"): 3,
        ("F", "H", "V", "W", "Y"): 4,
        ("K",): 5,
        ("J", "X"): 8,
        ("Q", "Z"): 10,
    }

    out = 0

    for char in word:
        for k, v in mapping.items():
            if char.upper() in k:
                out += v
                break

    return out
