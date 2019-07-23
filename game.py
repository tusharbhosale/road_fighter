import pygame
import time
import random

pygame.init()

clock = pygame.time.Clock()

background = pygame.image.load('Images/background.png')
title = pygame.image.load('Images/title.png')
start = pygame.image.load('Images/start.png')
complete = pygame.image.load('Images/complete.png')
pause_img = pygame.image.load('Images/pause.png')
car_one = pygame.image.load('Images/car_1.png')
car_two = pygame.image.load('Images/car_2.png')
car_three = pygame.image.load('Images/car_3.png')
truck = pygame.image.load('Images/truck.png')
car_left = pygame.image.load('Images/left.png')
car_right = pygame.image.load('Images/right.png')
crash = pygame.image.load('Images/crash_1.png')

begin = pygame.mixer.Sound('Sounds/begin.wav')
win = pygame.mixer.Sound('Sounds/win.wav')
crash_sound = pygame.mixer.Sound('Sounds/crash_sound.wav')
truck_sound = pygame.mixer.Sound('Sounds/truck_sound.wav')
car_slide = pygame.mixer.Sound('Sounds/car_slide.wav')
pygame.mixer.music.load('Sounds/car_sound.wav')

background_size = background.get_size()
start_size = start.get_size()
car_size = car_one.get_size()
crash_size = crash.get_size()
truck_size = truck.get_size()

game_win = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Road Fighter")

start_win = True
pause = False
seconds = 0

back_w, back_h = background_size
start_w, start_h = start_size
car_w, car_h = car_size
truck_w, truck_h = truck_size
crash_w, crash_h = crash_size

back_x = 0
back_y = 0

back_x1 = 0
back_y1 = -back_h

start_x = 220
start_y = 150

car_one_x = 425
car_one_y = 650

road_start = 220
road_end = 220 + 356

car_two_x1 = random.randrange(road_start, road_end - car_w)
car_two_y1 = -car_h

car_three_x1 = random.randrange(road_start, road_end - car_w)
car_three_y1 =  -(2*car_h + 100)

car_two_x2 = random.randrange(road_start, road_end - car_w)
car_two_y2 = -(3*car_h + 200)

car_three_x2 = random.randrange(road_start, road_end - car_w)
car_three_y2 =  -(4*car_h + 300)

truck_x = random.randrange(road_start, road_end - truck_h)
truck_y = 850

l = []
car_traveled = 0

opp_car = True
car_initial = (380, 650)

def car_crash():
    global back_x, back_y, back_x1, back_y1, car_one_x, car_one_y, car_two_x1, car_two_y1, car_two_x2, car_two_y2,car_three_x1, car_three_y1, car_three_x2, car_three_y2, opp_car, truck_x, truck_y, car_traveled
    
    pygame.mixer.music.stop()
    truck_sound.stop()
    crash_sound.play(0)

    if opp_car:
        while car_two_y1 > -car_h or car_two_y2 > -car_h or car_three_y1 > -car_h or car_three_y2 > -car_h or (truck_y > -60 and truck_y < 800):
            game_win.fill((0, 0, 0))
            game_win.blit(background, (back_x, back_y))
            game_win.blit(background, (back_x1, back_y1))
            game_win.blit(crash, (car_one_x, car_one_y))
            game_win.blit(car_two, (car_two_x1, car_two_y1))
            game_win.blit(car_three, (car_three_x1, car_three_y1))
            game_win.blit(car_two, (car_two_x2, car_two_y2))
            game_win.blit(car_three, (car_three_x2, car_three_y2))
            game_win.blit(truck, (truck_x, truck_y))
            pygame.display.update()

            car_two_y1 += -10
            car_two_y2 += -10
            car_three_y1 += -10
            car_three_y2 += -10
            if truck_y < 800:
                truck_y += -10
            print_sec(seconds, car_traveled)

    game_win.fill((0, 0, 0))
    game_win.blit(background, (back_x, back_y))
    game_win.blit(background, (back_x1, back_y1))
    game_win.blit(crash, (car_one_x, car_one_y))
    print_sec(seconds, car_traveled)
    pygame.display.update()

    time.sleep(2)
    pygame.mixer.music.play(-1)

