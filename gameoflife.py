import pygame
import time
import sys
import random
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
pygame.display.set_caption('Game of life')

delay = 200
press_down = False
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (179, 0, 71)
GREY = (30, 30, 30)
MARINE1 = (17, 30, 108)
MAR1_LIGHT = (70, 130, 180)
MARINE2 = (14, 77, 146)
MAR2_LIGHT = (67, 160, 211)
MARINE3 = (0, 142, 204)
MAR3_LIGHT = (115, 194, 251)
MARINE4 = (24, 80, 120)
MAR4_LIGHT = (0, 100, 150)
A1 = (17, 30, 108)
A2 = (14, 77, 146)
A3 = (0, 142, 204)
A4 = (17, 30, 108)
A5 = (14, 77, 146)
A6 = (0, 142, 204)
A11 = (17, 30, 108)
A22 = (14, 77, 146)
A33 = (0, 142, 204)
A44 = (17, 30, 108)
A55 = (14, 77, 146)
A66 = (0, 142, 204)

cell_size = 20
cells_x = int(screen_width / cell_size)
cells_y = int(screen_height / cell_size)
dead = 0
alive = 1

num_alive = []
num_dead = []

clock = pygame.time.Clock()
image_surf = pygame.image.load('images/fon800600.jpg')


def draw_rect(color_rect, rect_x, rect_y, width, height):
    pygame.draw.rect(screen, color_rect, Rect(rect_x, rect_y, width, height))


def print_text(text, color_text, size_text, center_x, center_y, font):
    font = pygame.font.Font(font, size_text)
    text = font.render(text, True, color_text)
    text_rect = text.get_rect()
    text_rect.center = (center_x, center_y)
    screen.blit(text, text_rect)


