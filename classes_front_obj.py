class FrontObj:
    def __init__(self, the_tile):
        self.x = the_tile.x
        self.y = the_tile.y
        self.screen = the_tile.screen

    def draw(self):
        pass


class Player(FrontObj):  # TODO переделать под новый класс FrontObj
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
