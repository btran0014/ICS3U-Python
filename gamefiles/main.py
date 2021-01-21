import pygame
import random, math, time
pygame.init()

from startMenu import menu
from controlsMenu import controls
from instructionsMenu import instructions
from playMenu import char_selection
from pauseMenu import pause
from endMenu import end_menu
from scoreboardMenu import scoreboard_menu

#Basic game setup
pygame.display.set_caption("League Of Invaders")
clock = pygame.time.Clock()
size = (1280, 720)
screen = pygame.display.set_mode(size)
bg = pygame.image.load("gamefiles/images/background.jpg").convert_alpha()
char1_img = pygame.image.load("gamefiles/images/green_char.png").convert_alpha()
char2_img = pygame.image.load("gamefiles/images/blue_char.png").convert_alpha()
arrow_img = pygame.image.load("gamefiles/images/arrow.png").convert_alpha()
sword_img = pygame.image.load("gamefiles/images/sword.png").convert_alpha()
staff_img = pygame.image.load("gamefiles/images/staff.png").convert_alpha()
bolt_img = [pygame.image.load("gamefiles/images/fire_ball.png").convert_alpha(), pygame.image.load("gamefiles/images/ice_spikes.png").convert_alpha(), pygame.image.load("gamefiles/images/green_rock.png").convert_alpha()]
enemy_img = [pygame.image.load("gamefiles/images/green_enemy.png").convert_alpha(), pygame.image.load("gamefiles/images/red_enemy.png").convert_alpha(), pygame.image.load("gamefiles/images/blue_enemy.png").convert_alpha(), pygame.image.load("gamefiles/images/yellow_enemy.png").convert_alpha(), pygame.image.load("gamefiles/images/orange_enemy.png").convert_alpha(), pygame.image.load("gamefiles/images/turquoise_enemy.png").convert_alpha(), pygame.image.load("gamefiles/images/white_enemy.png").convert_alpha(), pygame.image.load("gamefiles/images/boss_enemy.png").convert_alpha(), pygame.image.load("gamefiles/images/gold_enemy.png").convert_alpha(), pygame.image.load("gamefiles/images/pink_enemy1.png").convert_alpha(), pygame.image.load("gamefiles/images/lime_enemy.png").convert_alpha(), pygame.image.load("gamefiles/images/pirate_enemy.png").convert_alpha()]
pink_enemy_img = [pygame.image.load("gamefiles/images/pink_enemy1.png").convert_alpha(), pygame.image.load("gamefiles/images/pink_enemy2.png").convert_alpha()]
ball_img = pygame.image.load("gamefiles/images/spike_ball.png").convert_alpha()
ice_img = pygame.image.load("gamefiles/images/icicle.png").convert_alpha()
heart_img = pygame.image.load("gamefiles/images/heart.png").convert_alpha()
empty_heart_img = pygame.image.load("gamefiles/images/heart_empty.png").convert_alpha()
frozen_img = pygame.image.load("gamefiles/images/ice.png").convert_alpha()
frozen_img.set_alpha(200)
cannon_ball_img = pygame.image.load("gamefiles/images/pirate_shot.png").convert_alpha()
heal_powerup_img = pygame.image.load("gamefiles/images/heal_powerup.png").convert_alpha()
speed_powerup_img = pygame.image.load("gamefiles/images/speed_powerup.png").convert_alpha()
cooldown_powerup_img = pygame.image.load("gamefiles/images/cooldown_powerup.png").convert_alpha()
pygame.display.set_icon(enemy_img[1])

#Game variables
multiplayer = False
char, char_x, char_y, char_width, char_height, char_face, char_ability, char_health, char_side = [0, 1], [size[0] / 2, size[0] / 2 + 100], [size[1] / 2, size[1] / 2], 64, 64, [0, 0], [-1, -1], [3, 3], [0, 0]
ability_x, ability_y, ability_width, ability_height, ability_face, ability_collision_occured = [[-100, -100], [-100, -100], [-100, -100]], [[-100, -100], [-100, -100], [-100, -100]], [[10, 10], [22, 22], [64, 64]], [[62, 62], [50, 50], [64, 64]], [[0, 0], [0, 0], [0, 0]], [False, False]
staff_x, staff_y, staff_face, img_num = [-100, -100], [-100, -100], [0, 0], [0, 0]
sword_cooldown_started, sword_start_time, sword_passed_time, bolt_cooldown_started, bolt_start_time, bolt_passes_time = [False, False], [0, 0], [0, 0], [False, False], [0, 0], [0, 0]
ability_start_time, ability_cooldown_started, ability_passed_time = [0, 0], [False, False], [0, 0]
is_active, can_use = [False, False], [True, True]
enemy_type, enemy_x, enemy_y, enemy_width, enemy_height, enemy_face, enemy_speed, is_alive, enemy_points, enemy_amount_killed, enemy_end_screen_type = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100], [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100], [64, 64, 64, 64, 64, 32, 64, 96, 64, 64, 64, 96], [64, 64, 64, 64, 64, 32, 64, 96, 64, 64, 64, 96], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0.5, 1, 0.5, 0, 0.25, 1.25, 0.75, 0.35, 0.5, 1.75, 0.75, 0.4], [False, False, False, False, False, False, False, False, False, False, False, False], [5, 10, 20, 25, 40, 50, 50, 100, 60, 75, 60, 150], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0
b_enemy_type, b_enemy_health, b_enemy_hit, gold_max_health = [0, 1, 2, 3], [4, 1, 3, 2], [[False, False, False, False], [False, False, False, False]], 1
enemy_ball_x, enemy_ball_y, enemy_ball_width, enemy_ball_height, enemy_ball_face = -100, -100, 18, 18, 0
pirate_shot_x, pirate_shot_y, pirate_shot_width, pirate_shot_height, pirate_shot_face = -100, -100, 48, 48, 0
icicle_x, icicle_y, icicle_width, icicle_height, icicle_face = -100, -100, 32, 64, 0
explosion, explosion_x, explosion_y, explosion_radius, explosion_color = 1, -100, -100, 64, [255, 255, 255]
ball_ammo, ball_is_active, ball_can_shoot, ball_cooldown_started, ball_start_time, ball_passed_time = 1, False, True, False, 0, 0
pirate_shot_ammo, pirate_shot_is_active, pirate_shot_can_shoot, pirate_shot_cooldown_started, pirate_shot_start_time, pirate_shot_passed_time, pirate_enemy_shot = 1, False, True, False, 0, 0, True
icicle_ammo, icicle_is_active, icicle_can_shoot, icicle_cooldown_started, icicle_start_time, icicle_passed_time, is_frozen, frozen_cooldown_started, frozen_start_time, frozen_passed_time = 1, False, True, False, 0, 0, [False, False], [False, False], [0, 0], [0, 0]
invisible_value, decrease, is_invisible, invisible_cooldown_started, invisible_start_time, invisible_passed_time = 255, True, False, False, 0, 0
explosion_ammo, explosion_is_active, can_take_damage, explosion_can_shoot, explosion_cooldown_started, explosion_start_time, explosion_passed_time = 1, False, False, True, False, 0, 0
time_to_spawn, respawn_timer, unpause_time = [0, 20, 40, 60, 80, 100, 120, 140, 180, 200, 220, 240], [0, 2, 10, 15, 15, 10, 10, 20, 15, 15, 10, 20], 0
has_saved = False
text_box_active, user_name, name_score, text1_transparency_value, text2_transparency_value, text3_transparency_value = False, "", [[], [], []], 0, 0, 0
powerup_type, powerup_x, powerup_y, powerup_width, powerup_height = [0, 1, 2], [-100, -100, -100], [-100, -100, -100], 64, 64
powerup_time_to_spawn, powerup_respawn_timer, is_powerup_active = 30, 40, False
bonus_speed, has_bonus_speed, speed_cooldown_started, speed_start_time, speed_passed_time = [0, 0], [False, False], [False, False], [0, 0], [0, 0]
bonus_cooldown, has_bonus_cooldown, cooldown_cooldown_started, cooldown_start_time, cooldown_passed_time = [0, 0], [False, False], [False, False], [0, 0], [0, 0]

