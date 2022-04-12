class Block:
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0


class Player(Block):
    def __init__(self, x0, y0):
        super().__init__(x0, y0)
        self.step = 1

    def move_up(self):
        self.y -= self.step

    def move_down(self):
        self.y += self.step

    def move_left(self):
        self.x -= self.step

    def move_right(self):
        self.x += self.step
