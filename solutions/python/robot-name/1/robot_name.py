from secrets import choice
from string import ascii_uppercase, digits


class Robot:
    def __init__(self):
        self._name = gen_name()

    def reset(self):
        self._name = gen_name()

    @property
    def name(self):
        return self._name


def gen_name():
    return f"{choice(ascii_uppercase)}{choice(ascii_uppercase)}{choice(digits)}{choice(digits)}{choice(digits)}"
