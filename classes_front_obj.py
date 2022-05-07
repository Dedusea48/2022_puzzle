import pygame.draw as dr
import images


# def border_control(x, y, level):
#     if 0 <= x < level.horizontal_side and 0 <= y < level.vertical_side and level.tiles[x][y].front_obj is None:
#         return True
#     return False


class FrontObj:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, x0, y0):
        pass


class Box(FrontObj):
    def __init__(self, screen, images):
        super().__init__(screen)
        self.images = images
        self.image = self.images[0]

    def draw(self, x, y):
        rect = self.image.get_rect()
        rect.center = (x + 20, y + 20)
        self.screen.blit(self.image, rect)

    # def check_floor(self, level):
    #     if level.tiles[self.x][self.y].back_obj.name == 'water':
    #         level.tiles[self.x][self.y].front_obj = None
    #         level.tiles[self.x][self.y].back_obj = self
    #         self.image = self.images[1]


class Wall(Box):
    def __init__(self, screen, images):
        super().__init__(screen, images)


class Player(FrontObj):
    """
    Создаёт игрока. При создании ему передаюся его координаты на платформе, а не на экране.
    Знает, как нарисовать себя.
    """

    def __init__(self, screen, x, y, images):
        super().__init__(screen)
        self.x = x
        self.y = y
        self.sprites = images
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.side = 'R'

    def draw(self, x, y):
        rect = self.image.get_rect()
        rect.center = (x + 20, y + 20)
        self.screen.blit(self.image, rect)

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

    # def check(self):
    #     # kick_list = images.upload_kick()
    #     # flag = True
    #     # for i in self.sprites:
    #     #     for j in kick_list:
    #     #         if j!= i:
    #     #             flag = False
    #     # if flag:
    #     if int(self.current_sprite) >= len(self.sprites):
    #         self.sprites = images.upload_images_player()


