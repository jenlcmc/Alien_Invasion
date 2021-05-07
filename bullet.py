import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired"""

    def __init__(self, ai_game):
        """Create a bullet obj at curr ship pos"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #create a bullet at (0,0) and set corrrect pos
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store bullet's pos as decimal value
        self.y = float(self.rect.y)

    def update(self):
        """MOve bullet up the screen"""
        #update decimal pos of bullet
        self.y -= self.settings.bullet_speed
        #update rect pos
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)