#Menu setup
window = 0
title_font = pygame.font.SysFont("Cambria", 65)
big_font = pygame.font.SysFont("Cambria", 54)
med_font = pygame.font.SysFont("Cambria", 36)
sml_font = pygame.font.SysFont("Cambria", 24)
back_ground = pygame.image.load("gamefiles/images/game_background.jpg").convert_alpha()
grayed_out = pygame.image.load("gamefiles/images/gray_out.png").convert_alpha()
menu_select_sound = pygame.mixer.Sound("gamefiles/sounds/menu_select_sound.wav")
sword_use = pygame.mixer.Sound("gamefiles/sounds/sword_use.wav")
bow_use = pygame.mixer.Sound("gamefiles/sounds/bow_use.wav")
staff_use = pygame.mixer.Sound("gamefiles/sounds/staff_use.wav")
enemy_hit = pygame.mixer.Sound("gamefiles/sounds/enemy_hit.wav")
player_hit = pygame.mixer.Sound("gamefiles/sounds/player_hit.wav")
ice_effect = pygame.mixer.Sound("gamefiles/sounds/ice_effect.wav")
heal_powerup = pygame.mixer.Sound("gamefiles/sounds/heal_powerup.wav")
speed_powerup = pygame.mixer.Sound("gamefiles/sounds/speed_powerup.wav")
cooldown_powerup = pygame.mixer.Sound("gamefiles/sounds/cooldown_powerup.wav")
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_GR = (211, 211, 211)
DARK_GR = (71, 71, 71)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)
BRONZE = (205, 127, 50)
ORANGE = (255, 126, 28)
BLUE = (88, 231, 252)
player_count = 0
player_score, enemies_killed, abilities_used, time_played, distance_travelled = [0, 0], [0, 0], [0, 0], 0, [0, 0]
button_cooldown_started, button_start_time, button_passed_time, is_button_pressed = False, 0, 0, False

#Draw characters
def draw_char(img, x, y, face):
    new_char = pygame.transform.rotate(img, face)
    screen.blit(new_char, (x, y))

#Draws all the abilities
def draw_ability(x, y, face, img_num, staff_x, staff_y, staff_face, char):
    import main

    t = main.char_ability[char]
    if t == 0:
        new_img = pygame.transform.rotate(arrow_img, face)
        if face == 0 or face == 180:
            x -= 30
        elif face == 90 or face == 270:
            y -= 30
    elif t == 1:
        new_img = pygame.transform.rotate(sword_img, face)
        if face == 0:
            x -= 22
        elif face == 90:
            y -= 22
        elif face == 180:
            x -= 22
            y -= 10
        elif face == 270:
            x -= 10
            y -= 22
    elif t == 2:
        new_img = bolt_img[img_num]
        new_staff = pygame.transform.rotate(staff_img, staff_face)
        screen.blit(new_staff, (staff_x, staff_y))
    screen.blit(new_img, (x, y))   

#Draw arrows
def draw_icicle(img, x, y, face):
    new_icicle = pygame.transform.rotate(img, face)
    screen.blit(new_icicle, (x, y))

#Draw pause button
def pause_button():
    import main

    #Allows for interaction with the mouse
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #Allow for interactions with the pause button
    if 1233 <= mouse[0] <= 1270 and 8 <= mouse[1] <= 43 and pressed[0] == True:
        main.startpause = pygame.time.get_ticks()
        menu_select_sound.play()
        main.window = 5
        pygame.time.delay(100)
    elif 1233 <= mouse[0] <= 1270 and 8 <= mouse[1] <= 43:
        pygame.draw.rect(screen, DARK_GR, (1235, 10, 12, 31), 2, 15)
        pygame.draw.rect(screen, DARK_GR, (1237, 12, 8, 27))
        pygame.draw.rect(screen, DARK_GR, (1258, 10, 12, 31), 2, 15)
        pygame.draw.rect(screen, DARK_GR, (1260, 12, 8, 27))
        pygame.draw.rect(screen, BLACK, (1234, 8, 14, 35), 2, 20)
        pygame.draw.rect(screen, BLACK, (1257, 8, 14, 35), 2, 20)
    else:
        pygame.draw.rect(screen, LIGHT_GR, (1235, 10, 12, 31), 2, 15)
        pygame.draw.rect(screen, LIGHT_GR, (1237, 12, 8, 27))
        pygame.draw.rect(screen, LIGHT_GR, (1258, 10, 12, 31), 2, 15)
        pygame.draw.rect(screen, LIGHT_GR, (1260, 12, 8, 27))
        pygame.draw.rect(screen, BLACK, (1234, 8, 14, 35), 2, 20)
        pygame.draw.rect(screen, BLACK, (1257, 8, 14, 35), 2, 20)

#Draw the cooldown indicators
def draw_cooldowns():
    import main
    pos = (0, 0)
    font = med_font
    if ability_passed_time[0] / 1000 == 1 or ability_passed_time[0] / 1000 == 0:
        cooldown = "READY!"
        pos = (527, 637)
        font = sml_font
    else:
        cooldown = str(round(1 - (main.bonus_cooldown[0] / 1000) - ability_passed_time[0] / 1000, 2))
        pos = (535, 627)
        font = med_font
    pygame.draw.rect(screen, BLACK, (515, 595, 110, 110), 0, 0, 30, 0, 30, 0)
    pygame.draw.rect(screen, DARK_GR, (520, 600, 100, 100), 0, 0, 30, 0, 30, 0)
    if main.has_bonus_cooldown[0] == True:
        pygame.draw.rect(screen, LIGHT_GR, (520, 600, (ability_passed_time[0] / 10) * 2, 100), 0, 0, 30, 0, 30, 0)
    else:
        pygame.draw.rect(screen, LIGHT_GR, (520, 600, ability_passed_time[0] / 10, 100), 0, 0, 30, 0, 30, 0)
    p1cooldown = font.render((cooldown), True, WHITE)
    screen.blit(p1cooldown, pos)
    if multiplayer:
        if ability_passed_time[1] / 1000 == 1 or ability_passed_time[1] / 1000 == 0:
            cooldown = "READY!"
            pos = (670, 637)
            font = sml_font
        else:
            cooldown = str(round(1 - (main.bonus_cooldown[1] / 1000) - ability_passed_time[1] / 1000, 2))
            pos = (675, 627)
            font = med_font
        pygame.draw.rect(screen, BLACK, (655, 595, 110, 110), 0, 0, 0, 30, 0, 30)
        pygame.draw.rect(screen, DARK_GR, (660, 600, 100, 100), 0, 0, 0, 30, 0, 30)
        if main.has_bonus_cooldown[1] == True:
            pygame.draw.rect(screen, LIGHT_GR, (760, 600, (0.99 - ability_passed_time[1] * 2) / 1000 * 100, 100), 0, 0, 0, 30, 0, 30)
        else:
            pygame.draw.rect(screen, LIGHT_GR, (760, 600, 0.99 - ability_passed_time[1] / 1000 * 100, 100), 0, 0, 0, 30, 0, 30)
        p2cooldown = font.render((cooldown), True, WHITE)
        screen.blit(p2cooldown, pos)

#Draws the amount of hearts the players have
def draw_hearts(img, empty_img):
    #Character 1
    for i in range(0, char_health[0]):
        screen.blit(img, (400 - 100 * i, 620))
    for i in range(0, 3 - char_health[0]):
        screen.blit(empty_img, (200 + 100 * i, 620))

    #Character 2
    if multiplayer:
        for i in range(0, char_health[1]):
            screen.blit(img, (820 + 100 * i, 620))
        for i in range(0, 3 - char_health[1]):
            screen.blit(empty_img, (1020 - 100 * i, 620))

#Creates the text that will show total player score
def draw_player_score(player_score):
    total_score = sum(player_score)
    score = big_font.render("Score: " + str(total_score), True, BLACK)
    pygame.draw.rect(screen, BLACK, (465, 5, 385, 80), 0, 30, 30, 30, 30)
    pygame.draw.rect(screen, LIGHT_GR, (470, 10, 375, 70), 0, 30, 30, 30, 30)
    screen.blit(score, (500, 10))

