import pygame
from pygame.sprite import Sprite

class Alien_bullet(Sprite):
    def __init__(self, aliens_game):
        super().__init__()
        self.screen = aliens_game.screen
        self.settings = aliens_game.settings
        self.color = self.settings.alien_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midbottom = aliens_game.alien.rect.midbottom

        self.y = float(self.rect.y)

    def upadte(self):
        self.y += self.settings.bullet_speed
        self.rect.y = self.y

    def draw_alien_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
