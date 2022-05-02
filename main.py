import classes
import pygame
import classes_front_obj as front
import classes_back_obj as back
import images

WIDTH = 600
HEIGHT = 600
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
finished = [False]

level = classes.Level(10, 10, screen, 100, 100)
player = front.Player(level.tiles[1][2], level, images.upload_images_player())
level.tiles[1][2].front_obj = player

front.Box(level.tiles[3][2], images.box_images())
front.Box(level.tiles[6][7], images.box_images())

front.Wall(level.tiles[5][3], images.wall())

water_block1 = back.Water(level.tiles[7][3], images.water_images())
water_block2 = back.Water(level.tiles[7][4], images.water_images())
back.next_level_tile(level.tiles[7][7], images.ladder())
level2 = classes.Level(10, 10, screen, 100, 100)

FLOORS = (level, level2)


def game_process(is_finished, player):
    FLOORS[player.floor].draw()
    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move('up')
            elif event.key == pygame.K_DOWN:
                player.move('down')
            elif event.key == pygame.K_LEFT:
                player.change_sprites(images.upload_images_mirrored())
                player.move('left')
                player.to_left()
            elif event.key == pygame.K_RIGHT:
                player.change_sprites(images.upload_images_player())
                player.move('right')
                player.to_right()
            elif event.key == pygame.K_ESCAPE:
                finished[0] = True

    player.update(0.5)
    water_block1.update(0.2)
    water_block2.update(0.2)

