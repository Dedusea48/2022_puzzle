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


class Level:
    """
    Создаёт игровую клеточную платформу, на которой будут находится объекты.
    Платформа состоит из клеток. Каждая клетка имеет два уровня: фундамент (0) и то, что стоит на фундаменте (1).
    Чтобы что-то извлечь из платформы, нужно указать координаты клетки - x и y, потом указать уровень (0 или 1),
    например Platform.squares[x][y][0] (извлечение объекта фундамента клетки с координатами x и y)
    Платформа самостоятельно организовывает свой пол(фундамент) из плиток (Tile).
    """

    def __init__(self, horizontal_side, vertical_side, screen, x0, y0):
        self.screen = screen
        self.x0 = x0
        self.y0 = y0

        self.vertical_side = vertical_side
        self.horizontal_side = horizontal_side
        self.colors = [GREEN, GREY]
        self.tiles = []

        for i in range(horizontal_side):
            column = []
            for j in range(vertical_side):
                tile = Tile(i, j, self.screen)
                floor = Floor(tile)
                tile.back_obj = floor
                column.append(tile)
            self.tiles.append(column)

    def draw(self):
        """
        Рисует все объекты, которые находятся в клетках (squares).
        :return:
        """
        for i in range(self.horizontal_side):
            for j in range(self.vertical_side):
                self.tiles[i][j].draw(self.x0, self.y0)


class Tile:
    """
    Игровая единица площади, которая содержит задние объекты (BackObj) и верхнии (FrontObj)
    """

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.back_obj = None
        self.front_obj = None
        self.size = 40
        self.screen = screen

    def draw(self, x0, y0):
        if self.back_obj is not None:
            self.back_obj.draw(x0, y0)
        if self.front_obj is not None:
            self.front_obj.draw(x0, y0)


class BackObj:
    def __init__(self, the_tile):
        self.x = the_tile.x
        self.y = the_tile.y
        self.size = the_tile.size
        self.screen = the_tile.screen

    def draw(self, x0, y0):
        pass


class Floor(BackObj):

    def draw(self, x0, y0):
        dr.rect(self.screen, 'black', [x0 + self.x * self.size, y0 + self.y * self.size,
                                       self.size, self.size])


class Water(BackObj):
    def draw(self, x0, y0):
        pass
