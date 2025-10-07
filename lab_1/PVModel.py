import numpy as np


class PVModel:
    def __init__(self, V: np.ndarray) -> None:
        self.V = V

    def calculate_Plin(self, a: float, b: float) -> None:
        """Calculates pressure for a linear model.

        a, b - linear model coefficients"""
        self.P_lin = a * self.V + b

    def calculate_Pexp(self, P0: float, alfa: float, V0: float) -> None:
        """Calculates pressure for an exponential model.

        P0 - pressure for V0,
        alpha - vessel stiffness coefficient,
        V0 - volume for which no transmutational pressure is generated."""
        self.P_exp = P0 * np.exp(alfa * (self.V - V0)) - 1

    def calculate_Plog(self, Pmax: float, beta: float, V50: float) -> None:
        """Calculates pressure for a sigmoidal model.

        Pmax - maximum pressure (at very high volumes),
        beta - ???,
        V50 - volume for half of Pmax"""
        self.P_log = Pmax / (1 + np.exp(beta * (V50 - self.V)))

    def calculate_Windkessel(
        self, Pd: float, Pi: float, R: float, C: float, t: np.ndarray
    ) -> None:
        """Calculates the two-element Windkessel model.

        Pd - pressure limit during diastole,
        Pi - pressure at the beginning of diastole,
        R - vascular resistance,
        C - vascular compliance,
        t - time"""
        self.P_t = Pd + (Pi - Pd) * np.exp(-t / (R * C))
