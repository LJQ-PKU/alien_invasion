import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        #初始化位置与状态
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.alien = pygame.image.load('images/alien.bmp')
        self.rect = self.alien.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top
        self.hp = ai_settings.alien_hp
        self.omega = 0

        #角度范围
        self.omega_max=20
        self.omega_min=-12
        #角速度
        self.beta=0.00003

        #攻击冷却
        self.fire_cooldown_1 = 40
        self.fire_cooldown_2 = 250
        self.fire_cooldown_3 = 40

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.moving_slow = False
        self.firing = False
        self.last_fire_time1 = 0
        self.last_fire_time2 = 0

    def update(self):
        #更新位置
        if self.moving_left:
            self.centerx -= self.ai_settings.alien_speed
        if self.moving_right:
            self.centerx += self.ai_settings.alien_speed
        if self.moving_up:
            self.centery -= self.ai_settings.alien_speed
        if self.moving_down:
            self.centery += self.ai_settings.alien_speed


    def blitme(self):
        #更新显示
        self.screen.blit(self.alien, self.rect)