def draw_powerup_cooldown(char):
    import main
    if main.has_bonus_speed[char] == True:
        pygame.draw.rect(screen, BLACK, (char_x[char], char_y[char] - 25, char_width, 15))
        pygame.draw.rect(screen, ORANGE, (char_x[char], char_y[char] - 25, char_width - (main.speed_passed_time[char] / 10000 * char_width), 15))
    elif main.has_bonus_cooldown[char] == True:
        pygame.draw.rect(screen, BLACK, (char_x[char], char_y[char] - 25, char_width, 15))
        pygame.draw.rect(screen, BLUE, (char_x[char], char_y[char] - 25, char_width - (main.cooldown_passed_time[char] / 10000 * char_width), 15))

#Draw the screen
def draw_screen():
    import main

    #Background
    screen.blit(bg, (0, 0))

    #Draw powerups
    screen.blit(heal_powerup_img, (main.powerup_x[0], main.powerup_y[0]))
    screen.blit(speed_powerup_img, (main.powerup_x[1], main.powerup_y[1]))
    screen.blit(cooldown_powerup_img, (main.powerup_x[2], main.powerup_y[2]))

    #Characters
    draw_char(char1_img, char_x[0], char_y[0], char_face[0])
    if multiplayer == True:
        draw_char(char2_img, char_x[1], char_y[1], char_face[1])

    #Abilities
    for i in range(0, 3):
        draw_ability(ability_x[i][0], ability_y[i][0], ability_face[i][0], img_num[0], staff_x[0], staff_y[0], staff_face[0], char[0])
        if multiplayer == True:
            draw_ability(ability_x[i][1], ability_y[i][1], ability_face[i][1], img_num[1], staff_x[1], staff_y[1], staff_face[1], char[1])

    #Enemies
    for i in range(len(enemy_type)):
        if i != 10:
            screen.blit(enemy_img[i], (enemy_x[i], enemy_y[i]))
        else:
            new_enemy_size = pygame.transform.scale(enemy_img[10], (main.enemy_width[10], main.enemy_height[10]))
            screen.blit(new_enemy_size, (enemy_x[i], enemy_y[i]))

    #Draw boss healths
    pygame.draw.rect(screen, BLACK, (enemy_x[7], enemy_y[7] - 25, enemy_width[7], 15))
    pygame.draw.rect(screen, RED, (enemy_x[7], enemy_y[7] - 25, enemy_width[7] / 4 * b_enemy_health[0], 15))

    pygame.draw.rect(screen, BLACK, (enemy_x[8], enemy_y[8] - 20, enemy_width[8], 10))
    pygame.draw.rect(screen, GOLD, (enemy_x[8], enemy_y[8] - 20, enemy_width[8] / main.gold_max_health * b_enemy_health[1], 10))

    pygame.draw.rect(screen, BLACK, (enemy_x[11], enemy_y[11] - 25, enemy_width[11], 15))
    pygame.draw.rect(screen, RED, ( enemy_x[11], enemy_y[11] - 25, enemy_width[11] / 2 * b_enemy_health[3], 15))

    #Spike ball
    screen.blit(ball_img, (enemy_ball_x, enemy_ball_y))

    #Pirate shot
    screen.blit(cannon_ball_img, (pirate_shot_x, pirate_shot_y))

    #Explosion
    pygame.draw.circle(screen, explosion_color, [explosion_x + 32, explosion_y + 32], explosion_radius / 2)

    #Icicle
    draw_icicle(ice_img, icicle_x, icicle_y, icicle_face)
    if main.is_frozen[0]:
        screen.blit(frozen_img, (char_x[0], char_y[0]))
    elif multiplayer == True and main.is_frozen[1]:
        screen.blit(frozen_img, (char_x[1], char_y[1]))
    else:
        screen.blit(frozen_img, (-100, -100))

    #Pause Button
    pause_button()

    #Draw timer
    pygame.draw.rect(screen, BLACK, (10, 10, 185, 70), 0, 30, 30, 30, 30)
    pygame.draw.rect(screen, LIGHT_GR, (15, 15, 175, 60), 0, 30, 30, 30, 30)
    time = med_font.render(str(gametime), True, BLACK)
    screen.blit(time, (25, 20))

    #Cooldown
    draw_cooldowns()

    #Hearts
    draw_hearts(heart_img, empty_heart_img)

    #Total score
    draw_player_score(player_score)

    draw_powerup_cooldown(char[0])
    if multiplayer == True:
        draw_powerup_cooldown(char[1])

#Move character function
def move_char(char):
    import main

    keys = pygame.key.get_pressed()
    if char == 0:
        key_type = [keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP], keys[pygame.K_DOWN]]
    elif char == 1:
        key_type = [keys[pygame.K_a], keys[pygame.K_d], keys[pygame.K_w],keys[pygame.K_s]]

    #Changes speed based on ability
    extraspeed = 0
    if main.char_ability[char] == 1:
        extraspeed = 0.5
    elif main.char_ability[char] == 2:
        extraspeed = 0.3

    # Movement for both players
    if main.char_health[char] > 0 and main.is_frozen[char] == False:
        if key_type[0]:
            main.char_face[char] = 90
            if main.char_x[char] - 1 <= 0:
                main.char_x[char] = 0
            else:
                main.char_x[char] -= 2 + extraspeed + main.bonus_speed[char]
                main.distance_travelled[char] += 2 + extraspeed + main.bonus_speed[char]
        elif key_type[1]:
            main.char_face[char] = 270
            if main.char_x[char] + 1 >= size[0] - char_width:
                main.char_x[char] = size[0] - char_width
            else:
                main.char_x[char] += 2 + extraspeed + main.bonus_speed[char]
                main.distance_travelled[char] += 2 + extraspeed + main.bonus_speed[char]
        elif key_type[2]:
            main.char_face[char] = 0
            if main.char_y[char] - 1 <= 0:
                main.char_y[char] = 0
            else:
                main.char_y[char] -= 2 + extraspeed + main.bonus_speed[char]
                main.distance_travelled[char] += 2 + extraspeed + main.bonus_speed[char]
        elif key_type[3]:
            main.char_face[char] = 180
            if main.char_y[char] + 1 >= size[1] - char_height:
                main.char_y[char] = size[1] - char_height
            else:
                main.char_y[char] += 2 + extraspeed + main.bonus_speed[char]
                main.distance_travelled[char] += 2 + extraspeed + main.bonus_speed[char]

def frozen(char):
    if is_frozen[char] == True:
        #Freezes the player for 0.75 seconds
        main.frozen_cooldown_started[char], main.frozen_start_time[char], main.frozen_passed_time[char] = ability_cooldown(main.frozen_cooldown_started[char], main.frozen_start_time[char], main.frozen_passed_time[char])
        if main.frozen_passed_time[char] >= 750:
            main.frozen_passed_time[char] = 0
            main.frozen_cooldown_started[char] = False
            main.is_frozen[char] = False

#Use ability function
def use_ability(char):
    import main

    keys = pygame.key.get_pressed()
    if char == 0: key_type = keys[pygame.K_SPACE]
    elif char == 1: key_type = keys[pygame.K_e]
    t = main.char_ability[char]

    if key_type and main.is_active[char] == False and main.can_use[char] == True and main.char_health[char] > 0:
        main.is_active[char] = True
        main.can_use[char] = False
        main.abilities_used[char] += 1

        #Arrow ability    
        if main.char_ability[char] == 0:
            bow_use.play()
            main.ability_face[t][char] = main.char_face[char]
            if main.ability_face[t][char] == 0 or main.ability_face[t][char] == 180:
                main.ability_width[t][char], main.ability_height[t][char] = 8, 64
                main.ability_x[t][char], main.ability_y[t][char] = main.char_x[char] + (char_width / 2) - main.ability_width[t][char] / 2, main.char_y[char] + (char_height / 2)
            elif main.ability_face[t][char] == 90 or main.ability_face[t][char] == 270:
                main.ability_width[t][char], main.ability_height[t][char] = 64, 8
                main.ability_x[t][char], main.ability_y[t][char] = main.char_x[char] + (char_width / 2), main.char_y[char] + (char_height / 2) - main.ability_height[t][char] / 2

        #Sword ability
        elif main.char_ability[char] == 1:
            sword_use.play()
            main.ability_face[t][char] = main.char_face[char]
            if main.ability_face[t][char] == 0:
                main.ability_width[t][char], main.ability_height[t][char] = 22, 50
                main.ability_x[t][char], main.ability_y[t][char] = main.char_x[char], main.char_y[char] - char_height + 10
            elif main.ability_face[t][char] == 90:
                main.ability_width[t][char], main.ability_height[t][char] = 50, 22
                main.ability_x[t][char], main.ability_y[t][char] = main.char_x[char] - char_width + 10, main.char_y[char]
            elif main.ability_face[t][char] == 180:
                main.ability_width[t][char], main.ability_height[t][char] = 22, 50
                main.ability_x[t][char], main.ability_y[t][char] = main.char_x[char], main.char_y[char] + char_height - 10
            elif main.ability_face[t][char] == 270:
                main.ability_width[t][char], main.ability_height[t][char] = 50, 22
                main.ability_x[t][char], main.ability_y[t][char] = main.char_x[char] + char_width - 10, main.char_y[char]   

        #Mage bolt ability
        elif main.char_ability[char] == 2:
            staff_use.play()
            main.ability_face[t][char] = main.char_face[char]
            main.img_num[char] = random.randrange(0, 3)
            if main.ability_face[t][char] == 0:
                main.ability_x[t][char], main.ability_y[t][char] = main.char_x[char], main.char_y[char] - char_height - 128
            elif main.ability_face[t][char] == 90:
                main.ability_x[t][char], main.ability_y[t][char] = main.char_x[char] - char_width - 128, main.char_y[char]
            elif main.ability_face[t][char] == 180:
                main.ability_x[t][char], main.ability_y[t][char] = main.char_x[char], main.char_y[char] + char_height + 128
            elif main.ability_face[t][char] == 270:
                main.ability_x[t][char], main.ability_y[t][char] = main.char_x[char] + char_width + 128, main.char_y[char]

