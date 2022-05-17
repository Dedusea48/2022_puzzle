import pygame
import pygame.draw as dr


class BottomObj:
    def draw(self, screen, x, y):
        """
        Функция рисует обьект.
        :param screen: - экран
        :param x: - координата x
        :param y: - координата y
        :return:
        """
        pass


class Floor(BottomObj):
    def __init__(self, _images):
        self.current = 0
        # self.images = images
        self.image = _images  # [self.current]
        self.name = "floor"

    def draw(self, screen, x, y):
        """
        Функция рисует пол.
        :param screen: - экран
        :param x: - координата x
        :param y: - координата y
        :return:

        """
        rect = self.image.get_rect()
        rect.center = (x + 20, y + 20)
        screen.blit(self.image, rect)


class Water(BottomObj):
    def __init__(self, _images):
        self.current = 0
        self.images = _images
        self.image = self.images[self.current]
        self.name = "water"

    def draw(self, screen, x, y):
        """
        Функция рисует воду.
        :param screen: - экран
        :param x: - координата x
        :param y: - координата y
        :return:
        """
        rect = self.image.get_rect()
        rect.center = (x + 20, y + 20)
        screen.blit(self.image, rect)

    def update(self, speed):
        self.current += speed
        if int(self.current) >= len(self.images):
            self.current = 0
        self.image = self.images[int(self.current)]


class NextLevelTile(BottomObj):
    def __init__(self, image, x=0, y=0):
        self.x = x
        self.y = y
        self.image = image[0]

    def draw(self, screen, x, y):
        """
        Функция рисует клетку.
        :param screen: - экран
        :param x: - координата x
        :param y: - координата y
        :return:

        """
        rect = self.image.get_rect()
        rect.center = (x + 20, y + 20)
        screen.blit(self.image, rect)


class Spring(BottomObj):
    def __init__(self, direction, power, _images):
        self.direction = direction
        self.power = power
        self.current = 0
        angle = 0
        if direction == 'up':
            angle = 0
        if direction == 'down':
            angle = 180
        if direction == 'left':
            angle = 90
        if direction == 'right':
            angle = 270

        self.images = []
        for image in _images:
            self.images.append(pygame.transform.rotozoom(image, angle, 1))
        self.image = pygame.transform.rotozoom(_images[self.current], angle, 1)

    def draw(self, screen, x, y):
        """
        Функция рисует пружину.
        :param screen: - экран
        :param x: - координата x
        :param y: - координата y
        :return:
        """
        dr.rect(screen, 'yellow', (x, y, 40, 40))
        rect = self.image.get_rect()
        rect.center = (x + 20, y + 20)
        screen.blit(self.image, rect)

    def update(self, speed):
        self.current += speed
        if int(self.current) >= len(self.images):
            self.current = 0
        self.image = self.images[int(self.current)]
