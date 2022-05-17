import pygame
import pygame.draw as dr


class BottomObj:
    def __init__(self, _images):
        self.current = 0
        self.images = _images
        self.image = self.images[self.current]

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


class Floor(BottomObj):
    def __init__(self, _images):
        super().__init__(_images)


class Water(BottomObj):
    def __init__(self, _images):
        super().__init__(_images)


class NextLevelTile(BottomObj):
    def __init__(self, _images, x=0, y=0):
        super().__init__(_images)
        self.x = x
        self.y = y
        self.image = _images[0]


class Spring(BottomObj):
    def __init__(self, direction, power, _images):
        super().__init__(_images)
        self.direction = direction
        self.power = power
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
