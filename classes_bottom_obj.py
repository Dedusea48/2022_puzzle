import pygame.draw as dr


class BottomObj:
    def draw(self, screen, x, y):
        pass


class Floor(BottomObj):
    def __init__(self, image):
        self.image = image

    def draw(self, screen, x, y):
        rect = self.image.get_rect()
        rect.center = (x + 20, y + 20)
        screen.blit(self.image, rect)


class Water(BottomObj):
    def __init__(self, images):
        self.current = 0
        self.images = images
        self.image = self.images[self.current]

    def draw(self, screen, x, y):
        rect = self.image.get_rect()
        rect.center = (x + 20, y + 20)
        screen.blit(self.image, rect)

    def update(self, speed):
        self.current += speed
        if int(self.current) >= len(self.images):
            self.current = 0
        self.image = self.images[int(self.current)]


class Spring(BottomObj):
    def __init__(self, direction, power):
        self.direction = direction
        self.power = power

    def draw(self, screen, x, y):
        dr.rect(screen, 'green', [x, y, 40, 40])


class NextLevelTile(BottomObj):
    def __init__(self, image, x=0, y=0):
        self.x = x
        self.y = y
        self.image = image

    def draw(self, screen, x, y):
        rect = self.image.get_rect()
        rect.center = (x + 20, y + 20)
        screen.blit(self.image, rect)
