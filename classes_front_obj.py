class FrontObj:
    def __init__(self, the_tile):
        self.x = the_tile.x
        self.y = the_tile.y
        self.name = None
        self.screen = the_tile.screen

    def draw(self):
        pass


class Box(FrontObj):
    def __init__(self, the_tile):
        super().__init__(the_tile)
        self.name = "box"

    def draw(self):
        pass


class Player(FrontObj):  # TODO переделать под новый класс FrontObj
    """
    Создаёт игрока. При создании ему передаюся его координаты на платформе, а не на экране.
    Знает, как нарисовать себя.
    """

    def draw(self):
        pass

    def move_up(self, objects):
        for obj in objects:
            if obj.name == "box" and obj.y + 1 == self.y:
                obj.y -= 1
                break
        self.y -= 1

    def move_down(self, objects):
        for obj in objects:
            if obj.name == "box" and obj.y - 1 == self.y:
                obj.y += 1
                break
        self.y += 1

    def move_left(self, objects):
        for obj in objects:
            if obj.name == "box" and obj.x + 1 == self.x:
                obj.x -= 1
                break
        self.x -= 1

    def move_right(self, objects):
        for obj in objects:
            if obj.name == "box" and obj.x - 1 == self.y:
                obj.x += 1
                break
        self.x += 1
