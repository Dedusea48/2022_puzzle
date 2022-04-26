import classes
import pygame
import classes_front_obj as front
import classes_back_obj as back
# import classes_front_obj
# from PIL import Image, ImageSequence
# import glob
import images
import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Tuple, Any

surface = create_example_window('Example - Simple', (600, 400))


def start_the_game() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """

    WIDTH = 600
    HEIGHT = 600
    FPS = 30

    standing = images.upload_images_player()
    right = images.upload_images_right()
    kick = images.upload_kick()
    box_img = pygame.image.load('box.png')
    wall_img = pygame.image.load('wall.png')
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

    while not finished:
        level.draw()
        pygame.display.update()
        clock.tick(FPS)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    finished = True
                elif event.key == pygame.K_UP:
                    player.move('up')
                elif event.key == pygame.K_DOWN:
                    player.move('down')
                elif event.key == pygame.K_LEFT:
                    player.move('left')
                elif event.key == pygame.K_RIGHT:
                    player.move('right')
                elif event.key == pygame.K_SPACE:
                    player.change_floor('up', floors)  # TODO СДЕЛАТЬ МАССИВ ЭТАЖЕЙ (наверное)
                elif event.key == pygame.K_LSHIFT:
                    player.change_floor('down',
                                        floors)  # TODO СДЕЛАТЬ МАССИВ ЭТАЖЕЙ (я не знаю как вы будете это делать)

        player.update(0.25)


mytheme = pygame_menu.Theme(widget_font=pygame_menu.font.FONT_8BIT,
                            title_font = pygame_menu.font.FONT_8BIT,
                            background_color=(249, 199, 61), # transparent background
                            title_background_color=(182, 146, 48))


menu = pygame_menu.Menu(
    height=300,
    width=400,
    theme=mytheme,
    title = ''
)

menu.add.button('Play', start_the_game)
menu.add.button('Continue', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)