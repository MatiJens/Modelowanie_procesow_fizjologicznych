import numpy as np
import pandas as pd
from scipy.optimize import curve_fit


class PVModel:
    @staticmethod
    def calculate_Plin(V: np.ndarray, a: float, b: float) -> np.ndarray:
        """Calculates pressure for a linear model.

        a, b - linear model coefficients"""
        return a * V + b

    @staticmethod
    def calculate_Pexp(V: np.ndarray, P0: float, alfa: float, V0: float) -> np.ndarray:
        """Calculates pressure for an exponential model.

        P0 - pressure for V0,
        alpha - vessel stiffness coefficient,
        V0 - volume for which no transmutational pressure is generated."""
        return P0 * np.exp(alfa * (V - V0)) - 1

    @staticmethod
    def calculate_Plog(
        V: np.ndarray, Pmax: float, beta: float, V50: float
    ) -> np.ndarray:
        """Calculates pressure for a sigmoidal model.

        Pmax - maximum pressure (at very high volumes),
        beta - ???,
        V50 - volume for half of Pmax"""
        return Pmax / (1 + np.exp(-beta * (V - V50)))

    @staticmethod
    def calculate_Windkessel(
        Pd: float, Pi: float, R: float, C: float, t: np.ndarray
    ) -> np.ndarray:
        """Calculates the two-element Windkessel model.

        Pd - pressure limit during diastole,
        Pi - pressure at the beginning of diastole,
        R - vascular resistance,
        C - vascular compliance,
        t - time"""
        return Pd + (Pi - Pd) * np.exp(-t / (R * C))

    @staticmethod
    def fit_and_evaluate(
        models_to_fit: list,
        p0_list: list,
        x_data: pd.Series | np.ndarray,
        y_data: pd.Series | np.ndarray,
    ) -> dict:
        r_squared = 0.0
        for model in models_to_fit:
            params = curve_fit(model, x_data, y_data, p0=p0_list[model.__name__])[0]
            y_predicted = model(x_data, *params)
            if (
                current_r_squared := PVModel.calculate_r_squared(y_data, y_predicted)
            ) > r_squared:
                result = {
                    "model": model.__name__,
                    "parameters": params,
                    "r_squared": current_r_squared,
                }
        return result

    @staticmethod
    def calculate_r_squared(
        y_real: pd.Series | np.ndarray, y_predicted: pd.Series | np.ndarray
    ) -> float:
        ss_res = np.sum((y_real - y_predicted) ** 2)
        ss_tot = np.sum((y_real - np.mean(y_real)) ** 2)
        return 1 - (ss_res / ss_tot)
