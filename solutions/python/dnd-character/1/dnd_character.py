from secrets import randbelow

class Character:
    def __init__(self):
        self.strength = _roll()
        self.dexterity = _roll()
        self.constitution = _roll()
        self.intelligence = _roll()
        self.wisdom = _roll()
        self.charisma = _roll()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        # what does ability() mean exactly?
        return _roll()


def modifier(num: int) -> int:
    return (num - 10) // 2

def _roll() -> int:
    result = [randbelow(6) + 1 for _ in range(4)]
    return sum(sorted(result)[1:])
