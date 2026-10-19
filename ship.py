import pygame
from pygame.sprite import Sprite
from hit_point import Hitbox


class Ship(Sprite):
    
    def __init__(self,ai_settings,screen,config):
        super().__init__()

        #初始化
        self.screen = screen
        self.ai_settings = ai_settings
        self.ship = pygame.image.load('images/shooter.bmp')
        self.rect = self.ship.get_rect()
        self.screen_rect = screen.get_rect()

        #碰撞箱初始化
        self.hitbox = Hitbox(size=ai_settings.ship_hitbox_size)

        #位置初始化
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
 
        #移动状态初始化
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.moving_slow = False
        self.firing = False
        self.last_fire_time = 0

        #参数初始化
        self.hp = 10
        self.last_hurt_time = 0
        self.invulnerable_time = 1000#ms
        self.invulnerable = config

    def update(self):
        if self.moving_slow:
            #慢速移动
            if self.moving_left and self.rect.left > self.screen_rect.left:
                self.centerx -= self.ai_settings.ship_speed_slow
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.centerx += self.ai_settings.ship_speed_slow
            if self.moving_up and self.rect.top > self.screen_rect.top:
                self.centery -= self.ai_settings.ship_speed_slow
            if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
                self.centery += self.ai_settings.ship_speed_slow
        else:
            #快速移动
            if self.moving_left and self.rect.left > self.screen_rect.left:
                self.centerx -= self.ai_settings.ship_speed
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.centerx += self.ai_settings.ship_speed
            if self.moving_up and self.rect.top > self.screen_rect.top:
                self.centery -= self.ai_settings.ship_speed
            if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
                self.centery += self.ai_settings.ship_speed
        
        #更新中心位置
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        self.hitbox.follow(self.rect)
    
    def blitme(self):
        '''plot the ship'''
        self.screen.blit(self.ship,self.rect)


