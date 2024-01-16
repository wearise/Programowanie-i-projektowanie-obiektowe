import os


class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    MINT = (int(0.667 * 255), int(0.941 * 255), int(0.82 * 255))

    @staticmethod
    def random_RGB() -> (int, int, int):
        x = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)

        if x < 0.33:
            return Colors.RED

        elif x < 0.66:
            return Colors.GREEN

        else:
            return Colors.MINT
