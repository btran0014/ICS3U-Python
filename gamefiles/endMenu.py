#Menu to display the end of the game and show some interesting stats
def end_menu():
    import main 
    from main import pygame, window, title_font, big_font, med_font, sml_font, BLACK, RED, DARK_GR, LIGHT_GR, back_ground, screen, player_score, enemies_killed, abilities_used, gametime, distance_travelled, menu_select_sound, reset_menu, enemy_amount_killed, enemy_end_screen_type, enemy_img, enemy_type, ability_cooldown, multiplayer
    pygame.init()

    main.invisible_value = 255

    #Allows for a quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #Handles mouse interaction
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #Setpup the screen
    screen.blit(back_ground, (0, 0))

    #Initiate all the texts
    text1 = big_font.render("NEXT", True, BLACK)
    text2 = big_font.render("NEXT", True, RED)
    text3 = title_font.render("GAME OVER", True, BLACK)
    text4 = sml_font.render("Total Score:", True, BLACK)
    text5 = sml_font.render("P1 Score:", True, BLACK)
    text6 = sml_font.render("P2 Score:", True, BLACK)
    text7 = sml_font.render("Total enemies killed:", True, BLACK)
    text8 = sml_font.render("P1 enemies killed:", True, BLACK)
    text9 = sml_font.render("P2 enemies killed:", True, BLACK)
    text10 = sml_font.render("Total abilities used: ", True, BLACK)
    text11 = sml_font.render("P1 abilities used:", True, BLACK)
    text12 = sml_font.render("P2 abilities used:", True, BLACK)
    text13 = sml_font.render("Time played:", True, BLACK)
    text14 = sml_font.render("P1 distance travelled:", True, BLACK)
    text15 = sml_font.render("P2 distance travelled:", True, BLACK)
    text16 = med_font.render("Enemies killed", True, BLACK)

    #Initiate all the stats
    stat1 = sml_font.render(str(sum(player_score)), True, BLACK)
    stat2 = sml_font.render(str(player_score[0]), True, BLACK)
    stat3 = sml_font.render(str(player_score[1]), True, BLACK)
    stat4 = sml_font.render(str(sum(enemies_killed)), True, BLACK)
    stat5 = sml_font.render(str(enemies_killed[0]), True, BLACK)
    stat6 = sml_font.render(str(enemies_killed[1]), True, BLACK)
    stat7 = sml_font.render(str(sum(abilities_used)), True, BLACK)
    stat8 = sml_font.render(str(abilities_used[0]), True, BLACK)
    stat9 = sml_font.render(str(abilities_used[1]), True, BLACK)
    stat10 = sml_font.render(str(gametime) + " secs", True, BLACK)
    stat11 = sml_font.render(str(round(distance_travelled[0], 2)), True, BLACK)
    stat12 = sml_font.render(str(round(distance_travelled[1], 2)), True, BLACK)
    stat13 = sml_font.render("You killed this enemy " + str(enemy_amount_killed[main.enemy_end_screen_type]) + " times!", True, BLACK)

    #Output all stats and text to the screen
    pygame.draw.rect(screen, LIGHT_GR, (50, 25, 500, 670), 50, 75)
    pygame.draw.rect(screen, LIGHT_GR, (100, 75, 400, 570))
    pygame.draw.rect(screen, BLACK, (45, 20, 510, 680), 8, 80)
    screen.blit(text3, (122, 30))
    pygame.draw.rect(screen, BLACK, (70, 110, 460, 2))
    screen.blit(text4, (80, 160))
    screen.blit(text5, (80, 190))
    screen.blit(text7, (80, 280))
    screen.blit(text8, (80, 310))
    screen.blit(text10, (80, 400))
    screen.blit(text11, (80, 430))
    screen.blit(text13, (80, 520))
    screen.blit(text14, (80, 580))
    screen.blit(stat1, (415, 160))
    screen.blit(stat2, (415, 190))
    screen.blit(stat4, (415, 280))
    screen.blit(stat5, (415, 310))
    screen.blit(stat7, (415, 400))
    screen.blit(stat8, (415, 430))
    screen.blit(stat10, (415, 520))
    screen.blit(stat11, (415, 580))

    #Output multiplayer stats
    if multiplayer == True:
        screen.blit(text6, (80, 220))
        screen.blit(text9, (80, 340))
        screen.blit(text12, (80, 460))
        screen.blit(text15, (80, 610))
        screen.blit(stat3, (415, 220))
        screen.blit(stat6, (415, 340))
        screen.blit(stat9, (415, 460))
        screen.blit(stat12, (415, 610))

    #Output enemy killed stats
    pygame.draw.rect(screen, BLACK, (795, 45, 410, 310), 0, 30, 30, 30, 30)
    pygame.draw.rect(screen, LIGHT_GR, (800, 50, 400, 300), 0, 30, 30, 30, 30)
    if main.enemy_end_screen_type != 5 and main.enemy_end_screen_type != 7 and main.enemy_end_screen_type != 11:
        screen.blit(enemy_img[main.enemy_end_screen_type], (965, 125))
    elif main.enemy_end_screen_type == 5:
        screen.blit(enemy_img[main.enemy_end_screen_type], (981, 141))
    elif main.enemy_end_screen_type == 7 or main.enemy_end_screen_type == 11:
        screen.blit(enemy_img[main.enemy_end_screen_type], (949, 109))    
    screen.blit(text16, (875, 60))
    screen.blit(stat13, (830, 225))
    #Draw the arrow buttons
    if 1050 <= mouse[0] <= 1100 and 275 <= mouse[1] <= 325 and pressed[0] == True and main.enemy_end_screen_type < enemy_type[-1] and main.is_button_pressed == False:
        pygame.draw.polygon(screen, BLACK, ((1050, 275), (1050, 325), (1100, 300)))
        menu_select_sound.play()
        main.enemy_end_screen_type += 1
        main.is_button_pressed = True
    elif 1050 <= mouse[0] <= 1100 and 275 <= mouse[1] <= 325:
        pygame.draw.polygon(screen, BLACK, ((1050, 275), (1050, 325), (1100, 300)))
    else:
        pygame.draw.polygon(screen, DARK_GR, ((1050, 275), (1050, 325), (1100, 300)))
    if 900 <= mouse[0] <= 950 and 275 <= mouse[1] <= 325 and pressed[0] == True and main.enemy_end_screen_type > enemy_type[0] and main.is_button_pressed == False:
        pygame.draw.polygon(screen, BLACK, ((950, 275), (950, 325), (900, 300)))
        menu_select_sound.play()
        main.enemy_end_screen_type -= 1
        main.is_button_pressed = True
    elif 900 <= mouse[0] <= 950 and 275 <= mouse[1] <= 325:
        pygame.draw.polygon(screen, BLACK, ((950, 275), (950, 325), (900, 300)))
    else:
        pygame.draw.polygon(screen, DARK_GR, ((950, 275), (950, 325), (900, 300)))
    
    if main.is_button_pressed == True:
        main.button_cooldown_started, main.button_start_time, main.button_passed_time = ability_cooldown(main.button_cooldown_started, main.button_start_time, main.button_passed_time)
        if main.button_passed_time >= 500:
            main.button_passed_time = 0
            main.button_cooldown_started = False
            main.is_button_pressed = False

    #Main menu button to return and play again if wanted
    pygame.draw.rect(screen, BLACK, (800, 540, 410, 135), 5, 8)
    if 805 <= mouse[0] <= 1205 and 545 <= mouse[1] <= 670 and pressed[0] == True:
        menu_select_sound.play()
        main.window = 7
        pygame.time.delay(200)
    elif 805 <= mouse[0] <= 1205 and 545 <= mouse[1] <= 670:
        pygame.draw.rect(screen, DARK_GR, (805, 545, 400, 125))
        screen.blit(text2, (930, 575))
    else:
        pygame.draw.rect(screen, LIGHT_GR, (805, 545, 400, 125))
        screen.blit(text1, (930, 575))