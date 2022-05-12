class BackObj:
    def draw(self, screen, x, y):
        pass


class Floor(BackObj):
    def __init__(self, image):
        self.image = image

    def draw(self, screen, x, y):
        rect = self.image.get_rect()
        rect.center = (x + 20, y + 20)
        screen.blit(self.image, rect)


class Water(BackObj):
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


# class Spring(BackObj):
#     def __init__(self, the_tile, _x_jump, _y):
#         super().__init__(the_tile)
#         self.name = 'spring'
#         self.x_jump = 0
#         self.y_jump = 0
#
#     def draw(self, x0, y0):
#         dr.rect(self.screen, 'green', [x0 + self.x * self.size, y0 + self.y * self.size,
#                                        self.size, self.size])
#
#     def check_up(self, level):
#         if level.tiles[self.x][self.y].front_obj is not None:
#             level.tiles[self.x + self.x_jump][self.y + self.y_jump].front_obj = level.tiles[self.x][self.y].front_obj
#             level.tiles[self.x + self.x_jump][self.y + self.y_jump].front_obj.x = self.x + self.x_jump
#             level.tiles[self.x + self.x_jump][self.y + self.y_jump].front_obj.y = self.y + self.y_jump
#             level.tiles[self.x][self.y].front_obj = None


class NextLevelTile(BackObj):
    def __init__(self, image, x=0, y=0):
        self.x = x
        self.y = y
        self.image = image[0]

    def draw(self, screen, x, y):
        rect = self.image.get_rect()
        rect.center = (x + 20, y + 20)
        screen.blit(self.image, rect)
