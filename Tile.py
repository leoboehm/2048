import random

class Tile:
    value: 0

    colordict = {
        0: (0,0,0), # black
        2: (255,0,0), # red
        4: (0,128,0), # green
        8: (156,39,176), # purple
        16: (103,58,183), # deep purple
        32: (255,87,34), # deep orange
        64: (0,150,136), # teal
        128: (139,195,74), # light green
        256: (234,30,99), # pink
        512: (255,152,0), # orange
        1024: (33,150,136), # blue
        2048: (121,85,72) # brown
    }

    def __init__(self):
        self.value = random.choice([2, 4])

    def getColor(self):
        return self.colordict[self.value]

    def doubleValue(self):
        self.value = self.value * 2