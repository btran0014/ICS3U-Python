def scene1():
    import main
    from main import screen, pygame, light_grey, size, largefont, black, smallfont, cool_green, dark_grey, white
    
    pygame.init()
    
    #quits when prompted to
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #background
    menu_bg = pygame.image.load("adventure_game/images/purple_wallpaper.jpg")
    screen.blit(menu_bg, (0,0))
    menu_bg_scale = pygame.transform.scale(menu_bg,(1280,720))
    screen.blit(menu_bg_scale,(0,0))

    #scene image on screen
    scene_image = pygame.image.load("adventure_game/images/plane_wreck.png")
    menu_bg_scale = pygame.transform.scale(scene_image,(240,240))
    screen.blit(scene_image,(0,0))