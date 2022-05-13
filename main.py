import pygame
import levels
import images
import classes_front_obj as front

WIDTH = 600
HEIGHT = 600
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
finished = [False]

LEVELS = (levels.level1(screen), levels.level2(screen))
cur_level = 0


def game_process(is_finished, cur_level):
    """"""
    LEVELS[cur_level].draw()
    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                front.move_up(LEVELS[cur_level].player, LEVELS[cur_level], LEVELS[cur_level].screen)
                LEVELS[cur_level].player_move('up')
            elif event.key == pygame.K_DOWN:
                front.move_down(LEVELS[cur_level].player, LEVELS[cur_level], LEVELS[cur_level].screen)
                LEVELS[cur_level].player_move('down')

            elif event.key == pygame.K_LEFT:
                LEVELS[cur_level].player.change_sprites(images.load_images_mirrored())
                front.move_left(LEVELS[cur_level].player, LEVELS[cur_level], LEVELS[cur_level].screen)
                LEVELS[cur_level].player_move('left')
                LEVELS[cur_level].player.to_left()
            elif event.key == pygame.K_RIGHT:
                LEVELS[cur_level].player.change_sprites(images.load_images_player())
                front.move_right(LEVELS[cur_level].player, LEVELS[cur_level], LEVELS[cur_level].screen)
                LEVELS[cur_level].player_move('right')
                LEVELS[cur_level].player.to_right()
            elif event.key == pygame.K_ESCAPE:
                finished[0] = True

    LEVELS[cur_level].player.update(0.5)
    LEVELS[cur_level].check_interaction()
    if LEVELS[cur_level].completed:
        cur_level += 1
    return cur_level
