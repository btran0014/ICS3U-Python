def scene1():
    import main
    from main import screen, pygame, light_grey, size, largefont, black, smallfont, cool_green, dark_grey, white, smallestfont
    
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

    #text variables
    box1text = "*"
    box2text = "l"
    box3text = "l"
    box4text = "l"
    #text
    text1 = smallestfont.render(box1text,True, black)
    text2 = smallestfont.render(box1text,True, white)
    text3 = smallestfont.render(box2text,True, black)
    text4 = smallestfont.render(box2text,True, white)
    text5 = smallestfont.render(box3text,True, black)
    text6 = smallestfont.render(box3text,True, white)
    text7 = smallestfont.render(box4text,True, black)
    text8 = smallestfont.render(box4text,True, white)


    #scene image on screen
    scene_image = pygame.image.load("adventure_game/images/plane_wreck.png")
    scene_image = pygame.transform.scale(scene_image,(550,310))
    screen.blit(scene_image,(15,15))
   
    #text box background
    pygame.draw.rect(screen, dark_grey, ((size[0]/2) + 75, 15, 550, 310))
    pygame.draw.rect(screen, black, ((size[0]/2) + 72, 9, 556, 319), 7, 11)

    pygame.draw.rect(screen, dark_grey, ((size[0]/2 - 625, 380, 610, 140 )))
    pygame.draw.rect(screen, light_grey, ((size[0]/2 + 15, 380, 610, 140 )))
    pygame.draw.rect(screen, light_grey, ((size[0]/2 - 625, 535, 610, 140 )))
    pygame.draw.rect(screen, dark_grey, ((size[0]/2 + 15, 535, 610, 140 )))

"""
    #button 1
    if 446 <= mouse[0] <= 835 and 180 <= mouse[1] <= 294 and pressed[0] == True:
        main.clicksound.play()
        #main.window = 
    elif 446 <=mouse[0] <= 835 and 170 <= mouse[1] <=294:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 - 194, 180, 389, 114 )))
        screen.blit(text2, (575, 204))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 - 194, 180, 389, 114)))
        screen.blit(text1, (575, 204))
    pygame.draw.rect(screen, black, ((size[0]/2) - 197, 174, 395, 123), 7, 11)
"""