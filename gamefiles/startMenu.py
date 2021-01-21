#Start Menu
def menu():
    #Importing the necessary libraries and varibales from the main
    import main
    from main import pygame, window, big_font, med_font, back_ground, BLACK, RED, DARK_GR, LIGHT_GR, screen, size, menu_select_sound
    pygame.init()

    #Handles a quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #Allows for interaction with the mouse
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #Importing the logo file for the menu
    logo = pygame.image.load("gamefiles/images/leagueofinvaders.png")

    #Generation of the background and logo onto the screen
    screen.blit(back_ground, (0, 0))
    screen.blit(logo, ((size[0]/2) - 403, 0))

    #Creating all texts that will be used in the menu
    text1 = big_font.render("PLAY", True, BLACK)
    text2 = big_font.render("PLAY", True, RED)
    text3 = med_font.render("CONTROLS", True, BLACK)
    text4 = med_font.render("CONTROLS", True, RED)
    text5 = med_font.render("INSTRUCTIONS", True, BLACK)
    text6 = med_font.render("INSTRUCTIONS", True, RED)
    
    # Play Button
    if 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675 and pressed[0] == True:
        menu_select_sound.play()
        main.window = 3
        pygame.time.delay(200)
    elif 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675:
        pygame.draw.rect(screen, DARK_GR, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text2, (575, 585))
    else:
        pygame.draw.rect(screen, LIGHT_GR, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text1, (575, 585))
    pygame.draw.rect(screen, BLACK, ((size[0]/2) - 200, 555, 400, 125), 7, 10)

    #Controls Button
    if 78 <= mouse[0] <= 372 and 578 <= mouse[1] <= 657 and pressed[0] == True:
        menu_select_sound.play()
        main.window = 1
        pygame.time.delay(200)
    elif 78 <= mouse[0] <= 372 and 578 <= mouse[1] <= 657:
        pygame.draw.rect(screen, DARK_GR, (78, 578, 294, 79))
        screen.blit(text4, (133, 595))
    else:
        pygame.draw.rect(screen, LIGHT_GR, (78, 578, 294, 79))
        screen.blit(text3, (133, 595))
    pygame.draw.rect(screen, BLACK, (75, 575, 300, 85), 5, 8)

    #Instructions Button
    if 908 <= mouse[0] <= 1202 and 578 <= mouse[1] <= 657 and pressed[0] == True:
        menu_select_sound.play()
        main.window = 2
        pygame.time.delay(200)
    elif 908 <= mouse[0] <= 1202 and 578 <= mouse[1] <= 657:
        pygame.draw.rect(screen, DARK_GR, (908, 578, 294, 79))
        screen.blit(text6, (930, 595))
    else:
        pygame.draw.rect(screen, LIGHT_GR, (908, 578, 294, 79))
        screen.blit(text5, (930, 595))
    pygame.draw.rect(screen, BLACK, (905, 575, 300, 85), 5, 8)