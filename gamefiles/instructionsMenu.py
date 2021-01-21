#Instructions Menu
def instructions():
    #Importing the necessary libraries and varibales from the main
    import main
    from main import pygame, window, big_font, med_font, title_font, back_ground, BLACK, RED, DARK_GR, LIGHT_GR, WHITE, screen, size, menu_select_sound, enemy_img, ball_img
    pygame.init()

    #Handles a quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #Handles mouse interactions
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #Adds the backgroun to the menu
    screen.blit(back_ground, (0, 0))

    #Declaring all the texts that will be used
    text1 = title_font.render("Instructions", True, BLACK)
    text2 = med_font.render("Defend youselves from incoming enemies!", True, WHITE)
    text3 = med_font.render("Use your chracter's unique abilities to kill your foes!", True, WHITE)
    text4 = med_font.render("If you get attacked too many times, you may lose your life!", True, WHITE)
    text5 = med_font.render("Earn points for each enemy you defeat!", True, WHITE)
    text6 = med_font.render("The game ends when you and your ally both fall!", True, WHITE)
    text7 = med_font.render("Some enemies may have special abilities that allow them to fire projectiles!", True, WHITE)
    text8 = med_font.render("Others may have abilities that allow them to take multiple hits!", True, WHITE)
    text9 = big_font.render("MAIN MENU", True, BLACK)
    text10 = big_font.render("MAIN MENU", True, RED)

    #Outputting all texts to the screen at proper locations
    screen.blit(text1, (455, 25))
    screen.blit(text2, (290, 120))
    screen.blit(text3, (200, 180))
    screen.blit(text4, (165, 240))
    screen.blit(text5, (320, 300))
    screen.blit(text6, (250, 360))
    screen.blit(text7, (25, 420))
    screen.blit(text8, (115, 480))
    screen.blit(enemy_img[4], (150, 580))
    screen.blit(ball_img, (300, 580))
    pygame.draw.rect(screen, RED, (975, 563, 146, 12))
    screen.blit(enemy_img[-5], (1000, 580))

    #Creates the main menu button and handles animations
    if 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675 and pressed[0] == True:
        menu_select_sound.play()
        main.window = 0
        pygame.time.delay(200)
    elif 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675:
        pygame.draw.rect(screen, DARK_GR, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text10, (493, 585))
    else:
        pygame.draw.rect(screen, LIGHT_GR, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text9, (493, 585))
    pygame.draw.rect(screen, BLACK, ((size[0]/2) - 200, 555, 400, 125), 7, 10)