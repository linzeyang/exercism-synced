class Allergies:

    def __init__(self, score):
        self.repr = f"{bin(score)[-8:]:0>8}"

    def allergic_to(self, item):
        if item not in items:
            return False

        return self.repr[-items.index(item) - 1] == "1"

    @property
    def lst(self):
        return [
            item for idx, item in enumerate(items) if self.repr[-idx - 1] == "1"
        ]

items = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]
