import pygame

# Assigning colors (RGB)
BLACK = pygame.Color(  0,   0,   0)
WHITE = pygame.Color(150, 150, 150)
GREY  = pygame.Color(128, 128, 128)
BLUE  = pygame.Color(  0,   0, 128)
GREEN = pygame.Color(  0, 128,   0)
RED   = pygame.Color(128,   0,   0)

# Set frames per second
framerate = 60
FPS = pygame.time.Clock() # instantiates an object called FPS with the class pygame.time.Clock()

# Create display
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
DISPLAY_SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # width, height in px
pygame.display.set_caption("The world's greatest game!") # game window caption

# Sprites
player_img = 'assets/images/gothic-hero-idle.gif'
enemy_img = 'assets/images/demon-idle.gif'