def decode(string: str):
    if not string:
        return ""

    lis: list[str] = []

    count: int = 0

    for char in string:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            lis.append(char * count if count else char)
            count = 0

    return "".join(lis)


def encode(string: str):
    if not string:
        return ""

    lis: list[str] = []

    current: str = string[0]
    count: int = 1

    for idx in range(1, len(string)):
        if string[idx] == current:
            count += 1
        else:
            lis.append(f"{count}{current}" if count > 1 else current)
            current = string[idx]
            count = 1

    lis.append(f"{count}{current}" if count > 1 else current)

    return "".join(lis)
