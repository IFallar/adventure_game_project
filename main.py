import pygame
import os

# DEFINED VALUES

WIDTH, HEIGHT = 1100, 706

FPS = 60

MAP = pygame.image.load(os.path.join(
    'Resources', 'Maps', 'Map - Baleares Large - Schema.png'))
MAP = pygame.transform.scale(MAP, (706, 706))


# PLAY ELEMENTS

PLAYER = pygame.image.load(os.path.join(
    'Resources', 'Icons', 'coolmandude.png'))
PLAYER = pygame.transform.scale(PLAYER, (50, 50))

PLAYER_SIZE = PLAYER.get_size()

PLAYER_X, PLAYER_Y = 564, 542

PLAYER_TX, PLAYER_TY = (PLAYER_X/1.45) - PLAYER_SIZE[0]/2, (
    PLAYER_Y/1.45) - PLAYER_SIZE[1]/2

# WINDOW DETAILS

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Baleares")


# FUNCTIONS

def bg_draw(player_ch):
    WIN.blit(MAP, (0, 0))
    WIN.blit(PLAYER, (player_ch.x, player_ch.y))
    pygame.display.update()


def main():

    player_ch = pygame.Rect(
        PLAYER_TX, PLAYER_TY, PLAYER_SIZE[0], PLAYER_SIZE[1])

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if player_ch.y > 450/1.45 - 25:
            player_ch.x += -1
            player_ch.y += -.4
            
        bg_draw(player_ch)

    pygame.QUIT


if __name__ == "__main__":
    main()
