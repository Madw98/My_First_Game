# test

import pygame
pygame.init()

WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test Platform")

FONT = pygame.font.SysFont("Arial", 50)

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)

PLAYER_SIZE = 7
STARTING_HEALTH = 3


class Player:
    COLOR = BLACK
    VEL = 4

    def __init__(self, x, y, radius, health):
        self.x = x
        self.y = y
        self.radius = radius
        self.health = health

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self, up=False, left=False, down=False, right=False):
        if up:
            self.y -= self.VEL
        if left:
            self.x -= self.VEL
        if down:
            self.y += self.VEL
        if right:
            self.x += self.VEL


def draw(win, player, lives):
    win.fill(CYAN)

    lives_text = FONT.render("Lives: " + f"{lives}", 1, BLACK)
    win.blit(lives_text, (20, 20))

    player.draw(win)

    pygame.display.update()


def handle_player_movement(keys, player):
    if keys[pygame.K_w]:
        player.move(up=True)
    if keys[pygame.K_a]:
        player.move(left=True)
    if keys[pygame.K_s]:
        player.move(down=True)
    if keys[pygame.K_d]:
        player.move(right=True)


def main():
    run = True
    clock = pygame.time.Clock()

    player = Player(WIDTH//2, HEIGHT//2, PLAYER_SIZE, STARTING_HEALTH)
    lives = player.health

    while run:
        clock.tick(FPS)
        draw(WIN, player, lives)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_player_movement(keys, player)

    pygame.quit()


if __name__ == '__main__':
    main()
