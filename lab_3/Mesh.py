import numpy as np


class Mesh:
    def __init__(self, L: float, N: int, target_x: float) -> None:
        if N < 2:
            raise ValueError("N must be >= 2")
        elif L <= 0:
            raise ValueError("L must be > 0")
        elif L <= 0:
            raise ValueError("target_x must be > 0")

        self.L = L
        self.N = N
        self.target_x = target_x

    @property
    def dx(self) -> float:
        return self.L / self.N

    @property
    def idx(self) -> np.signedinteger:
        return np.argmin(np.abs(np.linspace(0, self.L, self.N) - self.target_x))
