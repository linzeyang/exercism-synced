MAPPING = {
    "earth": 1,
    "mercury": 0.2408467,
    "venus": 0.61519726,
    "mars": 1.8808158,
    "jupiter": 11.862615,
    "saturn": 29.447498,
    "uranus": 84.016846,
    "neptune": 164.79132,
}

class SpaceAge:
    def __init__(self, seconds):
        self.age = seconds

    @property
    def _earth_age(self):
        return self.age / 31557600

    def on_earth(self):
        return round(self._earth_age / MAPPING["earth"] , 2)

    def on_mercury(self):
        return round(self._earth_age / MAPPING["mercury"] , 2)

    def on_venus(self):
        return round(self._earth_age / MAPPING["venus"] , 2)

    def on_jupiter(self):
        return round(self._earth_age / MAPPING["jupiter"] , 2)

    def on_mars(self):
        return round(self._earth_age / MAPPING["mars"] , 2)

    def on_saturn(self):
        return round(self._earth_age / MAPPING["saturn"] , 2)

    def on_uranus(self):
        return round(self._earth_age / MAPPING["uranus"] , 2)

    def on_neptune(self):
        return round(self._earth_age / MAPPING["neptune"] , 2)
