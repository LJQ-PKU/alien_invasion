class Rect_size:
    def __init__(self,width:float,height:float):
        self.width = width
        self.height = height

class Settings:
    #游戏设置(就是config)
    _Setting = {#所有常量都在这里

        #屏幕设置
        "screen_width":800,
        "screen_height":900,
        "background_color":(10,10,50),

        #ship参数设置
        "ship_speed":1,
        "ship_speed_slow":0.35,
        "ship_size":Rect_size(8,8),
        "ship_max_HP":10,
        "ship_invulnerable_time":1000,#ms

        #alien参数设置
        "alien_speed":0.25,
        "alien_max_HP":1000,
        "alien_omega_max":20,
        "alien_omega_min":-12,
        "alien_beta":0.00003,
        "alien_fire_cooldown_1":40,
        "alien_fire_cooldown_2":250,
        "alien_fire_cooldown_3":40,

        #bullet参数设置
        "bullet_speed":1.5,
        "bullet_interval":50,
        "bullet_size":Rect_size(5,27),#这个是从图片上读出来的

        #curtain_bullet参数设置(Tips:碰撞箱大小记得调)
        "curtain_bullet_1_size":Rect_size(1,1),
        "curtain_bullet_2_size":Rect_size(1,1),
        "curtain_bullet_3_size":Rect_size(1,1),

        #最大帧率,暂时不能调,所有单位的移动距离还没有和帧率绑定,帧率改变会影响游戏速度:(
        "max_FPS":600
    }

    _mode = 1
    _speed_settings = [0.5,0.25,0.5,0.65,0.75]
    _ship_invulnerable = False

    def get_Const(constname:str):
        #根据常量名返回常量值
        return Settings._Setting[constname]

    def get_speed():
        #根据游戏模式返回速度
        return Settings._speed_settings[Settings._mode]

    def set_game_mode(mode_input:int):
        #设置游戏模式
        Settings._mode = mode_input
        return

    def set_ship_invulnerable():
        #测试模式下飞船无敌
        Settings._ship_invulnerable = True
        return

    def ship_invulnerable():
        #返回飞船是否无敌
        return Settings._ship_invulnerable