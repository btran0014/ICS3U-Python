import pygame
pygame.init()
from startingmenu import main_menu


pygame.display.set_caption("Solitude")
clock = pygame.time.Clock()

size = (1280,720)
screen = pygame.display.set_mode(size)

#set colours as variables
light_grey = (120, 122, 118)
black = (0, 0, 0)
dark_grey = (48, 50, 54)
cool_green = (19, 173, 130)

largefont = pygame.font.SysFont("Corbel", 75) 
subtitlefont = pygame.font.SysFont("Corbel", 50)

rungame = True
while rungame: 
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False
    main_menu()
    pygame.display.update()