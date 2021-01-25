import pygame
def blit_text(surface, text, pos, font, color):
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
    text1 = tinyfont.render(box1text,True, black)
    text2 = tinyfont.render(box1text,True, white)
    #text 2
    text3 = tinyfont.render(box2text,True, black)
    text4 = tinyfont.render(box2text,True, white)
    #text 3
    text5 = tinyfont.render(box3text,True, black)
    text6 = tinyfont.render(box3text,True, white)
    #text 4
    text7 = tinyfont.render(box4text,True, black)
    text8 = tinyfont.render(box4text,True, white)

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
        pygame.time.delay(100)
        main.window = 4
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
        pygame.time.delay(100)
        main.window = 5
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
        pygame.time.delay(100)
        main.window = 6
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
        pygame.time.delay(100)
        main.window = 7
    elif (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 535 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 + 15, 535, 610, 140 )))
        screen.blit(text8, (670, 550))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 + 15, 535, 610, 140 )))
        screen.blit(text7, (670, 550))
    pygame.draw.rect(screen, black, ((size[0]/2) + 12, 529, 616, 149), 7, 11)

    #screen.blit(scene_text,(735, 30))
    blit_text(screen, scenetext, (size[0]/2+84, 20), tinyfont, pygame.Color('white'))

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
    box1text = "Huddle around a fire burning from plane wreck."
    box2text = "Look for shelter in a nearby cave."
    box3text = "Keep warm by holing up under the snow."
    box4text = "Press on through the weather, trying to stay warm."
    scenetext = "You gather all that you can but it’s helpless. The supplies in the luggage won’t do you any good. The skin on your arms begins to whiten, the feeling in your fingers slowly disappears. You’re suffering from hypothermia. The conditions are too cold for you. You know that if you don’t warm up soon, you’ll die. What’s next for you?"
    #text 1
    text1 = tinyfont.render(box1text,True, black)
    text2 = tinyfont.render(box1text,True, white)
    #text 2
    text3 = tinyfont.render(box2text,True, black)
    text4 = tinyfont.render(box2text,True, white)
    #text 3
    text5 = tinyfont.render(box3text,True, black)
    text6 = tinyfont.render(box3text,True, white)
    #text 4
    text7 = tinyfont.render(box4text,True, black)
    text8 = tinyfont.render(box4text,True, white)

    #scene image on screen
    scene_image = pygame.image.load("adventure_game/images/luggage.png")
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
        pygame.time.delay(100)
        main.window = 8
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
        pygame.time.delay(100)
        main.window = 9
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
        pygame.time.delay(100)
        main.window = 10
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
        pygame.time.delay(100)
        main.window = 11
    elif (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 535 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 + 15, 535, 610, 140 )))
        screen.blit(text8, (670, 550))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 + 15, 535, 610, 140 )))
        screen.blit(text7, (670, 550))
    pygame.draw.rect(screen, black, ((size[0]/2) + 12, 529, 616, 149), 7, 11)

    #screen.blit(scene_text,(735, 30))
    blit_text(screen, scenetext, (size[0]/2+84, 20), tinyfont, pygame.Color('white'))

def scene3():
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
    box1text = "Huddle around a fire burning from plane wreck."
    box2text = "Look for shelter in a nearby cave."
    box3text = "Keep warm by holing up under the snow."
    box4text = "Press on through the weather, trying to stay warm."
    scenetext = "You decide to search for crash survivors. Scattered across the rocks are bodies. All torn apart from the accident. It's no use. No one could have survived the crash. You’re the only exception. You’re all alone out here. Knowing this, you proceed through the canyon, praying that there will be any sign of civilization. Your body starts to get numb from the cold gusts of winter air. You know you’re going to need to find a heat source soon or you’ll be in trouble."
    #text 1
    text1 = tinyfont.render(box1text,True, black)
    text2 = tinyfont.render(box1text,True, white)
    #text 2
    text3 = tinyfont.render(box2text,True, black)
    text4 = tinyfont.render(box2text,True, white)
    #text 3
    text5 = tinyfont.render(box3text,True, black)
    text6 = tinyfont.render(box3text,True, white)
    #text 4
    text7 = tinyfont.render(box4text,True, black)
    text8 = tinyfont.render(box4text,True, white)

    #scene image on screen
    scene_image = pygame.image.load("adventure_game/images/valley.png")
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
        pygame.time.delay(100)
        main.window = 8
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
        pygame.time.delay(100)
        main.window = 9
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
        pygame.time.delay(100)
        main.window = 10
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
        pygame.time.delay(100)
        main.window = 11
    elif (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 535 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 + 15, 535, 610, 140 )))
        screen.blit(text8, (670, 550))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 + 15, 535, 610, 140 )))
        screen.blit(text7, (670, 550))
    pygame.draw.rect(screen, black, ((size[0]/2) + 12, 529, 616, 149), 7, 11)

    #screen.blit(scene_text,(735, 30))
    blit_text(screen, scenetext, (size[0]/2+84, 20), tinyfont, pygame.Color('white'))

