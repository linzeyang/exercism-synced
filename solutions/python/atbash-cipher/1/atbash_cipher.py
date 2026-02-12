"""atbash_cipher.py"""

from string import ascii_lowercase
from typing import LiteralString

ENCODING_DICT: dict[LiteralString, str] = dict(
    zip(ascii_lowercase, reversed(ascii_lowercase), strict=True)
)
DECODING_DICT: dict[LiteralString, str] = dict(
    zip(reversed(ascii_lowercase), ascii_lowercase, strict=True)
)


def encode(plain_text: str) -> str:
    buffer: list[str] = []
    temp: list[str] = []

    for char in plain_text.lower():
        if char.isalpha():
            buffer.append(ENCODING_DICT[char])
        elif char.isdigit():
            buffer.append(char)

        if len(buffer) == 5:
            temp.extend(buffer)
            temp.append(" ")
            buffer.clear()

    if buffer:
        temp.extend(buffer)

    return "".join(temp).strip()


def decode(ciphered_text: str) -> str:
    temp: list[str] = []
    
    for char in ciphered_text.lower():
        if char.isalpha():
            temp.append(DECODING_DICT[char])
        elif char.isdigit():
            temp.append(char)
    
    return "".join(temp)
