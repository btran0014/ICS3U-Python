#Pause menu for mid game pauses
def pause():
    #Importing the necessary variables and functions
    import main
    from main import pygame, window, title_font, big_font, RED, BLACK, LIGHT_GR, DARK_GR, grayed_out, screen, size, reset_menu, bg, menu_select_sound
    pygame.init()

    #Generating any new vaiables
    gray_out_screen = pygame.transform.scale(grayed_out, (1280, 720))
    GRAY = (128, 128, 128)

    #Handles a quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #Allows for interaction with the mouse
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #Generating all needed text
    text1 = title_font.render("PAUSED", True, BLACK)
    text2 = big_font.render("Resume game", True, BLACK)
    text3 = big_font.render("Resume game", True, RED)
    text4 = big_font.render("Main menu", True, BLACK)
    text5 = big_font.render("Main menu", True, RED)

    #Graying out the play screen and generating the pause box
    screen.blit(bg, (0, 0))
    screen.blit(gray_out_screen, (0, 0))
    pygame.draw.rect(screen, GRAY, ((size[0]/2) - 240, (size[1]/2) - 270, 480, 520), 15, 30)
    pygame.draw.rect(screen, GRAY, ((size[0]/2) - 225, (size[1]/2) - 255, 450, 490))
    pygame.draw.rect(screen, BLACK, ((size[0]/2) - 243, (size[1]/2) - 273, 486, 526), 3, 35)
    screen.blit(text1, (525, 120))

    #Allows for interactions with the resume game button
    if 440 <= mouse[0] <= 840 and 240 <= mouse[1] <= 365 and pressed[0] == True:
        menu_select_sound.play()
        main.window = 4
        pygame.time.delay(200)
    elif 440 <= mouse[0] <= 840 and 240 <= mouse[1] <= 365:
        pygame.draw.rect(screen, DARK_GR, ((size[0]/2) - 200, (size[1]/2) - 120, 400, 125))
        pygame.draw.rect(screen, BLACK, ((size[0]/2) - 203, (size[1]/2) + - 123, 406, 131), 3, 7)
        screen.blit(text3, (470, 268))
    else:
        pygame.draw.rect(screen, LIGHT_GR, ((size[0]/2) - 200, (size[1]/2) - 120, 400, 125))
        pygame.draw.rect(screen, BLACK, ((size[0]/2) - 203, (size[1]/2) - 123, 406, 131), 3, 7)
        screen.blit(text2, (470, 268))

    #Allows for interactions with the main menu button
    if 440 <= mouse[0] <= 840 and 440 <= mouse[1] <= 565 and pressed[0] == True:
        menu_select_sound.play()
        main.window = 0
        reset_menu()
        pygame.time.delay(200)
    elif 440 <= mouse[0] <= 840 and 440 <= mouse[1] <= 565:
        pygame.draw.rect(screen, DARK_GR, ((size[0]/2) - 200, (size[1]/2) + 80, 400, 125))
        pygame.draw.rect(screen, BLACK, ((size[0]/2) - 203, (size[1]/2) + 77, 406, 131), 3, 7)
        screen.blit(text5, (495, 468))
    else:
        pygame.draw.rect(screen, LIGHT_GR, ((size[0]/2) - 200, (size[1]/2) + 80, 400, 125))
        pygame.draw.rect(screen, BLACK, ((size[0]/2) - 203, (size[1]/2) + 77, 406, 131), 3, 7)
        screen.blit(text4, (495, 468))