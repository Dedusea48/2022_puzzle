import images


class FrontObj:
    def draw(self, screen, x0, y0):
        pass


class Box(FrontObj):
    def __init__(self, images):
        self.images = images
        self.image = self.images[0]

    def draw(self, screen, x, y):
        rect = self.image.get_rect()
        rect.center = (x + 20, y + 20)
        screen.blit(self.image, rect)


class Wall(Box):
    def __init__(self, images):
        super().__init__(images)


class Player(FrontObj):
    """
    Создаёт игрока. При создании ему передаюся его координаты на платформе, а не на экране.
    Знает, как нарисовать себя.
    """

    def __init__(self, images, x=0, y=0):
        self.x = x
        self.y = y
        self.sprites = images
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.side = 'R'

    def draw(self, screen, x, y):
        rect = self.image.get_rect()
        rect.center = (x + 20, y + 20)
        screen.blit(self.image, rect)

    def change_sprites(self, images):
        self.sprites = images

    def to_left(self):
        self.side = 'L'

    def to_right(self):
        self.side = 'R'

    def update(self, speed):
        """
        Функция меняет изображения игрока с заданной скоростью
        :param speed: - скорость анимации
        :return:
        """
        self.current_sprite += speed
        if int(self.current_sprite) >= len(self.sprites):
            if self.side == 'R':
                self.sprites = images.upload_images_player()
            else:
                self.sprites = images.upload_images_mirrored()
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

    def draw_kick(self, x):
        if x > self.x:
            self.sprites = images.upload_kick()
        else:
            self.sprites = images.upload_kick_left()
