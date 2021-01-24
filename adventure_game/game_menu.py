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
    blit_text(screen, scenetext, (size[0]/2+84, 20), tinyfont)

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
    blit_text(screen, scenetext, (size[0]/2+84, 20), tinyfont)

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
    blit_text(screen, scenetext, (size[0]/2+84, 20), tinyfont)

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
    blit_text(screen, scenetext, (size[0]/2+84, 20), tinierfont)
