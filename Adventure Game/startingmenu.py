def main_menu():
    from main import screen, pygame, grey, size, largefont, black
    pygame.init()

    menu_bg = pygame.image.load("Adventure Game/Images/menu_image.png")
    screen.blit(menu_bg, (0,0))

    menu_bg_scale = pygame.transform.scale(menu_bg,(1280,720))
    screen.blit(menu_bg_scale,(0,0))

    #print buttons onto screen
    pygame.draw.rect(screen, grey, (size[0]/2-175, 200, 350, 130))
    pygame.draw.rect(screen, grey, (size[0]/2-175, 350, 350, 130))
    pygame.draw.rect(screen, grey, (size[0]/2-175, 500, 350, 130))
    
    title_text = largefont.render("Survival Game", True, black)
    screen.blit(title_text, )
