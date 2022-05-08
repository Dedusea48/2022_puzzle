import main
import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Tuple, Any

surface = create_example_window('puzzle', (600, 400))


def start_the_game() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    surface = create_example_window('puzzle', (600, 600))
    while not main.finished[0]:
        main.cur_level = main.game_process(main.finished, main.cur_level)
    main.finished[0] = False
    surface = create_example_window('puzzle', (600, 400))


def contininue_the_game() -> None:
    surface = create_example_window('puzzle', (600, 600))
    while not main.finished[0]:
        main.cur_level = main.game_process(main.finished, main.cur_level)
    main.finished[0] = False
    surface = create_example_window('puzzle', (600, 400))


mytheme = pygame_menu.Theme(widget_font=pygame_menu.font.FONT_8BIT,
                            title_font=pygame_menu.font.FONT_8BIT,
                            background_color=(249, 199, 61),  # transparent background
                            title_background_color=(182, 146, 48))

menu = pygame_menu.Menu(
    height=300,
    width=400,
    theme=mytheme,
    title=''
)

menu.add.button('Play', start_the_game)
menu.add.button('Continue', contininue_the_game)
menu.add.button('Quit', quit)

if __name__ == '__main__':
    menu.mainloop(surface)
