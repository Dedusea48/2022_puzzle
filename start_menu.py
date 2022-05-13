#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame
import sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
import pygame.locals as pl
import main


pygame.init()
pygame.display.set_caption('puzzle')
screen = pygame.display.set_mode((500, 500), pl.RESIZABLE)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def button_1(pup):
    w, h = pygame.display.get_surface().get_size()
    font = pygame.font.Font('fonts/undertale battle font_0.ttf', min(int(h / 8), int(w / 8)))

    mx, my = pygame.mouse.get_pos()

    button1 = pygame.Rect(2 * w / 6, 3 * h / 8, w / 3, h / 8)

    if button1.collidepoint((mx, my)):
        pygame.draw.rect(screen, (255, 0, 0), button1)
        if pup:
            game()
    else:
        pygame.draw.rect(screen, (0, 0, 255), button1)
    draw_text('play', font, (255, 255, 255), screen, w / 2 - min(int(h / 8), int(w / 8)), 77 * h / 200)


def button_2(pup):
    w, h = pygame.display.get_surface().get_size()
    font = pygame.font.Font('fonts/undertale battle font_0.ttf', min(int(h / 8), int(w / 8)))
    draw_text('main menu', font, (255, 255, 255), screen, w / 200, h / 20)

    mx, my = pygame.mouse.get_pos()

    button2 = pygame.Rect(2 * w / 6, 5 * h / 8, w / 3, h / 8)
    if button2.collidepoint((mx, my)):
        pygame.draw.rect(screen, (255, 0, 0), button2)
        if pup:
            quit()
    else:
        pygame.draw.rect(screen, (0, 255, 255), button2)
    draw_text('quit', font, (255, 255, 255), screen, w / 2 - min(int(h / 8), int(w / 8)), 127 * h / 200)


def main_menu():
    click = False
    pic = pygame.image.load("image/fon.jpg")
    while True:
        button_1(click)
        button_2(click)
        if click:
            screen.blit(pygame.transform.scale(pic, screen.get_size()), (0, 0))
            click = False
        for event in pygame.event.get():
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pl.KEYDOWN:
                if event.key == pl.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pl.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    print("111")
            elif event.type == pl.VIDEORESIZE:
                screen.blit(pygame.transform.scale(pic, event.dict['size']), (0, 0))
            elif event.type == pl.VIDEOEXPOSE:  # handles window minimising/maximising
                screen.fill((0, 0, 0))
                screen.blit(pygame.transform.scale(pic, screen.get_size()), (0, 0))

        pygame.display.update()
        mainClock.tick(60)


def game():
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    screen.fill((0, 0, 0))
    while not main.finished[0]:
        main.cur_level = main.game_process(main.finished, main.cur_level)
    main.finished[0] = False


main_menu()
