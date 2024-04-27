from assets import *

pygame.init() # initalize pygame engine

# instantiate sprite classes
player = Player(DISPLAY_SURF, player_img, 5)
enemy = Enemy(DISPLAY_SURF, enemy_img, 5)

# group sprites
enemies = pygame.sprite.Group()
enemies.add(enemy)
all_sprites = pygame.sprite.Group()
all_sprites.add([player, enemy])


while True:
    # quitting the game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    move_sprites(all_sprites)
    DISPLAY_SURF.fill('BLACK')
    draw_sprites(all_sprites)

    # update the display
    pygame.display.update()
    FPS.tick(framerate)