#Run ability function
def run_ability(char):
    import main

    t = main.char_ability[char]
    #Arrow ability
    if main.char_ability[char] == 0 and main.is_active[char] == True:
        if main.ability_face[t][char] == 0 and main.ability_y[t][char] > -64:
            main.ability_y[t][char] -= 10
        elif main.ability_face[t][char] == 180 and main.ability_y[t][char] < size[1] + 64:
            main.ability_y[t][char] += 10
        elif main.ability_face[t][char] == 270 and main.ability_x[t][char] < size[0] + 64:
            main.ability_x[t][char] += 10
        elif main.ability_face[t][char] == 90 and main.ability_x[t][char] > -64:
            main.ability_x[t][char] -= 10
        else:
            main.is_active[char] = False

    #Sword ability
    if main.char_ability[char] == 1 and main.is_active[char] == True:
        if main.ability_face[t][char] == 0:
            main.ability_width[t][char], main.ability_height[t][char] = 22, 50
            main.ability_x[t][char], main.ability_y[t][char] = main.char_x[char] + main.ability_width[t][char], main.char_y[char] - char_height + 10
        elif main.ability_face[t][char] == 90:
            main.ability_width[t][char], main.ability_height[t][char] = 50, 22
            main.ability_x[t][char], main.ability_y[t][char] = main.char_x[char] - char_width + 10, main.char_y[char] + main.ability_height[t][char]
        elif main.ability_face[t][char] == 180:
            main.ability_width[t][char], main.ability_height[t][char] = 22, 50
            main.ability_x[t][char], main.ability_y[t][char] = main.char_x[char] + main.ability_width[t][char], main.char_y[char] + char_height 
        elif main.ability_face[t][char] == 270:
            main.ability_width[t][char], main.ability_height[t][char] = 50, 22
            main.ability_x[t][char], main.ability_y[t][char] = main.char_x[char] + char_width, main.char_y[char] + main.ability_height[t][char]
        #Makes the sword appear for 0.5 seconds
        main.sword_cooldown_started[char], main.sword_start_time[char], main.sword_passed_time[char] = ability_cooldown(main.sword_cooldown_started[char], main.sword_start_time[char], main.sword_passed_time[char])
        if main.sword_passed_time[char] >= 500:
            main.sword_passed_time[char] = 0
            main.sword_cooldown_started[char] = False
            main.is_active[char] = False
            main.ability_x[t][char], main.ability_y[t][char] = -100, -100
            for i in range(len(main.b_enemy_type)):
                main.b_enemy_hit[char][i] = False

    #Mage bolt ability
    if main.char_ability[char] == 2 and main.is_active[char] == True:
        main.staff_face[char] = main.char_face[char]
        if main.staff_face[char] == 0:
            main.staff_x[char], main.staff_y[char] = main.char_x[char], main.char_y[char] - char_height
        elif main.staff_face[char] == 90:
            main.staff_x[char], main.staff_y[char] = main.char_x[char] - char_width, main.char_y[char]
        elif main.staff_face[char] == 180:
            main.staff_x[char], main.staff_y[char] = main.char_x[char], main.char_y[char] + char_height
        elif staff_face[char] == 270:
            main.staff_x[char], main.staff_y[char] = main.char_x[char] + char_width, main.char_y[char]
        #Makes the bolt disapear after 0.5 second
        main.bolt_cooldown_started[char], main.bolt_start_time[char], main.bolt_passes_time[char] = ability_cooldown(main.bolt_cooldown_started[char], main.bolt_start_time[char], main.bolt_passes_time[char])
        if main.bolt_passes_time[char] >= 500:
            main.bolt_passes_time[char] = 0
            main.bolt_cooldown_started[char] = False
            main.is_active[char] = False
            main.ability_x[t][char], main.ability_y[t][char] = -100, -100
            main.staff_x[char], main.staff_y[char] = -100, -100
            for i in range(len(main.b_enemy_type)):
                main.b_enemy_hit[char][i] = False

    #Starts the cooldown after ability is done
    if main.is_active[char] == False and main.can_use[char] == False and main.ability_collision_occured[char] == False:
        main.ability_cooldown_started[char], main.ability_start_time[char], main.ability_passed_time[char] = ability_cooldown(main.ability_cooldown_started[char], main.ability_start_time[char], main.ability_passed_time[char])
        if main.ability_passed_time[char] >= 1000 - main.bonus_cooldown[char]:
            main.ability_passed_time[char] = 0
            main.ability_cooldown_started[char] = False
            main.can_use[char] = True

#Starts a cooldown
def ability_cooldown(cooldown_started, start_time, passed_time):
    if cooldown_started == False:
        cooldown_started = True
        start_time = pygame.time.get_ticks()
    if cooldown_started == True:
        passed_time = pygame.time.get_ticks() - start_time
    return cooldown_started, start_time, passed_time

#Run spike ball function
def enemy_shoot_spike_ball(): 
    import main
    
    #Enemy shoots the spike ball 
    if main.ball_ammo > 0 and main.ball_is_active == False and main.ball_can_shoot == True and main.is_alive[4] == True:
        main.ball_ammo -= 1
        main.enemy_ball_face = main.enemy_face[4]
        main.enemy_ball_x, main.enemy_ball_y = main.enemy_x[4], main.enemy_y[4]
        main.ball_is_active = True
        main.ball_can_shoot = False
    #Spike ball flies through the air
    if main.ball_is_active == True:
        if main.enemy_ball_face == 0 and main.enemy_ball_y > -main.enemy_ball_height * 3:
            main.enemy_ball_y -= 3
            main.enemy_ball_x += 5 * math.sin(0.1 * main.enemy_ball_y)
        elif main.enemy_ball_face == 270 and main.enemy_ball_x < size[0] + main.enemy_ball_width * 3:
            main.enemy_ball_x += 3
            main.enemy_ball_y += (5 * math.sin(0.1 * enemy_ball_x))
        elif main.enemy_ball_face == 180 and main.enemy_ball_y < size[1] + main.enemy_ball_height * 3:
            main.enemy_ball_y += 3
            main.enemy_ball_x += 5 * math.sin(0.1 * enemy_ball_y)
        elif main.enemy_ball_face == 90 and main.enemy_ball_x > -main.enemy_ball_width * 3:
            main.enemy_ball_x -= 3
            main.enemy_ball_y += (5 * math.sin(0.1 * main.enemy_ball_x))
        else:
            main.ball_is_active = False
            main.ball_ammo += 1
    elif main.is_alive[4] == True:
        main.ball_cooldown_started, main.ball_start_time, main.ball_passed_time = ability_cooldown(main.ball_cooldown_started, main.ball_start_time, main.ball_passed_time)
        if main.ball_passed_time >= 2000:
            main.ball_passed_time = 0
            main.ball_cooldown_started = False
            main.ball_can_shoot = True

