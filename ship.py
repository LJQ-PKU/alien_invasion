import pygame
from pygame.sprite import Sprite
from settings import Settings,Rect_size

class Ship(Sprite):
    #飞船类
    def __init__(self,screen:pygame.surface.Surface):
        #初始化
        super().__init__()

        #显示初始化
        self.screen = screen
        self.ship = pygame.image.load('images/shooter.bmp')
        self.rect = self.ship.get_rect()
        self.screen_rect = screen.get_rect()

        #碰撞箱初始化
        self.hitbox = Hitbox(Settings.get_Const("ship_size"))

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
        self.current_HP = Settings.get_Const("ship_max_HP")
        self.last_hurt_time = 0

    def update(self):
        #更新位置
        ship_speed_slow = Settings.get_Const("ship_speed_slow") if self.moving_slow else Settings.get_Const("ship_speed")
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= ship_speed_slow
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += ship_speed_slow
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= ship_speed_slow
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += ship_speed_slow
        
        #更新中心位置
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        self.hitbox.follow(self.rect)
    
    def blitme(self):
        #绘制ship
        self.screen.blit(self.ship,self.rect)

class Hitbox():
    def __init__(self,size:Rect_size):
        #初始化碰撞箱
        self.rect = pygame.rect.Rect(0,0,size.width,size.height)

    def follow(self,object_rect:pygame.rect.Rect):
        #更新碰撞箱位置
        self.rect.center = object_rect.center

    def hits_any(self,bullets:pygame.sprite.Group,ship:Ship):
        #伤害判定

        #测试模式下不进行伤害判定
        if Settings.ship_invulnerable():
            return
        
        #无敌时间内不进行伤害判定
        if pygame.time.get_ticks() - ship.last_hurt_time < Settings.get_Const("ship_invulnerable_time"):
            return
        
        for bullet in bullets:
            if self.rect.colliderect(bullet.rect):
                ship.current_HP -= 1
                print('get hurt! HP='+str(ship.current_HP))
                #更新上次受伤时间
                ship.last_hurt_time = pygame.time.get_ticks()
                #子弹造成伤害后移除
                bullet.kill()

    def draw(self,screen:pygame.surface.Surface):
        #绘制
        pygame.draw.rect(screen,(0,255,255),self.rect)