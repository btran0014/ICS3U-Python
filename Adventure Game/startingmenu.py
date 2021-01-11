def main_menu():
    from main import screen, pygame, light_grey, size, largefont, black, subtitlefont, cool_green, dark_grey
    pygame.init()

    #play button text
    text1 = subtitlefont.render("PLAY", True, black)
    text2 = subtitlefont.render("PLAY", True, cool_green )

    #title
    title_text = largefont.render("Solitude", True, black)
    screen.blit(title_text, (size[0]/2 - 120, size[1]/2 - 270))

    #hover and press
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #background image
    menu_bg = pygame.image.load("Adventure Game/Images/purple_wallpaper.jpg")
    screen.blit(menu_bg, (0,0))
    menu_bg_scale = pygame.transform.scale(menu_bg,(1280,720))
    screen.blit(menu_bg_scale,(0,0))

    #print buttons onto screen
    pygame.draw.rect(screen, light_grey, (size[0]/2-175, 200, 350, 130))
    pygame.draw.rect(screen, light_grey, (size[0]/2-175, 350, 350, 130))
    pygame.draw.rect(screen, light_grey, (size[0]/2-175, 500, 350, 130))
    
    #play button
    if 465 <=mouse[0] <=815 and 200 <= mouse[1] <=130 and pressed [0] == True:
        #menuselectsound.play 
        main.window = 3
        pygame.time.delay(100)
    elif 465 <=mouse[0] <=815 and 200 <= mouse[1] <=130:
        pygame.draw.rect(screen, dark_grey, ((size[0]/2-175, 200, 350, 130)))
        screen.blit(text2, (175, 35))



