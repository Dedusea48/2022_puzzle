class Block:
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0


class Player(Block):
    def __init__(self, x0, y0):
        super().__init__(x0, y0)
        self.step = 1

    def move_up(self, obj):
        if obj.y == self.y + self.step:
            self.obj += self.step
        else:
            self.y -= self.step

    def move_down(self, obj):
        if obj.y == self.y - self.step:
            self.obj -= self.step
        else:
            self.y += self.step

    def move_left(self, obj):
        if obj.x == self.x - self.step:
            obj.x -= self.step
        else:
            self.x -= self.step

    def move_right(self, obj):
        if obj.x == self.x + self.step:
            obj.x += self.step
        else:
            self.x += self.step
