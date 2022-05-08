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
                floor = back.Floor(grass)
                tile = Tile(None, floor)
                column.append(tile)
            self.tiles.append(column)

    def add_player(self, _player, x, y):
        """
        Добавляет игрока в уровень. Обязательно добавлять игрока именно этим методом.
        :param _player: объект игрока
        :param x: координата x игрока на поле
        :param y: координата y игрока на поле
        :return:
        """
        self.tiles[x][y].front_obj = _player
        self.player = _player
        _player.x = x
        _player.y = y

    def add_finish(self, _finish, x, y):
        """
        Добавляет плитку перехода на следующий уровень. Обязательно добавлять
        данную плитку именно этим методом.
        :param _finish: объект плитки перехода на следующий уровень
        :param x: координата x данной плитки
        :param y: координата y данной плитки
        :return:
        """
        self.tiles[x][y].back_obj = _finish
        self.finish = _finish
        _finish.x = x
        _finish.y = y

    def draw(self):
        """
        Рисует клетки на уровне - сначала все нижние, потом все верхние.
        """
        for i in range(self.horizontal_side):
            for j in range(self.vertical_side):
                if self.tiles[i][j].back_obj is not None:
                    self.tiles[i][j].back_obj.draw(self.screen, self.x0 + i * self.size, self.y0 + j * self.size)

        for i in range(self.horizontal_side):
            for j in range(self.vertical_side):
                if self.tiles[i][j].front_obj is not None:
                    self.tiles[i][j].front_obj.draw(self.screen, self.x0 + i * self.size, self.y0 + j * self.size)

    def player_move(self, direction):
        """
        Движение игрока в зависимости от направления.
        Если клетка по направлению движения свободна(т.е верхний объект пуст), то игрок пробует сделать шаг.
        Но если данная клетка занята, то игрок пинает объект на этой клетке.
        :param direction: направление движения
        :return:
        """
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
            if self.tiles[x][y].front_obj is not None:
                self.player_kick(x, y)
            else:
                self.player_step(x, y)

    def player_kick(self, x, y):
        """
        Пинок объекта с координатами x и y.
        Если следующая за объектом клетка по направлению пинка свободна(т.е верхний объект пуст),
        то объект перемщается в данную клетку, иначе не перемещается.
        Игрок не может пинком перемещать стены(Wall).
        :param x: координата x объекта
        :param y: координата y объекта
        :return:
        """
        self.player.draw_kick(x)
        if not isinstance(self.tiles[x][y].front_obj, front.Wall):
            _x = x + (x - self.player.x)
            _y = y + (y - self.player.y)

            if (0 <= _x < self.horizontal_side and
                    0 <= _y < self.vertical_side and
                    self.tiles[_x][_y].front_obj is None):
                self.tiles[_x][_y].front_obj = self.tiles[x][y].front_obj
                self.tiles[x][y].front_obj = None

    def player_step(self, x, y):
        """
        Перемещение игрока в клетку с координатами x и y.
        Если нижний объект клетки не вода(Water), то игрок перемещается в верхний объект клетки.
        :param x: координата x клетки
        :param y: координата y клетки
        :return:
        """
        if not isinstance(self.tiles[x][y].back_obj, back.Water):
            self.tiles[self.player.x][self.player.y].front_obj = None
            self.player.x = x
            self.player.y = y
            self.tiles[self.player.x][self.player.y].front_obj = self.player

    def check_interaction(self):
        """
        Метод проверяет весь уровень на наличие взаимодействий между объектами.
        :return:
        """
        for i in range(self.horizontal_side):
            for j in range(self.vertical_side):
                if self.water_interaction(i, j):
                    pass
                elif self.next_level_tile_interaction(i, j):
                    pass

    def water_interaction(self, i, j):
        """
        Проверка и выполнение действий воды.
        Если нижний объект клетки с координатами i и j - вода(Water), то картинка воды обновляется,
        чтобы создать эффект бликов воды.
        Также если верхний объект - это коробка(Box), то коробка проваливается вниз, заменяя собой воду
        и создавая таким образом мост, по которому игрок может ходить.
        :param i: координата x проверяемой клетки
        :param j: координата y проверяемой клетки
        :return: bool - является ли нижний объект водой, а верхний - коробкой
        """
        if isinstance(self.tiles[i][j].back_obj, back.Water):
            self.tiles[i][j].back_obj.update(0.2)
            if isinstance(self.tiles[i][j].front_obj, front.Box):
                self.tiles[i][j].back_obj = self.tiles[i][j].front_obj
                self.tiles[i][j].front_obj = None
                self.tiles[i][j].back_obj.image = self.tiles[i][j].back_obj.images[1]
                return True

    def next_level_tile_interaction(self, i, j):
        """
        Проверяет, находится ли игрок на плитке перехода на следующий уровень.
        Если да, то уровень отмечается завершённым.
        :param i: координата x проверяемой клетки
        :param j: координата y проверяемой клетки
        :return: bool - находится ли игрок на плитке перехода на следующий уровень
        """
        if (isinstance(self.tiles[i][j].back_obj, back.NextLevelTile) and
                isinstance(self.tiles[i][j].front_obj, front.Player)):
            self.completed = True
            return True


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
