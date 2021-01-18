import pygame
import startingmenu
from startingmenu import main_menu
import gm1 
from gm1 import scene1

pygame.init()
#setup the window and the name
pygame.display.set_caption("Solitude")
clock = pygame.time.Clock()
size = (1280,720)
screen = pygame.display.set_mode(size)

#set colours as variables
light_grey = (120, 122, 118)
black = (0, 0, 0)
dark_grey = (48, 50, 54)
cool_green = (19, 173, 130)
white = (255, 255, 255)

#font sizes
largefont = pygame.font.SysFont("Corbel", 75) 
smallfont = pygame.font.SysFont("Corbel", 50)

#defining a click sound
clicksound = pygame.mixer.Sound("adventure_game/audio/click_sound.wav")
forestsound = pygame.mixer.Sound("adventure_game/audio/forest_sounds.wav")

#main loop for the game
rungame = True
while rungame: 
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False
    main_menu()

    pygame.display.update()