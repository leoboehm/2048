import random

class Tile:
    width: 10
    height: 10

    posX: 0
    posY: 0

    value: 0

    def __init__(self):
        # set position

        self.value = random.choice([2, 4])

    def doubleValue(self):
        self.value = self.value * 2