import pygame.draw as dr


class BackObj:
    def __init__(self, the_tile):
        self.x = the_tile.x
        self.y = the_tile.y
        self.size = the_tile.size
        self.screen = the_tile.screen

    def draw(self, x0, y0):
        pass


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
        super().__init__(the_tile)
        self.name = 'water'

    def draw(self, x0, y0):
        dr.rect(self.screen, 'blue', [x0 + self.x * self.size, y0 + self.y * self.size,
                                      self.size, self.size])