def scene4():
    #importing important things
    import main
    from main import screen, pygame, light_grey, size, largefont, black, smallfont, cool_green, dark_grey, white, smallestfont,tinyfont, tinierfont

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
    box1text = "Huddle around a fire burning from plane wreck."
    box2text = "Look for shelter in a nearby cave."
    box3text = "Keep warm by holing up under the snow."
    box4text = "Press on through the weather, trying to stay warm."
    scenetext = "You take a moment to catch your breath and really get an idea of the situation you’re in right now. A red stream of blood drips down your leg. You’re bleeding. Your adrenaline must have been pumping so hard you didn’t notice your injuries. Having once taken a first aid course at summer camp, you know exactly what to do. You take off your scarf and wrap it tightly around your leg creating a tourniquet  preventing the blood loss and your eventual death. The cold winter air presses against your face and body. Being a Canadian resident, you understand the severity of the cold. You need to warm yourself up or else this might be the end of your life."

    #text 1
    text1 = tinyfont.render(box1text,True, black)
    text2 = tinyfont.render(box1text,True, white)
    #text 2
    text3 = tinyfont.render(box2text,True, black)
    text4 = tinyfont.render(box2text,True, white)
    #text 3
    text5 = tinyfont.render(box3text,True, black)
    text6 = tinyfont.render(box3text,True, white)
    #text 4
    text7 = tinyfont.render(box4text,True, black)
    text8 = tinyfont.render(box4text,True, white)

    #scene image on screen
    scene_image = pygame.image.load("adventure_game/images/first_aid_kit.png")
    scene_image = pygame.transform.scale(scene_image,(360, 220))
    pygame.draw.rect(screen, light_grey, ((size[0] - size[0] + 15), 15, 546, 310))
    screen.blit(scene_image,(125,50))
    pygame.draw.rect(screen, black, ((size[0] - size[0] + 12), 9, 556, 319), 7, 11)
   
    #text box background
    pygame.draw.rect(screen, dark_grey, ((size[0]/2) + 75, 15, 550, 310))
    pygame.draw.rect(screen, black, ((size[0]/2) + 72, 9, 556, 319), 7, 11)
   
    #mouse actions
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    
    #button 1
    if (size[0]/2 - 625) <= mouse[0] <= ((size[0]/2 - 625)+610) and 380 <= mouse[1] <= 520 and pressed[0] == True:
        main.clicksound.play()
        pygame.time.delay(100)
        main.window = 8
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
        pygame.time.delay(100)
        main.window = 9
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
        pygame.time.delay(100)
        main.window = 10
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
        pygame.time.delay(100)
        main.window = 11
    elif (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 535 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 + 15, 535, 610, 140 )))
        screen.blit(text8, (670, 550))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 + 15, 535, 610, 140 )))
        screen.blit(text7, (670, 550))
    pygame.draw.rect(screen, black, ((size[0]/2) + 12, 529, 616, 149), 7, 11)

    #screen.blit(scene_text,(735, 30))
    blit_text(screen, scenetext, (size[0]/2+84, 20), tinierfont, pygame.Color('white'))

