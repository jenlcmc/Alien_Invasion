import pygame

class Ship:
    """A class to manage ship"""
    
    def __init__(self, ai_game):
        """Initialize the ship and its starting pos"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load ship image and get its react
        self.image = pygame.image.load('images/shipA.bmp')
        self.rect = self.image.get_rect()

        #start each ship at bot center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store decimal value for ship's hori pos
        self.x = float(self.rect.x)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's pos based on movement flag"""
        #update ship x value not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #update rect obj from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw shop at its current location"""
        self.screen.blit(self.image, self.rect)