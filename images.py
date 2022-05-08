import pygame


def upload_images_player():
    """
    функция загружает изображения игрока, когда он не движется, и возвращает список изображений
    :return: - список изображений
    """
    sprites = list([])
    sprites.append(pygame.image.load('image/tile000.png'))
    sprites.append(pygame.image.load('image/tile001.png'))
    sprites.append(pygame.image.load('image/tile002.png'))
    sprites.append(pygame.image.load('image/tile003.png'))

    return sprites


def upload_images_mirrored():
    """
    функция загружает изображения игрока, когда он не движется, и возвращает список изображений
    :return: - список изображений
    """
    sprites = list([])
    sprites.append(pygame.image.load('image/m0.png'))
    sprites.append(pygame.image.load('image/m1.png'))
    sprites.append(pygame.image.load('image/m2.png'))
    sprites.append(pygame.image.load('image/m3.png'))

    return sprites


def upload_images_right():
    sprites = list([])
    sprites.append(pygame.image.load('image/r0.png'))
    sprites.append(pygame.image.load('image/r1.png'))
    sprites.append(pygame.image.load('image/r2.png'))
    sprites.append(pygame.image.load('image/r3.png'))
    sprites.append(pygame.image.load('image/r4.png'))

    return sprites


def upload_kick():
    sprites = list([])
    sprites.append(pygame.image.load('image/k0.png'))
    sprites.append(pygame.image.load('image/k1.png'))
    sprites.append(pygame.image.load('image/k2.png'))
    sprites.append(pygame.image.load('image/k3.png'))
    sprites.append(pygame.image.load('image/k4.png'))
    sprites.append(pygame.image.load('image/k5.png'))

    return sprites


def upload_kick_left():
    sprites = list([])
    sprites.append(pygame.image.load('image/kl0.png'))
    sprites.append(pygame.image.load('image/kl1.png'))
    sprites.append(pygame.image.load('image/kl2.png'))
    sprites.append(pygame.image.load('image/kl3.png'))
    sprites.append(pygame.image.load('image/kl4.png'))
    sprites.append(pygame.image.load('image/kl5.png'))

    return sprites


def box_images():
    images = list([])
    images.append(pygame.image.load('image/box.png'))
    images.append(pygame.image.load('image/bridge.png'))

    return images


def water_images():
    images = list([])
    images.append(pygame.image.load('image/w0.png'))
    images.append(pygame.image.load('image/w1.png'))
    images.append(pygame.image.load('image/w2.png'))

    return images


def grass():
    return pygame.image.load('image/Grass.jpg')


def ladder():
    return pygame.image.load('image/ladder.png')


def wall():
    wall_image = list([])
    wall_image.append(pygame.image.load('image/wall.png'))
    return wall_image
