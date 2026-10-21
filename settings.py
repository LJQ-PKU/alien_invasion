class Rect_size:
    def __init__(self,width,height):
        self.width = width
        self.height = height

class Settings:
    _Setting = {
        #屏幕设置
        "screen_width":800,
        "screen_height":900,
        "bg_color":(10,10,50),

        #ship参数设置
        "ship_speed":1,
        "ship_speed_slow":0.35,
        "ship_hitbox_size":8,
        "ship_max_hp":10,
        "ship_invulnerable_time":1000,#ms

        #alien参数设置
        "alien_speed":0.25,
        "alien_max_hp":1000,
        "alien_omega_max":20,
        "alien_omega_min":-12,
        "alien_beta":0.00003,
        "alien_fire_cooldown_1":40,
        "alien_fire_cooldown_2":250,
        "alien_fire_cooldown_3":40,

        #bullet参数设置
        "bullet_speed":1.5,
        "bullet_interval":50,
        "bullet_size":Rect_size(5,27),

        #curtain_bullet参数设置(Tips:碰撞箱大小记得调)
        "curtain_bullet_1_size":Rect_size(1,1),
        "curtain_bullet_2_size":Rect_size(1,1),
        "curtain_bullet_3_size":Rect_size(1,1),
        
        #单帧时间(ms)
        "frame_time":600
    }#所有常量

    _mode = 1
    _speed_settings = [0.5,0.25,0.5,0.65,0.75]
    _ship_invulnerable = False

    def get_Const(constname):
        return Settings._Setting[constname]

    def get_speed():
        return Settings._speed_settings[Settings._mode]

    def set_game_mode(mode_input):
        Settings._mode = mode_input
        return

    def set_ship_invulnerable():
        Settings._ship_invulnerable = True
        return

    def ship_invulnerable():
        return Settings._ship_invulnerable