import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.bullet = pygame.image.load('images/bullet.bmp')
        self.screen = screen
        self.rect = self.bullet.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.centery = ship.rect.top
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.speed = ai_settings.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = int(self.y)

    def draw_bullet(self):
        self.screen.blit(self.bullet,self.rect)

