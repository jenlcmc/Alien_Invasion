class Settings:
    """A class to store all settings"""

    def __init__(self):
        """Initialize game settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color = (25, 25, 112)

        #speed setting
        self.ship_speed = 2.0

        #bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 4
        self.bullet_height = 16
        self.bullet_color = (255,0,0)