#Run shoot explosion function
def enemy_shoot_explosion():
    import main

    #Shoot the exlosion
    if main.explosion_ammo > 0 and main.explosion_is_active == False and main.explosion_can_shoot == True and main.is_alive[3] == True:
        main.can_take_damage = False
        main.explosion_ammo -= 1
        main.explosion_x, main.explosion_y = find_closest_char(main.enemy_x[3], main.enemy_y[3])
        main.explosion_is_active = True
    #Explosion countdown
    if main.explosion_is_active == True and main.is_alive[3] == True:
        if main.explosion_color[0] > 82 and main.explosion_color[1] > 72 and main.explosion_color[2] > 0:
            main.explosion_color[0] -= 0.67
            main.explosion_color[1] -= 0.71
            main.explosion_color[2] -= 1
        else:
            main.explosion_ammo += 1
            main.explosion_color = [255, 255, 255]
            main.can_take_damage = True
            main.explosion_is_active = False
            main.explosion_can_shoot = False
    elif main.is_alive[3] == True:
        main.explosion_cooldown_started, main.explosion_start_time, main.explosion_passed_time = ability_cooldown(main.explosion_cooldown_started, main.explosion_start_time, main.explosion_passed_time)
        if main.explosion_passed_time >= 1000:
            main.explosion_passed_time = 0
            main.explosion_cooldown_started = False
            main.explosion_can_shoot = True
    else:
        main.explosion_x, main.explosion_y = -100, -100

#Run the invisible function
def enemy_invisible():
    import main
    if main.is_alive[6] == True:
        enemy_img[6].set_alpha(main.invisible_value)
        if main.invisible_value == 0:
            main.is_invisible = True
            main.invisible_cooldown_started, main.invisible_start_time, main.invisible_passed_time = ability_cooldown(main.invisible_cooldown_started, main.invisible_start_time, main.invisible_passed_time)
            if main.invisible_passed_time >= 3000:
                main.decrease = False
                main.invisible_passed_time = 0
                main.invisible_cooldown_started = False
                main.is_invisible = False
        elif main.invisible_value >= 255:
            main.decrease = True
        if main.is_invisible == False:
            if main.decrease == True and main.invisible_value >= 1:
                main.invisible_value -= 1
            elif main.decrease == False and main.invisible_value <= 255:
                main.invisible_value += 1

#Run spike ball function
def enemy_shoot_icicle(): 
    import main
    #Enemy shoots the spike ball 
    if main.icicle_ammo > 0 and main.icicle_is_active == False and main.icicle_can_shoot == True and main.is_alive[2] == True:
        main.icicle_ammo -= 1
        main.icicle_face = main.enemy_face[2]
        main.icicle_x, main.icicle_y = main.enemy_x[2] + main.enemy_width[2] / 4, main.enemy_y[2] + main.enemy_height[2] / 4
        main.icicle_is_active = True
        main.icicle_can_shoot = False
    #Spike ball flies through the air
    if main.icicle_is_active == True:
        if main.icicle_face == 0 and main.icicle_y > -main.icicle_height * 2:
            main.icicle_width, main.icicle_height = 32, 64
            main.icicle_y -= 10
        elif main.icicle_face == 270 and main.icicle_x < size[0] + main.icicle_width * 2:
            main.icicle_width, main.icicle_height = 64, 32
            main.icicle_x += 10
        elif main.icicle_face == 180 and main.icicle_y < size[1] + main.icicle_height * 2:
            main.icicle_width, main.icicle_height = 32, 64
            main.icicle_y += 10
        elif main.icicle_face == 90 and main.icicle_x > -main.icicle_width * 2:
            main.icicle_width, main.icicle_height = 64, 32
            main.icicle_x -= 10
        else:
            main.icicle_is_active = False
            main.icicle_ammo += 1
    elif main.is_alive[2] == True:
        main.icicle_cooldown_started, main.icicle_start_time, main.icicle_passed_time = ability_cooldown(main.icicle_cooldown_started, main.icicle_start_time, main.icicle_passed_time)
        if main.icicle_passed_time >= 2000:
            main.icicle_passed_time = 0
            main.icicle_cooldown_started = False
            main.icicle_can_shoot = True

#Run for pirate to shoot cannon ball
def pirate_shoot_shot():
    import main
    #Pirate shoots the cannon ball
    if main.pirate_shot_ammo > 0 and main.pirate_shot_is_active == False and main.pirate_shot_can_shoot == True and main.is_alive[11] == True:
        main.pirate_shot_ammo -= 1
        main.pirate_shot_face = main.enemy_face[11]
        main.pirate_shot_x, main.pirate_shot_y = main.enemy_x[11] + 24, main.enemy_y[11] + 24
        main.pirate_shot_is_active = True
        main.pirate_shot_can_shoot = False
        main.pirate_enemy_shot = True
    #Pirate cannon ball in air
    if main.pirate_shot_is_active == True:
        if main.pirate_shot_face == 0 and main.pirate_shot_y > -main.pirate_shot_height:
            main.pirate_shot_y -= 2.5
        elif main.pirate_shot_face == 270 and main.pirate_shot_x < size[0] + main.pirate_shot_width:
            main.pirate_shot_x += 2.5
        elif main.pirate_shot_face == 180 and main.pirate_shot_y < size[1] + main.pirate_shot_height:
            main.pirate_shot_y += 2.5
        elif main.pirate_shot_face == 90 and main.pirate_shot_x > -main.pirate_shot_width:
            main.pirate_shot_x -= 2.5
        else:
            main.pirate_shot_is_active = False
            main.pirate_shot_ammo += 1
            main.b_enemy_hit[0][3] = False
            main.b_enemy_hit[1][3] = False
    elif main.is_alive[11] == True:
        main.pirate_shot_cooldown_started, main.pirate_shot_start_time, main.pirate_shot_passed_time = ability_cooldown(main.pirate_shot_cooldown_started, main.pirate_shot_start_time, main.pirate_shot_passed_time)
        if main.pirate_shot_passed_time >= 4000:
            main.pirate_shot_passed_time = 0
            main.pirate_shot_cooldown_started = False
            main.pirate_shot_can_shoot = True 

#Changes the enemy stats when hit
def enemy_change_size():
    import main

    main.enemy_width[10], main.enemy_height[10] = 16 + (16 * main.b_enemy_health[2]), 16 + (16 * main.b_enemy_health[2])
    main.enemy_speed[10] = 0.75 + (3 - main.b_enemy_health[2]) * 0.35 

#Find closest character
def find_closest_char(enemy_x, enemy_y):
    if multiplayer:
        if (abs(enemy_x - char_x[0]) ** 2 + abs(enemy_y - char_y[0]) ** 2) < (abs(enemy_x - char_x[1]) ** 2 + abs(enemy_y - char_y[1]) ** 2):
            closest_char = [char_x[0], char_y[0]]
        else:
            closest_char = [char_x[1], char_y[1]]
    else:
        closest_char = [char_x[0], char_y[0]]
    return closest_char

