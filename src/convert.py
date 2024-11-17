from random import randint


def gyroscope_convert(
    alpha: float,
    beta: float,
    gamma: float,
) -> tuple[int, int]:
    return (
        randint(200, 500),
        randint(200, 500),
    )
