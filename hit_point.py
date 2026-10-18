import pygame
from pygame.sprite import Sprite

import pygame

import ship


class Hitbox():
    def __init__(self, size=6):
        self.rect = pygame.Rect(0, 0, size, size)

    def follow(self, ship_rect):
        self.rect.center = ship_rect.center

    def hits_any(self, curtain_bullets,ship):
        now = pygame.time.get_ticks()
        for b in curtain_bullets:
            if self.rect.colliderect(b.rect) and (now - ship.last_hurt_time >= 1000):
                ship.hp -= 1
                print('get hurt! hp='+str(ship.hp))
                ship.last_hurt_time = now
                b.kill()

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 255), self.rect)