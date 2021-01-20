def instructions_menu():
    import main 
    from main import screen, pygame, light_grey, size, largefont, black, smallfont, dark_grey, white
    pygame.init()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    