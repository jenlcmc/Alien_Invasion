import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """class for single aline in fleet"""
    def __init__(self, ai_game):
        """Initial the alien and set pos"""
        super().__init__()
        self.screen = ai_game.screen

        #load alien imagine and set react attributes
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #start each new alien near top left 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store alien's hori pos
        self.x = float(self.rect.x)