def car_collision(x, y, car_no):
    global back_x, back_y, back_x1, back_y1, car_one_x, car_one_y, car_two_x1, car_two_y1, car_two_x2, car_two_y2,car_three_x1, car_three_y1, car_three_x2, car_three_y2, car_initial, truck_x, truck_y, car_traveled
    cnt = 80
    if car_one_y + 3 < y + car_h and car_one_y + 3 > y or car_one_y + car_h - 3 < y + car_h and car_one_y + car_h - 3 > y:
        if car_one_x + 5 > x and car_one_x + 5 < x + car_w or car_one_x + car_w - 5 > x and car_one_x + car_w - 5 < x + car_w:
            if car_one_x + 5 > x and car_one_x + 5 < x + car_w:
                move = 0.4
                car = car_right
            else:
                move = -0.4
                car = car_left
            
            car_slide.play()
            print_sec(seconds, car_traveled)

            while  cnt:
                game_win.blit(background, (back_x, back_y))
                game_win.blit(background, (back_x1, back_y1))
                game_win.blit(car, (car_one_x, car_one_y))
                game_win.blit(car_two, (car_two_x1, car_two_y1))
                game_win.blit(car_three, (car_three_x1, car_three_y1))
                game_win.blit(car_two, (car_two_x2, car_two_y2))
                game_win.blit(car_three, (car_three_x2, car_three_y2))
                game_win.blit(truck, (truck_x, truck_y))
                pygame.display.update()

                back_y += 10
                back_y1 += 10
                
                car_one_x += move

                if car_one_x < road_start or car_one_x + car_w > road_end:
                    l.clear()
                    car_slide.stop()
                    car_crash()
                    car_one_x, car_one_y = car_initial

                    car_two_x1 = random.randrange(road_start, road_end - car_w)
                    car_two_y1 = -car_h

                    car_three_x1 = random.randrange(road_start, road_end - car_w)
                    car_three_y1 =  -(2*car_h + 100)

                    car_two_x2 = random.randrange(road_start, road_end - car_w)
                    car_two_y2 = -(3*car_h + 200)

                    car_three_x2 = random.randrange(road_start, road_end - car_w)
                    car_three_y2 =  -(4*car_h + 300)

                    truck_x = random.randrange(road_start, road_end - truck_h)
                    truck_y = 850

                    speed = 5
                    
                    return False

                if car_one_y + 3 < truck_y + truck_h - 2 and car_one_y + 3 > truck_y + 2 or car_one_y + car_h - 3 < truck_y + truck_h - 2 and car_one_y + car_h - 3 > truck_y + 2:
                    if car_one_x + 5 > truck_x + 5 and car_one_x + 5 < truck_x + truck_w - 5 or car_one_x + car_w - 5 > truck_x  + 5 and car_one_x + car_w - 5 < truck_x + truck_w - 5:
                        l.clear()
                        car_slide.stop()
                        car_crash()
                        car_one_x, car_one_y = car_initial

                        car_two_x1 = random.randrange(road_start, road_end - car_w)
                        car_two_y1 = -car_h

                        car_three_x1 = random.randrange(road_start, road_end - car_w)
                        car_three_y1 =  -(2*car_h + 100)

                        car_two_x2 = random.randrange(road_start, road_end - car_w)
                        car_two_y2 = -(3*car_h + 200)

                        car_three_x2 = random.randrange(road_start, road_end - car_w)
                        car_three_y2 =  -(4*car_h + 300)

                        truck_x = random.randrange(road_start, road_end - truck_h)
                        truck_y = 850

                        speed = 5
                        return False
                
                if car_no == 1 and (car_two_x1 > road_start and car_two_x1 + car_w < road_end):
                    car_two_x1 -= move*2
                if car_no == 2 and (car_three_x1 > road_start and car_three_x1 + car_w < road_end):
                    car_three_x1 -= move*2
                if car_no == 3 and (car_two_x2 > road_start and car_two_x2 + car_w < road_end):
                    car_two_x2 -= move*2
                if car_no == 4 and (car_three_x2 > road_start and car_three_x2 + car_w < road_end):
                    car_three_x2 -= move*2
                
                if car_no == 1:
                    car_two_y1 += -1
                if car_no == 3:
                    car_two_y2 += -1
                if car_no == 2:
                    car_three_y1 += -1   
                if car_no == 4:
                    car_three_y2 += -1
                
                cnt -= 1
                
                if back_y > back_h:
                    back_y = -back_h
                    back_y1 = 0
                if back_y1 > back_h:
                    back_y1 = -back_h
                    back_y = 0
            
            car_slide.stop()
            return True
    return False

