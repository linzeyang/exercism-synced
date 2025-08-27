from secrets import randbelow

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        result = [randbelow(6) + 1 for _ in range(4)]
        return sum(sorted(result)[1:])


def modifier(num: int) -> int:
    return (num - 10) // 2