def scene5():
    #importing important things
    import main
    from main import screen, pygame, light_grey, size, largefont, black, smallfont, cool_green, dark_grey, white, smallestfont,tinyfont, tinierfont

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
    box1text = "Take a minute to get ahold of yourself."
    box2text = "Rest and replenish your energy."
    scenetext = "You move towards the hollow frame of the plane. A eery breeze chills your body. You grab onto the frame of the machine, grasping anything available to hoist your way into the plane. Using all of your might, you pull yourself into the plane. The body starts to creak. You worry something is going to snap. Nonetheless, you proceed onward. Making it inside the plane, you feel warmer. Safer. The walls of the vessel are protecting you from the harsh weather outside. How do you choose to proceed?"

    #text 1
    text1 = tinyfont.render(box1text,True, black)
    text2 = tinyfont.render(box1text,True, white)
    #text 2
    text3 = tinyfont.render(box2text,True, black)
    text4 = tinyfont.render(box2text,True, white)

    #scene image on screen
    scene_image = pygame.image.load("adventure_game/images/climb_plane.jpg")
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
        pygame.time.delay(100)
        #main.window = 8
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
        pygame.time.delay(100)
        #main.window = 9
    elif (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 380 <= mouse[1] <= 520:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 + 15, 380, 610, 140 )))
        screen.blit(text4, (670, 400))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 + 15, 380, 610, 140 )))
        screen.blit(text3, (670, 400))
    pygame.draw.rect(screen, black, ((size[0]/2) + 12, 374, 616, 149), 7, 11)

    #screen.blit(scene_text,(735, 30))
    blit_text(screen, scenetext, (size[0]/2+84, 20), tinierfont, pygame.Color('white'))

def scene6():
    import main
    from main import screen, pygame, light_grey, size, largefont, black, smallfont, dark_grey, white, smallestfont, tinyfont
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

    vfulltext = "You decide that huddling around a fire is a good idea. You spot in the distance, a fire still burning from the engine components left behind after the wreckage of the plane. You approach it and sit down. The warmth of the flame enters your body. You feel safe and at ease. It is getting dark and you are struggling to survive out here alone. You hear a creaking noise. Then, a snap. Your body is pinned. The plane collapses on you and you aren’t able to escape. You lay there, struggling to breathe and slowly giving in to the cold. Your life flashes in front of your eyes. "
    btext1 = smallfont.render("CONTINUE", True, black)
    btext2 = smallfont.render("CONTINUE", True, white)

    #background
    menu_bg = pygame.image.load("adventure_game/images/purple_wallpaper.jpg")
    screen.blit(menu_bg, (0,0))
    menu_bg_scale = pygame.transform.scale(menu_bg,(1280,720))
    screen.blit(menu_bg_scale,(0,0))


    # Exit Button
    if 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675 and pressed[0] == True:
        main.clicksound.play()
        pygame.time.delay(100)
        main.window = 100
    elif 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(btext2, (525, 585))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(btext1, (525, 585))
    pygame.draw.rect(screen, black, ((size[0]/2) - 197, 555, 395, 123), 7, 11)

    blit_text(screen, vfulltext, (15,300),tinyfont, pygame.Color('white'))

    #scene image on screen
    scene_image = pygame.image.load("adventure_game/images/broken_heart.png")
    scene_image = pygame.transform.scale(scene_image,(260, 150))
    pygame.draw.rect(screen, light_grey, ((size[0] - size[0] + 480), 35, 300, 200))
    screen.blit(scene_image,(500,50))
    pygame.draw.rect(screen, black, ((size[0] - size[0] + 477), 26, 310, 209), 7, 11)

def scene7():
    import main
    from main import screen, pygame, light_grey, size, largefont, black, smallfont, cool_green, dark_grey, white, smallestfont, tinyfont, tinierfont


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
    box1text = "Climb the steep walls of the cave onto a ledge."
    box2text = "Lay down flat on the ground."
    box3text = "Zig zag away from the bear. "
    box4text = "Hold your ground. "
    scenetext = "You venture into a nearby cave for shelter. The thick rock walls surround you, sheltering you from the harsh weather and providing warmth. You get a feeling that you aren’t alone. You look around only to see the remnants of animal carcasses. Skulls and bones. Something’s here with you. You hear a rough grumbling noise. It's the sound of the grizzly bear’s belly, the one that’s approaching your direction. Luckily it doesn’t see you yet. What do you do?"
    #text 1
    text1 = tinyfont.render(box1text,True, black)
    text2 = tinyfont.render(box1text,True, white)
    #text 2
    text3 = tinyfont.render(box2text,True, black)
    text4 = tinyfont.render(box2text,True, white)
    #text 3
    text5 = tinyfont.render(box3text,True, black)
    text6 = tinyfont.render(box3text,True, white)
    #text 4
    text7 = tinyfont.render(box4text,True, black)
    text8 = tinyfont.render(box4text,True, white)

    #scene image on screen
    scene_image = pygame.image.load("adventure_game/images/cave.jpg")
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
        pygame.time.delay(100)
        main.window = 12
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
        pygame.time.delay(100)
        main.window = 13
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
        pygame.time.delay(100)
        main.window = 14
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
        pygame.time.delay(100)
        main.window = 15
    elif (size[0]/2 + 15) <= mouse[0] <= ((size[0]/2 + 15)+610) and 535 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2 + 15, 535, 610, 140 )))
        screen.blit(text8, (670, 550))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2 + 15, 535, 610, 140 )))
        screen.blit(text7, (670, 550))
    pygame.draw.rect(screen, black, ((size[0]/2) + 12, 529, 616, 149), 7, 11)

    #screen.blit(scene_text,(735, 30))
    blit_text(screen, scenetext, (size[0]/2+84, 20), tinierfont, pygame.Color('white'))

