import math


class Vessel:
    def __init__(self, L: float, r: float, eta: float) -> None:
        self.L = L
        self.r = r
        self.eta = eta

    @property
    def R(self) -> float:
        return (8 * self.eta * self.L) / (math.pi * math.pow(self.r, 4))

    def __add__(self, other: "Vessel | float") -> float:
        if isinstance(other, Vessel):
            return self.R + other.R
        elif isinstance(other, float):
            return self.R + other
        else:
            raise TypeError("You can only add vessels or floats")

    def __or__(self, other: "Vessel | float") -> float:
        if isinstance(other, Vessel):
            return 1 / (1 / self.R + 1 / other.R)
        elif isinstance(other, float):
            return 1 / (1 / self.R + 1 / other)
        else:
            raise TypeError("You can only add vessels or floats")
