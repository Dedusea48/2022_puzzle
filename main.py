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
mirrored = images.upload_images_mirrored()
right = images.upload_images_right()
kick = images.upload_kick()
wall = []
box_images = images.box_images()
grass = pygame.image.load('Grass.jpg')
ladder = pygame.image.load('ladder.png')
wall.append(pygame.image.load('wall.png'))
water = images.water_images()
water_images = images.water_images()
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
finished = [False]
level = classes.Level(10, 10, screen, 100, 100)
player = front.Player(level.tiles[1][2], level, standing)
level.tiles[1][2].front_obj = player

front.Box(level.tiles[3][2], box_images)
front.Box(level.tiles[6][7], box_images)

front.Wall(level.tiles[5][3], wall)

water_block1 = back.Water(level.tiles[7][3], water_images)
water_block2 = back.Water(level.tiles[7][4], water_images)
back.Ladder(level.tiles[7][7], ladder)

level2 = classes.Level(10, 10, screen, 100, 100)

FLOORS = (level, level2)


def game_process(is_finished, player):
    FLOORS[player.floor].draw()
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_finished[0] = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move('up')
            elif event.key == pygame.K_DOWN:
                player.move('down')
            elif event.key == pygame.K_LEFT:
                player.change_sprites(mirrored)
                player.move('left')
            elif event.key == pygame.K_RIGHT:
                player.change_sprites(standing)
                player.move('right')
            elif event.key == pygame.K_SPACE:
                player.change_floor('up', FLOORS)
            elif event.key == pygame.K_LSHIFT:
                player.change_floor('down', FLOORS)
    player.update(0.25)
    water_block1.update(0.1)
    water_block2.update(0.1)

while not finished[0]:
    game_process(finished, player)

    player.update(0.25)
