def show_score():
    import main

    #Creates the files if they are not already created
    f = open("highscores.txt", "a+")
    f.close()
    f = open("usernames.txt", "a+")
    f.close()

    #Create a list of the scores and names, converts the scores from strings to ints
    f = open("highscores.txt", "r")
    scores = f.read().splitlines()
    for i in range(len(scores)):
        scores[i] = int(scores[i])
    f.close()
    f = open("usernames.txt", "r")
    names = f.read().splitlines()
    f.close()

    main.name_score = []
    #Convert the scores back to string and replaces any blank space with "No score Data"
    f = open("highscores.txt", "r")
    for i in range(len(scores)):
        scores[i] = str(scores[i])
        main.name_score.append([names[i], scores[i]])
    for i in range(3 - len(scores)):
        scores.append("No Score Data")
        names.append("")
    f.close()

    #Outputs a list of the scores and names
    return scores, names

def save_score():
    import main

    #Adds the name and score to the list when user clicks "save score"
    if main.user_name != "":
        main.has_saved = True
        main.name_score.append([main.user_name, sum(main.player_score)])

        #Sorts all values
        for i in range(len(main.name_score)):
            biggest = int(main.name_score[i][1])
            for n in range(i, len(main.name_score)):
                if biggest < int(main.name_score[n][1]):
                    main.name_score[i], main.name_score[n] = main.name_score[n], main.name_score[i]

        if sum(main.player_score) == main.name_score[-1][1] and len(main.name_score) > 3:
            main.text3_transparency_value = 255

        #Removes lowest value if there are more than 3
        while len(main.name_score) > 3:
            main.name_score.pop(-1)

        #Rewrite the files with the new scores and names
        f = open("highscores.txt", "w")
        for i in range(len(main.name_score)):
            f.write(str(main.name_score[i][1]) + "\n")
        f.close()
        f = open("usernames.txt", "w")
        for i in range(len(main.name_score)):
            f.write(str(main.name_score[i][0]) + "\n")
        f.close()
    else:
        main.text1_transparency_value = 255

#Creates the textbot that allows the user to enter their username
def enter_name():
    import main
    from main import pygame, screen, LIGHT_GR, DARK_GR, BLACK, sml_font

    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    pygame.draw.rect(screen, BLACK, (95, 495, 160, 40))

    if 100 <= mouse[0] <= 235 and 500 <= mouse[1] <= 530 and pressed[0] == True:
        if main.text_box_active == False:
            main.text_box_active = True
            pygame.draw.rect(screen, DARK_GR, (100, 500, 150, 30))
        else:
            main.text_box_active = False
            pygame.draw.rect(screen, LIGHT_GR, (100, 500, 150, 30))
        pygame.time.delay(200)
    else:
        if main.text_box_active == False:
            pygame.draw.rect(screen, DARK_GR, (100, 500, 150, 30))
        else:
            pygame.draw.rect(screen, LIGHT_GR, (100, 500, 150, 30))

    #Checks if the user is able to type
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if main.text_box_active == True:
                if event.key == pygame.K_BACKSPACE:
                    main.user_name = main.user_name[:-1]
                elif len(main.user_name) < 9:
                    main.user_name += event.unicode

    txt_surface = sml_font.render(main.user_name, True, BLACK)
    screen.blit(txt_surface, (100, 500))

