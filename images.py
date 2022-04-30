import pygame


def upload_images_player():
    """
    функция загружает изображения игрока, когда он не движется, и возвращает список изображений
    :return: - список изображений
    """
    sprites = list([])
    sprites.append(pygame.image.load('tile000.png'))
    sprites.append(pygame.image.load('tile001.png'))
    sprites.append(pygame.image.load('tile002.png'))
    sprites.append(pygame.image.load('tile003.png'))

    return sprites


def upload_images_right():
    sprites = list([])
    sprites.append(pygame.image.load('r0.png'))
    sprites.append(pygame.image.load('r1.png'))
    sprites.append(pygame.image.load('r2.png'))
    sprites.append(pygame.image.load('r3.png'))
    sprites.append(pygame.image.load('r4.png'))


    return sprites

def upload_kick():
    sprites = list([])
    sprites.append(pygame.image.load('k0.png'))
    sprites.append(pygame.image.load('k1.png'))
    sprites.append(pygame.image.load('k2.png'))
    sprites.append(pygame.image.load('k3.png'))
    sprites.append(pygame.image.load('k4.png'))
    sprites.append(pygame.image.load('k5.png'))

    return sprites

def box_images():
    images = list([])
    images.append(pygame.image.load('box.png'))
    images.append(pygame.image.load('bridge.png'))

    return images

