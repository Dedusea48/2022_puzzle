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
level1 = classes.Level(5, 5, screen, 100, 100)
front.Player(level1.tiles[0][0], level1, images.upload_images_player())
back.next_level_tile(level1.tiles[4][0], images.ladder())

front.Box(level1.tiles[2][1], images.box_images())
front.Box(level1.tiles[1][2], images.box_images())

front.Wall(level1.tiles[0][1], images.wall())
front.Wall(level1.tiles[1][1], images.wall())
front.Wall(level1.tiles[3][0], images.wall())
front.Wall(level1.tiles[3][1], images.wall())
front.Wall(level1.tiles[1][3], images.wall())

back.Water(level1.tiles[4][1], images.water_images())
back.Water(level1.tiles[4][2], images.water_images())

# LEVEL 2
level2 = classes.Level(6, 8, screen, 100, 100)
front.Player(level2.tiles[0][7], level2, images.upload_images_player())
back.next_level_tile(level2.tiles[5][7], images.ladder())

front.Wall(level2.tiles[4][2], images.wall())
front.Wall(level2.tiles[5][2], images.wall())
front.Wall(level2.tiles[3][5], images.wall())
front.Wall(level2.tiles[3][6], images.wall())
front.Wall(level2.tiles[3][7], images.wall())

back.Water(level2.tiles[0][3], images.water_images())
back.Water(level2.tiles[1][3], images.water_images())
back.Water(level2.tiles[2][3], images.water_images())
back.Water(level2.tiles[3][3], images.water_images())
back.Water(level2.tiles[4][3], images.water_images())
back.Water(level2.tiles[5][3], images.water_images())
back.Water(level2.tiles[0][4], images.water_images())
back.Water(level2.tiles[1][4], images.water_images())
back.Water(level2.tiles[2][4], images.water_images())
back.Water(level2.tiles[3][4], images.water_images())
back.Water(level2.tiles[4][4], images.water_images())
back.Water(level2.tiles[5][4], images.water_images())

front.Box(level2.tiles[1][2], images.box_images())
front.Box(level2.tiles[4][1], images.box_images())
front.Box(level2.tiles[1][5], images.box_images())
front.Box(level2.tiles[1][6], images.box_images())
front.Box(level2.tiles[2][5], images.box_images())

LEVELS = (level1, level2)
cur_level = 0


def game_process(is_finished, cur_level):
    LEVELS[cur_level].draw()
    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
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
            elif event.key == pygame.K_ESCAPE:
                finished[0] = True

    LEVELS[cur_level].return_player().update(0.5)
    # FIXME должно работать для всех уровней
    # water_block1.update(0.2)
    # water_block2.update(0.2)
    if LEVELS[cur_level].check_next_level():
        cur_level += 1
    return cur_level
