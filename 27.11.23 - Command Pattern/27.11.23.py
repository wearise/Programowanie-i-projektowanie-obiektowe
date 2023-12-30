import copy
import math
from abc import ABC, abstractmethod

class GraphicsDevice(ABC):
    @abstractmethod
    def line(self, xb, yb, xe, ye):
        print(f"linia od {xb}, {yb} do {xe}, {ye}")

class SVGDevice:
    def __init__(self,fname:str):
        self.__file = open(fname, "w")
        self.__file.write("""<svg viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">\n""")
    def line(self, xb, yb, xe, ye):
        print(f"<line x1='{xb}' y1='{yb}' x2='{xe}' y2='{ye}' stroke='black' />", file=self.__file)
    def __del__(self):
        self.__file.write("</svg>\n")
        self.__file.close()


class Turtle:

    def __init__(self, gd: GraphicsDevice):
        self.__device = gd
        self.__x = 0
        self.__y = 0
        self.__a = 0  # angle
        self.__if_drawing = False

    def up(self):
        self.__if_drawing = False

    def down(self):
        self.__if_drawing = True

    def jump(self, new_x, new_y):
        self.__x = new_x
        self.__y = new_y

    def right(self, d_alpha_deg):
        self.__a -= d_alpha_deg

    def left(self, d_alpha_deg):
        self.__a += d_alpha_deg

    def foreward(self, displacement):
        # new_x = displacement * math.cos(self.__a) + self.__x
        # new_y = displacement * math.sin(self.__a) + self.__y
        new_x = displacement * math.cos(self.__a / 180.0 * math.pi) + self.__x
        new_y = displacement * math.sin(self.__a / 180.0 * math.pi) + self.__y
        if self.__if_drawing:
            self.__device.line(self.__x, self.__y, new_x, new_y)
        self.__x = new_x
        self.__y = new_y


class Command(ABC):
    def __init__(self, trtl: Turtle):
        self._turtle = trtl

    @abstractmethod
    def execute(self, *params): pass


class UpCommand(Command):
    def __init__(self, trtl: Turtle):
        super().__init__(trtl)

    def execute(self, *params): self._turtle.up()


class DownCommand(Command):
    def __init__(self, trtl: Turtle):
        super().__init__(trtl)

    def execute(self, *params): self._turtle.down()


class ForewardCommand(Command):
    def __init__(self, trtl: Turtle):
        super().__init__(trtl)

    def execute(self, *params): self._turtle.foreward(float(params[0][0]))


class LeftCommand(Command):
    def __init__(self, trtl: Turtle):
        super().__init__(trtl)

    def execute(self, *params): self._turtle.left(float(params[0][0]))


class RightCommand(Command):
    def __init__(self, trtl: Turtle):
        super().__init__(trtl)

    def execute(self, *params): self._turtle.right(float(params[0][0]))


# class AngleCommand(Command):
#     def __init__(self, trtl: Turtle):
#         super().__init__(trtl)
#
#     def execute(self, *params): self._turtle.angle(float(params[0][0]))

class Interpreter:
    def __init__(self, turtle):
        self.__my_turtle = turtle
        self.__command_dispatch = {}  # dystpozytor komend
        self.add_command("F", ForewardCommand(self.__my_turtle))
        self.add_command("UP", UpCommand(self.__my_turtle))
        self.add_command("DOWN", DownCommand(self.__my_turtle))
        self.add_command("REPEAT", LoopCommand(self.__my_turtle))
        self.add_command("L", LeftCommand(self.__my_turtle))
        self.add_command("R", RightCommand(self.__my_turtle))
        # self.add_command("DEF", DefCommand(self.__my_turtle), self) #żeby dodało do listy komand

    def add_command(self, key, command):  # /register_command
        self.__command_dispatch[key] = command

    def run(self, program_text):
        for line in program_text.split("\n"):
            tokens = line.strip().split()  # strip usuwa białe znaki z przodu i z końca
            if len(tokens) > 0:
                cmd_to_run = self.__command_dispatch[tokens[0]]
                cmd_to_run.execute(tokens[1:])


class LoopCommand(Command):  # składnia pętli w VisuaLife: REPEAT n[]
    def __init__(self, trtl: Turtle):#, commands: list[Command], n_repeats: int):
        super().__init__(trtl)
        #Zmieniamy koncepcję
        # self.__mycommands = copy.deepcopy(commands)
        # self.__n_repeats = n_repeats

    def execute(self, *params):
        argumenty = params[0]
        n_repeat = int(argumenty[0])
        l = " ".join(argumenty[1:]).strip("[").strip("]").replace(",","\n") #string
        # print(params, n_repeat, ">"+l+"<")
        inter = Interpreter(self._turtle)
        for _ in range(n_repeat):
            inter.run(l)


if __name__ == '__main__':
    # moj_program = """
    # DOWN
    # F 30
    # A 10
    # F 30
    # REPEAT 5 [UP, F 10, L 10, DOWN, F 10, R 20]
    # REPEAT 3 [ F 10, L 10]
    # """
    moj_program = """
    DOWN
    F 30
    F 30
    REPEAT 5 [UP, F 10, L 10, DOWN, F 10, R 20]
    REPEAT 3 [ F 10, L 10]
    """
    svg_gd = SVGDevice("plik.svg")
    trtl = Turtle(svg_gd)
    interpreter = Interpreter(trtl)
    interpreter.run(moj_program)
