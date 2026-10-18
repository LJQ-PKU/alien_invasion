class Settings():
    '''储存所有类'''

    def __init__(self,mode):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 900
        self.bg_color = (10,10,50)
        self.ship_speed = 1
        self.alien_speed = 0.25
        self.alien_hp = 1000
        self.ship_speed_slow = 0.35
        self.bullet_speed = 1.5
        self.bullet_interval = 50
        self.ship_hitbox_size = 8

        #子弹速率设定
        self.speed_settings = [0.25,0.5,0.65,0.75]
        self.mode = mode
        self.curtain_bullet_speed = self.speed_settings[mode-1]

        #单帧时间(ms)
        self.frame_time=600