def unpause_game():
    global pause
    pause = False
    pygame.mixer.music.unpause()

def pause_game():
    global pause
    pygame.mixer.music.pause()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_win.blit(pause_img, (0, 0))
        button('Resume', 30, 450, 500, 100, 50, unpause_game)
        button('Restart', 30, 450, 550, 100, 50, game)
        button('Quit', 30, 450, 600, 100, 50, end)
        pygame.display.update()
        clock.tick(40)

def end():
    global start_win
    start_win = False
    pygame.quit()
    quit()

def button(msg, size, x, y, w, h, func = None):
    white = (255, 255, 0)
    red = (255, 0, 0)

    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    font = pygame.font.SysFont('Chilanka', size)
    if x < pos[0] < x+w and y < pos[1] < y + h:
        text = font.render(msg, True, red)
        pygame.draw.line(game_win, red, (x, y+h), (x+w, y+h))
        if click[0] == 1 and func != None:
            win.stop()
            func()
    else:
        text = font.render(msg, True, white)
    text_rect = text.get_rect()
    text_rect.center = (x + w/2, y + h/2)
    game_win.blit(text, text_rect)

def complete_game():
    
    pygame.mixer.music.stop()
    truck_sound.stop()
    win.play(-1)

    j = 0
    sec = list(str(seconds))
    for i in sec:
        if i == '.':
            sec[j] = ':'
        j += 1
    sec = ''.join(sec)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        game_win.blit(complete, (0, 0))
        font = pygame.font.SysFont('Chilanka', 60)
        text = font.render('Time Required', True, (255, 255, 0))
        text_rect = text.get_rect()
        text_rect.center = (500 , 300)
        game_win.blit(text, text_rect)

        font = pygame.font.SysFont('Chilanka', 60)
        text = font.render(sec, True, (255, 255, 0))
        text_rect = text.get_rect()
        text_rect.center = (500 , 400)
        game_win.blit(text, text_rect)
        
        button('Play Again', 30, 500, 600, 100, 50, game)
        button('Quit', 30, 700, 600, 100, 50, end)
        pygame.display.update()
        clock.tick(30)

def start_game():
    global start_win
    while start_win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_win.blit(title, (0, 0))
        button('Play', 30, 450, 500, 100, 50, game)
        button('Quit', 30, 450, 550, 100, 50, end)
        pygame.display.update()
        clock.tick(30)

