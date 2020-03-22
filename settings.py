class Settings():
    """存储《外星人入侵》的所有类"""
    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 5
        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #1右移-1左移
        self.fleet_direction = 1

        #以什么样的速度加快游戏频率
        self.speedup_scale=1.1
        #外星人分值提高速度
        self.score_scale=1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
         #1右移-1左移
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        #外星人得分增加
        self.alien_points=int(self.alien_points*self.score_scale)

