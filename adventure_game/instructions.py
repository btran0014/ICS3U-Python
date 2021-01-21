def instructions_menu():
    import main 
    from main import screen, pygame, light_grey, size, largefont, black, smallfont, dark_grey, white, smallestfont
    import startingmenu
    from startingmenu import main_menu

    pygame.init()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #hover and press with mouse
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #text
     
    itext1 = "Welcome to Solitude, a solo survival adventure. From the moment "
    itext2 =  "you enter the game, all of your decisions will matter so make sure you "
    itext3 = "think about all of your choices. There are multiple endings to this game. "
    itext4 = "Follow the path that you would, in real life! "
    itext5 = "Remember to have fun! "
    
    instructions_text1 = smallestfont.render(itext1, True, black)
    instructions_text2 = smallestfont.render(itext2, True, black)
    instructions_text3 = smallestfont.render(itext3, True, black)
    instructions_text4 = smallestfont.render(itext4, True, black)
    instructions_text5 = smallestfont.render(itext5, True, black)
    text1 = smallfont.render("BACK", True, black)
    text2 = smallfont.render("BACK", True, white)

    #background
    menu_bg = pygame.image.load("adventure_game/images/purple_wallpaper.jpg")
    screen.blit(menu_bg, (0,0))
    menu_bg_scale = pygame.transform.scale(menu_bg,(1280,720))
    screen.blit(menu_bg_scale,(0,0))
    
    #prints the instructions
    screen.blit(instructions_text1, (size[0]/2-520, size[1]/2 - 260))
    screen.blit(instructions_text2, (size[0]/2-550, size[1]/2 - 220))
    screen.blit(instructions_text3, (size[0]/2-560, size[1]/2 - 180))
    screen.blit(instructions_text4, (size[0]/2-330, size[1]/2 - 140))
    screen.blit(instructions_text5, (size[0]/2-200, size[1]/2 - 100))

    # Exit Button
    if 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675 and pressed[0] == True:
        main.clicksound.play()
        main.window = 0
    elif 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text2, (575, 585))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text1, (575, 585))