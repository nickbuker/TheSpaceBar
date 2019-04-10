import pygame


class Sprite(pygame.sprite.Sprite):

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    def __init__(self, color, width, height):
        """
        TODO

        :param color:   color of the sprite
        :param width:   width of the sprite
        :param height:  height of the sprite
        """
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)