#Run function to move enemy
def move_enemy(enemy_type):
    import main
    closest_char = find_closest_char(enemy_x[enemy_type], enemy_y[enemy_type])
    if (main.enemy_x[enemy_type] + main.enemy_width[enemy_type] / 2) - (closest_char[0] + char_width / 2) == 0:
        slope = 0.01
    else:
        slope = abs(((main.enemy_y[enemy_type] + main.enemy_height[enemy_type] / 2) - (closest_char[1] + char_height / 2)) / ((main.enemy_x[enemy_type] + main.enemy_width[enemy_type] / 2) - (closest_char[0] + char_width / 2)))
    if slope < 1:
        if (main.enemy_x[enemy_type] + main.enemy_width[enemy_type] / 2) - (closest_char[0] + char_width / 2) > 0:
            main.enemy_x[enemy_type] -= main.enemy_speed[enemy_type]
            main.enemy_face[enemy_type] = 90
        elif (main.enemy_x[enemy_type] + main.enemy_width[enemy_type] / 2) - (closest_char[0] + char_width / 2) < 0:
            main.enemy_x[enemy_type] += main.enemy_speed[enemy_type]
            main.enemy_face[enemy_type] = 270
        if (main.enemy_y[enemy_type] + main.enemy_height[enemy_type] / 2) - (closest_char[1] + char_height / 2) > 0:
            main.enemy_y[enemy_type] -= slope * main.enemy_speed[enemy_type]
        elif (main.enemy_y[enemy_type] + main.enemy_height[enemy_type] / 2) - (closest_char[1] + char_height / 2) < 0:
            main.enemy_y[enemy_type] += slope * main.enemy_speed[enemy_type]
    else:
        if (main.enemy_y[enemy_type] + main.enemy_y[enemy_type] / 2) - (closest_char[1] + char_height / 2) == 0:
            slope = 0.01
        else:
            slope = abs(((enemy_x[enemy_type] + enemy_width[enemy_type] / 2) - (closest_char[0] + char_width / 2)) / ((enemy_y[enemy_type] + enemy_height[enemy_type] / 2) - (closest_char[1] + char_height / 2)))             
        if (main.enemy_x[enemy_type] + main.enemy_width[enemy_type] / 2) - (closest_char[0] + char_width / 2) > 0:
            main.enemy_x[enemy_type] -= slope * main.enemy_speed[enemy_type]
        elif (main.enemy_x[enemy_type] + main.enemy_width[enemy_type] / 2) - (closest_char[0] + char_width / 2) < 0:
            main.enemy_x[enemy_type] += slope * main.enemy_speed[enemy_type]
        if (main.enemy_y[enemy_type] + main.enemy_height[enemy_type] / 2) - (closest_char[1] + char_height / 2) > 0:
            main.enemy_y[enemy_type] -= main.enemy_speed[enemy_type]
            main.enemy_face[enemy_type] = 0
        elif (main.enemy_y[enemy_type] + main.enemy_height[enemy_type] / 2) - (closest_char[1] + char_height / 2) < 0:
            main.enemy_y[enemy_type] += main.enemy_speed[enemy_type]
            main.enemy_face[enemy_type] = 180

#Resets the enemy position on death
def set_enemy_position(enemy_type):
    import main
    if main.is_alive[enemy_type] == False:
        main.enemy_x[enemy_type], main.enemy_y[enemy_type] = 100000, 100000

#Finds whichever side the player is closest to
def find_player_side(char):
    import main

    currentside = [main.char_y[char], main.char_x[char], main.size[1] - main.char_y[char], main.size[0] - main.char_x[char]]
    currentside.sort()
    if currentside[0] == main.char_y[char]:
        main.char_side[char] = 0
    elif currentside[0] == main.char_x[char]:
        main.char_side[char] = 1
    elif currentside[0] == main.size[1] - main.char_y[char]:
        main.char_side[char] = 2
    elif currentside[0] == main.size[0] - main.char_x[char]:
        main.char_side[char] = 3

#Figures out when and where to spawn an enemy
def spawn_enemy(enemy_type):
    import main

    if main.is_alive[enemy_type] == False and (main.gametime >= main.time_to_spawn[enemy_type]):
        if enemy_type == 7:
            main.b_enemy_health[0] = 4
        elif enemy_type == 8:
            main.b_enemy_health[1] = main.gold_max_health
        elif enemy_type == 10:
            main.b_enemy_health[2] = 3
        elif enemy_type == 11:
            main.b_enemy_health[3] = 2
        if enemy_type == 9:
            pink_skin = round(random.randrange(0, 2))
            main.enemy_img[enemy_type] = main.pink_enemy_img[pink_skin]
        main.is_alive[enemy_type] = True

        #Prevents enemies from spawning on same side as players
        while True:
            chooseside = round(random.randrange(0, 4))
            if (multiplayer == False and chooseside != main.char_side[0]) or (multiplayer == True and chooseside != main.char_side[0] and chooseside != main.char_side[1]):
                if chooseside == 0:
                    main.enemy_x[enemy_type], main.enemy_y[enemy_type] = random.randrange(enemy_width[enemy_type], size[0] - enemy_width[enemy_type]), 0
                elif chooseside == 1:
                    main.enemy_x[enemy_type], main.enemy_y[enemy_type] = 0, random.randrange(enemy_height[enemy_type], size[1] - enemy_height[enemy_type])
                elif chooseside == 2:
                    main.enemy_x[enemy_type], main.enemy_y[enemy_type] = random.randrange(enemy_width[enemy_type], size[0] - enemy_width[enemy_type]), size[1] - enemy_height[enemy_type]
                elif chooseside == 3:
                    main.enemy_x[enemy_type], main.enemy_y[enemy_type] = size[0] - enemy_width[enemy_type], random.randrange(enemy_height[enemy_type], size[1] - enemy_height[enemy_type])
                break

#Spawns powerups
def spawn_powerup(powerup_type):
    if main.is_powerup_active == False and main.powerup_time_to_spawn <= main.gametime:
        main.is_powerup_active = True
        powerup_type_rand = random.randrange(0, 3)
        main.powerup_x[powerup_type_rand], main.powerup_y[powerup_type_rand] = random.randrange(96, size[0] - 96), random.randrange(96, size[1] - 96)

#Gives player extra speed powerup
def speed(char):
    import main
    if main.has_bonus_speed[char] == True:
        #Gives player bonus speed for 10 seconds
        main.bonus_speed[char] = 1
        main.speed_cooldown_started[char], main.speed_start_time[char], main.speed_passed_time[char] = ability_cooldown(main.speed_cooldown_started[char], main.speed_start_time[char], main.speed_passed_time[char])
        if main.speed_passed_time[char] >= 10000:
            main.speed_passed_time[char] = 0
            main.speed_cooldown_started[char] = False
            main.has_bonus_speed[char] = False
    else:
        main.bonus_speed[char] = 0

#Gives player shorter cooldowns powerup
def cooldown(char):
    import main
    if main.has_bonus_cooldown[char] == True:
        #Gives player bonus cooldown reduction for 10 seconds
        main.bonus_cooldown[char] = 500
        main.cooldown_cooldown_started[char], main.cooldown_start_time[char], main.cooldown_passed_time[char] = ability_cooldown(main.cooldown_cooldown_started[char], main.cooldown_start_time[char], main.cooldown_passed_time[char])
        if main.cooldown_passed_time[char] >= 10000:
            main.cooldown_passed_time[char] = 0
            main.cooldown_cooldown_started[char] = False
            main.has_bonus_cooldown[char] = False
    else:
        main.bonus_cooldown[char] = 0

#Gives points to player when enemy killed
def give_points(char, enemy_type):
    import main

    main.player_score[char] += enemy_points[enemy_type]
    main.enemies_killed[char] += 1
    main.enemy_amount_killed[enemy_type] += 1

#What happens when a boss enemy dies
def boss_collision_sorting(char, enemy_type, b_enemy_type):
    import main

    #Checks if the boss is dead
    if main.b_enemy_health[b_enemy_type] == 1 and main.b_enemy_hit[char][b_enemy_type] == False:
        if b_enemy_type == 1:
            main.gold_max_health += 1
            main.b_enemy_health[1] = main.gold_max_health
        elif b_enemy_type == 2:
            main.b_enemy_health[2] = 3
        elif b_enemy_type == 3:
            main.b_enemy_health[3] = 2
        else:
            main.b_enemy_health[b_enemy_type] = 4
        enemy_hit.play()
        main.is_alive[enemy_type] = False
        give_points(char, enemy_type)
    elif main.b_enemy_hit[char][b_enemy_type] == False:
        if b_enemy_type == 2:
            main.enemy_x[enemy_type] += 8
            main.enemy_y[enemy_type] += 8
        if main.char_ability[char] != 0:
            main.b_enemy_hit[char][b_enemy_type] = True
        enemy_hit.play()
        main.b_enemy_health[b_enemy_type] -= 1

#What happens when an enemy dies
def collision_sorting(char, enemy_type):
    import main    
    
    if enemy_type == 7: 
        boss_collision_sorting(char, enemy_type, main.b_enemy_type[0])
    elif enemy_type == 8:
        boss_collision_sorting(char, enemy_type, main.b_enemy_type[1])
    elif enemy_type == 10:
        boss_collision_sorting(char, enemy_type, main.b_enemy_type[2])
    elif enemy_type == 11:
        boss_collision_sorting(char, enemy_type, main.b_enemy_type[3])
    if enemy_type != 7 and enemy_type != 8 and enemy_type != 10 and enemy_type != 11:
        if enemy_type == 6:
            main.invisible_value = 255
            main.invisible_cooldown_started = False
            main.is_invisible = False
        enemy_hit.play()
        main.is_alive[enemy_type] = False
        give_points(char, enemy_type)
    if main.is_alive[enemy_type] == False:
        main.time_to_spawn[enemy_type] = main.gametime + main.respawn_timer[enemy_type] + random.randrange(0, 5)
        
