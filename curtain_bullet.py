import pygame
import random
import math
from pygame.sprite import Sprite
from settings import Settings

class CurtainBullet_1(Sprite):
    def __init__(self,screen,mode):
        super().__init__()
        self.screen = screen
        self.curtain_bullet = pygame.image.load('images/curtain_bullet.bmp')
        self.rect = self.curtain_bullet.get_rect()
        self.x = random.randint(0,Settings.get_Const("screen_width"))
        self.y = random.randint(20,30)
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        #速度设定
        self.speed_factor_1 = 1
        self.curtain_bullet_speed = Settings.get_speed(mode) * self.speed_factor_1

    def update(self):
        self.y += self.curtain_bullet_speed
        self.rect.y = int(self.y)

    def draw_bullet(self):
        self.screen.blit(self.curtain_bullet,self.rect)

####################################################

class CurtainBullet_2(Sprite):
    def __init__(self,screen,angle,mode):
        super().__init__()
        self.screen = screen
        self.curtain_bullet = pygame.image.load('images/curtain_bullet2.bmp')
        self.rect = self.curtain_bullet.get_rect()
        self.angle = angle
        self.screen_rect = screen.get_rect()
        self.x = self.screen_rect.centerx
        self.y = 0
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        #速度设定
        self.speed_factor_2 = 0.5
        self.curtain_bullet_speed = Settings.get_speed(mode) * self.speed_factor_2

    def update(self):
        self.x += self.curtain_bullet_speed*math.cos(self.angle*math.pi/180)
        self.y += self.curtain_bullet_speed*math.sin(self.angle*math.pi/180)
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw_bullet(self):
        self.screen.blit(self.curtain_bullet,self.rect)

###########################################################

class CurtainBullet_3(Sprite):
    def __init__(self,screen,angle,mode):
        super().__init__()
        self.screen = screen
        self.curtain_bullet = pygame.image.load('images/curtain_bullet2.bmp')
        self.rect = self.curtain_bullet.get_rect()
        self.angle = angle
        self.screen_rect = screen.get_rect()
        self.x = self.screen_rect.centerx
        self.y = 0
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        #速度设定
        self.speed_factor_3 = 1
        self.curtain_bullet_speed = Settings.get_speed(mode) * self.speed_factor_3

    def update(self):
        self.x += self.curtain_bullet_speed*math.cos(self.angle*math.pi/180)
        self.y += self.curtain_bullet_speed*math.sin(self.angle*math.pi/180)
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw_bullet(self):
        self.screen.blit(self.curtain_bullet,self.rect)
