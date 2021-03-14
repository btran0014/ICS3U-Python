def introduction_menu():
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
    itext1 = "On the plane to your annual trip to the Himalayas "
    itext2 =  'you hear a loud "BANG" from the outside of '
    itext3 = "the plane. Oxygen masks fall from the ceiling as the"
    itext4 = "pilot tells everyone to buckle up. You're going down fast! "
    itext5 = "Your last memory is the plane crash. You're all alone out here. "
    
    introduction_text1 = smallestfont.render(itext1, True, white)
    introduction_text2 = smallestfont.render(itext2, True, white)
    introduction_text3 = smallestfont.render(itext3, True, white)
    introduction_text4 = smallestfont.render(itext4, True, white)
    introduction_text5 = smallestfont.render(itext5, True, white)
    text1 = smallfont.render("CONTINUE", True, black)
    text2 = smallfont.render("CONTINUE", True, white)

    #background
    menu_bg = pygame.image.load("personal/projects/adventure_game/images/purple_wallpaper.jpg")
    screen.blit(menu_bg, (0,0))
    menu_bg_scale = pygame.transform.scale(menu_bg,(1280,720))
    screen.blit(menu_bg_scale,(0,0))
    
    #prints the introduction
    screen.blit(introduction_text1, (size[0]/2-345, size[1]/2 - 60))
    screen.blit(introduction_text2, (size[0]/2-330, size[1]/2 - 20))
    screen.blit(introduction_text3, (size[0]/2-365, size[1]/2 + 20))
    screen.blit(introduction_text4, (size[0]/2-430, size[1]/2 + 60))
    screen.blit(introduction_text5, (size[0]/2-430, size[1]/2 + 100))

    # Continue Button
    if 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675 and pressed[0] == True:
        main.clicksound.play()
        pygame.time.delay(100)
        main.window = 3
    elif 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text2, (525, 585))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(text1, (525, 585))
    pygame.draw.rect(screen, black, ((size[0]/2) - 197, 555, 395, 123), 7, 11)

    #scene image on screen
    scene_image = pygame.image.load("personal/projects/adventure_game/images/plane_crashing.png")
    scene_image = pygame.transform.scale(scene_image,(480,240))
    screen.blit(scene_image,(400,45))
    pygame.draw.rect(screen, black, (( 397), 39, 490, 250), 7, 11)