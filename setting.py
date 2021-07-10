import pygame
class Settings:
    """A class to store all settings"""

    def __init__(self):
        """Initialize game settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color = (25, 25, 112)
        self.bg = pygame.image.load("images/space.png")
        self.rect = self.bg.get_rect()

        #ship setting
        self.ship_limit = 3

        #bullet settings
        self.bullet_width = 4
        self.bullet_height = 16
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 12
        
        #how uickly the game speed up 
        self.speedup_scale = 1.1    
        self.difficulty_level = 'medium'

        #how quickly alien point values increase
        self.score_scale = 0.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Init settings that change throughut the game"""
        if self.difficulty_level == 'easy':
            self.ship_limit = 6 
            self.bullets_allowed = 10
            self.ship_speed =  0.5
            self.bullet_speed = 1.5
            self.alien_speed = 0.5 

        if self.difficulty_level == 'medium':
            self.ship_limit = 3 
            self.bullets_allowed = 5
            self.ship_speed =  1.5
            self.bullet_speed = 3.0
            self.alien_speed = 1.5 

        if self.difficulty_level == 'hard':
            self.ship_limit = 2 
            self.bullets_allowed = 3
            self.ship_speed =  3.0
            self.bullet_speed = 6.0
            self.alien_speed = 2.0
            
            # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #scoring
        self.alien_points = 30

    def increse_speed(self):
        """Incerese speed setting"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    def set_difficulty(self):
        if diff_setting == 'easy':
            print('easy')
        elif diff_setting == 'medium':
            pass
        elif diff_setting == 'hard':
            pass
