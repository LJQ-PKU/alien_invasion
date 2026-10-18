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
    mode = int(input('选择难度：1.easy 2.normal 3.hard 4.lunatic：'))
    time.sleep(3)
    pygame.init()
    ai_settings = Settings(mode)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption('alien invasion')

    bg_color = pygame.Color(ai_settings.bg_color)
    #create ship
    ship = Ship(ai_settings, screen)
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

