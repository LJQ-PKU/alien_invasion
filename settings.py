class Settings:
    #屏幕设置
    _screen_width = 800
    _screen_height = 900
    _bg_color = (10,10,50)

    #ship与alien参数设置
    _ship_speed = 1
    _ship_speed_slow = 0.35
    _ship_hitbox_size = 8
    _alien_speed = 0.25
    _alien_hp = 1000

    #bullet参数设置
    _bullet_speed = 1.5
    _bullet_interval = 50
    _speed_settings = [0.5,0.25,0.5,0.65,0.75]

    #单帧时间(ms)
    _frame_time=600

    def get_Const(constname):
        match constname:
            case "screen_width":
                return Settings._screen_width
            case "screen_height":
                return Settings._screen_height
            case "bg_color":
                return Settings._bg_color
            case "ship_speed":
                return Settings._ship_speed
            case "ship_speed_slow":
                return Settings._ship_speed_slow
            case "ship_hitbox_size":
                return Settings._ship_hitbox_size
            case "alien_speed":
                return Settings._alien_speed
            case "alien_hp":
                return Settings._alien_hp
            case "bullet_speed":
                return Settings._bullet_speed
            case "bullet_interval":
                return Settings._bullet_interval
            case "frame_time":
                return Settings._frame_time

    def get_speed(mode):
        return Settings._speed_settings[mode]
