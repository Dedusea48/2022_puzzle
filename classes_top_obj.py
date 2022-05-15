import images
import pygame
import time
import classes_bottom_obj as bottom


class TopObj:
    def draw(self, screen, x0, y0):
        pass


class Box(TopObj):
    def __init__(self, images):
        self.dx = 0
        self.dy = 0
        self.a = 1
        self.b = 0
        self.size = 1
        self.images = images
        self.image = self.images[0]

    def draw(self, screen, x, y):
        temp_image = pygame.transform.rotozoom(self.image, 0, self.size)
        rect = temp_image.get_rect()
        rect.center = (x + 20 + self.dx, y + 20 + self.dy)
        screen.blit(temp_image, rect)
        self.keep_moving()

    def start_moving(self, dx, dy):
        self.dx = -40 * dx
        self.dy = -40 * dy

    def start_flight(self, max_dx, max_dy):
        self.size += 0.1
        if max_dy == 0:
            temp = max_dx * 40
        else:
            temp = max_dy * 40

        self.a = -2 / temp ** 2
        self.b = 2 / temp

    def keep_moving(self):
        if 0 < abs(self.dx) or 0 < abs(self.dy):
            if self.dx != 0:
                self.dx += -self.dx / abs(self.dx) * 5
                time.sleep(0.01)
                if self.size > 1:
                    self.size = self.a * self.dx ** 2 + self.b * self.dx + 1
            if self.dy != 0:
                self.dy += -self.dy / abs(self.dy) * 5
                time.sleep(0.01)
                if self.size > 1:
                    self.size = self.a * abs(self.dy) ** 2 + self.b * abs(self.dy) + 1
                    print(self.size)
                else:
                    self.size = 1


class Wall(Box):
    def __init__(self, images):
        super().__init__(images)


class Player(TopObj):
    """
    Создаёт игрока. При создании ему передаюся его координаты на платформе, а не на экране.
    Знает, как нарисовать себя.
    """

    def __init__(self, images, x=0, y=0):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.sprites = images
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.side = 'R'
        self.check = 0

    def draw(self, screen, x, y):
        rect = self.image.get_rect()
        rect.center = (x + 20 + self.dx, y + 20 + self.dy)
        screen.blit(self.image, rect)
        self.keep_moving()

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
                self.sprites = images.load_images_player()
            else:
                self.sprites = images.load_images_mirrored()
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

    def draw_kick(self, x):
        if x > self.x:
            self.sprites = images.load_kick()
        else:
            self.sprites = images.load_kick_left()

    def start_moving(self, dx, dy):
        """
        Функция рисует игрока, когда он движется направо.
        :param player: - игрок
        :param level: - уровень
        :param screen:- экран
        :return:
        """
        if dx > 0:
            self.change_sprites(images.walking_right())
        elif dx < 0:
            self.change_sprites(images.walking_left())
        elif self.side == 'R':
            self.change_sprites(images.walking_right())
        elif self.side == 'L':
            self.change_sprites(images.walking_left())

        self.dx = -40 * dx
        self.dy = -40 * dy

    def keep_moving(self):
        if 0 < abs(self.dx) or 0 < abs(self.dy):
            if self.dx != 0:
                self.dx += -self.dx / abs(self.dx) * 4
                time.sleep(0.02)
                self.update(0.5)

            if self.dy != 0:
                self.dy += -self.dy / abs(self.dy) * 4
                time.sleep(0.02)
                self.update(0.5)

        # else:
        #     self.dx = 0
        #     self.dy = 0

    def move_left(self, level, screen):
        """
        Функция рисует игрока, когда он движется налево.
        :param player: - игрок
        :param level: - уровень
        :param screen:- экран

        :return:
        """
        n = level.x0 + 40 * self.x
        if isinstance(level.tiles[self.x - 1][self.y].bottom_obj, bottom.Floor) and level.tiles[self.x - 1][
            self.y].top_obj is None:
            self.change_sprites(images.walking_left())
            for i in range(10):
                n -= 4
                level.tiles[self.x][self.y].bottom_obj.draw(screen, 100 + 40 * self.x, level.y0 + self.y * 40)
                level.tiles[self.x - 1][self.y].bottom_obj.draw(screen, 100 + 40 * (self.x - 1),
                                                                level.y0 + self.y * 40)
                self.draw(screen, n, level.y0 + self.y * 40)
                time.sleep(0.1)
                self.update(0.5)
                pygame.display.update()

    def move_down(self, level, screen):
        """
        Функция рисует игрока, когда он движется вниз.
        :param player: - игрок
        :param level: - уровень
        :param screen:- экран
        :return:
        """
        n = level.y0 + 40 * self.y
        if isinstance(level.tiles[self.x][self.y + 1].bottom_obj, bottom.Floor) and level.tiles[self.x][
            self.y + 1].top_obj is None:
            self.change_sprites(images.player_turn())
            for i in range(10):
                n += 4
                level.tiles[self.x][self.y].bottom_obj.draw(screen, 100 + 40 * self.x, level.y0 + self.y * 40)
                level.tiles[self.x - 1][self.y].bottom_obj.draw(screen, 100 + 40 * (self.x),
                                                                level.y0 + (self.y + 1) * 40)
                self.draw(screen, level.x0 + self.x * 40, n, )
                time.sleep(0.04)
                self.update(0.5)
                pygame.display.update()

    def move_up(self, level, screen):
        """
        Функция рисует игрока, когда он движется вверх.
        :param player: - игрок
        :param level: - уровень
        :param screen:- экран
        :return:
        """
        n = level.y0 + 40 * self.y
        if isinstance(level.tiles[self.x][self.y - 1].bottom_obj, bottom.Floor) and level.tiles[self.x][
            self.y - 1].top_obj is None:
            self.change_sprites(images.player_turn())
            for i in range(10):
                n -= 4
                level.tiles[self.x][self.y].bottom_obj.draw(screen, 100 + 40 * self.x, level.y0 + self.y * 40)
                level.tiles[self.x - 1][self.y].bottom_obj.draw(screen, 100 + 40 * (self.x),
                                                                level.y0 + (self.y - 1) * 40)
                self.draw(screen, level.x0 + self.x * 40, n, )
                time.sleep(0.04)
                self.update(0.5)
                pygame.display.update()
