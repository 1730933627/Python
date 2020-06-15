import pygame
import sys
import random
import time

class Bird:
    def __init__(self):
        self.status=[pygame.image.load(resource_path+f'{i}.png') for i in range(3)]
        #三种状态
        self.x=100
        self.y=250
        self.flap=False
        #振翅
        self.drop=1
        #下降速度
        self.velocity=0
        #爬升速度
    def update(self):
        if self.flap:
            self.velocity=50
            self.drop=1
            self.flap=False
            #重置
        else:
            self.velocity=0
            self.drop+=0.2
            #加速
        self.y-=self.velocity-self.drop

class Ground:
    def __init__(self):
        self.ground=pygame.image.load(resource_path+'ground.png')
        #地板图片
        self.x=0
        self.y=480
    def update(self):
        self.x-=4
        if self.x==-48:
            self.x=0
        screen.blit(self.ground,(self.x,self.y))

class Pipe:
    def __init__(self):
        self.top=pygame.image.load(resource_path+'top.png')
        self.bottom=pygame.image.load(resource_path+'bottom.png')
        self.x=3*width
        self.random=0
        self.top_y=0
        self.bottom_y=0
    def update(self):
        self.x-=4
        #相对地板静止
        if self.x==-52:
            self.x=width
            self.random=random.randint(60,160)
        self.top_y=-230+self.random
        self.bottom_y=230+self.random
        screen.blit(self.top,(self.x,self.top_y))
        screen.blit(self.bottom,(self.x,self.bottom_y))

def check():
#碰撞检测
    global running
    is_over=False
    if bird.y+40>=ground.y:
    #落地
        is_over=True
    if bird.x+38>=pipe.x and (bird.y<pipe.top_y+320 or bird.y>pipe.bottom_y):
    #撞杆
        is_over=True
    if pipe.x<bird.x+20<pipe.x+52 and bird.y-24<pipe.top_y+320 and bird.y+20>pipe.bottom_y:
    #撞孔
        is_over=True
    if is_over:
        screen.blit(over,(45,140))
        running=False
if __name__ == '__main__':
    pygame.init()
    size=(width,height)=(288,512)
    pygame.display.set_caption('Flappy Bird')
    screen=pygame.display.set_mode(size)
    font=pygame.font.Font('freesansbold.ttf',50)
    resource_path='F:\\Yan_Linn\\文档\MyProject\\Python\\PyGame\\flappy bird\\'
    #素材路径
    back_ground=pygame.image.load(resource_path+'bg.png')
    #背景图片
    title=pygame.image.load(resource_path+'title.png')
    #标题
    ready=pygame.image.load(resource_path+'ready.png')
    over=pygame.image.load(resource_path+'over.png')
    #提示语
    bird=Bird()
    ground=Ground()
    pipe=Pipe()
    #实例化
    clock=pygame.time.Clock()
    count=0
    score=0
    #得分
    running=True
    start=False
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                start=True
                bird.flap=True
        screen.blit(back_ground,(0,0))
        screen.blit(title,(55,140))
        if start:
        #游戏开始
            screen.blit(back_ground,(0,0))
            if pipe.x>width+100:
                screen.blit(ready,(55,140))
            bird.update()
            count+=1
            if count<24:
                screen.blit(bird.status[count//8],(bird.x,bird.y))
            else:
                count=0
            #视觉残留
            pipe.update()
            check()
            if bird.x==pipe.x+52:
                score+=1
                #穿越得分
            score_render=font.render(f'{score}',True,(255,255,255))
            screen.blit(score_render,(130,20))
        ground.update()
        pygame.display.flip()
        clock.tick(60)
    time.sleep(0.5)
