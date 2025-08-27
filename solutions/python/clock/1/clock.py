class Clock:
    def __init__(self, hour, minute):
        x, y = divmod(minute, 60)
        self._hour = (x + hour) % 24
        self._minute = y

    def __repr__(self):
        return f"Clock({self._hour}, {self._minute})"

    def __str__(self):
        return f"{self._hour:0>2}:{self._minute:0>2}"

    def __eq__(self, other):
        return self._hour == other._hour and self._minute == other._minute

    def __add__(self, minutes):
        x, y = divmod(self._minute + minutes, 60)
        return Clock((self._hour + x) % 24, y)

    def __sub__(self, minutes):
        x, y = divmod(self._minute - minutes, 60)
        return Clock((self._hour + x) % 24, y)
