import pygame
import random
import math
from pygame.sprite import Sprite
from settings import Settings

class CurtainBullet(Sprite):
    def __init__(self,screen,load_image,factor):
        #初始化
        super().__init__()
        self.screen = screen
        self.screen_rect =screen.get_rect()

        self.curtain_bullet = pygame.image.load(load_image)
        self.rect = self.curtain_bullet.get_rect()

        #速度设置
        self.speed_factor = factor
        self.curtain_bullet_speed = Settings.get_speed() * self.speed_factor

    def draw_bullet(self):
        #更新显示
        self.screen.blit(self.curtain_bullet,self.rect)

class CurtainBullet_1(CurtainBullet):
    def __init__(self,screen):
        super().__init__(screen,'images/curtain_bullet.bmp',1)
        self.x = random.randint(0,Settings.get_Const("screen_width"))
        self.y = random.randint(20,30)
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def update(self):
        self.y += self.curtain_bullet_speed
        self.rect.y = int(self.y)

####################################################

class CurtainBullet_2(CurtainBullet):
    def __init__(self,screen,angle):
        super().__init__(screen,'images/curtain_bullet2.bmp',0.5)
        self.angle = angle
        self.x = self.screen_rect.centerx
        self.y = 0
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def update(self):
        self.x += self.curtain_bullet_speed*math.cos(self.angle*math.pi/180)
        self.y += self.curtain_bullet_speed*math.sin(self.angle*math.pi/180)
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

###########################################################

class CurtainBullet_3(CurtainBullet):
    def __init__(self,screen,angle):
        super().__init__(screen,'images/curtain_bullet2.bmp',1)
        self.angle = angle
        self.x = self.screen_rect.centerx
        self.y = 0
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def update(self):
        self.x += self.curtain_bullet_speed*math.cos(self.angle*math.pi/180)
        self.y += self.curtain_bullet_speed*math.sin(self.angle*math.pi/180)
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
