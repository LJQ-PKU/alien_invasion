import sys
import time
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from bullet import Bullet
from alien import Alien


def run_game():
    #初始化+难度设定
    while True:
        mode_string = input('选择难度\n1.easy\n2.normal\n3.hard\n4.lunatic    ')
        try:
            mode = int(mode_string)
        except ValueError as e:
            print('输入无效',e)
        else:
            if mode == 0:
                print('测试模式开启,飞船不会受伤')
            if mode >= 0 and mode <= 4:
                break
            print('难度无效:(')
        time.sleep(1)
    time.sleep(2)
    pygame.init()
    ai_settings = Settings(mode)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption('alien invasion')

    bg_color = pygame.Color(ai_settings.bg_color)
    #create ship
    ship = Ship(ai_settings, screen, mode == 0)
    #create a group of bullets
    bullets = Group()
    aliens = Group()
    curtain_bullets = pygame.sprite.Group()
    gf.create_alien(ai_settings,screen,aliens)

    #main loop 单帧循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        gf.curtain_fire(aliens)
        ship.update()
        gf.bullets_fire(ai_settings,screen,ship,bullets)
        gf.update_bullets(bullets,aliens,curtain_bullets,ai_settings)
        gf.curtain_bullets_fire_1(ai_settings,screen,aliens,curtain_bullets)
        gf.check_ship_hit(ship, curtain_bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets,curtain_bullets)
        clock.tick(ai_settings.frame_time)

        if ship.hp <= 0:
            #飞船生命非正时终止
            print('game over')
            break

run_game()

