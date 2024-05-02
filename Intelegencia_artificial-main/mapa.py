from matplotlib import pyplot as plt
from matplotlib import colors
from enum import Enum
from vector import Vector


WALL = 0
TRACK = 1
START = 2
FINISH = 3


class Mapa:

    def __init__(self, trackFile):
        self.content = []
        self.start = Vector(-1, -1)
        self.finish = []
        self.rows = -1
        self.lines = -1

        self.read_file(trackFile)
        self.initStartFinish()

    def __str__(self):
        string = "[ \n"
        for line in self.content:
            string = string + str(line) + "," + "\n"
        string = string + "]"
        return string

    def read_file(self, filename):

        fich = open(filename, "r")
        text = fich.read()

        matriz = []
        line = []
        x = 0
        y = 0
        for char in text:
            if char == 'X':
                line.append(WALL)

            if char == '-':
                line.append(TRACK)

            if char == 'P':
                line.append(START)

            if char == 'F':
                line.append(FINISH)

            if char == '\n':
                y += 1
                x = 0
                matriz.append(line)
                line = []
            x += 1
        matriz.append(line)
        self.rows = x-1
        self.lines = y + 1

        self.content = matriz

    def initStartFinish(self):
        x = 0
        y = 0
        for line in self.content:
            if 3 in line or 2 in line:

                for elem in line:

                    if elem == 2:
                        self.start = Vector(x, self.lines-y-1)
                    if elem == 3:
                        self.finish.append(Vector(x, self.lines-y-1))

                    x += 1
            y += 1
            x = 0
        return

    def show(self, final=False):
        cmap = colors.ListedColormap(['Black', 'white', 'green', 'red'])
        plt.figure(figsize=(10, 10))
        plt.pcolor(self.content[::-1], cmap=cmap)

        if final:
            plt.show()

    def getCelValue(self, search):
        (x, y) = search
        i = 0
        j = self.lines - 1
        for line in self.content:
            for elem in line:
                if (x == i) and (j == y):
                    return elem
                i += 1
            j -= 1
            i = 0
