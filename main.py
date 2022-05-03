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

# LEVEL 1
level1 = classes.Level(10, 10, screen, 100, 100)
player = front.Player(level1.tiles[1][2], level1, images.upload_images_player())
exit1 = back.next_level_tile(level1.tiles[7][7], images.ladder())

front.Box(level1.tiles[3][2], images.box_images())
front.Box(level1.tiles[6][7], images.box_images())

front.Wall(level1.tiles[5][3], images.wall())

water_block1 = back.Water(level1.tiles[7][3], images.water_images())
water_block2 = back.Water(level1.tiles[7][4], images.water_images())

# LEVEL 2
level2 = classes.Level(10, 10, screen, 100, 100)
player2 = front.Player(level2.tiles[4][4], level2, images.upload_images_player())
exit2 = back.next_level_tile(level2.tiles[3][2], images.ladder())

front.Box(level2.tiles[5][5], images.box_images())

LEVELS = (level1, level2)
cur_level = 0


def game_process(is_finished, cur_level):
    LEVELS[cur_level].draw()
    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_finished[0] = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                LEVELS[cur_level].return_player().move('up')
            elif event.key == pygame.K_DOWN:
                LEVELS[cur_level].return_player().move('down')
            elif event.key == pygame.K_LEFT:
                LEVELS[cur_level].return_player().change_sprites(images.upload_images_mirrored())
                LEVELS[cur_level].return_player().move('left')
                LEVELS[cur_level].return_player().to_left()
            elif event.key == pygame.K_RIGHT:
                LEVELS[cur_level].return_player().change_sprites(images.upload_images_player())
                LEVELS[cur_level].return_player().move('right')
                LEVELS[cur_level].return_player().to_right()

    LEVELS[cur_level].return_player().update(0.5)
    # FIXME должно работать для всех уровней
    # water_block1.update(0.2)
    # water_block2.update(0.2)
    if LEVELS[cur_level].check_next_level():
        cur_level += 1
    return cur_level


while not finished[0]:
    cur_level = game_process(finished, cur_level)
