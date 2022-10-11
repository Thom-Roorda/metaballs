import pygame as pg
import colorsys
import metaball
import random
import math


#define functions
def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))


#init values
WIDTH = 400
HEIGHT = 400

SIZE = 5

METABALLS = []
N_METABALLS = 4

MAX_SPEED = N_METABALLS * 4

RUNNING = True


#init metaballs
for i in range(N_METABALLS):
    r = random.randint(5, 40)
    x = random.randint(0 + r, WIDTH - r)
    y = random.randint(0 + r, HEIGHT - r)
    dx = random.random() * MAX_SPEED - (MAX_SPEED / 2) 
    dy = random.random() * MAX_SPEED - (MAX_SPEED / 2)
    mb = metaball.MetaBall(x, y, dx, dy, r)
    METABALLS.append(mb)


#init pygame window
pg.init()

window = pg.display.set_mode((WIDTH, HEIGHT))



#pygame loop
while RUNNING:

    #pygame event handling
    for event in pg.event.get():
            if event.type == pg.QUIT:
                RUNNING = False

            if event.type == pg.KEYDOWN:

                #change position, velocity and radius if key X is pressed
                if event.key == pg.K_x:
                    for mb in METABALLS:
                        x = random.randint(0 + r, WIDTH - r)
                        y = random.randint(0 + r, HEIGHT - r)
                        dx = random.random() * MAX_SPEED - (MAX_SPEED / 2) 
                        dy = random.random() * MAX_SPEED - (MAX_SPEED / 2)

                        mb.r = random.randint(5, 40)
                        mb.x = x
                        mb.y = y
                        mb.dx = dx
                        mb.dy = dy

                if event.key == pg.K_ESCAPE:
                    RUNNING = False


    #update metaballs
    for mb in METABALLS:
        mb.update(window)
    

    #draw color
    for x in range(0, WIDTH, SIZE):
        for y in range(0, HEIGHT, SIZE):

            value_sum = 0

            #check distance to each metaball for each pixel 
            for mb in METABALLS:
                dx = abs(mb.x - x)
                dy = abs(mb.y - y)
                value = mb.r  / math.sqrt(dx * dx + dy * dy) * 200 
                value_sum += value 
            
            #convert rgb value to hsv color
            value_sum = max(0, min(value_sum, 255)) / 255
            color = hsv2rgb(value_sum, 1, 0.75)

            pg.draw.rect(window, color, pg.Rect(x, y, SIZE, SIZE))

    
    #update screen
    pg.display.update()