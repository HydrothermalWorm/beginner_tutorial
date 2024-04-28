# Import dependencies
from assets import *
import os
import time

# Center game window
os.environ['SDL_VIDEO_WINDOW_CENTERED'] = '1'

# Initialize pygame engine
pygame.init()

# Sprites
player_img = 'assets/images/gothic-hero-idle.gif'
player = Player(DISPLAY_SURF, player_img, 5)

enemy_img = 'assets/images/demon-idle.gif'
enemy = Enemy(DISPLAY_SURF, enemy_img, 5)
number_of_enemies: int = 1
enemy_group = pygame.sprite.Group()
for i in range(number_of_enemies):
    enemy_group = pygame.sprite.Group(enemy)

# Game Loop
while True:

    # quitting the game loop by closing the window
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # game over if enemy collides with player
    if pygame.sprite.collide_rect(player, enemy):
            DISPLAY_SURF.fill(RED)
            pygame.display.update()
            player.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()

    player.move()
    enemy.move()

    DISPLAY_SURF.fill('BLACK')
    player.draw()
    enemy.draw()

    # update the display
    pygame.display.update()
    FPS.tick(framerate)
