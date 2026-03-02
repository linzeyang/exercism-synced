from collections import defaultdict


class School:
    def __init__(self) -> None:
        self.grades: dict[int, list[str]] = defaultdict(list)
        self.known_students: set[str] = set()
        self._added: list[bool] = []

    def add_student(self, name: str, grade: int) -> None:
        if name in self.known_students:
            self._added.append(False)
            return

        self.grades[grade].append(name)
        self.grades[grade].sort()
        self.known_students.add(name)
        self._added.append(True)

    def roster(self) -> list[str]:
        r: list[str] = []

        for grade in sorted(self.grades.keys()):
            r.extend(self.grades[grade])

        return r

    def grade(self, grade_number: int) -> list[str]:
        return self.grades[grade_number]

    def added(self) -> list[bool]:
        return self._added
