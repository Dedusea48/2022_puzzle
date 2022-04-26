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

images = images.upload_images_player()
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
finished = False
level = classes.Level(10, 10, screen, 100, 100)
player = front.Player(level.tiles[1][2], level)
level.tiles[1][2].front_obj = player

level.tiles[3][2].front_obj = front.Box(level.tiles[3][2])

level.tiles[5][3].front_obj = front.Wall(level.tiles[5][3])

level.tiles[7][3].back_obj = back.Water(level.tiles[7][3])

while not finished:
    level.draw()
    pygame.display.update()
    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move('up')
            elif event.key == pygame.K_DOWN:
                player.move('down')
            elif event.key == pygame.K_LEFT:
                player.move('left')
            elif event.key == pygame.K_RIGHT:
                player.move('right')
    # player.update(0.25)
