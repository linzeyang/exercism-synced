MAPPING = {
    "R": "Radishes",
    "G": "Grass",
    "C": "Clover",
    "V": "Violets",
}

DEFAULT_STUDENTS = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
    "Kincaid",
    "Larry",
]

class Garden:
    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self._plants = diagram.split("\n")
        self._students = sorted(students)

    def plants(self, name: str) -> list[str]:
        idx = self._students.index(name)
        ps = self._plants[0][2 * idx: 2 * idx + 2] + self._plants[1][2 * idx: 2 * idx + 2]

        return [MAPPING[p] for p in ps]
