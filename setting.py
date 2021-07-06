class Settings:
    """A class to store all settings"""

    def __init__(self):
        """Initialize game settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color = (25, 25, 112)

        #ship setting
        self.ship_speed = 2.0
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 4
        self.bullet_height = 16
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 50
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
