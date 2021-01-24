import pygame
from startingmenu import main_menu 
from gm1 import scene1
from instructions import instructions_menu
from introduction import introduction_menu

pygame.init()
#setup the window and the name
pygame.display.set_caption("Solitude")
clock = pygame.time.Clock()
size = (1280,720)
screen = pygame.display.set_mode(size)

#hover and press with mouse
mouse = pygame.mouse.get_pos()
pressed = pygame.mouse.get_pressed()


#set colours as variables
light_grey = (120, 122, 118)
black = (0, 0, 0)
dark_grey = (48, 50, 54)
cool_green = (19, 173, 130)
white = (255, 255, 255)

#font sizes
largefont = pygame.font.SysFont("Corbel", 75) 
smallfont = pygame.font.SysFont("Corbel", 50)
smallestfont = pygame.font.SysFont("Corbel", 40)

#defining a click sound
clicksound = pygame.mixer.Sound("adventure_game/audio/click_sound.wav")
forestsound = pygame.mixer.Sound("adventure_game/audio/forest_sounds.wav")

window = 0

#main loop for the game
rungame = True
while rungame: 
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False
    #main menu
    if window == 0:
        main_menu()
    
    #instructions menu
    elif window == 1:
        instructions_menu()
    
    # introduction
    elif window == 2:
        introduction_menu()
    
    # scene 1
    elif window == 3:
        scene1()


    pygame.display.update()