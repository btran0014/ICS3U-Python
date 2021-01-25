import pygame
from startingmenu import main_menu 
from game_menu import scene1, scene2, scene3, scene4, scene5, scene6, scene7, scene8, scene9, scene10, scene11, scene12, scene13, scene14, scene15, scene16
from instructions import instructions_menu
from introduction import introduction_menu
from deathmenu import death_menu

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
tinyfont = pygame.font.SysFont("Corbel", 30)
tinierfont = pygame.font.SysFont("Corbel", 20)

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

    #scene 2
    elif window == 4:
        scene2()
   
    elif window == 100:
        death_menu()
    
    
    elif window == 5:
        scene3()
    
    
    elif window == 6:
        scene4()

    elif window == 7:
        scene5()
    
    elif window == 8:
        scene6()

    elif window == 9:
        scene7()

    elif window == 10:
        scene8()

    elif window == 11:
        scene9()
    
    elif window == 12:
        scene10()
    
    elif window == 13:
        scene11()

    elif window == 14:
        scene12()
    
    elif window == 15:
        scene13()

    elif window == 16:
        scene14()#surviving
    
    elif window == 17:
        scene15()#see the light
    
    elif window == 18:
        scene16()#
    
    pygame.display.update()