def print_sec(sec, x):
    j = 0
    sec = list(str(sec))
    for i in sec:
        if i == '.':
            sec[j] = ':'
        j += 1
    sec = ''.join(sec)

    font = pygame.font.SysFont('arial', 40)
    text = font.render('Time', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (920 , 250)
    game_win.blit(text, text_rect)

    font = pygame.font.SysFont('arial', 40)
    text = font.render(sec, True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (920 , 300)
    game_win.blit(text, text_rect)

    font = pygame.font.SysFont('arial', 40)
    text = font.render('Distance', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (900 , 450)
    game_win.blit(text, text_rect)

    font = pygame.font.SysFont('arial', 40)
    text = font.render(str(x) + ' Km', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (920 , 500)
    game_win.blit(text, text_rect)
    pygame.display.update()

def start_pos():

    x = 325
    y = 240

    game_win.fill((0, 0, 0))
    game_win.blit(background, (0, 0))
    game_win.blit(start, (220, 150))
    game_win.blit(car_two, (x + 100, y))
    game_win.blit(car_two, (x, y + 70))
    game_win.blit(car_two, (x + 100, y + 140))
    game_win.blit(car_two, (x, y + 210))
    game_win.blit(car_two, (x + 100, y + 280))
    game_win.blit(car_two, (x, y + 350))
    game_win.blit(car_one, (car_one_x, car_one_y))
    print_sec(seconds, car_traveled)
    pygame.display.update()
    
    begin.play(0)
    time.sleep(3)

    while y > -422:
    
        game_win.blit(background, (0, 0))
        game_win.blit(start, (220, 150))
        game_win.blit(car_two, (x + 100, y))
        game_win.blit(car_two, (x, y + 70))
        game_win.blit(car_two, (x + 100, y + 140))
        game_win.blit(car_two, (x, y + 210))
        game_win.blit(car_two, (x + 100, y + 280))
        game_win.blit(car_two, (x, y + 350))
        game_win.blit(car_one, (car_one_x, car_one_y))
        pygame.display.update()

        y -= 10

def game():
    game_run = True
    speed = 5
    max_speed = 50
    speed_vertical = 0
    move = 0
    track_length = 50
    opp_move1 = 0
    opp_move2 = 0
    k = 40
    cnt1 = 0
    cnt2 = 0
    cnt = 1
    move_choice = [-k, k]

    global back_x, back_y, back_x1, back_y1, start_x, start_y, car_one_x, car_one_y, car_two_x1, car_two_y1, car_two_x2, car_two_y2,car_three_x1, car_three_y1, car_three_x2, car_three_y2, road_start, road_end, opp_car, car_initial, truck_x, truck_y

    global pause, seconds, opp_car, car_traveled

    seconds = 0
    game_run= True
    car_traveled = 0
    game_loop_cnt = 1
    back_x = 0
    back_y = 0

    back_x1 = 0
    back_y1 = -back_h

    start_x = 220
    start_y = 150

    car_one_x = 425
    car_one_y = 650

    road_start = 220
    road_end = 220 + 356

    car_two_x1 = random.randrange(road_start, road_end - car_w)
    car_two_y1 = -car_h

    car_three_x1 = random.randrange(road_start, road_end - car_w)
    car_three_y1 =  -(2*car_h + 100)

    car_two_x2 = random.randrange(road_start, road_end - car_w)
    car_two_y2 = -(3*car_h + 200)

    car_three_x2 = random.randrange(road_start, road_end - car_w)
    car_three_y2 =  -(4*car_h + 300)

    truck_x = random.randrange(road_start, road_end - truck_h)
    truck_y = 850

    start_ticks=pygame.time.get_ticks()
    pause_sec = 0
    
    opp_car = True
    l = []

    while game_run:

        game_win.fill((0, 0, 0))
        game_win.blit(background, (back_x, back_y))
        game_win.blit(background, (back_x1, back_y1))

        if start_y <= back_h and car_traveled < track_length:
            game_win.blit(start, (start_x, start_y))
            start_y += speed

        if  car_traveled >= track_length:
            if speed:
                speed_vertical = speed
            speed = 0
            start_x = 220
            start_y = 150
            if car_one_y + car_h <= start_y:
                speed_vertical = 0
                complete_game()
            game_win.blit(start, (start_x, start_y))
        
        game_win.blit(car_two, (car_two_x1, car_two_y1))
        game_win.blit(car_three, (car_three_x1, car_three_y1))
        game_win.blit(car_two, (car_two_x2, car_two_y2)) 
        game_win.blit(car_three, (car_three_x2, car_three_y2))
        game_win.blit(truck, (truck_x, truck_y))
        game_win.blit(car_one, (car_one_x, car_one_y))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                game_run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    move = -5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    move = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    move = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    move = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    pause_game()
                    pause_sec = pygame.time.get_ticks() - seconds*1000

        if game_loop_cnt == 1:
            start_pos()
            pygame.mixer.music.play(-1)

        if speed < max_speed and speed:
            speed += 0.2
        if speed_vertical < max_speed and speed_vertical:
            speed_vertical += 0.2

        if speed > 30:
            car_two_y1 += 20
            car_three_y1 += 20
            car_two_y2 += 20
            car_three_y2 += 20
            truck_y += 20
    
        if car_two_y1 < 350 and car_two_y1 > 335:
            opp_move1 = random.choice(move_choice)
            if opp_move1 == -k and car_two_x1 + opp_move1 < road_start:
                opp_move1 = k
            if opp_move1 == k and car_two_x1 + opp_move1 + car_w > road_end:
                opp_move1 = -k
            cnt1 = k / 5

        if car_two_y2 < 350 and car_two_y2 > 335:
            opp_move2 = random.choice(move_choice)
            if opp_move2 == -k and car_two_x2 + opp_move2 < road_start:
                opp_move2 = k
            if opp_move2 == k and car_two_x2 + opp_move2 + car_w > road_end:
                opp_move2 = -k
            cnt2 = k / 5

        if cnt1:
            if opp_move1 == -k:
                car_two_x1 -= 5
            else:
                car_two_x1 += 5
            cnt1 -= 1

        if cnt2:
            if opp_move2 == -k:
                car_two_x2 -= 5
            else:
                car_two_x2 += 5
            cnt2 -= 1

        if car_one_y + car_h <= start_y and car_traveled >= track_length:
            move = 0
        car_one_x += move
        car_one_y -= speed_vertical
        back_y1 += speed
        back_y += speed

        if car_collision(car_two_x1, car_two_y1, 1) :
            speed = 30
            l.append(1)
        elif car_collision(car_three_x1, car_three_y1, 2):
            speed = 30
            l.append(2)
        elif car_collision(car_two_x2, car_two_y2, 3):
            speed = 30
            l.append(3)
        elif car_collision(car_three_x2, car_three_y2, 4):
            speed = 30
            l.append(4)

        if opp_car:
            if car_two_y1 > back_h:
                car_two_x1 = random.randrange(road_start, road_end - car_w)
                car_two_y1 = -car_h
                if len(l):
                    if l[0] == 1:
                        car_two_y1 += 80
                        l.pop(0)
    
            if car_three_y1 > back_h:
                car_three_x1 = random.randrange(road_start, road_end - car_w)
                car_three_y1 = -car_h
                if len(l):
                    if l[0] == 2:
                        car_three_y1 += 80
                        l.pop(0)
    
            if car_two_y2 > back_h:
                car_two_x2 = random.randrange(road_start, road_end - car_w)
                car_two_y2 = -car_h
                if len(l):
                    if l[0] == 3:
                        car_two_y2 += 80
                        l.pop(0)
    
            if car_three_y2 > back_h:
                cnt += 1
                car_three_x2 = random.randrange(road_start, road_end - car_w)
                car_three_y2 =  -car_h
                if len(l):
                    if l[0] == 4:
                        car_three_y2 += 80
                        l.pop(0)

            if cnt % 4 == 0:
                truck_x = random.randrange(road_start, road_end - car_w)
                truck_y =  -car_h - 260
        
        if car_one_x < road_start or car_one_x + car_w > road_end:
            l.clear()
            car_crash()
            car_one_x, car_one_y = car_initial
            
            car_two_x1 = random.randrange(road_start, road_end - car_w)
            car_two_y1 = -car_h

            car_three_x1 = random.randrange(road_start, road_end - car_w)
            car_three_y1 =  -(2*car_h + 100)

            car_two_x2 = random.randrange(road_start, road_end - car_w)
            car_two_y2 = -(3*car_h + 200)

            car_three_x2 = random.randrange(road_start, road_end - car_w)
            car_three_y2 =  -(4*car_h + 300)
            
            truck_x = random.randrange(road_start, road_end - truck_h)
            truck_y = 850

            speed = 5
        if car_one_y + 3 < truck_y + truck_h - 2 and car_one_y + 3 > truck_y + 2 or car_one_y + car_h - 3 < truck_y + truck_h - 2 and car_one_y + car_h - 3 > truck_y + 2:
            if car_one_x + 5 > truck_x + 5 and car_one_x + 5 < truck_x + truck_w - 5 or car_one_x + car_w - 5 > truck_x  + 5 and car_one_x + car_w - 5 < truck_x + truck_w - 5:
                l.clear()
                car_crash()
                car_one_x, car_one_y = car_initial

                car_two_x1 = random.randrange(road_start, road_end - car_w)
                car_two_y1 = -car_h

                car_three_x1 = random.randrange(road_start, road_end - car_w)
                car_three_y1 =  -(2*car_h + 100)

                car_two_x2 = random.randrange(road_start, road_end - car_w)
                car_two_y2 = -(3*car_h + 200)

                car_three_x2 = random.randrange(road_start, road_end - car_w)
                car_three_y2 =  -(4*car_h + 300)

                truck_x = random.randrange(road_start, road_end - truck_h)
                truck_y = 850

                speed = 5

        if truck_y > 0:
            truck_sound.play()
        if truck_y > 800:
            truck_sound.stop()

        if back_y > back_h:
            car_traveled += 1
            back_y = -back_h
            back_y1 = 0
        if back_y1 > back_h:
            back_y1 = -back_h
            back_y = 0
 
        seconds = (pygame.time.get_ticks() - start_ticks - pause_sec) / 1000
        seconds = round(seconds, 2)
        print_sec(seconds, car_traveled)
        
        if car_traveled == track_length - 1:
            opp_car = False
        game_loop_cnt += 1
        clock.tick(40)

start_game()
pygame.quit()
quit()
