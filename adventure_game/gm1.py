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
    scene_image = pygame.transform.scale(scene_image,(550,310))
    screen.blit(scene_image,(15,15))
   
    #text box background
    pygame.draw.rect(screen, dark_grey, ((size[0]/2) + 75, 15, 550, 310))
    pygame.draw.rect(screen, black, ((size[0]/2) + 72, 9, 556, 319), 7, 11)