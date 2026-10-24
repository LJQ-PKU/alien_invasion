import pygame
import random
import math

from pygame.sprite import Sprite
from settings import Settings,Rect_size
from ship import Ship

class Bullet(Sprite):
    def __init__(self,screen:pygame.surface.Surface,load_image,factor:float,rect_size:Rect_size,angle:float):
        #初始化
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.angle = angle

        self.bullet = pygame.image.load(load_image)
        self.rect = pygame.rect.Rect(0,0,rect_size.width,rect_size.height)

        #速度设置
        self.bullet_speed = Settings.get_speed() * factor

    def update(self):
        self.x += self.bullet_speed * math.cos(self.angle*math.pi/180)
        self.y += self.bullet_speed * math.sin(self.angle*math.pi/180)
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw_bullet(self):
        #更新显示
        self.screen.blit(self.bullet,self.rect)

class Curtain_Bullet_1(Bullet):
    def __init__(self,screen:pygame.surface.Surface):
        #调用Bullet初始化
        super().__init__(screen,'images/curtain_bullet.bmp',1,Settings.get_Const("curtain_bullet_1_size"),90)

        #初始化位置
        self.x = random.randint(0,Settings.get_Const("screen_width"))
        self.y = random.randint(20,30)
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

class Curtain_Bullet_2(Bullet):
    def __init__(self,screen:pygame.surface.Surface,angle:float):
        #调用Bullet初始化
        super().__init__(screen,'images/curtain_bullet2.bmp',0.5,Settings.get_Const("curtain_bullet_2_size"),angle)

        #初始化位置
        self.x = self.screen_rect.centerx
        self.y = 0
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

class Curtain_Bullet_3(Bullet):
    def __init__(self,screen:pygame.surface.Surface,angle:float):
        #调用Bullet初始化
        super().__init__(screen,'images/curtain_bullet2.bmp',1,Settings.get_Const("curtain_bullet_3_size"),angle)

        #初始化位置
        self.x = self.screen_rect.centerx
        self.y = 0
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

class Ship_Bullet(Bullet):
    def __init__(self,screen:pygame.surface.Surface,ship:Ship):
        #调用Bullet初始化
        super().__init__(screen,'images/ship_bullet.bmp',1,Settings.get_Const("bullet_size"),-90)
        
        #初始化位置
        self.rect.centerx = ship.rect.centerx
        self.rect.centery = ship.rect.top
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def draw_bullet(self):
        #绘制bullet
        self.screen.blit(self.bullet,self.rect)