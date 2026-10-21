import sys
import pygame
from pygame.examples import aliens
from settings import Settings

#引入各单位
import curtain_bullet
from alien import Alien
from bullet import Bullet
from ship import Ship
from curtain_bullet import CurtainBullet_1,CurtainBullet_2,CurtainBullet_3

def check_events(ship):
    #键盘输入处理
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                sys.exit()
            case pygame.KEYDOWN:
                match event.key: 
                    case pygame.K_LSHIFT:
                        ship.moving_slow = True
                    case pygame.K_LEFT:
                        ship.moving_left = True
                    case pygame.K_RIGHT:
                        ship.moving_right = True
                    case pygame.K_UP:
                        ship.moving_up = True
                    case pygame.K_DOWN:
                        ship.moving_down = True
                    case pygame.K_z:
                        ship.firing = True
            case pygame.KEYUP:
                match event.key:
                    case pygame.K_LSHIFT:
                        ship.moving_slow = False
                    case pygame.K_LEFT:
                        ship.moving_left = False
                    case pygame.K_RIGHT:
                        ship.moving_right = False
                    case pygame.K_UP:
                        ship.moving_up = False
                    case pygame.K_DOWN:
                        ship.moving_down = False
                    case pygame.K_z:
                        ship.firing = False


def update_screen(screen,ship,aliens\
                  ,bullets,curtain_bullets):
    #更新显示
    screen.fill(Settings.get_Const("bg_color"))
    ship.blitme()
    ship.hitbox.draw(screen)
    for bullet in bullets:
        bullet.draw_bullet()
    for alien in aliens:
        alien.blitme()
    for curtain_fire in curtain_bullets:
        curtain_fire.draw_bullet()
    pygame.display.flip()

def bullets_fire(screen,ship,bullets):
    #飞船开火
    if not ship.firing:
        return
    if pygame.time.get_ticks() - ship.last_fire_time >= Settings.get_Const("bullet_interval"):
        new_bullet = Bullet(screen,ship)
        bullets.add(new_bullet)
        ship.last_fire_time = pygame.time.get_ticks()


def curtain_bullets_fire_1(screen,aliens,curtain_bullets):
    curtain_bullet_speed = Settings.get_speed()
    dir = 1 #旋转方向
    for alien in aliens.copy():
        if not alien.firing:
            continue
        if (pygame.time.get_ticks() - alien.last_fire_time1 >= Settings.get_Const("alien_fire_cooldown_1")) and pygame.time.get_ticks() < 25000:
            new_bullet = CurtainBullet_1(screen)
            curtain_bullets.add(new_bullet)
            alien.last_fire_time1 = pygame.time.get_ticks()
        if (pygame.time.get_ticks() - alien.last_fire_time2 >= Settings.get_Const("alien_fire_cooldown_2") / curtain_bullet_speed) \
                and 10000 < pygame.time.get_ticks() < 25000:
            for i in range(1,41):
                new_bullet = CurtainBullet_2(screen,9*i)
                curtain_bullets.add(new_bullet)
                alien.last_fire_time2 = pygame.time.get_ticks()
        if (pygame.time.get_ticks() - alien.last_fire_time2 >= Settings.get_Const("alien_fire_cooldown_3") / curtain_bullet_speed) \
                and 28000 < pygame.time.get_ticks():
            if alien.omega > Settings.get_Const("alien_omega_max"):
                dir = -1 #角度过大时反向旋转
            if alien.omega < Settings.get_Const("alien_omega_min"):
                dir = 1  #角度过小时正向旋转
            for i in range(1,30):
                new_bullet = CurtainBullet_3(screen,12*i+pygame.time.get_ticks()*alien.omega)
                curtain_bullets.add(new_bullet)
                alien.last_fire_time2 = pygame.time.get_ticks()
                alien.omega += Settings.get_Const("alien_beta") * dir

def bullets_in_screen(curtain_bullet_rect):
    #判定子弹是否仍在屏幕内
    if curtain_bullet_rect.bottom <= -100:
        return False
    if curtain_bullet_rect.top >= Settings.get_Const("screen_height"):
        return False
    if curtain_bullet_rect.left <= 0:
        return False
    if curtain_bullet_rect.right >= Settings.get_Const("screen_width"):
        return False
    return True

def update_bullets(bullets,aliens,curtain_bullets):
    #子弹相关判定:消失 伤害
    bullets.update()
    curtain_bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for alien in aliens.copy():
        if alien.hp <= 0:
            aliens.remove(alien)
    for curtain_bullet in curtain_bullets.copy():
        if not bullets_in_screen(curtain_bullet.rect,):
            curtain_bullets.remove(curtain_bullet)

    collisions = pygame.sprite.groupcollide(bullets,aliens,True,False)
    for collision in collisions:
        for alien in collisions[collision]:
            alien.hp -= 1


def create_alien(screen,aliens):
    new_alien = Alien(screen)
    aliens.add(new_alien)

def curtain_fire(aliens):
    for alien in aliens:
        alien.firing = True

def check_ship_hit(ship,curtain_bullets):
    ship.hitbox.hits_any(curtain_bullets,ship)
