def label(colors):
    unit = "ohms"

    base = (MAPPING[colors[0]] * 10 + MAPPING[colors[1]]) * 10 ** MAPPING[colors[2]]

    if base > 1e9:
        unit = "gigaohms"
        base //= int(1e9)
    elif base > 1e6:
        unit = "megaohms"
        base //= int(1e6)
    elif base > 1e3:
        unit = "kiloohms"
        base //= int(1e3)

    return f"{base} {unit}"

MAPPING = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}
