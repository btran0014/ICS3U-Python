#Controls Menu
def controls():
    #Importing the necessary libraries and varibales from the main
    import main
    from main import pygame, window, big_font, title_font, back_ground, BLACK, RED, DARK_GR, LIGHT_GR, WHITE, screen, size, menu_select_sound
    pygame.init()
    
    #Allows for a quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #Handles mouse interaction
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #Importing all the files and creating a new font
    space_bar = pygame.image.load("gamefiles/images/space.jpg")
    mouse_img = pygame.image.load("gamefiles/images/mouse.png")
    e_img = pygame.image.load("gamefiles/images/e_key.png")
    keys_img = pygame.image.load("gamefiles/images/move_keys.png")
    small_font = pygame.font.SysFont("Cambria", 20)

    #Setpup the screen
    screen.blit(back_ground, (0, 0))

    #Declaring all text that will be used in the menu
    text1 = big_font.render("MAIN MENU", True, BLACK)
    text2 = big_font.render("MAIN MENU", True, RED)
    text3 = title_font.render("Controls", True, BLACK)
    text4 = small_font.render("To interact with clickable objects use", True, WHITE)
    text5 = small_font.render("the mouse and the left click button.", True, WHITE)
    text6 = small_font.render("Movement and direction will be made using", True, WHITE)
    text7 = small_font.render("the WASD and arrow keys. Player 1 will use", True, WHITE)
    text8 = small_font.render("the arrow keys. Player 2 will use WASD", True, WHITE)
    text9 = small_font.render("during multiplayer mode.", True, WHITE)
    text10 = small_font.render("Player 1 will use the space bar key as their action", True, WHITE)
    text11 = small_font.render("button, this will cause their character to attack.", True, WHITE)
    text12 = small_font.render("Player 2 will use the 'e' key as their action", True, WHITE)
    text13 = small_font.render("button, and will cause their attack with this.", True, WHITE)

    #Adding the text to the menu in specific locations
    screen.blit(text3, (445, 25))
    screen.blit(text4, (25, 125))
    screen.blit(text5, (25, 150))
    screen.blit(mouse_img, (75, 200))
    screen.blit(text6, (385, 125))
    screen.blit(text7, (385, 150))
    screen.blit(text8, (385, 175))
    screen.blit(text9, (385, 200))
    screen.blit(keys_img, (424, 275))
    screen.blit(text10, (835, 125))
    screen.blit(text11, (835, 150))
    screen.blit(text12, (835, 175))
    screen.blit(text13, (835, 200))
    screen.blit(e_img, (970, 250))
    screen.blit(space_bar, (875, 450))

    #Creates the main menu button and handles animations
    if 431 <= mouse[0] <= 820 and 561 <= mouse[1] <= 675 and pressed[0] == True:
        menu_select_sound.play()
        main.window = 0
        pygame.time.delay(200)
    elif 431 <= mouse[0] <= 820 and 561 <= mouse[1] <= 675:
        pygame.draw.rect(screen, DARK_GR, ((size[0]/2) - 209, 561, 389, 114))
        screen.blit(text2, (478, 585))
    else:
        pygame.draw.rect(screen, LIGHT_GR, ((size[0]/2) - 209, 561, 389, 114))
        screen.blit(text1, (478, 585))
    pygame.draw.rect(screen, BLACK, ((size[0]/2) - 215, 555, 400, 125), 7, 10)