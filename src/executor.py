import logging

from mouse import move

from convert import gyroscope_convert
from network import get_state

logging.basicConfig(level=logging.DEBUG)


async def main_loop():
    while True:
        phonemeta = await anext(get_state())

        if not phonemeta:
            break

        logging.debug(phonemeta)

        x, y = gyroscope_convert(*phonemeta)
        move(x, y, absolute=True)
