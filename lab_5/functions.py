def lotki_volterry_model(
    t: float, z: list[float], alpha: float, beta: float, gamma: float, delta: float
) -> list[float]:
    x, y = z
    return [x * (alpha + beta * y), y * (gamma + delta * x)]


def competition_model(
    t: float, z: list[float], r1: float, r2: float, K1: float, K2: float, alpha12: float, alpha21: float
) -> list[float]:
    x1, x2 = z
    x1 = r1 * x1 * (1 - (x1 + alpha12 * x2) / K1)
    x2 = r2 * x2 * (1 - (x2 + alpha21 * x1) / K2)
    return [x1, x2]
