import pygame.draw as dr


class BackObj:
    def __init__(self, the_tile):
        self.x = the_tile.x
        self.y = the_tile.y
        self.size = the_tile.size
        self.screen = the_tile.screen

    def draw(self, x0, y0):
        pass

    # def check_up(self, level):
    #     pass


class Floor(BackObj):
    def __init__(self, the_tile):
        super().__init__(the_tile)
        self.name = 'floor'

    def draw(self, x0, y0):
        dr.rect(self.screen, 'white', [x0 + self.x * self.size, y0 + self.y * self.size,
                                       self.size, self.size])
        dr.rect(self.screen, 'black', [x0 + self.x * self.size, y0 + self.y * self.size,
                                       self.size, self.size], width=1)


class Water(BackObj):
    def __init__(self, the_tile):
        the_tile.back_obj = self
        super().__init__(the_tile)
        self.name = 'water'

    def draw(self, x0, y0):
        dr.rect(self.screen, 'blue', [x0 + self.x * self.size, y0 + self.y * self.size,
                                      self.size, self.size])


class Spring(BackObj):
    def __init__(self, the_tile, _x_jump, _y):
        super().__init__(the_tile)
        self.name = 'spring'
        self.x_jump = 0
        self.y_jump = 0

    def draw(self, x0, y0):
        dr.rect(self.screen, 'green', [x0 + self.x * self.size, y0 + self.y * self.size,
                                       self.size, self.size])

    def check_up(self, level):
        if level.tiles[self.x][self.y].front_obj is not None:
            level.tiles[self.x + self.x_jump][self.y + self.y_jump].front_obj = level.tiles[self.x][self.y].front_obj
            level.tiles[self.x + self.x_jump][self.y + self.y_jump].front_obj.x = self.x + self.x_jump
            level.tiles[self.x + self.x_jump][self.y + self.y_jump].front_obj.y = self.y + self.y_jump
            level.tiles[self.x][self.y].front_obj = None


class Ladder(BackObj):
    def __init__(self, the_tile):
        super().__init__(the_tile)
        self.name = "ladder"

    def draw(self, x0, y0):
        dr.rect(self.screen, 'orange', [x0 + self.x * self.size, y0 + self.y * self.size,
                                        self.size, self.size])

    def floor_up(self, player):
        player.floor += 1

    def floor_down(self, player):
        player.floor -= 1
