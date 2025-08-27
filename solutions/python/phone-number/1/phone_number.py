import re

PATTERN = re.compile(r"^\+?(1)? ?\(?([0-9]{1}\d{2})\)?[\- \.]*([0-9]{1}\d{2})[\- \.]*(\d{4}) *$")

class PhoneNumber:
    def __init__(self, number):
        if m := PATTERN.match(number):
            self._groups = m.groups()

            if self._groups[2].startswith("0"):
                raise ValueError("exchange code cannot start with zero")

            if self._groups[2].startswith("1"):
                raise ValueError("exchange code cannot start with one")

            if self._groups[1].startswith("0"):
                raise ValueError("area code cannot start with zero")

            if self._groups[1].startswith("1"):
                raise ValueError("area code cannot start with one")
        else:
            count = 0
            for char in number:
                if "a" <= char <= "z":
                    raise ValueError("letters not permitted")
                if char in "@:!":
                    raise ValueError("punctuations not permitted")
                if "0" <= char <= "9":
                    count += 1
            if count < 10:
                raise ValueError("incorrect number of digits")
            if count > 11:
                raise ValueError("more than 11 digits")
            if count == 11 and not number.startswith("1"):
                raise ValueError("11 digits must start with 1")

    @property
    def number(self):
        return "".join(self._groups[1:])

    @property
    def area_code(self):
        return self._groups[1]
    
    def pretty(self):
        return f"({self._groups[1]})-{self._groups[2]}-{self._groups[3]}"
