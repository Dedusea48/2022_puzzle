"""
Модуль, в котором содержатся классы Level и Tile
"""

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
        """
        Создает уровень, заполняя каждую клекту объектом Floor
        :param horizontal_side: кол-во клеток по горизонтали
        :param vertical_side: кол-во клеток по вертикали
        :param screen: экран
        :param x0: x-координата верхнего левого угла уровня
        :param y0: y-координата верхнего левого угла уровня
        """
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
        Рисует клетки на уровне.
        """
        for i in range(self.horizontal_side):
            for j in range(self.vertical_side):
                self.tiles[i][j].draw(self.x0, self.y0)

    def return_obj(self, obj):
        """
        Возвращает объект на уровне с названием obj
        :param obj: название объекта
        :return: объект
        """
        for column in self.tiles:
            for tile in column:
                if tile.return_back_obj() and tile.return_back_obj().name == obj:
                    return tile.return_back_obj()
                elif tile.return_front_obj() and tile.return_front_obj().name == obj:
                    return tile.return_front_obj()

    def check_next_level(self):
        """
        Проверяет, находится ли игрок на клетке финиша
        :return: True или False
        """
        return self.return_obj('next_level_tile').x == self.return_obj('player').x and \
               self.return_obj('next_level_tile').y == self.return_obj('player').y


class Tile:
    """
    Игровая единица площади, которая содержит задние объекты (BackObj) и верхние (FrontObj).
    """

    def __init__(self, x, y, screen):
        """
        Создает клетку
        :param x: x-координата клетки
        :param y: y-координата клетки
        :param screen: экран
        """
        self.x = x
        self.y = y
        self.back_obj = None
        self.front_obj = None
        self.size = 40
        self.screen = screen

    def draw(self, x0, y0):
        """Рисует клетку, то есть все объекты на клетке"""
        if self.back_obj is not None:
            self.back_obj.draw(x0, y0)
        if self.front_obj is not None:
            self.front_obj.draw(x0, y0)

    def return_back_obj(self):
        """
        Возвращает задний объект на клетке
        :return: задний объект
        """
        return self.back_obj

    def return_front_obj(self):
        """
        Возвращает передний объект на клетке
        :return: передний объектч
        """
        return self.front_obj
