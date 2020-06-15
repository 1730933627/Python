import pygame
import sys

pygame.init()

bg = (240,255,255)
black = (0,0,0)
size = width,hight = 900,600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("demo")

vol_x,vol_y = 4,3
pos_x,pos_y = 50,50

vel_x,vel_y = 4,0
post_x,post_y = 0,550

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if pos_x+50 > width or pos_x-50 < 0:
        vol_x = -vol_x
    if pos_y+50 > hight or pos_y-50 < 0:
        vol_y = -vol_y
    if post_x+200 > width or post_x < 0:
        vel_x = -vel_x
    if pos_y + post_y > width+150:
        vol_y = -vol_y
        
    screen.fill(bg)
    pos_x += vol_x
    pos_y += vol_y
    post_x += vel_x
    pygame.draw.circle(screen,black,(pos_x,pos_y),50,0)
    pygame.draw.rect(screen,black,(post_x,post_y,200,50))
    pygame.display.flip()
    clock.tick(60)
