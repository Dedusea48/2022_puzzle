"""
Модуль, в котором содержатся классы Level и Tile
"""

import classes_back_obj as back
import classes_front_obj as front
import pygame

grass = pygame.image.load('image/Grass.jpg')


class Level:
    """
    Создаёт игровой клеточный уровень, в котором будут находится объекты.
    Уровень состоит из клеток. Каждая клетка состоит из двух частей:
    back_obj(то, на чём стоят) и front_obj(то, что стоит на back_obj).
    Чтобы что-то извлечь из платформы, нужно указать координаты клетки - x и y, потом через точку указать часть клетки.
    Например Platform.squares[x][y].back_obj (извлечение нижней части клетки с координатами x и y)
    Уровень самостоятельно организовывает свой пол из класса Floor.
    """

    def __init__(self, screen, x0, y0, horizontal_side, vertical_side):
        """
        Создает уровень, заполняя каждую клекту объектом Floor
        :param horizontal_side: кол-во клеток по горизонтали
        :param vertical_side: кол-во клеток по вертикали
        :param screen: экран
        :param x0: x-координата верхнего левого угла уровн
        :param y0: y-координата верхнего левого угла уровня
        """
        self.screen = screen
        self.x0 = x0
        self.y0 = y0

        self.vertical_side = vertical_side
        self.horizontal_side = horizontal_side
        self.size = 40
        self.tiles = []

        self.player = None
        self.finish = None
        self.completed = False

        for i in range(horizontal_side):
            column = []
            for j in range(vertical_side):
                floor = back.Floor(self.screen, grass)
                tile = Tile(None, floor)
                column.append(tile)
            self.tiles.append(column)

    def draw(self):
        """
        Рисует клетки на уровне.
        """
        for i in range(self.horizontal_side):
            for j in range(self.vertical_side):
                if self.tiles[i][j].back_obj is not None:
                    self.tiles[i][j].back_obj.draw(self.x0 + i * self.size, self.y0 + j * self.size)

        for i in range(self.horizontal_side):
            for j in range(self.vertical_side):
                if self.tiles[i][j].front_obj is not None:
                    self.tiles[i][j].front_obj.draw(self.x0 + i * self.size, self.y0 + j * self.size)

    def player_move(self, direction):
        y = self.player.y
        x = self.player.x
        if direction == 'up':
            y -= 1
        if direction == 'down':
            y += 1
        if direction == 'left':
            x -= 1
        if direction == 'right':
            x += 1

        if 0 <= x < self.horizontal_side and 0 <= y < self.vertical_side:
            print(1)
            if self.tiles[x][y].front_obj is not None:
                self.player_kick(x, y)
            else:
                print(2)
                self.player_step(x, y)

    def player_kick(self, x, y):
        self.player.draw_kick(x)
        if not isinstance(self.tiles[x][y].front_obj, front.Wall):
            _x = x + (x - self.player.x)
            _y = y + (y - self.player.y)

            if (0 <= _x < self.horizontal_side and
                    0 <= _y < self.vertical_side and
                    self.tiles[_x][_y].front_obj is None):
                self.tiles[_x][_y].front_obj = self.tiles[x][y].front_obj
                self.tiles[x][y].front_obj = None
                self.check_interaction()

    def player_step(self, x, y):
        if not isinstance(self.tiles[x][y].back_obj, back.Water):
            print(3)
            self.tiles[self.player.x][self.player.y].front_obj = None
            self.player.x = x
            self.player.y = y
            self.tiles[self.player.x][self.player.y].front_obj = self.player
            self.check_interaction()

    def check_interaction(self):
        for i in range(self.horizontal_side):
            for j in range(self.vertical_side):
                if (isinstance(self.tiles[i][j].back_obj, back.Water) and
                        isinstance(self.tiles[i][j].front_obj, front.Box)):
                    self.tiles[i][j].back_obj = self.tiles[i][j].front_obj
                    self.tiles[i][j].front_obj = None
                    self.tiles[i][j].back_obj.image = self.tiles[i][j].back_obj.images[1]
                elif (isinstance(self.tiles[i][j].back_obj, back.NextLevelTile) and
                      isinstance(self.tiles[i][j].front_obj, front.Player)):
                    self.completed = True


class Tile:
    """
    Игровая единица площади, которая содержит задние объекты (BackObj) и верхние (FrontObj).
    """

    def __init__(self, front_obj, back_obj):
        """
        Создает клетку

        """
        self.back_obj = back_obj
        self.front_obj = front_obj
