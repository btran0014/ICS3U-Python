def death_menu():
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
     
    dtext = "You've reached the end of the line. Will you play again? "
    
    death_text = smallestfont.render(dtext, True, white)
    text1 = smallfont.render("RESTART", True, black)
    text2 = smallfont.render("RESTART", True, white)

    #background
    menu_bg = pygame.image.load("personal/projects/adventure_game/images/purple_wallpaper.jpg")
    screen.blit(menu_bg, (0,0))
    menu_bg_scale = pygame.transform.scale(menu_bg,(1280,720))
    screen.blit(menu_bg_scale,(0,0))
    
    #prints the death text
    screen.blit(death_text, (size[0]/2-450, size[1]/2 + 100))
   
    # Exit Button
    if 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675 and pressed[0] == True:
        main.clicksound.play()
        pygame.time.delay(100)
        main.window = 0
    elif 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text2, (550, 585))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text1, (550, 585))
    pygame.draw.rect(screen, black, ((size[0]/2) - 197, 555, 395, 123), 7, 11)

    #scene image on screen
    scene_image = pygame.image.load("personal/projects/adventure_game/images/death.png")
    scene_image = pygame.transform.scale(scene_image,(360,280))
    screen.blit(scene_image,(460, 100))