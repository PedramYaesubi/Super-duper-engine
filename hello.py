# COMPOUND SHAPES
# DRAW WITH A LOOP
# pygame template

import pygame
import math


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

cloud_x = 50
cloud_y = 125
twitch_frame = 0

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    cloud_x += 3

    if cloud_x > WIDTH + 40:
        cloud_x = -97

    twitch_frame += 1

    # DRAWING
    screen.fill((54, 69, 79))  # always the first drawing command

    cloud_color = (154, 128, 144)

    pygame.draw.circle(screen, cloud_color, (cloud_x, cloud_y), 40)
    pygame.draw.circle(screen, cloud_color, (cloud_x + 52, cloud_y - 42), 40)
    pygame.draw.circle(screen, cloud_color, (cloud_x + 57, cloud_y - 17), 40)
    pygame.draw.circle(screen, cloud_color, (cloud_x - 17, cloud_y - 31), 40)
    pygame.draw.circle(screen, cloud_color, (cloud_x + 40, cloud_y + 35), 40)

    # Hill 1
    rect = (-125, HEIGHT - 50, WIDTH + 80, HEIGHT // 2)
    pygame.draw.ellipse(screen, (123, 119, 35), rect)

     # Hill 2
    rect = (225, HEIGHT - 100, WIDTH + 80, HEIGHT // 2)
    pygame.draw.ellipse(screen, (203, 119, 35), rect)

    # Pumpkin 1
    if (twitch_frame // 10) % 2 == 0:
        eye_y = 416
        mouth_height = 10
    else:
        eye_y = 420
        mouth_height = 5
    # Stem
    pygame.draw.rect(screen, (46, 139, 87), (124, 393, 12, 15))
    # Body
    pygame.draw.ellipse(screen, (203, 119, 35), (92, 403, 76, 50))
    pygame.draw.ellipse(screen, (255, 165, 0), (100, 405, 60, 46))
    
    # Left Eye 
    pygame.draw.rect(screen, (54, 69, 79), (110, eye_y, 10, 12))
    
    # Right Eye 
    pygame.draw.rect(screen, (54, 69, 79), (140, eye_y, 10, 12))
    
    # Mouth 
    pygame.draw.rect(screen, (54, 69, 79), (116, 438, 28, mouth_height))

    # Corn Maze Layer 1
    x = 310
    while x < WIDTH:
        y = (math.sin(x/25) * 25) + 425
        pygame.draw.rect(screen, (255, 243, 128), (x, y, 3, 15))
        x += 20

    # Pumpkin 2
    if (twitch_frame // 10) % 2 == 0:
        eye_y = 416
        mouth_height = 10
    else:
        eye_y = 420
        mouth_height = 5
    # Stem
    pygame.draw.rect(screen, (46, 139, 87), (194, 393, 12, 15))
    # Body
    pygame.draw.ellipse(screen, (203, 119, 35), (162, 403, 76, 50))
    pygame.draw.ellipse(screen, (255, 165, 0), (170, 405, 60, 46))
    
    # Left Eye 
    pygame.draw.rect(screen, (54, 69, 79), (180, eye_y, 10, 12))
    
    # Right Eye 
    pygame.draw.rect(screen, (54, 69, 79), (210, eye_y, 10, 12))
    
    # Mouth 
    pygame.draw.rect(screen, (54, 69, 79), (186, 438, 28, mouth_height))

    # Corn Maze Layer 1
    x = 310
    while x < WIDTH:
        y = (math.sin(x/25) * 25) + 425
        pygame.draw.rect(screen, (255, 243, 128), (x, y, 3, 15))
        x += 20

    # Corn Maze Layer 2
    x = 301
    while x < WIDTH:
        y = (math.sin(x/25) * 25) + 425
        pygame.draw.rect(screen, (255, 243, 128), (x, y, 3, 15))
        x += 20

    # Corn Maze Layer 3
    x = 305
    while x < WIDTH:
        y = (math.sin(x/25) * 25) + 430
        pygame.draw.rect(screen, (255, 243, 128), (x, y, 3, 15))
        x += 20

    # Corn Maze Layer 4
    x = 311
    while x < WIDTH:
        y = (math.sin(x/25) * 25) + 405
        pygame.draw.rect(screen, (255, 243, 128), (x, y, 3, 15))
        x += 20

    # Corn Maze Layer 5
    x = 315
    while x < WIDTH:
        y = (math.sin(x/25) * 25) + 405
        pygame.draw.rect(screen, (255, 243, 128), (x, y, 3, 15))
        x += 20

    # Corn Maze Layer 6
    x = 320
    while x < WIDTH:
        y = (math.sin(x/25) * 25) + 410
        pygame.draw.rect(screen, (255, 243, 128), (x, y, 3, 15))
        x += 20

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()