#Run function to detect collision between enemy and player
def enemy_player_collision(char, enemy_type):
    import main

    for enemy_xpos in range(int(main.enemy_x[enemy_type]), int(main.enemy_x[enemy_type] + main.enemy_width[enemy_type])):
        if char_x[char] + char_width >= enemy_xpos >= char_x[char]:
            for enemy_ypos in range(int(main.enemy_y[enemy_type]), int(main.enemy_y[enemy_type] + main.enemy_height[enemy_type])):
                if main.char_y[char] + char_height >= enemy_ypos >= main.char_y[char]:
                    main.is_alive[enemy_type] = False
                    player_hit.play()
                    main.char_health[char] -= 1
                    if main.char_health[char] <= 0:
                        main.char_x[char], main.char_y[char] = -100000, -100000
                    break
            break

#Run function to detect collision between player and ball
def player_ball_collision(char):
    import main

    for ballxpos in range(int(main.enemy_ball_x + 18), int(main.enemy_ball_x + 48)):
        if main.char_x[char] + main.char_width >= ballxpos >= main.char_x[char]:
            for ballypos in range(int(main.enemy_ball_y + 18), int(main.enemy_ball_y + 48)):
                if main.char_y[char] + main.char_height >= ballypos >= main.char_y[char]:
                    player_hit.play()
                    main.enemy_ball_x, main.enemy_ball_y = 100000, 100000 
                    main.ball_is_active = False
                    main.ball_ammo += 1
                    main.char_health[char] -= 1
                    if main.char_health[char] <= 0:
                        main.char_x[char], main.char_y[char] = -100000, -100000
                    break
            break

#Run function to detect collision between player and icicle
def player_icicle_collision(char):
    import main

    for ballxpos in range(int(main.icicle_x), int(main.icicle_x + main.icicle_width)):
        if main.char_x[char] + main.char_width >= ballxpos >= main.char_x[char]:
            for ballypos in range(int(main.icicle_y), int(main.icicle_y + main.icicle_height)):
                if main.char_y[char] + main.char_height >= ballypos >= main.char_y[char]:
                    ice_effect.play()
                    main.icicle_x, main.icicle_y = 100000, 100000 
                    main.icicle_is_active = False
                    main.icicle_ammo += 1
                    main.is_frozen[char] = True
            break

#Run function to detect collision between explosion and player
def explosion_player_collision(char):
    import main
    for enemy_xpos in range(int(main.explosion_x), int(main.explosion_x + main.explosion_radius)):
        if main.char_x[char] + main.char_width >= enemy_xpos >= main.char_x[char]:
            for enemy_ypos in range(int(main.explosion_y), int(main.explosion_y + main.explosion_radius)):
                if main.char_y[char] + main.char_height >= enemy_ypos >= main.char_y[char]:
                    player_hit.play()
                    main.char_health[char] -= 1
                    if main.char_health[char] <= 0:
                        main.char_x[char], main.char_y[char] = -100000, -100000
                    break
            break

#Run function to detect collision between player and pirate shot
def player_pirate_shot_collision(char):
    import main

    for shotxpos in range(int(main.pirate_shot_x), int(main.pirate_shot_x + main.pirate_shot_width)):
        if main.char_x[char] + main.char_width >= shotxpos >= main.char_x[char]:
            for shotypos in range(int(main.pirate_shot_y), int(main.pirate_shot_y + main.pirate_shot_height)):
                if main.char_y[char] + main.char_height >= shotypos >= main.char_y[char]:
                    player_hit.play()
                    main.pirate_shot_x, main.pirate_shot_y = 100000, 100000
                    main.pirate_shot_is_active = False
                    main.pirate_shot_ammo += 1
                    main.char_health[char] -= 1
                    if main.char_health[char] <= 0:
                        main.char_x[char], main.char_y[char] = -100000, -100000
                    break
            break

#Run function to detect collision between pirate and abilities
def pirate_ability_collision(char, enemy_type, t):
    import main

    #Allows players to attack cannon ball when it is first shot
    if enemy_type == 11 and main.pirate_enemy_shot == True and main.pirate_shot_is_active == True:
        for pirate_shot_pos_x in range(int(main.pirate_shot_x), int(main.pirate_shot_x + main.pirate_shot_width)):
            if main.ability_x[t][char] + main.ability_width[t][char] >= pirate_shot_pos_x >= main.ability_x[t][char]:
                for pirate_shot_pos_y in range(int(main.pirate_shot_y), int(main.pirate_shot_y + main.pirate_shot_height)):
                    if main.ability_y[t][char] + main.ability_height[t][char] >= pirate_shot_pos_y >= main.ability_y[t][char]:
                        enemy_hit.play()
                        main.pirate_enemy_shot = False
                        main.pirate_shot_face = main.ability_face[t][char]
                        if t == 0:
                            main.ability_collision_occured[char] = True
                            main.ability_x[t][char], main.ability_y[t][char] = -100000, -100000 
                            main.is_active[char] = False
                        break
                break

    #Collision between the cannon ball and pirate after it has been hit by player
    elif enemy_type == 11 and main.pirate_enemy_shot == False and main.pirate_shot_is_active == True:
        for pirate_pos_x in range(int(main.enemy_x[11]), int(main.enemy_x[11] + main.enemy_width[11])):
            if main.pirate_shot_x + main.pirate_shot_width >= pirate_pos_x >= main.pirate_shot_x:
                for pirate_pos_y in range(int(main.enemy_y[11]), int(main.enemy_y[11] + main.enemy_height[11])):
                    if main.pirate_shot_y + main.pirate_shot_height >= pirate_pos_y >= main.pirate_shot_y:
                        collision_sorting(char, enemy_type)
                        main.pirate_shot_x, main.pirate_shot_y = 100000, 100000
                        main.pirate_shot_is_active = False
                        main.pirate_shot_ammo += 1
                        break
                break

#Run function to detect collision between enemy and ability
def enemy_ability_collision(char, enemy_type, t):
    import main

    #Abilities and enemies
    if enemy_type != 11:
        for enemy_xpos in range(int(main.enemy_x[enemy_type]), int(main.enemy_x[enemy_type] + main.enemy_width[enemy_type])):
          if main.ability_x[t][char] + main.ability_width[t][char] >= enemy_xpos >= main.ability_x[t][char]:
                for enemy_ypos in range(int(main.enemy_y[enemy_type]), int(main.enemy_y[enemy_type] + main.enemy_height[enemy_type])):
                    if main.ability_y[t][char] + main.ability_height[t][char] >= enemy_ypos >= main.ability_y[t][char]:
                        collision_sorting(char, enemy_type)
                        if t == 0:
                            main.ability_collision_occured[char] = True
                            main.ability_x[t][char], main.ability_y[t][char] = -100000, -100000 
                            main.is_active[char] = False
                        break
                break

    if t == 0 and main.ability_collision_occured[char] == True:
        main.ability_cooldown_started[char], main.ability_start_time[char], main.ability_passed_time[char] = ability_cooldown(main.ability_cooldown_started[char], main.ability_start_time[char], main.ability_passed_time[char])
        if main.ability_passed_time[char] >= 1000 - main.bonus_cooldown[char]:
            main.ability_passed_time[char] = 0
            main.ability_cooldown_started[char] = False
            main.ability_collision_occured[char] = False
            main.can_use[char] = True

