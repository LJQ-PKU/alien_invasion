import sys
import time
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions

def run_game():

    #难度设定
    while True:
        mode_string = input('选择难度\n1.easy\n2.normal\n3.hard\n4.lunatic\n')
        try:
            mode = int(mode_string)
        except ValueError as e:
            print('输入无效',str(e),'\n')
        else:
            if mode == 0:
                print('测试模式开启,飞船不会受伤\n')
                Settings.set_ship_invulnerable()
            if mode >= 0 and mode <= 4:
                break
            print('\n难度无效:(\n')
        finally:
            time.sleep(1)
    time.sleep(1)

    #进程初始化
    pygame.init()
    screen = pygame.display.set_mode((Settings.get_Const("screen_width"),Settings.get_Const("screen_height")))
    clock = pygame.time.Clock()
    pygame.display.set_caption('alien invasion')
    Settings.set_game_mode(mode)

    #单位初始化
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    curtain_bullets = pygame.sprite.Group()
    game_functions.create_alien(screen,aliens)

    #单帧循环
    while True:
        game_functions.check_events(ship)
        game_functions.curtain_fire(aliens)
        game_functions.ship_update(ship)
        game_functions.bullets_fire(screen,ship,bullets)
        game_functions.update_bullets(bullets,aliens,curtain_bullets)
        game_functions.curtain_bullets_fire_1(screen,aliens,curtain_bullets)
        game_functions.check_ship_hit(ship,curtain_bullets)
        game_functions.update_screen(screen,ship,aliens,bullets,curtain_bullets)
        clock.tick(Settings.get_Const("max_FPS"))

        if ship.hp <= 0:
            #飞船生命非正时结束游戏
            print('game over\n')
            break

run_game()