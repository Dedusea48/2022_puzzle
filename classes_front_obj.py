import images
import pygame
import time
import classes_back_obj


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

def move_right(player, level, screen):
    """
    Функция рисует игрока, когда он движется направо.
    :param player: - игрок
    :param level: - уровень
    :return:
    """
    n = 100 + 40*player.x
    if (level.tiles[player.x +1][player.y].back_obj.name == 'floor') and (level.tiles[player.x +1][player.y].front_obj == None):
        player.change_sprites(images.walking_right())
        for i in range(10):
            n += 4
            level.tiles[player.x][player.y].back_obj.draw(screen, 100 + 40*player.x, level.y0 + player.y*40)
            level.tiles[player.x + 1][player.y].back_obj.draw(screen, 100 + 40*(player.x+1), level.y0 + player.y*40)
            player.draw(screen, n, level.y0 + player.y*40)
            time.sleep(0.04)
            player.update(0.5)

            pygame.display.update()

def move_left(player, level, screen):
    """
    Функция рисует игрока, когда он движется налево.
    :param player: - игрок
    :param level: - уровень
    :return:
    """
    n = level.x0 + 40*player.x
    if (level.tiles[player.x -1][player.y].back_obj.name == 'floor') and (level.tiles[player.x - 1][player.y].front_obj == None):
        player.change_sprites(images.walking_left())
        for i in range(10):
            n -= 4
            level.tiles[player.x][player.y].back_obj.draw(screen,100 + 40*player.x, level.y0 + player.y*40)
            level.tiles[player.x - 1][player.y].back_obj.draw(screen,100 + 40*(player.x-1), level.y0 + player.y*40)
            player.draw(screen, n, level.y0 + player.y*40)
            time.sleep(0.04)
            player.update(0.5)
            pygame.display.update()

def move_down(player, level, screen):
    """
    Функция рисует игрока, когда он движется вниз.
    :param player: - игрок
    :param level: - уровень
    :return:
    """
    n = level.y0 + 40*player.y
    if (level.tiles[player.x][player.y+1].back_obj.name == 'floor') and (level.tiles[player.x ][player.y+1].front_obj == None):
        player.change_sprites(images.player_turn())
        for i in range(10):
            n += 4
            level.tiles[player.x][player.y].back_obj.draw(screen,100 + 40*player.x, level.y0 + player.y*40)
            level.tiles[player.x - 1][player.y].back_obj.draw(screen,100 + 40*(player.x), level.y0 + (player.y+1)*40)
            player.draw(screen, level.x0 + player.x*40, n, )
            time.sleep(0.04)
            player.update(0.5)
            pygame.display.update()

def move_up(player, level, screen):
    """
    Функция рисует игрока, когда он движется вверх.
    :param player: - игрок
    :param level: - уровень
    :return:
    """
    n = level.y0 + 40*player.y
    if (level.tiles[player.x][player.y-1].back_obj.name == 'floor') and (level.tiles[player.x ][player.y-1].front_obj == None):
        player.change_sprites(images.player_turn())
        for i in range(10):
            n -= 4
            level.tiles[player.x][player.y].back_obj.draw(screen,100 + 40*player.x, level.y0 + player.y*40)
            level.tiles[player.x - 1][player.y].back_obj.draw(screen,100 + 40*(player.x), level.y0 + (player.y-1)*40)
            player.draw(screen, level.x0 + player.x*40, n, )
            time.sleep(0.04)
            player.update(0.5)
            pygame.display.update()
