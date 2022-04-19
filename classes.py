import pygame.draw as dr

# Палитра
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D


class Tile:
    """
    Игровая единица площади, которая содержит задние объекты (BackObj) и верхнии (FrontObj)
    """

    def __init__(self, x, y, back_obj, front_obj, screen):
        self.x = x
        self.y = y
        self.size = 40
        self.back_obj = back_obj
        self.front_obj = front_obj
        self.screen = screen

    def draw(self):
        self.back_obj.draw()
        self.front_obj.draw()


class BackObj:
    def __init__(self, the_tile):
        self.x = the_tile.x
        self.y = the_tile.y
        self.screen = the_tile.screen

    def draw(self):
        pass


class Floor(BackObj):
    def draw(self):
        pass


class Water(BackObj):
    def draw(self):
        pass
