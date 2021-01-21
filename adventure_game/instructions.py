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
    instructions = """
    Welcome to Solitude, a solo survival adventure. From the moment you enter the game,
    From the moment you enter the game, all of your decisions will matter so make sure you
    think about all of your choices. There are endings to this game. 
    Follow the path that you would, in real life!
    """
    instructions_text = smallestfont.render(instructions, True, black)
    text1 = smallfont.render("BACK", True, black)

    #background
    menu_bg = pygame.image.load("adventure_game/images/purple_wallpaper.jpg")
    screen.blit(menu_bg, (0,0))
    menu_bg_scale = pygame.transform.scale(menu_bg,(1280,720))
    screen.blit(menu_bg_scale,(0,0))
    
    #prints the instructions
    screen.blit(instructions_text, (size[0]/8, size[1]/2 - 280))

    # Exit Button
    if 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675 and pressed[0] == True:
        main.clicksound.play()
        main.window = 0
    elif 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text1, (575, 585))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text1, (575, 585))