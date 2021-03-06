def main_menu():
    #import all of the necessary things to run the code
    import main
    from main import screen, pygame, light_grey, size, largefont, black, smallfont, cool_green, dark_grey, white
    pygame.init()
    #quits when prompted to
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #ALL OF THE TEXT FOR THE MENU
    #play button text
    text1 = smallfont.render("PLAY", True, black)
    text2 = smallfont.render("PLAY", True, white )
    #title text
    title_text = largefont.render("SOLITUDE", True, black)
    #quit button text
    text3 = smallfont.render("QUIT", True, black)
    text4 = smallfont.render("QUIT", True, white)
    #instructions text
    text5 = smallfont.render("INSTRUCTIONS", True, black)
    text6 = smallfont.render("INSTRUCTIONS", True, white)


    #hover and press with mouse
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #background image
    menu_bg = pygame.image.load("personal/projects/adventure_game/images/purple_wallpaper.jpg")
    screen.blit(menu_bg, (0,0))
    menu_bg_scale = pygame.transform.scale(menu_bg,(1280,720))
    screen.blit(menu_bg_scale,(0,0))

    #print title to screen
    screen.blit(title_text, (size[0]/2 - 165, size[1]/2 - 280))

    #play Button
    if 446 <= mouse[0] <= 835 and 180 <= mouse[1] <= 294 and pressed[0] == True:
        main.clicksound.play()
        pygame.time.delay(100)
        main.window = 2
    elif 446 <=mouse[0] <= 835 and 170 <= mouse[1] <=294:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 - 194, 180, 389, 114 )))
        screen.blit(text2, (575, 204))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 - 194, 180, 389, 114)))
        screen.blit(text1, (575, 204))
    pygame.draw.rect(screen, black, ((size[0]/2) - 197, 174, 395, 123), 7, 11)

    #instructions button
    if 446 <= mouse[0] <= 835 and 375 <= mouse[1] <= 489 and pressed[0] == True:
        main.clicksound.play()
        pygame.time.delay(100)
        main.window = 1
    elif 446 <=mouse[0] <= 835 and 375 <= mouse[1] <=489:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 - 194, 375, 389, 114 )))
        screen.blit(text6, (485, 400))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 - 194, 375, 389, 114 )))
        screen.blit(text5, (485, 400))
    pygame.draw.rect(screen, black, ((size[0]/2) - 197, 369, 395, 123), 7, 11)

    # Quit Button
    if 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675 and pressed[0] == True:
        main.clicksound.play()
        pygame.time.delay(100)
        pygame.quit()
    elif 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text4, (575, 585))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text3, (575, 585))
    pygame.draw.rect(screen, black, ((size[0]/2) - 197, 555, 395, 123), 7, 11)