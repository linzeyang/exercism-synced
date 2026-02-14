"""diamond.py"""

from string import ascii_uppercase


def rows(letter) -> list[str]:
    number: int = ord(letter) - ord("A") + 1
    length: int = 2 * number - 1
    
    temp: list[list[str]] = [[" "] * length for _ in range(length)]
    
    for idx, letter in enumerate(ascii_uppercase[:number]):
        temp[idx][number - 1 - idx] = letter
        temp[idx][number - 1 + idx] = letter
        temp[length - idx - 1][number - 1 - idx] = letter
        temp[length - idx - 1][number - 1 + idx] = letter
    
    return ["".join(line) for line in temp]
