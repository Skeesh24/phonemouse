from mouse import move

from convert import giroscope_convert
from network import get_state


async def main_loop():
    while True:
        phonemeta = await anext(get_state())

        if not phonemeta:
            break

        x, y = giroscope_convert(*phonemeta)
        move(x, y, absolute=True)
