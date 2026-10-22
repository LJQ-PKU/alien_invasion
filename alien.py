import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    def __init__(self,screen:pygame.Surface):
        #初始化
        super().__init__()
        self.screen = screen
        self.alien = pygame.image.load('images/alien.bmp')
        self.rect = self.alien.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top
        self.hp = Settings.get_Const("alien_max_hp")
        self.alien_speed = Settings.get_Const("alien_speed")

        #初始化位置与状态
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.moving_slow = False
        self.firing = False
        self.last_fire_time_1 = 0
        self.last_fire_time_2 = 0
        self.last_fire_time_3 = 0
        self.omega = 0

    def update(self):
        #更新位置
        if self.moving_left:
            self.centerx -= self.alien_speed
        if self.moving_right:
            self.centerx += self.alien_speed
        if self.moving_up:
            self.centery -= self.alien_speed
        if self.moving_down:
            self.centery += self.alien_speed

    def blitme(self):
        #更新显示
        self.screen.blit(self.alien, self.rect)