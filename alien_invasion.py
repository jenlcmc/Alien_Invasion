import sys
import pygame
from setting import Settings
from ship import Ship

class AlienInvasion:
    """overall class for game and behavior"""
    def __init__(self):
        """initialize game and create game"""
        pygame.init()
        self.settings = Settings()

        #screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("ALIEN INVASION")
        #ship
        self.ship = Ship(self)

        #set background color
        self.bg_color = (230, 230, 230); #grey color

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #chekc for inputs activities
            self._check_events()
            #update ship
            self.ship.update()
            #monitor screen
            self._update_screen()
            #refill color after each pass with loop
            self.screen.fill(self.settings.bg_color)
    
    def _check_events(self):
        #watch for keyboard and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                #key up and left + right
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #move ship to right
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        #move ship to left
                        self.ship.moving_left = True
                
                #key down and left + right
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False

    def _update_screen(self):
        """update image on screen and flip to new screen"""
        #check for ship
        self.ship.blitme()
        #make most recently draw screen possible
        pygame.display.flip()

if __name__ == '__main__':
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()