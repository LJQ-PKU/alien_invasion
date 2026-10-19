import pygame
from pygame.sprite import Sprite

class Hitbox():
    def __init__(self, size=6):
        #初始化碰撞箱
        self.rect = pygame.Rect(0, 0, size, size)

    def follow(self, ship_rect):
        #更新碰撞箱位置
        self.rect.center = ship_rect.center

    def hits_any(self, curtain_bullets,ship):
        #伤害判定
        if ship.invulnerable:
            return
        if pygame.time.get_ticks() - ship.last_hurt_time < ship.invulnerable_time:
            return
        for b in curtain_bullets:
            if self.rect.colliderect(b.rect):
                ship.hp -= 1
                print('get hurt! hp='+str(ship.hp))
                ship.last_hurt_time = pygame.time.get_ticks()
                b.kill()

    def draw(self, screen):
        #绘制
        pygame.draw.rect(screen, (0, 255, 255), self.rect)