import classes_back_obj as back
import pygame
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
grass = pygame.image.load('image/Grass.jpg')

class Level:
    """
    Создаёт игровой клеточный уровень, в котором будут находится объекты.
    Уровень состоит из клеток. Каждая клетка состоит из двух частей: back_obj(то, на чём стоят)  и front_obj(то, что стоит на back_obj).
    Чтобы что-то извлечь из платформы, нужно указать координаты клетки - x и y, потом через точку указать часть клетки.
    Например Platform.squares[x][y].back_obj (извлечение нижней части клетки с координатами x и y)
    Уровень самостоятельно организовывает свой пол из класса Floor.
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
                floor = back.Floor(tile, grass)
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
    Игровая единица площади, которая содержит задние объекты (BackObj) и верхние (FrontObj).
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