def scoreboard_menu():
    import main
    from main import pygame, back_ground, screen, LIGHT_GR, DARK_GR, BLACK, RED, GOLD, SILVER, BRONZE, WHITE, size, menu_select_sound, reset_menu, big_font, med_font, sml_font
    pygame.init()

    #Allows for a quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main.rungame = False

    #Handles mouse interaction
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #Setpup the screen
    screen.blit(back_ground, (0, 0))

    #Initiate all the texts
    text1 = sml_font.render("MAIN MENU", True, BLACK)
    text2 = sml_font.render("MAIN MENU", True, RED)
    text3 = big_font.render("LEADERBOARD", True, BLACK)
    text4 = big_font.render("1", True, BLACK)
    text5 = big_font.render("2", True, BLACK)
    text6 = big_font.render("3", True, BLACK)
    text7 = sml_font.render(show_score()[0][0], True, BLACK)
    text8 = sml_font.render(show_score()[0][1], True, BLACK)
    text9 = sml_font.render(show_score()[0][2], True, BLACK)
    text10 = sml_font.render("SAVE SCORE", True, BLACK)
    text11 = sml_font.render("SAVE SCORE", True, RED)
    text12 = med_font.render(show_score()[1][0], True, BLACK)
    text13 = med_font.render(show_score()[1][1], True, BLACK)
    text14 = med_font.render(show_score()[1][2], True, BLACK)
    text15 = big_font.render("Please Enter Your Username!", True, WHITE)
    text16 = big_font.render("You've Already Saved Your Score!", True, WHITE)
    text17 = big_font.render("You're Score Is Too Low!", True, WHITE)

    #Draw all the things
    pygame.draw.rect(screen, BLACK, (size[0] / 2 - 500 / 2 - 5, 20, 510, 680), 0, 30, 30, 30, 30)
    pygame.draw.rect(screen, LIGHT_GR, (size[0] / 2 - 500 / 2, 25, 500, 670), 0, 30, 30, 30, 30)
    pygame.draw.rect(screen, BLACK, (400, 110, 480, 3))
    pygame.draw.circle(screen, GOLD, (485, 200), 75)
    screen.blit(text4, (467, 165))
    screen.blit(text7, (600, 200))
    screen.blit(text12, (600, 150))
    pygame.draw.rect(screen, BLACK, (400, 300, 480, 3))
    pygame.draw.circle(screen, SILVER, (485, 400), 75)
    screen.blit(text5, (467, 365))
    screen.blit(text8, (600, 400))
    screen.blit(text13, (600, 350))
    pygame.draw.rect(screen, BLACK, (400, 500, 480, 3))
    pygame.draw.circle(screen, BRONZE, (485, 600), 75)
    screen.blit(text6, (467, 565))
    screen.blit(text9, (600, 600))
    screen.blit(text14, (600, 550))

    screen.blit(text3, (450, 50))

    text15.set_alpha(main.text1_transparency_value)
    text16.set_alpha(main.text2_transparency_value)
    text17.set_alpha(main.text3_transparency_value)
    if main.text1_transparency_value > 0:
        main.text1_transparency_value -= 2
    if main.text2_transparency_value > 0:
        main.text2_transparency_value -= 2
    if main.text3_transparency_value > 0:
        main.text3_transparency_value -= 2
    screen.blit(text15, (275, 300))
    screen.blit(text16, (250, 300))
    screen.blit(text17, (330, 300))

    #Save button to add player score to leader board
    pygame.draw.rect(screen, BLACK, (70, 540, 210, 135), 5, 8)
    if 75 <= mouse[0] <= 255 and 545 <= mouse[1] <= 670 and pressed[0] == True:
        pygame.draw.rect(screen, DARK_GR, (75, 545, 200, 125))
        screen.blit(text11, (110, 595))
        menu_select_sound.play()
        if main.has_saved == False:
            save_score()
        else:
            main.text2_transparency_value = 255
        pygame.time.delay(200)
    elif 75 <= mouse[0] <= 255 and 545 <= mouse[1] <= 670:
        pygame.draw.rect(screen, DARK_GR, (75, 545, 200, 125))
        screen.blit(text11, (110, 595))
    else:
        pygame.draw.rect(screen, LIGHT_GR, (75, 545, 200, 125))
        screen.blit(text10, (110, 595))

    #Main menu button to return and play again if wanted
    pygame.draw.rect(screen, BLACK, (980, 540, 210, 135), 5, 8)
    if 985 <= mouse[0] <= 1165 and 545 <= mouse[1] <= 670 and pressed[0] == True:
        menu_select_sound.play()
        reset_menu()
        main.window = 0
        pygame.time.delay(200)
    elif 985 <= mouse[0] <= 1165 and 545 <= mouse[1] <= 670:
        pygame.draw.rect(screen, DARK_GR, (985, 545, 200, 125))
        screen.blit(text2, (1020, 595))
    else:
        pygame.draw.rect(screen, LIGHT_GR, (985, 545, 200, 125))
        screen.blit(text1, (1020, 595))

    enter_name()