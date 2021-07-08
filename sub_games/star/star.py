import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent single star"""

    def __init__(self, stars_game):
        """Init star and set """
        super().__init__()
        self.screen = stars_game.screen

        #load star image and set rect to
        self.image = pygame.image.load('star.png')
        self.rect = self.image.get_rect()

        #star new star near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store star's next exact vertical pos
        self.y = float(self.rect.y)