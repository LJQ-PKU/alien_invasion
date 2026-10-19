import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        #初始化
        super(Bullet,self).__init__()

        #显示初始化
        self.bullet = pygame.image.load('images/bullet.bmp')
        self.screen = screen

        #位置初始化
        self.rect = self.bullet.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.centery = ship.rect.top
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        #参数初始化
        self.speed = ai_settings.bullet_speed

    def update(self):
        #更新位置(背景子弹始终是下降的)
        self.y -= self.speed
        self.rect.y = int(self.y)

    def draw_bullet(self):
        #绘制bullet
        self.screen.blit(self.bullet,self.rect)

