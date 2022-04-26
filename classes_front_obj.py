import pygame.draw as dr


def border_control(x, y, level):
    if 0 <= x < level.horizontal_side and 0 <= y < level.vertical_side:
        return True
    return False


class FrontObj:
    def __init__(self, the_tile):
        self.x = the_tile.x
        self.y = the_tile.y
        self.name = None
        self.screen = the_tile.screen

    def draw(self, x0, y0):
        pass


class Box(FrontObj):
    def __init__(self, the_tile):
        super().__init__(the_tile)
        self.name = "box"

    def draw(self, x0, y0):
        dr.rect(self.screen, 'orange', [x0 + self.x * 40, y0 + self.y * 40,
                                        40, 40])


class Player(FrontObj):  # TODO переделать под новый класс FrontObj
    """
    Создаёт игрока. При создании ему передаюся его координаты на платформе, а не на экране.
    Знает, как нарисовать себя.
    """

    def __init__(self, the_tile, level):
        super().__init__(the_tile)
        self.name = 'player'
        self.level = level

    def draw(self, x0, y0):
        dr.rect(self.screen, 'yellow', [x0 + self.x * 40, y0 + self.y * 40,
                                        40, 40])

    def move(self, direction):
        _y = self.y
        _x = self.x

        if direction == 'up':
            _y -= 1
        if direction == 'down':
            _y += 1
        if direction == 'left':
            _x -= 1
        if direction == 'right':
            _x += 1

        if border_control(_x, _y, self.level):
            if self.level.tiles[_x][_y].front_obj is None:
                self.step(_x, _y)
            else:
                self.kick(_x, _y)

    def step(self, _x, _y):
        self.level.tiles[self.x][self.y].front_obj = None
        self.level.tiles[_x][_y].front_obj = self
        self.x = _x
        self.y = _y

    def kick(self, _x, _y):
        __x = 2 * _x - self.x
        __y = 2 * _y - self.y

        if border_control(__x, __y, self.level):
            self.level.tiles[__x][__y].front_obj = self.level.tiles[_x][_y].front_obj
            self.level.tiles[_x][_y].front_obj = None
            self.level.tiles[__x][__y].front_obj.x = __x
            self.level.tiles[__x][__y].front_obj.y = __y

    def move_down(self, objects):
        for obj in objects:
            if obj.name == "box" and obj.y - 1 == self.y:
                obj.y += 1
                break
        self.y += 1

    def move_left(self, objects):
        for obj in objects:
            if obj.name == "box" and obj.x + 1 == self.x:
                obj.x -= 1
                break
        self.x -= 1

    def move_right(self, objects):
        for obj in objects:
            if obj.name == "box" and obj.x - 1 == self.y:
                obj.x += 1
                break
        self.x += 1