def button(light_color, color_button, button_x, button_y, button_width, button_height, text_in_button, size_text,
           color_text):
    global press_down, num_alive, num_dead, delay
    game_field = [dead] * cells_x
    for i in range(cells_x):
        game_field[i] = [dead] * cells_y
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if button_x + button_width > cur[0] > button_x and button_y + button_height > cur[1] > button_y:
        draw_rect(light_color, button_x, button_y, button_width, button_height)
        if click[0] == 1:
            if text_in_button == "Pause":
                draw_rect(WHITE, 0, 0, screen_width, 40)
                print_text("P A U S E D", MARINE2, 40, screen_width // 2 + 20, 20, "fonts//LemonMilk.otf")
                print_text("Press C to continue", BLACK, 30, 150, 20, None)
                print_text("Press Q to start new", BLACK, 30, 690, 20, None)
                pygame.display.update()
                pause()
            if text_in_button == "Clear":
                game_field = clear2(game_field)
                game_loop(game_field)
            if text_in_button == "Draw your pattern":
                game_loop(game_field)
            if text_in_button == "Random pattern":
                game_field = random_choice(game_field)
                game_loop(game_field)
            if text_in_button == " ":
                delay = 200
                start_screen()
            if text_in_button == "Choose pattern":
                choose_pattern()
            if text_in_button == "Default":
                num_alive = [2, 3]
                num_dead = [3]
                time.sleep(0.2)
                start_screen()
            if text_in_button == "Worker bee":
                game_field = workerbee(game_field)
                game_loop(game_field)
            if text_in_button == "Worker bee":
                game_field = workerbee(game_field)
                game_loop(game_field)
            if text_in_button == "Pulsar":
                game_field = pulsar(game_field)
                game_loop(game_field)
            if text_in_button == "Barberfield":
                game_field = barberfield(game_field)
                game_loop(game_field)
            if text_in_button == "Figure eight":
                game_field = figure8(game_field)
                game_loop(game_field)
            if text_in_button == "Tumblr":
                game_field = tumblr(game_field)
                game_loop(game_field)
            if text_in_button == "Pentadecathlon":
                game_field = pentadecathlon(game_field)
                game_loop(game_field)
            if text_in_button == "Slow":
                delay += 20
                return delay
            elif text_in_button == "Fast":
                delay -= 20
                return delay
    else:
        draw_rect(color_button, button_x, button_y, button_width, button_height)
    print_text(text_in_button, color_text, size_text, button_x + button_width // 2, button_y + button_height // 2, None)


def pause():
    global A1, A2, A3, A4, A5, A6, A11, A22, A33, A44, A55, A66, num_alive, num_dead
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                paused = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                del num_dead[:]
                del num_alive[:]
                A1 = (17, 30, 108)
                A2 = (14, 77, 146)
                A3 = (0, 142, 204)
                A4 = (17, 30, 108)
                A5 = (14, 77, 146)
                A6 = (0, 142, 204)
                A11 = (17, 30, 108)
                A22 = (14, 77, 146)
                A33 = (0, 142, 204)
                A44 = (17, 30, 108)
                A55 = (14, 77, 146)
                A66 = (0, 142, 204)
                change_rules()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


def count_alive(field):
    num_alive = 0
    for y in range(cells_y):
        for x in range(cells_x):
            if field[x][y] == 1:
                num_alive += 1
    return num_alive


def starting():
    screen.fill(WHITE)
    image_rect = image_surf.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(image_surf, image_rect)
    print_text("GAME OF LIFE", RED, 100, screen_width // 2, screen_height // 2, "fonts//LemonMilk.otf")
    pygame.display.update()
    time.sleep(1)
    change_rules()


def start_screen():
    start = True

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(WHITE)
        image_rect = image_surf.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(image_surf, image_rect)
        print_text("Welcome to \"Game of life\" ", RED, 50, 410, 75, "fonts//LemonMilk.otf")
        button(MAR1_LIGHT, MARINE1, 0, 145, 800, 95, "Draw your pattern", 40, WHITE)
        button(MAR2_LIGHT, MARINE2, 0, 275, 800, 95, "Random pattern", 40, WHITE)
        button(MAR3_LIGHT, MARINE3, 0, 405, 800, 95, "Choose pattern", 40, WHITE)
        transp = pygame.Surface((80, 45))
        transp.set_alpha(128)
        transp.fill(WHITE)
        screen.blit(transp, (360, 530))
        button_exit()
        pygame.display.update()


def change_rules():
    global A1, A2, A3, A4, A5, A6
    change = True

    while change:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN and event.key == K_RETURN:
                start_screen()

        screen.fill(WHITE)
        image_rect = image_surf.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(image_surf, image_rect)
        print_text("RULES", RED, 50, screen_width // 2, 60, "fonts//LemonMilk.otf")
        button(RED ,MAR1_LIGHT, 320, 500, 150, 70, "Default", 50, WHITE)
        print_text("Dead cell becomes alive, if it has N living neighbours:", RED, 45, screen_width // 2, 150, None)
        button_alive(MAR1_LIGHT, A1, 130, 200, 90, 70, "1", 50, WHITE, 1)
        button_alive(MAR2_LIGHT, A2, 220, 200, 90, 70, "2", 50, WHITE, 2)
        button_alive(MAR3_LIGHT, A3, 310, 200, 90, 70, "3", 50, WHITE, 3)
        button_alive(MAR1_LIGHT, A4, 400, 200, 90, 70, "4", 50, WHITE, 4)
        button_alive(MAR2_LIGHT, A5, 490, 200, 90, 70, "5", 50, WHITE, 5)
        button_alive(MAR3_LIGHT, A6, 580, 200, 90, 70, "6", 50, WHITE, 6)

        print_text("Cell lives on, if it has N living neighbours:", RED, 45, screen_width // 2, 340, None)
        button_dead(MAR1_LIGHT, A11, 130, 390, 90, 70, "1", 50, WHITE, 1)
        button_dead(MAR2_LIGHT, A22, 220, 390, 90, 70, "2", 50, WHITE, 2)
        button_dead(MAR3_LIGHT, A33, 310, 390, 90, 70, "3", 50, WHITE, 3)
        button_dead(MAR1_LIGHT, A44, 400, 390, 90, 70, "4", 50, WHITE, 4)
        button_dead(MAR2_LIGHT, A55, 490, 390, 90, 70, "5", 50, WHITE, 5)
        button_dead(MAR3_LIGHT, A66, 580, 390, 90, 70, "6", 50, WHITE, 6)

        pygame.display.update()


def button_alive(light_color, color_button, button_x, button_y, button_width, button_height, text_in_button, size_text,
                 color_text, value):
    global num_alive, A1, A2, A3, A4, A5, A6
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    draw_rect(color_button, button_x, button_y, button_width, button_height)
    if button_x + button_width > cur[0] > button_x and button_y + button_height > cur[1] > button_y:
        draw_rect(light_color, button_x, button_y, button_width, button_height)
        if click[0] == 1:
            num_alive.append(value)
            if value == 1:
                A1 = RED
            if value == 2:
                A2 = RED
            if value == 3:
                A3 = RED
            if value == 4:
                A4 = RED
            if value == 5:
                A5 = RED
            if value == 6:
                A6 = RED
    print_text(text_in_button, color_text, size_text, button_x + button_width // 2, button_y + button_height // 2, None)


def button_dead(light_color, color_button, button_x, button_y, button_width, button_height, text_in_button, size_text,
                color_text, value):
    global num_dead, A11, A22, A33, A44, A55, A66
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if button_x + button_width > cur[0] > button_x and button_y + button_height > cur[1] > button_y:
        draw_rect(light_color, button_x, button_y, button_width, button_height)
        if click[0] == 1:
            num_dead.append(value)
            if value == 1:
                A11 = RED
            if value == 2:
                A22 = RED
            if value == 3:
                A33 = RED
            if value == 4:
                A44 = RED
            if value == 5:
                A55 = RED
            if value == 6:
                A66 = RED
    else:
        draw_rect(color_button, button_x, button_y, button_width, button_height)
    print_text(text_in_button, color_text, size_text, button_x + button_width // 2, button_y + button_height // 2, None)


def default():
    num_alive.append(2)
    num_alive.append(3)
    num_dead.append(3)


def button_exit():
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 440 > cur[0] > 360 and 575 > cur[1] > 530:
        print_text("EXIT", RED, 45, 400, 555, "fonts//LemonMilk.otf")
        if click[0] == 1:
            exit_func()
    else:
        print_text("EXIT", RED, 35, 400, 555, "fonts//LemonMilk.otf")


def przygotuj_populacje(field):
    global num_alive, num_dead
    nast_gen = [dead] * cells_x
    for i in range(cells_x):
        nast_gen[i] = [dead] * cells_y

    for y in range(cells_y):
        for x in range(cells_x):
            population = 0
            try:
                if field[x - 1][y - 1] == alive:
                    population += 1
            except IndexError:
                pass
            try:
                if field[x][y - 1] == alive:
                    population += 1
            except IndexError:
                pass
            try:
                if field[x + 1][y - 1] == alive:
                    population += 1
            except IndexError:
                pass

            # wiersz 2
            try:
                if field[x - 1][y] == alive:
                    population += 1
            except IndexError:
                pass
            try:
                if field[x + 1][y] == alive:
                    population += 1
            except IndexError:
                pass

            # wiersz 3
            try:
                if field[x - 1][y + 1] == alive:
                    population += 1
            except IndexError:
                pass
            try:
                if field[x][y + 1] == alive:
                    population += 1
            except IndexError:
                pass
            try:
                if field[x + 1][y + 1] == alive:
                    population += 1
            except IndexError:
                pass

            # if field[x][y] == alive and (population < 2 or population > 3):
            #     nast_gen[x][y] = dead
            # elif field[x][y] == alive and (population == 3 or population == 2):
            #     nast_gen[x][y] = alive
            # elif field[x][y] == dead and population == 3:
            #     nast_gen[x][y] = alive
            for i in range(len(num_alive)):
                if field[x][y] == alive and population == num_alive[i]:
                    nast_gen[x][y] = alive
            for b in range(len(num_dead)):
                if field[x][y] == dead and population == num_dead[b]:
                    nast_gen[x][y] = alive
            if field[x][y] == alive and all(k != population for k in num_alive):
                nast_gen[x][y] = dead
    return nast_gen


def pulsar(field_pulsar):
    field_pattern = [dead] * cells_x
    for i in range(cells_x):
        field_pattern[i] = [dead] * cells_y
    field_pulsar[15][7] = 1
    field_pulsar[16][7] = 1
    field_pulsar[17][7] = 1
    field_pulsar[21][7] = 1
    field_pulsar[22][7] = 1
    field_pulsar[23][7] = 1
    field_pulsar[13][9] = 1
    field_pulsar[13][10] = 1
    field_pulsar[13][11] = 1
    field_pulsar[18][9] = 1
    field_pulsar[18][10] = 1
    field_pulsar[18][11] = 1
    field_pulsar[20][9] = 1
    field_pulsar[20][10] = 1
    field_pulsar[20][11] = 1
    field_pulsar[25][9] = 1
    field_pulsar[25][10] = 1
    field_pulsar[25][11] = 1
    field_pulsar[15][12] = 1
    field_pulsar[16][12] = 1
    field_pulsar[17][12] = 1
    field_pulsar[21][12] = 1
    field_pulsar[22][12] = 1
    field_pulsar[23][12] = 1
    field_pulsar[15][14] = 1
    field_pulsar[21][14] = 1
    field_pulsar[22][14] = 1
    field_pulsar[23][14] = 1
    field_pulsar[16][14] = 1
    field_pulsar[17][14] = 1
    field_pulsar[13][15] = 1
    field_pulsar[13][16] = 1
    field_pulsar[13][17] = 1
    field_pulsar[18][15] = 1
    field_pulsar[18][16] = 1
    field_pulsar[18][17] = 1
    field_pulsar[20][15] = 1
    field_pulsar[20][16] = 1
    field_pulsar[20][17] = 1
    field_pulsar[25][15] = 1
    field_pulsar[25][16] = 1
    field_pulsar[25][17] = 1
    field_pulsar[15][19] = 1
    field_pulsar[16][19] = 1
    field_pulsar[17][19] = 1
    field_pulsar[21][19] = 1
    field_pulsar[22][19] = 1
    field_pulsar[23][19] = 1
    return field_pulsar


def tumblr(field_tumblr):
    field_tumblr[13][12] = 1
    field_tumblr[19][12] = 1
    field_tumblr[12][13] = 1
    field_tumblr[14][13] = 1
    field_tumblr[18][13] = 1
    field_tumblr[20][13] = 1
    field_tumblr[12][14] = 1
    field_tumblr[15][14] = 1
    field_tumblr[17][14] = 1
    field_tumblr[20][14] = 1
    field_tumblr[14][15] = 1
    field_tumblr[18][15] = 1
    field_tumblr[14][16] = 1
    field_tumblr[15][16] = 1
    field_tumblr[17][16] = 1
    field_tumblr[18][16] = 1
    return field_tumblr


def workerbee(field_bee):
    field_bee[13][10] = 1
    field_bee[13][20] = 1
    field_bee[14][10] = 1
    field_bee[14][11] = 1
    field_bee[14][12] = 1
    field_bee[14][18] = 1
    field_bee[14][19] = 1
    field_bee[14][20] = 1
    field_bee[15][13] = 1
    field_bee[15][17] = 1
    field_bee[16][12] = 1
    field_bee[16][13] = 1
    field_bee[16][17] = 1
    field_bee[16][18] = 1
    field_bee[18][15] = 1
    field_bee[19][15] = 1
    field_bee[20][15] = 1
    field_bee[21][15] = 1
    field_bee[22][15] = 1
    field_bee[23][15] = 1
    field_bee[25][12] = 1
    field_bee[25][13] = 1
    field_bee[25][17] = 1
    field_bee[25][18] = 1
    field_bee[26][13] = 1
    field_bee[26][17] = 1
    field_bee[26][13] = 1
    field_bee[27][10] = 1
    field_bee[27][11] = 1
    field_bee[27][12] = 1
    field_bee[27][18] = 1
    field_bee[27][19] = 1
    field_bee[27][20] = 1
    field_bee[28][10] = 1
    field_bee[28][20] = 1
    return field_bee


def figure8(field_fig):
    field_fig[16][10] = 1
    field_fig[16][11] = 1
    field_fig[17][10] = 1
    field_fig[17][11] = 1
    field_fig[17][13] = 1
    field_fig[18][14] = 1
    field_fig[19][11] = 1
    field_fig[20][12] = 1
    field_fig[20][14] = 1
    field_fig[20][15] = 1
    field_fig[21][14] = 1
    field_fig[21][15] = 1
    return field_fig


def pentadecathlon(field_pent):
    field_pent[16][13] = 1
    field_pent[17][13] = 1
    field_pent[19][13] = 1
    field_pent[20][13] = 1
    field_pent[21][13] = 1
    field_pent[22][13] = 1
    field_pent[24][13] = 1
    field_pent[25][13] = 1
    field_pent[18][12] = 1
    field_pent[18][14] = 1
    field_pent[23][12] = 1
    field_pent[23][14] = 1
    return field_pent


def barberfield(field):
    field[13][10] = 1
    field[13][11] = 1
    field[14][10] = 1
    field[14][20] = 1
    field[14][21] = 1
    field[15][12] = 1
    field[15][21] = 1
    field[16][12] = 1
    field[16][14] = 1
    field[16][18] = 1
    field[16][19] = 1
    field[18][14] = 1
    field[20][12] = 1
    field[20][14] = 1
    field[20][16] = 1
    field[22][11] = 1
    field[22][12] = 1
    field[22][16] = 1
    field[22][18] = 1
    field[23][9] = 1
    field[23][18] = 1
    field[24][9] = 1
    field[24][10] = 1
    field[24][20] = 1
    field[18][16] = 1
    field[18][18] = 1
    field[25][19] = 1
    field[25][20] = 1
    return field


def choose_pattern():
    choosing = True
    time.sleep(0.2)
    screen.fill(WHITE)
    image_rect = image_surf.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(image_surf, image_rect)
    print_text("Choose pattern:", RED, 50, screen_width // 2, 45, "fonts//LemonMilk.otf")
    while choosing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button(MAR1_LIGHT, MARINE1, 50, 120, 300, 120, "Worker bee", 40, WHITE)
        button(MAR2_LIGHT, MARINE2, 50, 275, 300, 120, "Pulsar", 40, WHITE)
        button(MAR3_LIGHT, MARINE3, 50, 430, 300, 120, "Barberfield", 40, WHITE)
        button(MAR1_LIGHT, MARINE1, 450, 120, 300, 120, "Figure eight", 40, WHITE)
        button(MAR2_LIGHT, MARINE2, 450, 275, 300, 120, "Tumblr", 40, WHITE)
        button(MAR3_LIGHT, MARINE3, 450, 430, 300, 120, "Pentadecathlon", 40, WHITE)
        pygame.display.update()


def exit_func():
    ex = True
    screen.fill(WHITE)
    image_rect = image_surf.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(image_surf, image_rect)
    print_text("Are you sure", MARINE2, 50, screen_width // 2, screen_height // 4, "fonts//LemonMilk.otf")
    print_text("you want to exit?", MARINE2, 50, screen_width // 2, screen_height // 4 + 75, "fonts//LemonMilk.otf")
    print_text("Press C to continue", RED, 45, screen_width // 2, screen_height // 2 + 50, None)
    print_text("Press Q to exit", RED, 45, screen_width // 2, screen_height // 2 + 120, None)
    pygame.display.update()
    while ex:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                ex = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()


def random_choice(field_rand):
    for y in range(cells_y):
        for x in range(cells_x):
            field_rand[x][y] = random.randint(0, 1)
    return field_rand


def draw_population(field):
    for y in range(cells_y):
        for x in range(cells_x):
            if field[x][y] == alive:
                pygame.draw.rect(screen, RED, Rect((x * cell_size, y * cell_size), (cell_size, cell_size)))
            pygame.draw.rect(screen, GREY, Rect((x * cell_size, y * cell_size), (cell_size, cell_size)), 1)
    return field


def clear2(field_to_clear):
    for y in range(cells_y):
        for x in range(cells_x):
            pygame.draw.rect(screen, WHITE, Rect((x * cell_size, y * cell_size), (cell_size, cell_size)))
            pygame.draw.rect(screen, GREY, Rect((x * cell_size, y * cell_size), (cell_size, cell_size)), 1)
    return field_to_clear


def death():
    global A1, A2, A3, A4, A5, A6, A11, A22, A33, A44, A55, A66, num_alive, num_dead
    gen_dead = True
    image_rect = image_surf.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(image_surf, image_rect)
    rect = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA, 32)
    rect.fill((255, 255, 255, 5))
    screen.blit(rect, (0, 0))
    print_text("All cells are dead!", RED, 60, screen_width // 2, screen_height * 0.35, "fonts//LemonMilk.otf")
    print_text("Press C to start new game", MARINE1, 45, screen_width // 2, screen_height * 0.7, None)
    print_text("Press Q to exit", MARINE1, 45, screen_width // 2, screen_height * 0.8, None)
    pygame.display.update()
    while gen_dead:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_c:
                del num_dead[:]
                del num_alive[:]
                A1 = (17, 30, 108)
                A2 = (14, 77, 146)
                A3 = (0, 142, 204)
                A4 = (17, 30, 108)
                A5 = (14, 77, 146)
                A6 = (0, 142, 204)
                A11 = (17, 30, 108)
                A22 = (14, 77, 146)
                A33 = (0, 142, 204)
                A44 = (17, 30, 108)
                A55 = (14, 77, 146)
                A66 = (0, 142, 204)
                change_rules()
                change_rules()
            if event.type == KEYDOWN and event.key == K_q:
                pygame.quit()
                sys.exit()


def game_loop(field):
    global n
    count_var = 0
    num_alive = 0

    cont_living = False
    # press_down = False
    global press_down
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_RETURN:
                cont_living = True

            if cont_living is False:
                if event.type == MOUSEBUTTONDOWN:
                    press_down = True
                    press_type = event.button

                if event.type == MOUSEBUTTONUP:
                    press_down = False

                if press_down:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    mouse_x = int(mouse_x / cell_size)
                    mouse_y = int(mouse_y / cell_size)
                    if press_type == 1:
                        field[mouse_x][mouse_y] = alive
                    if press_type == 3:
                        field[mouse_x][mouse_y] = dead
        if cont_living is True:
            field = przygotuj_populacje(field)
            count_var += 1
            num_alive = count_alive(field)
            if num_alive == 0:
                death()
                break
        screen.fill(WHITE)
        field = draw_population(field)
        draw_rect(WHITE, 0, 0, screen_width, 40)
        if count_var == 0:
            print_text("Press ENTER to start", RED, 36, 400, 20, None)
        else:
            print_text("Generation: " + str(count_var), RED, 36, 300, 20, None)
            print_text("Population: " + str(num_alive), RED, 36, 500, 20, None)
        if cont_living is True:
            button(MAR2_LIGHT, MARINE2, 670, 0, 90, 40, "Pause", 32, WHITE)
        button(MAR1_LIGHT, MARINE1, 760, 0, 40, 40, " ", 32, WHITE)
        draw_rect(WHITE, 770, 8, 20, 4)
        draw_rect(WHITE, 770, 18, 20, 4)
        draw_rect(WHITE, 770, 28, 20, 4)
        button(MAR1_LIGHT, MARINE1, 0, 0, 90, 40, "Slow", 32, WHITE)
        button(MAR3_LIGHT, MARINE3, 90, 0, 90, 40, "Fast", 32, WHITE)
        pygame.draw.line(screen, BLACK, (0, 40), (screen_width, 40), 2)
        pygame.display.update()
        pygame.time.delay(delay)


starting()
