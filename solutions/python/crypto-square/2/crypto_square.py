"""crypto_square.py"""


def cipher_text(plain_text: str) -> str:
    """implement square code, a encryption mechanism"""

    chars: list[str] = [char for char in plain_text.lower() if char.isalnum()]

    if not chars:
        return ""

    sqrt: int = len(chars) ** 0.5

    if sqrt % 1 == 0:
        row = col = int(sqrt)
    else:
        row = int(sqrt)
        col = int(sqrt) + 1

        if row * col < len(chars):
            row += 1

    temp: list[str] = []

    for column in range(col):
        temp.append("".join((chars[roww * col + column] if roww * col + column < len(chars) else " ") for roww in range(row) ))

    return " ".join(temp)
