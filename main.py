import pygame
import levels
import images

WIDTH = 600
HEIGHT = 600
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
finished = [False]

pygame.mixer.music.load("Sound/Backround.mp3")
pygame.mixer.music.play(-1)
LEVELS = (levels.level1(screen), levels.level2(screen), levels.level3(screen))
cur_level = 2


def game_process(is_finished, _cur_level):
    """"""
    LEVELS[_cur_level].draw()
    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and LEVELS[_cur_level].player.dx == LEVELS[_cur_level].player.dy:
            if event.key == pygame.K_UP:
                LEVELS[_cur_level].player_move('up')
            elif event.key == pygame.K_DOWN:
                LEVELS[_cur_level].player_move('down')

            elif event.key == pygame.K_LEFT:
                LEVELS[_cur_level].player.change_sprites(images.load_images_mirrored())
                LEVELS[_cur_level].player_move('left')
                LEVELS[_cur_level].player.to_left()
            elif event.key == pygame.K_RIGHT:
                LEVELS[_cur_level].player.change_sprites(images.load_images_player())
                LEVELS[_cur_level].player_move('right')
                LEVELS[_cur_level].player.to_right()
            elif event.key == pygame.K_ESCAPE:
                finished[0] = True

    LEVELS[_cur_level].player.update(0.4)
    LEVELS[_cur_level].check_interaction()
    if LEVELS[_cur_level].completed:
        _cur_level += 1
    return _cur_level
