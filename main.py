import classes
import pygame
import classes_front_obj as front
import classes_back_obj as back
# import classes_front_obj
# from PIL import Image, ImageSequence
# import glob
import images

WIDTH = 600
HEIGHT = 600
FPS = 30

standing = images.upload_images_player()
right = images.upload_images_right()
kick = images.upload_kick()
box_img = pygame.image.load('box.png')
wall = []
wall_img = pygame.image.load('wall.png')
bridge = pygame.image.load('bridge.png')
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
finished = False
level = classes.Level(10, 10, screen, 100, 100)
player = front.Player(level.tiles[1][2], level, standing)
level.tiles[1][2].front_obj = player

front.Box(level.tiles[3][2], box_img)
front.Box(level.tiles[6][7], box_img)

front.Wall(level.tiles[5][3], wall_img)

back.Water(level.tiles[7][3])
back.Water(level.tiles[7][4])
back.Ladder(level.tiles[7][7])

level2 = classes.Level(10, 10, screen, 100, 100)

FLOORS = (level, level2)


def game_process(is_finished, player):
    FLOORS[player.floor].draw()
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move('up')
            elif event.key == pygame.K_DOWN:
                player.move('down')
            elif event.key == pygame.K_LEFT:
                player.move('left')
            elif event.key == pygame.K_RIGHT:
                player.move('right')
            elif event.key == pygame.K_SPACE:
                player.change_floor('up', FLOORS)
            elif event.key == pygame.K_LSHIFT:
                player.change_floor('down', FLOORS)
    player.update(0.25)


while not finished:
    game_process(finished, player)

    player.update(0.25)
