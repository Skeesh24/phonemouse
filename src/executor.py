import logging

from mouse import move

from convert import get_screen_resolution, gyroscope_convert
from network import get_state

logging.basicConfig(level=logging.DEBUG)


async def main_loop():
    old_x, old_y = 0, 0
    x, y = get_screen_resolution()
    x /= 2
    y /= 2
    while True:
        phonemeta = await anext(get_state())

        if not phonemeta:
            break

        new_x, new_y = gyroscope_convert(*phonemeta, width=x, height=y)
        move(new_x - old_x, new_y - old_y, absolute=False)
        old_x, old_y = new_x, new_y

