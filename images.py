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

def upload_images_mirrored():
    """
    функция загружает изображения игрока, когда он не движется, и возвращает список изображений
    :return: - список изображений
    """
    sprites = list([])
    sprites.append(pygame.image.load('m0.png'))
    sprites.append(pygame.image.load('m1.png'))
    sprites.append(pygame.image.load('m2.png'))
    sprites.append(pygame.image.load('m3.png'))

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

def upload_kick_left():
    sprites = list([])
    sprites.append(pygame.image.load('kl0.png'))
    sprites.append(pygame.image.load('kl1.png'))
    sprites.append(pygame.image.load('kl2.png'))
    sprites.append(pygame.image.load('kl3.png'))
    sprites.append(pygame.image.load('kl4.png'))
    sprites.append(pygame.image.load('kl5.png'))

    return sprites

def box_images():
    images = list([])
    images.append(pygame.image.load('box.png'))
    images.append(pygame.image.load('bridge.png'))

    return images



def water_images():
    images = list([])
    images.append(pygame.image.load('w0.png'))
    images.append(pygame.image.load('w1.png'))
    images.append(pygame.image.load('w2.png'))

    return images

def grass():

    return pygame.image.load('Grass.jpg')

def ladder():

    return  pygame.image.load('ladder.png')

def wall():
    wall_image = list([])
    wall_image.append(pygame.image.load('wall.png'))
    return wall_image
