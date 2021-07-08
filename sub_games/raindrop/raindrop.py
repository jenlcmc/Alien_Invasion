import pygame
from pygame.sprite import Sprite
 
class Raindrop(Sprite):
    def __init__(self, raindrop_game):
        super().__init__()
        self.screen = raindrop_game.screen
        self.settings = raindrop_game.settings

        self.image = pygame.image.load('raindrop.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def check_disappeared(self):
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

    def update(self):
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y