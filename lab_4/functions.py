import numpy as np
from scipy.integrate import solve_ivp


def simulate(
    L: float,
    k_on: float = 1.0,
    k_off: float = 0.2,
    k_cat: float = 0.5,
    kdegK: float = 0.3,
    kact: float = 0.8,
    kdegE: float = 0.2,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    def f(t, y):
        R, K, E = y
        dR = k_on * L * (1 - R) - k_off * R
        dK = k_cat * R * (1 - K) - kdegK * K
        dE = kact * K * (1 - E) - kdegE * E
        return [dR, dK, dE]

    sol = solve_ivp(f, [0, 600], [0, 0, 0], max_step=0.1, dense_output=True)

    t = np.linspace(0, 600, 6000)
    R, K, E = sol.sol(t)

    return t, R, K, E


def calculate_t_half(E: np.ndarray, t: np.ndarray) -> float:
    E_half = np.max(E) / 2
    E_half_index = np.where(E >= E_half)[0][0]
    return t[E_half_index]
