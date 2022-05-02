import pygame.draw as dr
import images

def border_control(x, y, level):
    if 0 <= x < level.horizontal_side and 0 <= y < level.vertical_side and level.tiles[x][y].front_obj is None:
        return True
    return False


class FrontObj:
    def __init__(self, the_tile):
        self.x = the_tile.x
        self.y = the_tile.y
        self.name = None
        self.screen = the_tile.screen

    def draw(self, x0, y0):
        pass


class Box(FrontObj):
    def __init__(self, the_tile, images):
        super().__init__(the_tile)
        the_tile.front_obj = self
        self.name = "box"
        self.color = 'orange'
        self.images = images
        self.image = self.images[0]


    def draw(self, x0, y0):
        rect = self.image.get_rect()
        rect.center = (x0 + self.x * 40 + 20, y0 + self.y * 40 + 20)
        self.screen.blit(self.image, rect)

    def check_floor(self, level):
        if level.tiles[self.x][self.y].back_obj.name == 'water':
            level.tiles[self.x][self.y].front_obj = None
            level.tiles[self.x][self.y].back_obj = self
            self.image = self.images[1]


class Wall(Box):
    def __init__(self, the_tile, images):
        the_tile.front_obj = self
        super().__init__(the_tile, images)
        self.name = 'wall'
        self.color = 'gray'




class Player(FrontObj):
    """
    Создаёт игрока. При создании ему передаюся его координаты на платформе, а не на экране.
    Знает, как нарисовать себя.
    """

    def __init__(self, the_tile, level, images):
        the_tile.front_obj = self
        super().__init__(the_tile)
        self.name = 'player'
        self.floor = 0
        self.level = level
        self.sprites = images
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.side = 'R'



    def draw(self, x0, y0):
        rect = self.image.get_rect()
        rect.center = (x0 + self.x * 40 + 20, y0 + self.y * 40 + 20)
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




    def move(self, direction):
        _y = self.y
        _x = self.x

        if direction == 'up':
            _y -= 1
        if direction == 'down':
            _y += 1
        if direction == 'left':
            _x -= 1
        if direction == 'right':
            _x += 1

        if border_control(_x, _y, self.level):
            self.step(_x, _y)
        elif 0 <= _x < self.level.horizontal_side and 0 <= _y < self.level.vertical_side:
            self.kick(_x, _y)


    def step(self, _x, _y):
        if self.level.tiles[_x][_y].back_obj.name != 'water':
            self.level.tiles[self.x][self.y].front_obj = None
            self.level.tiles[_x][_y].front_obj = self
            self.x = _x
            self.y = _y


    def draw_kick(self, x):
        if x > self.x :
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



    def kick(self, _x, _y):
        if self.level.tiles[_x][_y].front_obj.name != 'wall':
            __x = 2 * _x - self.x
            __y = 2 * _y - self.y

            if border_control(__x, __y, self.level):
                self.level.tiles[__x][__y].front_obj = self.level.tiles[_x][_y].front_obj
                self.level.tiles[_x][_y].front_obj = None
                self.level.tiles[__x][__y].front_obj.x = __x
                self.level.tiles[__x][__y].front_obj.y = __y
                self.level.tiles[__x][__y].front_obj.check_floor(self.level)
                self.draw_kick(_x)
