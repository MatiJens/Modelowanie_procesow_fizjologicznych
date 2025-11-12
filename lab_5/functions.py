def lotki_volterry(t: float, z: list[float], alpha: float, beta: float, gamma: float, delta: float) -> list[float]:
    x, y = z
    return [x * (alpha + beta * y), y * (gamma + delta * x)]
