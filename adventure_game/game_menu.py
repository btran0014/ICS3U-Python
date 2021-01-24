import pygame
def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def scene1():
    #importing important things
    import main
    from main import screen, pygame, light_grey, size, largefont, black, smallfont, cool_green, dark_grey, white, smallestfont,tinyfont


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

    #text
    #text variables
    box1text = "Search the luggage for supplies."
    box2text = "Look for survivors and help as many as possible."
    box3text = "Check yourself for injuries before proceeding."
    box4text = "Climb the wreckage in search of aid."
    scenetext = "The sound of a fire awakes you. The smell of blood and the screech of metal attack your senses. You look over the snowy mountain ridge to see the remnants of the plane that was supposed to take you to the Himalayas. Bodies and luggage are spread accross the ground. How will you proceed?"
    #text 1
    text1 = smallestfont.render(box1text,True, black)
    text2 = smallestfont.render(box1text,True, white)
    #text 2
    text3 = smallestfont.render(box2text,True, black)
    text4 = smallestfont.render(box2text,True, white)
    #text 3
    text5 = smallestfont.render(box3text,True, black)
    text6 = smallestfont.render(box3text,True, white)
    #text 4
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
        screen.blit(text2, (30, 400))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 - 625, 380, 610, 140 )))
        screen.blit(text1, (30, 400))
    pygame.draw.rect(screen, black, ((size[0]/2) - 628, 374, 616, 149), 7, 11)

    #button 2
    if (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 380 <= mouse[1] <= 520 and pressed[0] == True:
        main.clicksound.play()
        main.window = 4
    elif (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 380 <= mouse[1] <= 520:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 + 15, 380, 610, 140 )))
        screen.blit(text4, (670, 400))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 + 15, 380, 610, 140 )))
        screen.blit(text3, (670, 400))
    pygame.draw.rect(screen, black, ((size[0]/2) + 12, 374, 616, 149), 7, 11)

    #button 3
    if (size[0]/2 - 625) <= mouse[0] <= ((size[0]/2 - 625)+610) and 535 <= mouse[1] <= 675 and pressed[0] == True:
        main.clicksound.play()
        #main.window = 
    elif (size[0]/2 - 625) <= mouse[0] <= ((size[0]/2 - 625)+610) and 535 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 - 625, 535, 610, 140 )))
        screen.blit(text6, (30, 550))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 - 625, 535, 610, 140 )))
        screen.blit(text5, (30, 550))
    pygame.draw.rect(screen, black, ((size[0]/2) - 628, 529, 616, 149), 7, 11)

    #button 4
    if (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 535 <= mouse[1] <= 675 and pressed[0] == True:
        main.clicksound.play()
        #main.window = 
    elif (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 535 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 + 15, 535, 610, 140 )))
        screen.blit(text8, (670, 550))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 + 15, 535, 610, 140 )))
        screen.blit(text7, (670, 550))
    pygame.draw.rect(screen, black, ((size[0]/2) + 12, 529, 616, 149), 7, 11)

    #screen.blit(scene_text,(735, 30))
    blit_text(screen, scenetext, (size[0]/2+81, 20), tinyfont)

def scene2():
    #importing important things
    import main
    from main import screen, pygame, light_grey, size, largefont, black, smallfont, cool_green, dark_grey, white, smallestfont,tinyfont

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

    #text
    #text variables
    box1text = "box 1"
    box2text = "box 2"
    box3text = "box 3"
    box4text = "box 4"
    scenetext = "text box"
    #text 1
    text1 = smallestfont.render(box1text,True, black)
    text2 = smallestfont.render(box1text,True, white)
    #text 2
    text3 = smallestfont.render(box2text,True, black)
    text4 = smallestfont.render(box2text,True, white)
    #text 3
    text5 = smallestfont.render(box3text,True, black)
    text6 = smallestfont.render(box3text,True, white)
    #text 4
    text7 = smallestfont.render(box4text,True, black)
    text8 = smallestfont.render(box4text,True, white)
    #scene text
    scene_text = smallestfont.render(sceneboxtext, True, white)

    #scene image on screen
    scene_image = pygame.image.load("adventure_game/images/plane_crashing.png")
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
        screen.blit(text2, (30, 400))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 - 625, 380, 610, 140 )))
        screen.blit(text1, (30, 400))
    pygame.draw.rect(screen, black, ((size[0]/2) - 628, 374, 616, 149), 7, 11)

    #button 2
    if (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 380 <= mouse[1] <= 520 and pressed[0] == True:
        main.clicksound.play()
        #main.window = 
    elif (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 380 <= mouse[1] <= 520:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 + 15, 380, 610, 140 )))
        screen.blit(text4, (670, 400))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 + 15, 380, 610, 140 )))
        screen.blit(text3, (670, 400))
    pygame.draw.rect(screen, black, ((size[0]/2) + 12, 374, 616, 149), 7, 11)

    #button 3
    if (size[0]/2 - 625) <= mouse[0] <= ((size[0]/2 - 625)+610) and 535 <= mouse[1] <= 675 and pressed[0] == True:
        main.clicksound.play()
        #main.window = 
    elif (size[0]/2 - 625) <= mouse[0] <= ((size[0]/2 - 625)+610) and 535 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 - 625, 535, 610, 140 )))
        screen.blit(text6, (30, 550))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 - 625, 535, 610, 140 )))
        screen.blit(text5, (30, 550))
    pygame.draw.rect(screen, black, ((size[0]/2) - 628, 529, 616, 149), 7, 11)

    #button 4
    if (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 535 <= mouse[1] <= 675 and pressed[0] == True:
        main.clicksound.play()
        #main.window = 
    elif (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 535 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 + 15, 535, 610, 140 )))
        screen.blit(text8, (670, 550))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 + 15, 535, 610, 140 )))
        screen.blit(text7, (670, 550))
    pygame.draw.rect(screen, black, ((size[0]/2) + 12, 529, 616, 149), 7, 11)
