class Settings:
    def __init__(self):
        self.screen_width = 1400
        self.screen_height = 1000 
        self.bg_color = (230, 230, 230)

        self.ship_limit = 3

        self.bullet_width = 15
        self.bullet_height = 4
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4

        self.target_height = 130
        self.target_width = 18 
        self.target_color = (160, 60, 10)

        self.miss_limit = 4
        self.speeup_scale = 1.2
        self.levelup_hits = 10  

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 3.2
        self.bullet_speed = 11.0
        self.target_speed = 1.5 

    def increse_speed(self):
        self.ship_speed *= self.speeup_scale
        self.bullet_speed *= self.speeup_scale
        self.target_height *= self.speeup_scale