def scene8(): #change the outcome of this button later!!!
    import main
    from main import screen, pygame, light_grey, size, largefont, black, smallfont, dark_grey, white, smallestfont, tinyfont
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

    vfulltext = "You decide that the best way to fight the cold is to dig into the snow, and huddle under it. You slowly but surely dig a hole large enough to fit your body, keeping you warm until the following snow storm passes over. Now warm, you are ready to proceed on through the wilderness in an attempt to find civilization. "
    btext1 = smallfont.render("CONTINUE", True, black)
    btext2 = smallfont.render("CONTINUE", True, white)

    #background
    menu_bg = pygame.image.load("adventure_game/images/purple_wallpaper.jpg")
    screen.blit(menu_bg, (0,0))
    menu_bg_scale = pygame.transform.scale(menu_bg,(1280,720))
    screen.blit(menu_bg_scale,(0,0))


    # Exit Button
    if 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675 and pressed[0] == True:
        main.clicksound.play()
        pygame.time.delay(100)
        main.window = 100
    elif 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(btext2, (525, 585))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(btext1, (525, 585))
    pygame.draw.rect(screen, black, ((size[0]/2) - 197, 555, 395, 123), 7, 11)

    blit_text(screen, vfulltext, (15,350),tinyfont, pygame.Color('white'))

    #scene image on screen
    scene_image = pygame.image.load("adventure_game/images/snow_shelter.jpg")
    scene_image = pygame.transform.scale(scene_image,(480,240))
    screen.blit(scene_image,(400,50))
    pygame.draw.rect(screen, black, ((size[0] -size[0] + 397), 44, 486, 249), 7, 11)

def scene9():
    import main
    from main import screen, pygame, light_grey, size, largefont, black, smallfont, dark_grey, white, smallestfont, tinyfont
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
    vfulltext = "You figure the best course of action at this point is to continue moving forward to find civilization while keeping your arms as close to your body as possible. You trudge through the snow, enduring the harsh winter storm that is brewing. You see a light. A faint light far off in the distance. Could it be? A sign of civilization? You press on forward, enduring the storm once more. You can no longer feel your toes. Your ears are frozen solid and numb. Your fingers are losing their sense of touch once again. You slow down to rub your hands but it's no use. Your fingers are frozen solid with their skin blackened by the winter frostbite. You collapse in the mountains, clinging on to your only hope of civilization. You black out due to hypothermia as your spirit leaves your body."
    btext1 = smallfont.render("CONTINUE", True, black)
    btext2 = smallfont.render("CONTINUE", True, white)

    #background
    menu_bg = pygame.image.load("adventure_game/images/purple_wallpaper.jpg")
    screen.blit(menu_bg, (0,0))
    menu_bg_scale = pygame.transform.scale(menu_bg,(1280,720))
    screen.blit(menu_bg_scale,(0,0))


    # Exit Button
    if 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675 and pressed[0] == True:
        main.clicksound.play()
        pygame.time.delay(100)
        main.window = 100
    elif 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(btext2, (525, 585))
    else:
        pygame.draw.rect(screen, light_grey, ((size[0]/2) - 194, 561, 389, 114))
        screen.blit(btext1, (525, 585))
    pygame.draw.rect(screen, black, ((size[0]/2) - 197, 555, 395, 123), 7, 11)

    blit_text(screen, vfulltext, (15,300),tinyfont, pygame.Color('white'))

    #scene image on screen
    scene_image = pygame.image.load("adventure_game/images/freezing.png")
    scene_image = pygame.transform.scale(scene_image,(170,170))
    screen.blit(scene_image,(560,80))
    pygame.draw.rect(screen, black, ((size[0] -size[0] + 557), 74, 176, 179), 7, 11) 