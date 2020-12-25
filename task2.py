class Road:

    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width

    def mass_calc(self):
        return self._length * self._width * 5 * 25


road_a = Road(24, 12)
print(road_a.mass_calc())

