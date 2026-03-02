"""simple_cipher.py"""

import secrets
from itertools import cycle
from string import ascii_lowercase


class Cipher:
    """class to represent simple implementation of vigenere cipher"""

    def __init__(self, key: str | None=None) -> None:
        """Initialization"""

        self.key = key or "".join(ascii_lowercase[secrets.randbelow(26)] for _ in range(100))

    def encode(self, text: str) -> str:
        """Plain text to encrypted"""

        return "".join(chr(ord("a") + (ord(char) + ord(key) - ord("a") * 2) % 26) for char, key in zip(text, cycle(self.key), strict=False))

    def decode(self, text: str) -> str:
        """Encrypted to plain text"""

        return "".join(chr(ord("a") + (ord(char) + ord("z") - ord(key) + 1 - ord("a")) % 26) for char, key in zip(text, cycle(self.key), strict=False))
