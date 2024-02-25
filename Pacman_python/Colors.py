import os


class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    ORANGE = (224, 130, 31)
    PINK = (255, 192, 203)
    GREEN = (0, 255, 0)
    BLUE = (23, 51, 150)
    # BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    MINT = (int(0.667 * 255), int(0.941 * 255), int(0.82 * 255))

    ghost_colors = list([RED, ORANGE, PINK, GREEN, MINT])
    __ghost_colors = list([RED, ORANGE, PINK, GREEN, MINT])

    @staticmethod
    def random_RGB() -> (int, int, int):
        x = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)

        try:
            dx = 1 / len(Colors.__ghost_colors)
            j = 0
            i = dx

            while i <= 1:

                if x < i:
                    color = Colors.__ghost_colors[j]
                    Colors.__ghost_colors.remove(color)
                    return color
                j += 1
                i += dx

        except:
            raise Exception("Too many ghost, not enough ghost colors")