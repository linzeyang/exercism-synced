# Globals for the directions
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self._direction = direction
        self._x = x_pos
        self._y = y_pos

    @property
    def coordinates(self):
        return self._x, self._y

    @property
    def direction(self):
        return self._direction

    def move(self, instructions: str) -> None:
        for ins in instructions:
            self._do_move(ins)

    def _do_move(self, instruction: str) -> None:
        if instruction == "L":
            self._direction = (self._direction + 1) % 4
        elif instruction == "R":
            self._direction = (self._direction - 1) % 4
        else:
            if self._direction == EAST:
                self._x += 1
            elif self._direction == NORTH:
                self._y += 1
            elif self._direction == WEST:
                self._x -= 1
            else:
                self._y -= 1
