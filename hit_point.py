import pygame
from settings import Settings

class Hitbox():
    def __init__(self,size):
        #初始化碰撞箱
        self.rect = pygame.Rect(0,0,size,size)

    def follow(self,object_rect):
        #更新碰撞箱位置
        self.rect.center = object_rect.center

    def hits_any(self,bullets,ship):
        #伤害判定

        #测试模式下不进行伤害判定
        if Settings.ship_invulnerable():
            return
        
        #无敌时间内不进行伤害判定
        if pygame.time.get_ticks() - ship.last_hurt_time < Settings.get_Const("ship_invulnerable_time"):
            return
        
        for b in bullets:
            if self.rect.colliderect(b.rect):
                ship.hp -= 1
                print('get hurt! HP='+str(ship.hp))
                #更新上次受伤时间
                ship.last_hurt_time = pygame.time.get_ticks()
                #子弹造成伤害后移除
                b.kill()

    def draw(self,screen):
        #绘制
        pygame.draw.rect(screen,(0,255,255),self.rect)