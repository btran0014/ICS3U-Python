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
    box1text = "l"
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
    pygame.draw.rect(screen, black, ((size[0] -size[0] + 12), 9, 556, 319), 7, 11)
   
    #text box background
    pygame.draw.rect(screen, dark_grey, ((size[0]/2) + 75, 15, 550, 310))
    pygame.draw.rect(screen, black, ((size[0]/2) + 72, 9, 556, 319), 7, 11)
   
    #mouse actions
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    
    #button 1
    if (size[0]/2 - 625) <= mouse[0] <= ((size[0]/2 - 625)+610) and 380 <= mouse[1] <= 520 and pressed[0] == True:
        main.clicksound.play()
        #main.window = 
    elif (size[0]/2 - 625) <= mouse[0] <= ((size[0]/2 - 625)+610) and 380 <= mouse[1] <= 520:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 - 625, 380, 610, 140 )))
        screen.blit(text2, (575, 204))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 - 625, 380, 610, 140 )))
        screen.blit(text1, (575, 204))
    pygame.draw.rect(screen, black, ((size[0]/2) - 628, 374, 616, 149), 7, 11)

    #button 2
    if (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 380 <= mouse[1] <= 520 and pressed[0] == True:
        main.clicksound.play()
        #main.window = 
    elif (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 380 <= mouse[1] <= 520:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 + 15, 380, 610, 140 )))
        screen.blit(text4, (575, 204))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 + 15, 380, 610, 140 )))
        screen.blit(text3, (575, 204))
    pygame.draw.rect(screen, black, ((size[0]/2) + 12, 374, 616, 149), 7, 11)

    #button 3
    if (size[0]/2 - 625) <= mouse[0] <= ((size[0]/2 - 625)+610) and 535 <= mouse[1] <= 675 and pressed[0] == True:
        main.clicksound.play()
        #main.window = 
    elif (size[0]/2 - 625) <= mouse[0] <= ((size[0]/2 - 625)+610) and 535 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 - 625, 535, 610, 140 )))
        screen.blit(text6, (575, 204))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 - 625, 535, 610, 140 )))
        screen.blit(text5, (575, 204))
    pygame.draw.rect(screen, black, ((size[0]/2) - 628, 529, 616, 149), 7, 11)

    #button 4
    if (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 535 <= mouse[1] <= 675 and pressed[0] == True:
        main.clicksound.play()
        #main.window = 
    elif (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 535 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 + 15, 535, 610, 140 )))
        screen.blit(text8, (575, 204))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 + 15, 535, 610, 140 )))
        screen.blit(text7, (575, 204))
    pygame.draw.rect(screen, black, ((size[0]/2) + 12, 529, 616, 149), 7, 11)