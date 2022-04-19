import classes
import pygame
from PIL import Image, ImageSequence
import glob
import images

WIDTH = 600
HEIGHT = 600
FPS = 30


images = images.upload_images_player()
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
finished = False
level = classes.Level(5, 10, screen, 100, 100)
player = classes.Player(1, 2, images)
level.tiles[1][2][1] = player

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
                player.step_up(level)
            elif event.key == pygame.K_DOWN:
                player.step_down(level)
            elif event.key == pygame.K_LEFT:
                player.step_left(level)
            elif event.key == pygame.K_RIGHT:
                player.step_right(level)
    player.update(0.25)
