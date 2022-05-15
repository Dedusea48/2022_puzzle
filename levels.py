"""
Данный файл хранит в себе функции, который могут построить уровень, если им передать
скрин, на котором уровень будет рисоваться.
"""
import classes
import classes_top_obj as front
import classes_bottom_obj as back
import images


def level1(screen):
    level1 = classes.Level(screen, 100, 100, 5, 5)
    level1.add_player(front.Player(images.load_images_player()), 0, 0)
    level1.add_finish(back.NextLevelTile(images.ladder()), 4, 0)
    level1.tiles[2][1].top_obj = front.Box(images.box_images())
    level1.tiles[1][2].top_obj = front.Box(images.box_images())

    level1.tiles[0][1].top_obj = front.Wall(images.wall())
    level1.tiles[1][1].top_obj = front.Wall(images.wall())
    level1.tiles[3][0].top_obj = front.Wall(images.wall())
    level1.tiles[3][1].top_obj = front.Wall(images.wall())
    level1.tiles[1][3].top_obj = front.Wall(images.wall())

    level1.tiles[4][1].bottom_obj = back.Water(images.water_images())
    level1.tiles[4][2].bottom_obj = back.Water(images.water_images())
    return level1


def level2(screen):
    level2 = classes.Level(screen, 100, 100, 6, 8)
    level2.add_player(front.Player(images.load_images_player()), 0, 7)
    level2.add_finish(back.NextLevelTile(images.ladder()), 5, 7)

    level2.tiles[4][2].top_obj = front.Wall(images.wall())
    level2.tiles[5][2].top_obj = front.Wall(images.wall())
    level2.tiles[3][5].top_obj = front.Wall(images.wall())
    level2.tiles[3][6].top_obj = front.Wall(images.wall())
    level2.tiles[3][7].top_obj = front.Wall(images.wall())

    level2.tiles[0][3].bottom_obj = back.Water(images.water_images())
    level2.tiles[1][3].bottom_obj = back.Water(images.water_images())
    level2.tiles[2][3].bottom_obj = back.Water(images.water_images())
    level2.tiles[3][3].bottom_obj = back.Water(images.water_images())
    level2.tiles[4][3].bottom_obj = back.Water(images.water_images())
    level2.tiles[5][3].bottom_obj = back.Water(images.water_images())
    level2.tiles[0][4].bottom_obj = back.Water(images.water_images())
    level2.tiles[1][4].bottom_obj = back.Water(images.water_images())
    level2.tiles[2][4].bottom_obj = back.Water(images.water_images())
    level2.tiles[3][4].bottom_obj = back.Water(images.water_images())
    level2.tiles[4][4].bottom_obj = back.Water(images.water_images())
    level2.tiles[5][4].bottom_obj = back.Water(images.water_images())

    level2.tiles[1][2].top_obj = front.Box(images.box_images())
    level2.tiles[4][1].top_obj = front.Box(images.box_images())
    level2.tiles[1][5].top_obj = front.Box(images.box_images())
    level2.tiles[1][6].top_obj = front.Box(images.box_images())
    level2.tiles[2][5].top_obj = front.Box(images.box_images())
    return level2


def level3(screen):
    level3 = classes.Level(screen, 100, 100, 6, 8)
    level3.add_player(front.Player(images.load_images_player()), 0, 7)
    level3.add_finish(back.NextLevelTile(images.ladder()), 5, 7)

    level3.tiles[1][2].top_obj = front.Box(images.box_images())
    level3.tiles[4][1].top_obj = front.Box(images.box_images())
    level3.tiles[1][5].top_obj = front.Box(images.box_images())
    level3.tiles[1][6].top_obj = front.Box(images.box_images())
    level3.tiles[2][5].top_obj = front.Box(images.box_images())

    level3.tiles[1][1].bottom_obj = back.Spring('down', 3, images.arrow())
    level3.tiles[1][4].bottom_obj = back.Water(images.water_images())

    return level3
