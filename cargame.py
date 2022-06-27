import pygame
from pygame.locals import *
import random

# shape parameters
size = width, height = (800, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
# location parameters
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
# animation parameters
speed = 1
lives = 3

# initiallize the app
pygame.init()
running = True

# set window size
screen = pygame.display.set_mode(size)
# set window title
pygame.display.set_caption("Lara's very exciting and fun to play game - George the Shark")
# set background colour
screen.fill((60, 220, 0))
# apply changes
pygame.display.update()

# load player vehicle
unicorn = pygame.image.load("unicorn.png")
#resize image
unicorn = pygame.transform.scale(unicorn, (250, 250))
unicorn_loc = unicorn.get_rect()
unicorn_loc.center = right_lane, height*0.8

# load enemy vehicle
shark = pygame.image.load("shark.png")
shark_loc = shark.get_rect()
shark_loc.center = left_lane, height*0.2

# Load life symbol
heart = pygame.image.load("life_symbol.png")
heart = pygame.transform.scale(heart, (30, 30))
heart_loc1 = heart.get_rect()
heart_loc2 = heart.get_rect()
heart_loc3 = heart.get_rect()
heart_loc1.center = (730, 25)
heart_loc2.center = (760, 25)
heart_loc3.center = (790, 25)

counter = 0
# game loop
while running:
    counter += 1
    # increase game difficulty overtime
    # if counter == 5000:
    #     speed += 0.15
    #     counter = 0
    #     print("level up", speed)

    # animate enemy vehicle
    shark_loc[1] += speed
    if shark_loc[1] > height:
        # randomly select lane
        if random.randint(0,1) == 0:
            shark_loc.center = right_lane, -200
        else:
            shark_loc.center = left_lane, -200

    # end game logic
    # TODO remove this logic and use lives to drive endgame
    print(unicorn_loc[0], unicorn_loc[1]) 
    print(shark_loc[0], shark_loc[1])

    if unicorn_loc[0] == shark_loc[0] and shark_loc[1] > unicorn_loc[1] - 250:
        print("GAME OVER! YOU LOST!")
        break

    # event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            # collapse the app
            running = False
        if event.type == KEYDOWN:
            # move user car to the left
            if event.key in [K_a, K_LEFT]:
                unicorn_loc = unicorn_loc.move([-int(road_w/2), 0])
            # move user car to the right
            if event.key in [K_d, K_RIGHT]:
                unicorn_loc = unicorn_loc.move([int(road_w/2), 0])



    screen.blit(heart, heart_loc1)
    screen.blit(heart, heart_loc2)
    screen.blit(heart, heart_loc3)

    # draw road
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width/2-road_w/2, 0, road_w, height))
    # draw centre line
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width/2 - roadmark_w/2, 0, roadmark_w, height))
    # draw left road marking
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
    # draw right road marking
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))


    # place car images on the screen
    screen.blit(unicorn, unicorn_loc)
    screen.blit(shark, shark_loc)

    # apply changes
    pygame.display.update()

# collapse application window
print('Did you have fun?')
pygame.quit()