#Run function to detect collision between explosion and player
def powerup_player_collision(char, powerup_type):
    import main
    for powerup_xpos in range(int(main.powerup_x[powerup_type]), int(main.powerup_x[powerup_type] + main.powerup_width)):
        if main.char_x[char] + main.char_width >= powerup_xpos >= main.char_x[char]:
            for powerup_ypos in range(int(main.powerup_y[powerup_type]), int(main.powerup_y[powerup_type] + main.powerup_width)):
                if main.char_y[char] + main.char_height >= powerup_ypos >= main.char_y[char]:
                    if powerup_type == 0:
                        heal_powerup.play()
                        if main.char_health[char] < 3:
                            main.char_health[char] += 1
                    elif powerup_type == 1:
                        speed_powerup.play()
                        main.has_bonus_speed[char] = True
                    elif powerup_type == 2:
                        cooldown_powerup.play()
                        main.has_bonus_cooldown[char] = True
                    main.powerup_x[powerup_type], main.powerup_y[powerup_type] = -100, -100
                    main.is_powerup_active = False
                    main.powerup_time_to_spawn = main.gametime + main.powerup_respawn_timer
                    break
            break

#Run function to reset menu variables when using a button to take you back to main menu
def reset_menu():
    import main
    import playMenu

    main.player_count, main.char_ability, main.char_x, main.char_y, main.ability_x, main.ability_y, main.staff_x, main.staff_y = 0, [-1, -1], [size[0] / 2, size[0] / 2 + 100], [size[1] / 2, size[1] / 2], [[-100, -100], [-100, -100], [-100, -100]], [[-100, -100], [-100, -100], [-100, -100]], [-100, -100], [-100, -100]
    main.enemy_x, main.enemy_y, main.is_alive = [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100], [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100], [False, False, False, False, False, False, False, False, False, False, False, False]
    main.time_to_spawn = [0, 20, 40, 60, 80, 100, 120, 140, 180, 200, 220, 240]
    main.b_enemy_health, main.gold_enemy, main.gold_max_health = [4, 1, 3, 2], 1, 1
    main.char_health = [3, 3]
    main.char_face = [0, 0]
    main.enemy_ball_x, main.enemy_ball_y, main.explosion_x, main.explosion_y, main.ball_is_active, main.ball_ammo, main.explosion_ammo, main.explosion_is_active, main.can_take_damage, main.explosion_color = -100, -100, -100, -100, False, 1, 1, False, False, [255, 255, 255]
    main.pirate_shot_x, main.pirate_shot_y, main. pirate_shot_is_active, main.pirate_shot_ammo, main.pirate_enemy_shot = -100, -100, False, 1, True
    main.icicle_ammo, main.icicle_is_active, main.icicle_can_shoot, main.icicle_cooldown_started, main.icicle_start_time, main.icicle_passed_time, main.is_frozen, main.frozen_cooldown_started, main.frozen_start_time, main.frozen_passed_time, main.icicle_x, main.icicle_y = 1, False, True, False, 0, 0, [False, False], [False, False], [0, 0], [0, 0], -100, -100
    playMenu.selected = [0, 0]
    main.ability_collision_occured, main.sword_cooldown_started, main.sword_start_time, main.sword_passed_time, main.bolt_cooldown_started, main.bolt_start_time, main.bolt_passes_time = [False, False], [False, False], [0, 0], [0, 0], [False, False], [0, 0], [0, 0]
    main.ability_passed_time, main.ability_cooldown_started, main.ability_start_time, main.is_active, main.can_use = [0, 0], [False, False], [0, 0], [False, False], [True, True]
    main.player_score, main.enemies_killed, main.abilities_used, main.time_played, main.distance_travelled = [0, 0], [0, 0], [0, 0], 0, [0, 0]
    main.unpause_time = 0
    main.button_cooldown_started, main.button_start_time, main.button_passed_time, main.is_button_pressed = False, 0, 0, False
    main.enemy_end_screen_type, main.enemy_amount_killed = 0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    main.has_saved, main.user_name, main.text_box_active, main.text1_transparency_value,  main.text2_transparency_value, main.text3_transparency_value = False, "", False, 0, 0, 0
    main.powerup_x, main.powerup_y, main.powerup_time_to_spawn, main.is_powerup_active, main.has_bonus_speed, main.has_bonus_cooldown = [-100, -100, -100], [-100, -100, -100], 30, False, [False, False], [False, False]
    main.speed_cooldown_started, main.speed_start_time, main.speed_passed_time = [False, False], [0, 0], [0, 0]
    main.cooldown_cooldown_started, main.cooldown_start_time, main.cooldown_passed_time = [False, False], [0, 0], [0, 0]

#Main game loop
rungame = True
while rungame:
    import main

    if window != 7:
        pygame.time.delay(10)
    else:
        pygame.time.delay(0)
    
    #Close game when quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False

    if window != 4 and window != 5:
        gamestart = pygame.time.get_ticks()

    #Main menu
    if window == 0:
        menu()

    #Control menu
    elif window == 1:
        controls()

    #Instruction menu
    elif window == 2:
        instructions()

    #Character select menu
    elif window == 3:
        char_selection()

    #Main game
    elif window == 4:
        gametime = round((pygame.time.get_ticks() - gamestart - unpause_time) / 1000, 2)

        #Drawing characters
        move_char(char[0])
        if multiplayer == True:
            move_char(char[1])

        #Finds out how long the player is frozen for
        frozen(char[0])
        if multiplayer == True:
            frozen(char[1])

        #Drawing abilities
        for i in range(0, 3):
            if char_ability[0] == i:
                use_ability(char[0])
                run_ability(char[0])
            if multiplayer == True and char_ability[1] == i:
                use_ability(char[1])
                run_ability(char[1])

        #Finds the side the player is on
        find_player_side(char[0])
        if multiplayer == True:
            find_player_side(char[1])

        #Spawning enemies
        for i in range(len(enemy_type)):
            set_enemy_position(enemy_type[i])
            spawn_enemy(enemy_type[i])

        #Drawing Enemies
        for i in range(len(enemy_type)):
            move_enemy(enemy_type[i])

        #Drawing enemy spike ball
        enemy_shoot_spike_ball()

        #Drawing the explosion
        enemy_shoot_explosion()

        #Sets the invisible value for the invisible enemy
        enemy_invisible()

        #Draws icicle
        enemy_shoot_icicle()

        #Changes size
        enemy_change_size()

        #Drawing pirate shot
        pirate_shoot_shot()

        #Spawning powerups
        for i in range(len(powerup_type)):
            spawn_powerup(powerup_type[i])

        #Applies powerup effects
        speed(char[0])
        cooldown(char[0])
        if multiplayer == True:
            speed(char[1])
            cooldown(char[1])
        
        #Enemy collision with player
        for i in range(len(enemy_type)):
            enemy_player_collision(char[0], enemy_type[i])  
            if multiplayer:
                enemy_player_collision(char[1], enemy_type[i])  
            
        #Enemy spike ball collision with player
        player_ball_collision(char[0])
        if multiplayer:
            player_ball_collision(char[1])

        #Explosion collision with player
        if can_take_damage == True:
            explosion_player_collision(char[0])
            if multiplayer == True:
                explosion_player_collision(char[1])
            main.explosion_x, main.explosion_y = -100, -100

        #Enemy pirate shot collision with player
        player_pirate_shot_collision(char[0])
        if multiplayer:
            player_pirate_shot_collision(char[1])

        #Enemy icicle collision with player
        player_icicle_collision(char[0])
        if multiplayer:
            player_icicle_collision(char[1])

        #Ability collision with enemies
        for i in range(len(enemy_type)):
            enemy_ability_collision(char[0], enemy_type[i], main.char_ability[char[0]])
            if multiplayer == True:
                enemy_ability_collision(char[1], enemy_type[i], main.char_ability[char[1]]) 

        #Ability collision with pirate
        pirate_ability_collision(char[0], enemy_type[11], main.char_ability[char[0]])
        if multiplayer == True:
            pirate_ability_collision(char[1], enemy_type[i], main.char_ability[char[1]]) 

        #Powerup collision with player
        for i in range(len(powerup_type)):
            powerup_player_collision(char[0], powerup_type[i])
            if multiplayer == True:
                powerup_player_collision(char[1], powerup_type[i])

        #Ends game when players lose all health
        if (multiplayer == False and char_health[0] <= 0) or (multiplayer == True and char_health[0] <= 0 and char_health[1] <= 0):
            window = 6

        #Draw all the changes
        draw_screen()

    #Pause window
    elif window == 5:
        main.unpause_time = pygame.time.get_ticks() - main.gamestart - main.gametime * 1000
        pause()

    #End screen
    elif window == 6:
        end_menu()

    elif window == 7:
        scoreboard_menu()

    pygame.display.update()
    
pygame.quit()