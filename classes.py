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


class Block:
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0


class Player(Block):
    """
    Создаёт игрока. При создании ему передаюся его координаты на платформе, а не на экране.
    Знает, как нарисовать себя.
    """

    def __init__(self, x0, y0, images):
        super().__init__(x0, y0)
        self.step = 1
        self.side = 40
        self.color = YELLOW
        self.sprites = images
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

    def move_up(self, obj):
        if obj.y == self.y + self.step:
            obj.y += self.step
        else:
            self.y -= self.step

    def move_down(self, obj):
        if obj.y == self.y - self.step:
            obj.y -= self.step
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

    def step_up(self, platform):
        """
        Делает шаг в верхнюю сторону.
        :param platform: платформа, на которой находится игрок.
        :return:
        """
        platform.squares[self.x][self.y][1] = None
        self.y -= self.step
        platform.squares[self.x][self.y][1] = self

    def step_down(self, platform):
        """
        Делает шаг в нижнюю сторону.
        :param platform: платформа, на которой находится игрок.
        :return:
        """
        platform.squares[self.x][self.y][1] = None
        self.y += self.step
        platform.squares[self.x][self.y][1] = self

    def step_left(self, platform):
        """
        Делает шаг в левую сторону.
        :param platform: платформа, на которой находится игрок.
        :return:
        """
        platform.squares[self.x][self.y][1] = None
        self.x -= self.step
        platform.squares[self.x][self.y][1] = self

    def step_right(self, platform):
        """
        Делает шаг в правую сторону.
        :param platform: платформа, на которой находится игрок.
        :return:
        """
        platform.squares[self.x][self.y][1] = None
        self.x += self.step
        platform.squares[self.x][self.y][1] = self

    def draw(self, screen, x, y):  # QUESTION Зачем? Можно же просто обратиться к полю.
        rect = self.image.get_rect()
        rect.center = (x + 20, y + 20)
        screen.blit(self.image, rect)

    def update(self, speed):
        """
        Функция меняет изображения игрока с заданной скоростью
        :param speed: - скорость анимации
        :return:
        """
        self.current_sprite += speed
        if int(self.current_sprite) >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]


class Platform:
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
        self.square_side = 40
        self.colors = [GREEN, GREY]
        self.squares = []

        check = 0
        for i in range(horizontal_side):
            column = []
            check = not check
            for j in range(vertical_side):
                tile = Tile(self.square_side, self.colors[check])
                square = [tile, None]
                column.append(square)
                check = not check
            self.squares.append(column)

    def size(self):
        return self.vertical_side, self.horizontal_side

    def draw(self):
        """
        Рисует все объекты, которые находятся в клетках (squares).
        :return:
        """
        check = 0
        for i in range(self.horizontal_side):
            check = not check
            for j in range(self.vertical_side):

                for k in [0, 1]:
                    if self.squares[i][j][k] is not None:
                        self.squares[i][j][k].draw(self.screen, self.x0 + i * self.square_side,
                                                   self.y0 + j * self.square_side)

                check = not check


class Tile:
    """
    Создаёт квадратную плитку данного цвета.
    Знает, как себя нарисовать.
    """

    def __init__(self, side, color):
        self.side = side
        self.color = color

    def draw(self, screen, x, y):
        dr.rect(screen, self.color, [x, y, self.side, self.side])
