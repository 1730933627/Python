import pygame
import sys

pygame.init()

size = width,height = 900,600
speed = [-4,3]
r_speed = [4,0]
bg = (240,255,255)

fullscreen = False

screen = pygame.display.set_mode(size)

pygame.display.set_caption('Yan_Lin')


turtle = pygame.image.load('1.png')
rectange = pygame.image.load('2.jpg')
positiont = rectange.get_rect()
position = turtle.get_rect()
positiont.bottom = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN | pygame.HWSURFACE)
                    size = width,height = 1920,1080
                    positiont.bottom = 1080
                else:
                    size = width,height = 900,600
                    screen = pygame.display.set_mode(size)
                    positiont.bottom = 600
                    
            if event.key == pygame.K_ESCAPE:
                sys.exit()

            if event.key == pygame.K_LEFT:
                r_speed = [-4,0]
            if event.key == pygame.K_RIGHT:
                r_speed = [4,0]
            if event.key == pygame.K_UP:
                if r_speed[0] >= 6:
                    if r_speed[0] % 2==0:
                        continue
                    else:
                        r_speed[0]-=1
                    r_speed[0] = r_speed[0]/2
                else:
                    r_speed[0] = r_speed[0]*2
            if event.key == pygame.K_DOWN:
                if r_speed[0] <= 1:
                    continue
                else:
                    r_speed[0] = r_speed[0]/2
                
    position = position.move(speed)
    positiont = positiont.move(r_speed)

    if position.left < 0 or position.right > width:
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    if positiont.left < 0 or positiont.right > width:
        r_speed[0] = -r_speed[0]

    if position.bottom > positiont.top:
        speed[1] = -speed[1]

    if positiont.left < 0 or position.right >width:
        positiont = positiont.move(r_speed)



    screen.fill(bg)
    screen.blit(turtle,position)
    screen.blit(rectange,positiont)
    pygame.display.flip()
    pygame.time.delay(10)
