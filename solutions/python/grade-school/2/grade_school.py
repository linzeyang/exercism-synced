"""grade_school.py"""

from collections import defaultdict


class School:
    """class to represent school's roster"""

    def __init__(self) -> None:
        """Initialization"""

        self.grades: dict[int, list[str]] = defaultdict(list)
        self.known_students: set[str] = set()
        self._added: list[bool] = []

    def add_student(self, name: str, grade: int) -> None:
        """Add a student (name) to given grade"""

        if name in self.known_students:
            self._added.append(False)
            return

        self.grades[grade].append(name)
        self.grades[grade].sort()
        self.known_students.add(name)
        self._added.append(True)

    def roster(self) -> list[str]:
        """Return the whole roster of the school"""

        ros: list[str] = []

        for grade in sorted(self.grades.keys()):
            ros.extend(self.grades[grade])

        return ros

    def grade(self, grade_number: int) -> list[str]:
        """Return the roster of given grade number"""

        return self.grades[grade_number]

    def added(self) -> list[bool]:
        """Return the results of each `add` operation"""

        return self._added
