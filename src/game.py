
import pygame
from src.Sprite import Sprite


def main():
    pygame.init()

    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 400
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    my_sprite = Sprite(
        color=(0, 255, 255),
        width=25,
        height=50
    )
    all_sprites = pygame.sprite.Group()
    all_sprites.add(my_sprite)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((200, 200, 255))
        all_sprites.draw(screen)
        pygame.display.flip()




if __name__ ==  '__main__':
    main()