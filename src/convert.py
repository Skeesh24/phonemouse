import logging
import tkinter as tk

ANGLE_RANGE = 60  # Длина половины диапазона углов


def get_screen_resolution():
    root = tk.Tk()
    root.withdraw()  # Скрыть главное окно
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    return width, height


def gyroscope_convert(
    _: float,
    gamma: float,
    beta: float,
    *,
    width: float,
    height: float,
) -> tuple[int, int]:
    # Получаем разрешение экрана

    # Вычисляем масштаб для перевода углов в пиксели
    gamma_scale = width / (2 * ANGLE_RANGE)
    beta_scale = height / (2 * ANGLE_RANGE)

    # Преобразуем углы в экранные координаты
    x = width / 2 + gamma * gamma_scale
    y = height / 2 - beta * beta_scale  # Инвертируем, так как ось Y направлена вниз

    logging.info(f"X: {x}, Y: {y}")

    return int(x), int(y)
